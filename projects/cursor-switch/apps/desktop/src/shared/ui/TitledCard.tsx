import type { ReactNode } from "react";
import { Card } from "./Card";
import styles from "./TitledCard.module.scss";

export function TitledCard({
  title,
  actions,
  children,
  className,
}: {
  title: ReactNode;
  actions?: ReactNode;
  children: ReactNode;
  className?: string;
}) {
  return (
    <Card className={[styles.root, className].filter(Boolean).join(" ")}>
      <div className={styles.header}>
        <h3 className={styles.title}>{title}</h3>
        {actions}
      </div>
      <div className={styles.body}>{children}</div>
    </Card>
  );
}
