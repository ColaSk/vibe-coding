import { FormEvent, useEffect, useState } from "react";
import {
  fetchDesktopSettings,
  fetchPorts,
  fetchProxy,
  updateDesktopSettings,
  updatePorts,
  updateProxy,
  type DesktopSettings,
  type PortSettings,
  type ProxySettings,
} from "../api/client";
import { Button } from "../shared/ui/Button";
import { Field } from "../shared/ui/Field";
import fieldStyles from "../shared/ui/Field.module.scss";
import { TitledCard } from "../shared/ui/TitledCard";
import { PageContent, pageStyles } from "../shell/layout/PageContent";

const controlUrl =
  (import.meta.env.VITE_CONTROL_URL as string | undefined) ?? "http://127.0.0.1:8787";

export function SettingsPage() {
  const [ports, setPorts] = useState<PortSettings>({ proxy_port: 0, service_port: 8787 });
  const [proxy, setProxy] = useState<ProxySettings>({
    mode: "default",
    address: "",
    auth_enabled: false,
    username: "",
    password: "",
  });
  const [desktop, setDesktop] = useState<DesktopSettings>({
    silent_start: false,
    show_dock_icon: true,
  });
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    void Promise.all([
      fetchPorts(controlUrl),
      fetchProxy(controlUrl),
      fetchDesktopSettings(controlUrl),
    ])
      .then(([nextPorts, nextProxy, nextDesktop]) => {
        setPorts(nextPorts);
        setProxy(nextProxy);
        setDesktop(nextDesktop);
      })
      .catch((cause: unknown) => {
        setError(cause instanceof Error ? cause.message : String(cause));
      });
  }, []);

  const onSave = async (event: FormEvent) => {
    event.preventDefault();
    setBusy(true);
    setError(null);
    setMessage(null);
    try {
      setPorts(await updatePorts(controlUrl, ports));
      setProxy(await updateProxy(controlUrl, proxy));
      setDesktop(await updateDesktopSettings(controlUrl, desktop));
      setMessage("已保存");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  return (
    <PageContent title="系统设置">
      {error ? <p className={pageStyles.err}>{error}</p> : null}
      {message ? <p className={pageStyles.ok}>{message}</p> : null}
      <form className={pageStyles.stack} onSubmit={(event) => void onSave(event)} data-no-drag>
        <TitledCard title="端口">
          <div className={pageStyles.form}>
            <Field label="服务端口">
              <input
                type="number"
                value={ports.service_port}
                onChange={(event) =>
                  setPorts({ ...ports, service_port: Number(event.target.value) })
                }
              />
            </Field>
            <Field label="代理端口（0 = 系统分配）">
              <input
                type="number"
                value={ports.proxy_port}
                onChange={(event) =>
                  setPorts({ ...ports, proxy_port: Number(event.target.value) })
                }
              />
            </Field>
          </div>
        </TitledCard>
        <TitledCard title="出站代理">
          <div className={pageStyles.form}>
            <Field label="模式">
              <select
                value={proxy.mode}
                onChange={(event) => setProxy({ ...proxy, mode: event.target.value })}
              >
                <option value="default">系统默认</option>
                <option value="off">关闭</option>
                <option value="custom">自定义</option>
              </select>
            </Field>
            <Field label="地址">
              <input
                value={proxy.address}
                onChange={(event) => setProxy({ ...proxy, address: event.target.value })}
                placeholder="http://127.0.0.1:7890"
              />
            </Field>
          </div>
        </TitledCard>
        <TitledCard title="桌面">
          <div className={pageStyles.form}>
            <label className={`${fieldStyles.root} ${fieldStyles.check}`}>
              <input
                type="checkbox"
                checked={desktop.silent_start}
                onChange={(event) =>
                  setDesktop({ ...desktop, silent_start: event.target.checked })
                }
              />
              静默启动（到托盘）
            </label>
            <label className={`${fieldStyles.root} ${fieldStyles.check}`}>
              <input
                type="checkbox"
                checked={desktop.show_dock_icon}
                onChange={(event) =>
                  setDesktop({ ...desktop, show_dock_icon: event.target.checked })
                }
              />
              显示 Dock 图标
            </label>
          </div>
        </TitledCard>
        <Button type="submit" variant="primary" disabled={busy}>
          保存设置
        </Button>
      </form>
    </PageContent>
  );
}
