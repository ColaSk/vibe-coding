/// <reference types="vite/client" />
/// <reference path="./i18n/global.d.ts" />
/// <reference path="./monaco.d.ts" />

interface ElectronAPI {
  windowMinimize: () => void;
  windowMaximize: () => void;
  windowClose: () => void;
}

interface Window {
  electronAPI?: ElectronAPI;
}

declare module "*.module.scss" {
  const classes: Record<string, string>;
  export default classes;
}
