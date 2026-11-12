import type { ComponentProps, ReactNode } from "react";
import styles from "./Field.module.scss";

export function Field({
  label,
  className,
  children,
  ...props
}: ComponentProps<"label"> & { label: ReactNode }) {
  return (
    <label {...props} className={[styles.root, className].filter(Boolean).join(" ")}>
      {label}
      {children}
    </label>
  );
}
