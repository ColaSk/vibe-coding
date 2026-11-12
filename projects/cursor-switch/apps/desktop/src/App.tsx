import { HashRouter, Navigate, Route, Routes } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { ModelsPage } from "./pages/ModelsPage";
import { SettingsPage } from "./pages/SettingsPage";
import { AppFrame } from "./shell/AppFrame";
import { AppLayout } from "./shell/AppLayout";

export function App() {
  return (
    <HashRouter>
      <Routes>
        <Route element={<AppFrame />}>
          <Route element={<AppLayout />}>
            <Route index element={<HomePage />} />
            <Route path="models" element={<ModelsPage />} />
            <Route path="settings" element={<SettingsPage />} />
          </Route>
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </HashRouter>
  );
}
