import { useEffect, useState } from "react";
import { NavLink, Outlet } from "react-router-dom";
import { fetchHarness, type HarnessStatus } from "../api/client";
import { Card } from "../shared/ui/Card";
import styles from "./AppLayout.module.scss";

const controlBase =
  (import.meta.env.VITE_CONTROL_URL as string | undefined) ?? "http://127.0.0.1:8787";

export function AppLayout() {
  const [harness, setHarness] = useState<HarnessStatus | null>(null);

  useEffect(() => {
    void fetchHarness(controlBase)
      .then(setHarness)
      .catch(() => setHarness(null));
    const timer = window.setInterval(() => {
      void fetchHarness(controlBase)
        .then(setHarness)
        .catch(() => undefined);
    }, 5000);
    return () => window.clearInterval(timer);
  }, []);

  return (
    <div className={styles.root}>
      <Card className={styles.menuCard}>
        <nav className={styles.navigation} data-no-drag>
          <div className={styles.navigationRow}>
            <NavLink to="/" end>
              数据概览
            </NavLink>
          </div>
          <div className={styles.navigationGroup}>模型配置</div>
          <div className={styles.navigationRow}>
            <NavLink to="/models">
              Cursor
              {harness ? (
                <span className={styles.menuStatusTag} data-taken={harness.enabled || undefined}>
                  {harness.enabled ? "已接管" : "未接管"}
                </span>
              ) : null}
            </NavLink>
          </div>
          <div className={styles.navigationGroup}>设置</div>
          <div className={styles.navigationRow}>
            <NavLink to="/settings">系统设置</NavLink>
          </div>
        </nav>
      </Card>
      <div className={styles.content}>
        <Outlet />
      </div>
    </div>
  );
}
