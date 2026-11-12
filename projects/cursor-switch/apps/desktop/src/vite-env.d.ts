/// <reference types="vite/client" />

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
