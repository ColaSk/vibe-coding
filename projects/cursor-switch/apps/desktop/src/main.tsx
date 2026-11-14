import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { App } from "./App";
import { initializeI18n } from "./i18n/store";
import { applyTheme, isThemeId } from "./shared/theme/theme";
import "./i18n/runtime";
import "./styles/globals.scss";

initializeI18n();
const savedTheme = localStorage.getItem("cursor-switch.theme");
applyTheme(isThemeId(savedTheme) ? savedTheme : "default-dark");

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
