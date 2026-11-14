import { useSyncExternalStore } from "react";
import { setRuntimeLocale, type Locale } from "./runtime";

export type LocalePreference = "system" | Locale;

type I18nSnapshot = {
  preference: LocalePreference;
  locale: Locale;
};

const listeners = new Set<() => void>();
let snapshot: I18nSnapshot = { preference: "zh-CN", locale: "zh-CN" };

export function initializeI18n() {
  setRuntimeLocale("zh-CN");
  document.documentElement.lang = "zh-CN";
}

export function setLocalePreference(preference: LocalePreference) {
  const locale = preference === "system" ? "zh-CN" : preference;
  snapshot = { preference, locale };
  setRuntimeLocale(locale);
  listeners.forEach((listener) => listener());
}

export function useI18n() {
  return useSyncExternalStore(
    (listener) => {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    () => snapshot,
  );
}
