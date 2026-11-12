import { Outlet } from "react-router-dom";
import { AppHeader } from "./AppHeader";
import styles from "./AppFrame.module.scss";

const isMac = navigator.platform.toLowerCase().includes("mac");

export function AppFrame() {
  document.documentElement.dataset.platform = isMac ? "macos" : "windows";
  return (
    <div className={[styles.shell, !isMac ? styles.windows : ""].filter(Boolean).join(" ")}>
      <AppHeader />
      <Outlet />
    </div>
  );
}
