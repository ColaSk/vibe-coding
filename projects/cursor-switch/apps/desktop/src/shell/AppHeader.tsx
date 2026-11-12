import styles from "./AppHeader.module.scss";

const isMac = navigator.platform.toLowerCase().includes("mac");
const isElectron = navigator.userAgent.toLowerCase().includes("electron");

export function AppHeader() {
  document.documentElement.dataset.platform = isMac ? "macos" : "windows";

  return (
    <header className={styles.root}>
      <div
        className={styles.dragLayer}
        data-electron-drag-region
        data-tauri-drag-region
        aria-hidden="true"
      />
      <div className={styles.uiLayer}>
        {isElectron && !isMac ? (
          <>
            <div className={styles.identity}>cursor-switch</div>
            <div className={styles.controls} data-no-drag>
              <button
                type="button"
                className={styles.winBtn}
                onClick={() => window.electronAPI?.windowMinimize()}
              >
                ─
              </button>
              <button
                type="button"
                className={styles.winBtn}
                onClick={() => window.electronAPI?.windowMaximize()}
              >
                □
              </button>
              <button
                type="button"
                className={`${styles.winBtn} ${styles.close}`}
                onClick={() => window.electronAPI?.windowClose()}
              >
                ✕
              </button>
            </div>
          </>
        ) : null}
      </div>
    </header>
  );
}
