import type { ComponentProps } from "react";
import styles from "./Card.module.scss";

export function Card({ className, ...props }: ComponentProps<"div">) {
  return <div {...props} className={[styles.root, className].filter(Boolean).join(" ")} />;
}
