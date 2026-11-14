import { useEffect, useState } from "react";
import type { IconifyIcon } from "@iconify/react/offline";
import { NavLink, Outlet, useLocation } from "react-router-dom";
import cursorIconUrl from "../shared/assets/icons/cursor.svg";
import { PageLayout } from "./layout/PageLayout";
import { Card } from "../shared/ui/Card";
import controls from "../shared/ui/Controls.module.scss";
import { Icon } from "../shared/ui/Icon";
import { TooltipTrigger } from "../shared/ui/TooltipTrigger";
import {
  flatColorAreaChartIcon,
  flatColorSalesPerformanceIcon,
  flatColorSettingsIcon,
  refreshIcon,
} from "../shared/ui/icons";
import { appStore, useAppStore } from "../shared/store/appStore";
import styles from "./AppLayout.module.scss";
import { PageActionsTarget } from "./PageActions";

type MenuItem =
  | { kind: "page"; path: string; label: string; icon: IconifyIcon | string }
  | { kind: "group"; label: string };

const menuItems: MenuItem[] = [
  { kind: "page", path: "/", label: "数据概览", icon: flatColorAreaChartIcon },
  { kind: "page", path: "/calls", label: "调用详细", icon: flatColorSalesPerformanceIcon },
  { kind: "group", label: "模型配置" },
  { kind: "page", path: "/harness/cursor", label: "Cursor", icon: cursorIconUrl },
  { kind: "group", label: "设置" },
  { kind: "page", path: "/settings", label: "系统设置", icon: flatColorSettingsIcon },
];

export function AppLayout() {
  const { busy, cursorHarness } = useAppStore();
  const location = useLocation();
  const [leftActionTarget, setLeftActionTarget] = useState<HTMLDivElement | null>(null);
  const [rightActionTarget, setRightActionTarget] = useState<HTMLDivElement | null>(null);

  useEffect(() => {
    void appStore.refresh();
  }, []);

  return (
    <PageLayout className={styles.root}>
      <Card as="aside" className={styles.menuCard}>
        <nav className={styles.navigation} aria-label="主菜单" data-no-drag>
          {menuItems.map((item) =>
            item.kind === "group" ? (
              <div className={styles.navigationGroup} key={`group-${item.label}`}>{item.label}</div>
            ) : (
              <div className={styles.navigationRow} key={item.path}>
                <NavLink to={item.path} end={item.path === "/"}>
                  {typeof item.icon === "string"
                    ? <Icon src={item.icon} size="1.3em" />
                    : <Icon icon={item.icon} size="1.3em" />}
                  <span>{item.label}</span>
                  {item.path === "/harness/cursor" && cursorHarness ? (
                    <span
                      className={styles.menuStatusTag}
                      data-taken={cursorHarness.settings_applied || undefined}
                    >
                      {cursorHarness.settings_applied ? "已接管" : "未接管"}
                    </span>
                  ) : null}
                </NavLink>
              </div>
            ))}
        </nav>
      </Card>
      <main className={styles.content}>
        <div className={styles.actionRegion}>
          <Card className={styles.actions}>
            <div ref={setLeftActionTarget} className={styles.pageActions} />
            {location.pathname !== "/" ? (
              <TooltipTrigger label="刷新">
                <button
                  className={controls.iconButton}
                  aria-label="刷新"
                  disabled={busy}
                  onClick={() => void appStore.refresh()}
                >
                  <Icon className={busy ? controls.spin : ""} icon={refreshIcon} size="1.1em" />
                </button>
              </TooltipTrigger>
            ) : null}
            <div ref={setRightActionTarget} className={styles.pageActions} />
          </Card>
        </div>
        <PageActionsTarget.Provider value={{ left: leftActionTarget, right: rightActionTarget }}>
          <div className={styles.keepAliveContainer}>
            <Outlet />
          </div>
        </PageActionsTarget.Provider>
      </main>
    </PageLayout>
  );
}
