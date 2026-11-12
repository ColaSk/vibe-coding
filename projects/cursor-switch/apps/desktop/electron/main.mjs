import { app, BrowserWindow, Menu, Tray, dialog, ipcMain, nativeImage } from "electron";
import { spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const isDev = !app.isPackaged;
const CONTROL_URL = process.env.CURSOR_SWITCH_CONTROL_URL ?? "http://127.0.0.1:8787";
const CONTROL_PORT = Number(new URL(CONTROL_URL).port || 8787);
const isMac = process.platform === "darwin";

let mainWindow = null;
let tray = null;
let backend = null;

function projectRoot() {
  return path.resolve(__dirname, "../../..");
}

function resolvePython() {
  const conda = process.env.CONDA_PREFIX
    ? path.join(process.env.CONDA_PREFIX, "bin", "python")
    : null;
  const candidates = [
    process.env.CURSOR_SWITCH_PYTHON,
    conda,
    path.join(process.env.HOME ?? "", "miniconda3/envs/cursor-switch/bin/python"),
    "python3",
  ].filter(Boolean);
  for (const candidate of candidates) {
    if (candidate === "python3" || fs.existsSync(candidate)) return candidate;
  }
  return "python3";
}

async function probeBackend(timeoutMs = 1500) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(`${CONTROL_URL}/healthz`, { signal: controller.signal });
    return response.ok;
  } catch {
    return false;
  } finally {
    clearTimeout(timer);
  }
}

async function ensureBackend() {
  if (await probeBackend()) return true;
  const python = resolvePython();
  const cwd = projectRoot();
  backend = spawn(
    python,
    ["-m", "cursor_switch.control.main", "--host", "127.0.0.1", "--port", String(CONTROL_PORT)],
    {
      cwd,
      env: {
        ...process.env,
        PYTHONPATH: path.join(cwd, "server"),
      },
      stdio: "ignore",
    },
  );
  backend.on("exit", () => {
    backend = null;
  });
  for (let i = 0; i < 40; i += 1) {
    await new Promise((resolve) => setTimeout(resolve, 200));
    if (await probeBackend()) return true;
  }
  return false;
}

function showWindow() {
  if (!mainWindow) {
    void createWindow();
    return;
  }
  if (mainWindow.isMinimized()) mainWindow.restore();
  mainWindow.show();
  mainWindow.focus();
}

async function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1180,
    height: 780,
    minWidth: 960,
    minHeight: 640,
    show: true,
    backgroundColor: "#141414",
    titleBarStyle: isMac ? "hiddenInset" : "hidden",
    trafficLightPosition: isMac ? { x: 14, y: 10 } : undefined,
    frame: isMac,
    autoHideMenuBar: true,
    webPreferences: {
      preload: path.join(__dirname, "preload.cjs"),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: false,
    },
  });

  mainWindow.on("close", (event) => {
    if (!app.isQuitting) {
      event.preventDefault();
      mainWindow.hide();
    }
  });

  if (isDev) {
    await mainWindow.loadURL("http://127.0.0.1:5173");
  } else {
    await mainWindow.loadFile(path.join(__dirname, "../dist/index.html"));
  }
}

function createTray() {
  const image = nativeImage.createEmpty();
  tray = new Tray(image);
  tray.setToolTip("cursor-switch");
  tray.setContextMenu(
    Menu.buildFromTemplate([
      { label: "打开控制台", click: () => showWindow() },
      {
        label: "退出",
        click: () => {
          app.isQuitting = true;
          app.quit();
        },
      },
    ]),
  );
  tray.on("click", () => showWindow());
}

ipcMain.on("window:minimize", () => mainWindow?.minimize());
ipcMain.on("window:maximize", () => {
  if (!mainWindow) return;
  if (mainWindow.isMaximized()) mainWindow.unmaximize();
  else mainWindow.maximize();
});
ipcMain.on("window:close", () => mainWindow?.close());

app.whenReady().then(async () => {
  const ok = await ensureBackend();
  if (!ok) {
    await dialog.showErrorBox(
      "cursor-switch",
      `无法拉起或连接控制面 ${CONTROL_URL}。请确认 conda 环境 cursor-switch 已安装后端。`,
    );
  }
  createTray();
  await createWindow();
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) void createWindow();
    else showWindow();
  });
});

app.on("before-quit", () => {
  app.isQuitting = true;
  if (backend && !backend.killed) backend.kill();
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});
