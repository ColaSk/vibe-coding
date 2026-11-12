import { useEffect, useState } from "react";
import {
  clearTraffic,
  fetchHarness,
  fetchHealth,
  fetchOverview,
  fetchTraffic,
  initializeCa,
  setHarnessEnabled,
  setHarnessMode,
  type HarnessStatus,
  type HealthResponse,
  type OverviewStats,
  type TrafficEvent,
} from "../api/client";
import { Button } from "../shared/ui/Button";
import { TitledCard } from "../shared/ui/TitledCard";
import { PageContent, pageStyles } from "../shell/layout/PageContent";

const controlUrl =
  (import.meta.env.VITE_CONTROL_URL as string | undefined) ?? "http://127.0.0.1:8787";

function formatTrafficLine(event: TrafficEvent): string {
  const host = `${event.host}:${event.port}`;
  if (event.event === "connect_close") {
    return `${event.event}  ${host}  ↑${event.bytes_up} ↓${event.bytes_down}`;
  }
  if (event.event === "http" || event.event === "http_error") {
    const path = event.path ?? "";
    const status = event.status != null ? ` ${event.status}` : "";
    const err = event.error ? ` ${event.error}` : "";
    return `${event.event}  ${host}  ${path}${status}${err}`;
  }
  if (event.error) {
    return `${event.event}  ${host}  ${event.error}`;
  }
  return `${event.event}  ${host}`;
}

export function HomePage() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [harness, setHarness] = useState<HarnessStatus | null>(null);
  const [overview, setOverview] = useState<OverviewStats | null>(null);
  const [traffic, setTraffic] = useState<TrafficEvent[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  const reload = async () => {
    const [nextHealth, nextHarness, nextOverview] = await Promise.all([
      fetchHealth(controlUrl),
      fetchHarness(controlUrl),
      fetchOverview(controlUrl),
    ]);
    setHealth(nextHealth);
    setHarness(nextHarness);
    setOverview(nextOverview);
  };

  useEffect(() => {
    let cancelled = false;
    void reload()
      .then(() => {
        if (!cancelled) setError(null);
      })
      .catch((cause: unknown) => {
        if (!cancelled) setError(cause instanceof Error ? cause.message : String(cause));
      });
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    if (!harness?.enabled) {
      setTraffic([]);
      return;
    }
    let cancelled = false;
    const pull = async () => {
      try {
        const log = await fetchTraffic(controlUrl, 60);
        if (!cancelled) setTraffic([...log.events].reverse());
      } catch {
        /* keep last good traffic snapshot */
      }
    };
    void pull();
    const timer = window.setInterval(() => void pull(), 2000);
    return () => {
      cancelled = true;
      window.clearInterval(timer);
    };
  }, [harness?.enabled]);

  const onInitializeCa = async () => {
    setBusy(true);
    try {
      setHarness(await initializeCa(controlUrl));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  const toggleHarness = async () => {
    if (!harness) return;
    setBusy(true);
    try {
      setHarness(await setHarnessEnabled(controlUrl, !harness.enabled));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  const onModeChange = async (mode: "passthrough" | "intercept") => {
    setBusy(true);
    setError(null);
    try {
      setHarness(await setHarnessMode(controlUrl, mode));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  const onClearTraffic = async () => {
    setBusy(true);
    try {
      await clearTraffic(controlUrl);
      setTraffic([]);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  const canEnable =
    !!harness &&
    (harness.enabled ||
      harness.mode === "passthrough" ||
      harness.ca === "ready");

  return (
    <PageContent title="数据概览">
      {error ? <p className={pageStyles.err}>{error}</p> : null}
      <TitledCard title="用量">
        {health ? (
          <p className={pageStyles.ok}>
            {health.service} · {health.status}
          </p>
        ) : (
          <p className={pageStyles.muted}>连接中…</p>
        )}
        {overview ? (
          <div className={pageStyles.stats}>
            <div className={pageStyles.stat}>
              <strong>{overview.enabled_model_count}</strong>
              <span>启用模型</span>
            </div>
            <div className={pageStyles.stat}>
              <strong>{overview.model_count}</strong>
              <span>全部模型</span>
            </div>
            <div className={pageStyles.stat}>
              <strong>{overview.call_count}</strong>
              <span>调用次数</span>
            </div>
            <div className={pageStyles.stat}>
              <strong>{overview.total_input_tokens + overview.total_output_tokens}</strong>
              <span>Token</span>
            </div>
          </div>
        ) : null}
      </TitledCard>
      <TitledCard
        title="本机接管"
        actions={
          <div className={pageStyles.actions} data-no-drag>
            {harness?.ca === "missing" ? (
              <Button size="small" disabled={busy} onClick={() => void onInitializeCa()}>
                {busy ? "初始化中…" : "初始化 CA"}
              </Button>
            ) : null}
            <Button
              size="small"
              variant="primary"
              disabled={busy || !canEnable}
              onClick={() => void toggleHarness()}
            >
              {busy
                ? "处理中…"
                : harness?.enabled
                  ? "关闭接管"
                  : "开启接管"}
            </Button>
          </div>
        }
      >
        {harness ? (
          <div className={pageStyles.stack}>
            <label className={pageStyles.muted}>
              流量模式{" "}
              <select
                value={harness.mode || "passthrough"}
                disabled={busy || harness.enabled}
                onChange={(event) =>
                  void onModeChange(event.target.value as "passthrough" | "intercept")
                }
              >
                <option value="passthrough">passthrough（原样转发）</option>
                <option value="intercept">intercept（MITM 拦截）</option>
              </select>
            </label>
            <p className={pageStyles.muted}>
              {harness.mode === "passthrough"
                ? "当前为隧道模式：不解密、不进本地网关，接入后 IDE 应保持可用。"
                : "拦截模式会 MITM Cursor 域名，需系统信任本地 CA。"}
            </p>
            <p className={pageStyles.muted}>CA：{harness.ca}</p>
            {harness.mode === "intercept" &&
            harness.ca === "untrusted" &&
            harness.ca_install_command ? (
              <>
                <p className={pageStyles.err}>
                  CA 已生成但系统尚未信任。先在终端执行下面命令，再开 intercept 接管。
                </p>
                <pre style={{ margin: 0, whiteSpace: "pre-wrap" }}>{harness.ca_install_command}</pre>
              </>
            ) : null}
            {harness.mode === "intercept" && harness.ca === "missing" ? (
              <p className={pageStyles.muted}>拦截模式需要本地 CA，先点「初始化 CA」。</p>
            ) : null}
            <p className={pageStyles.muted}>
              状态：{harness.enabled ? "已开启" : "未开启"}
              {harness.proxy_url ? ` · ${harness.proxy_url}` : null}
            </p>
          </div>
        ) : (
          <p className={pageStyles.muted}>尚未读取到接管状态。</p>
        )}
      </TitledCard>
      {harness?.enabled ? (
        <TitledCard
          title="代理流量"
          actions={
            <div className={pageStyles.actions} data-no-drag>
              <Button size="small" disabled={busy} onClick={() => void onClearTraffic()}>
                清空
              </Button>
            </div>
          }
        >
          {traffic.length === 0 ? (
            <p className={pageStyles.muted}>
              暂无 CONNECT 记录。在 Cursor-SwitchTest 里发一条对话后这里会出现
              api2/api3.cursor.sh。
            </p>
          ) : (
            <pre
              style={{
                margin: 0,
                maxHeight: 280,
                overflow: "auto",
                fontSize: 12,
                lineHeight: 1.45,
                whiteSpace: "pre-wrap",
              }}
            >
              {traffic.map(formatTrafficLine).join("\n")}
            </pre>
          )}
        </TitledCard>
      ) : null}
    </PageContent>
  );
}
