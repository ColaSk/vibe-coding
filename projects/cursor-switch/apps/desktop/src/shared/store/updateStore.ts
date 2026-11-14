import { useSyncExternalStore } from "react";

type UpdateSnapshot = {
  checking: boolean;
  installing: boolean;
  availableVersion: string | null;
  error: string | null;
};

let snapshot: UpdateSnapshot = {
  checking: false,
  installing: false,
  availableVersion: null,
  error: null,
};

const listeners = new Set<() => void>();

function notify() {
  listeners.forEach((listener) => listener());
}

export const updateStore = {
  subscribe(listener: () => void) {
    listeners.add(listener);
    return () => listeners.delete(listener);
  },
  getSnapshot: () => snapshot,
  async check() {
    snapshot = { ...snapshot, checking: false, availableVersion: null, error: null };
    notify();
    return null as string | null;
  },
  async install() {
    return;
  },
};

export function useUpdateStore() {
  return useSyncExternalStore(updateStore.subscribe, updateStore.getSnapshot);
}
