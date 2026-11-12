import type { ReactNode } from "react";
import styles from "./PageContent.module.scss";

export function PageContent({ title, children }: { title: ReactNode; children: ReactNode }) {
  return (
    <div className={styles.root}>
      <h1 className={styles.title}>{title}</h1>
      <div className={styles.body}>{children}</div>
    </div>
  );
}

export { styles as pageStyles };
