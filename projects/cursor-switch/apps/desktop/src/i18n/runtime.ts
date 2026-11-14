export type Locale = "zh-CN" | "en-US" | "pt-BR";
export type CommitPromptLocale = "zh-CN" | "en-US";
export type TranslationValue = string | number;
export type TranslationParams = Readonly<Record<string, TranslationValue>>;

export function commitPromptLocale(locale: Locale): CommitPromptLocale {
  return locale === "zh-CN" ? "zh-CN" : "en-US";
}

export function setRuntimeLocale(_locale: Locale) {
  // cursor-switch ships Chinese UI only.
}

export function t(source: string, params?: TranslationParams): string {
  if (!params) return source;
  return source.replace(/\{([A-Za-z_][A-Za-z0-9_]*)\}/g, (_match, name: string) => {
    if (!Object.prototype.hasOwnProperty.call(params, name)) {
      throw new Error(`Missing i18n parameter: ${name}`);
    }
    return String(params[name]);
  });
}

(globalThis as { t?: typeof t }).t = t;
