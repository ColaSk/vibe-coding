import { api, type DesktopSettings } from "../api";
import { desktopPlatform } from "./platform";

export function hasNativeAppLifecycle(): boolean {
  return Boolean(window.electronAPI);
}

export function hasDockVisibilitySetting(): boolean {
  return hasNativeAppLifecycle() && desktopPlatform() === "macos";
}

export async function currentAppVersion(): Promise<string> {
  return "0.1.0";
}

export async function readAutostart(): Promise<boolean> {
  const settings = await api.desktopSettings();
  return settings.silent_start;
}

export async function writeAutostart(enabled: boolean): Promise<void> {
  const settings = await api.desktopSettings();
  await api.setDesktopSettings({ ...settings, silent_start: enabled });
}

export async function readDesktopSettings(): Promise<DesktopSettings> {
  return api.desktopSettings();
}

export async function writeSilentStart(silentStart: boolean): Promise<void> {
  const settings = await readDesktopSettings();
  await api.setDesktopSettings({ ...settings, silent_start: silentStart });
}

export async function writeDockIconVisibility(visible: boolean): Promise<void> {
  const settings = await readDesktopSettings();
  await api.setDesktopSettings({ ...settings, show_dock_icon: visible });
}

export type AppUpdate = {
  version: string;
  install(): Promise<void>;
  close(): Promise<void>;
};

export async function checkForUpdate(): Promise<AppUpdate | null> {
  return null;
}

export async function relaunchApp(): Promise<void> {
  window.location.reload();
}
