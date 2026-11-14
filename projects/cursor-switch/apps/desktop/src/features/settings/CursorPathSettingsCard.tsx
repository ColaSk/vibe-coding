import cursorIconUrl from "../../shared/assets/icons/cursor.svg";
import type { CursorPathSettings } from "../../shared/api";
import { Button } from "../../shared/ui/Button";
import { TextInput } from "../../shared/ui/FormControls";
import { Icon } from "../../shared/ui/Icon";
import { TitledCard } from "../../shared/ui/TitledCard";
import styles from "./ProxySettingsCard.module.scss";

export function CursorPathSettingsCard({
  settings,
  draft,
  editing,
  saving,
  onDraftChange,
  onEdit,
  onCancel,
  onSave,
}: {
  settings: CursorPathSettings | null;
  draft: string;
  editing: boolean;
  saving: boolean;
  onDraftChange: (path: string) => void;
  onEdit: () => void;
  onCancel: () => void;
  onSave: () => void;
}) {
  const action = editing ? (
    <div className={styles.actionGroup}>
      <Button size="small" disabled={saving} onClick={onCancel}>{t("取消")}</Button>
      <Button variant="primary" size="small" disabled={saving} onClick={onSave}>{saving ? t("保存中…") : t("保存")}</Button>
    </div>
  ) : (
    <button type="button" className={styles.headerAction} disabled={!settings} onClick={onEdit}>{t("编辑")}</button>
  );

  return <TitledCard
    title={<div style={{ display: "flex", alignItems: "center", gap: 6 }}>
      <Icon src={cursorIconUrl} size="1.1em" />
      <span>{t("Cursor 路径")}</span>
    </div>}
    action={action}
  >
    <div className={styles.content}>
      {editing ? (
        <div className={styles.row}>
          <div>
            <strong>{t("settings.json 路径")}</strong>
            <small style={{ display: "block", marginTop: 4, color: "var(--vscode-descriptionForeground)" }}>
              {t("留空使用默认路径。可填 settings.json、User 目录，或 Cursor 用户数据目录。修改前需关闭接管。")}
            </small>
          </div>
          <div className={styles.control} style={{ width: "min(520px, 70%)" }}>
            <TextInput
              value={draft}
              placeholder={settings?.default_path ?? ""}
              aria-label={t("Cursor 路径")}
              onChange={(event) => onDraftChange(event.target.value)}
              onKeyDown={(event) => { if (event.key === "Enter") onSave(); }}
            />
          </div>
        </div>
      ) : settings ? (
        <>
          <div className={styles.row}>
            <strong>{t("配置路径")}</strong>
            <span className={styles.value}>{settings.path ? settings.path : t("默认")}</span>
          </div>
          <div className={styles.row}>
            <strong>{t("生效路径")}</strong>
            <span className={styles.value}>{settings.effective_path}</span>
          </div>
        </>
      ) : (
        <div className={styles.row}>
          <strong>{t("生效路径")}</strong>
          <span className={styles.value}>{t("加载中…")}</span>
        </div>
      )}
    </div>
  </TitledCard>;
}
