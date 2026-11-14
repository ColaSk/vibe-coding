export type HealthResponse = {
  status: string;
  service: string;
};

export type Model = {
  id: string;
  display_name: string;
  provider_type: "openai_chat" | "openai_responses" | "anthropic";
  base_url: string;
  api_key: string;
  model_name: string;
  notes: string;
  context_tokens: number;
  max_output_tokens: number;
  enabled: boolean;
  sort_order: number;
  extra: Record<string, unknown>;
  headers: Record<string, string>;
  group_name: string;
};

export type ModelInput = Omit<Model, "id">;

export type HarnessStatus = {
  enabled: boolean;
  ca: "missing" | "untrusted" | "ready" | "invalid" | string;
  integration: string;
  mode: "passthrough" | "intercept" | string;
  proxy_url: string | null;
  proxy_port: number | null;
  ca_install_command: string | null;
};

export type PortSettings = {
  proxy_port: number;
  service_port: number;
};

export type ProxySettings = {
  mode: string;
  address: string;
  auth_enabled: boolean;
  username: string;
  password: string;
};

export type DesktopSettings = {
  silent_start: boolean;
  show_dock_icon: boolean;
};

export type OverviewBucket = {
  bucket_start_ms: number;
  input_tokens: number;
  output_tokens: number;
  cache_read_tokens: number;
  cache_write_tokens: number;
  first_token_sum: number;
  first_token_count: number;
  calls: number;
};

export type OverviewStats = {
  model_count: number;
  enabled_model_count: number;
  call_count: number;
  total_input_tokens: number;
  total_output_tokens: number;
  avg_first_token_ms: number | null;
  successful_calls: number;
  failed_calls: number;
  cache_read_tokens: number;
  cache_write_tokens: number;
  estimated_value: number;
  token_usage_granularity: string;
  token_usage_series: OverviewBucket[];
};

export type CallSummary = {
  id: string;
  model_id: string;
  display_name: string;
  provider_type: string;
  model_name: string;
  status: string;
  created_at_ms: number;
  first_token_ms: number | null;
  duration_ms: number | null;
  input_tokens: number;
  output_tokens: number;
  cache_read_tokens: number;
  cache_write_tokens: number;
  error_message: string;
  detailed: boolean;
  request_json?: string;
  response_text?: string;
};

export type TabSettings = { mode: "direct" | "custom"; address: string };
export type PricingSettings = {
  input_per_million: number;
  output_per_million: number;
  cache_read_per_million: number;
  cache_write_per_million: number;
};
export type StorageStats = { call_count: number; trace_count: number };

export type ConnectivityResult = {
  ok: boolean;
  first_token_ms: number | null;
  total_ms: number;
  text: string;
  error: string | null;
  usage: Record<string, number> | null;
};

function base(url: string): string {
  return url.replace(/\/$/, "");
}

function formatApiError(status: number, body: string): string {
  const trimmed = body.trim();
  if (!trimmed) return `${status}: ${status}`;
  try {
    const parsed = JSON.parse(trimmed) as { detail?: unknown };
    if (typeof parsed.detail === "string" && parsed.detail) return parsed.detail;
  } catch {
    /* keep raw body */
  }
  return trimmed;
}

async function request<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
  });
  if (!response.ok) {
    const body = await response.text();
    throw new Error(formatApiError(response.status, body || response.statusText));
  }
  if (response.status === 204) {
    return undefined as T;
  }
  return (await response.json()) as T;
}

export async function fetchHealth(controlUrl: string): Promise<HealthResponse> {
  return request<HealthResponse>(`${base(controlUrl)}/healthz`);
}

export async function listModels(controlUrl: string): Promise<Model[]> {
  return request<Model[]>(`${base(controlUrl)}/api/models`);
}

export async function createModel(controlUrl: string, payload: ModelInput): Promise<Model> {
  return request<Model>(`${base(controlUrl)}/api/models`, {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export async function updateModel(
  controlUrl: string,
  id: string,
  payload: ModelInput,
): Promise<Model> {
  return request<Model>(`${base(controlUrl)}/api/models/${encodeURIComponent(id)}`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}

export async function deleteModel(controlUrl: string, id: string): Promise<void> {
  return request<void>(`${base(controlUrl)}/api/models/${encodeURIComponent(id)}`, {
    method: "DELETE",
  });
}

export async function testModel(
  controlUrl: string,
  id: string,
): Promise<ConnectivityResult> {
  return request<ConnectivityResult>(
    `${base(controlUrl)}/api/models/${encodeURIComponent(id)}/test`,
    { method: "POST" },
  );
}

export async function fetchHarness(controlUrl: string): Promise<HarnessStatus> {
  return request<HarnessStatus>(`${base(controlUrl)}/api/harness/cursor/status`);
}

export async function initializeCa(controlUrl: string): Promise<HarnessStatus> {
  return request<HarnessStatus>(`${base(controlUrl)}/api/harness/cursor/ca/initialize`, {
    method: "POST",
  });
}

export async function setHarnessEnabled(
  controlUrl: string,
  enabled: boolean,
): Promise<HarnessStatus> {
  return request<HarnessStatus>(`${base(controlUrl)}/api/harness/cursor/enabled`, {
    method: "PUT",
    body: JSON.stringify({ enabled }),
  });
}

export async function setHarnessMode(
  controlUrl: string,
  mode: "passthrough" | "intercept",
): Promise<HarnessStatus> {
  return request<HarnessStatus>(`${base(controlUrl)}/api/harness/cursor/mode`, {
    method: "PUT",
    body: JSON.stringify({ mode }),
  });
}

export type TrafficEvent = {
  ts: number;
  event: string;
  host: string;
  port: number;
  mode: string;
  cursor_host: boolean;
  bytes_up: number;
  bytes_down: number;
  path: string | null;
  status: number | null;
  error: string | null;
};

export type TrafficLog = {
  events: TrafficEvent[];
};

export async function fetchTraffic(
  controlUrl: string,
  limit = 80,
): Promise<TrafficLog> {
  return request<TrafficLog>(
    `${base(controlUrl)}/api/harness/cursor/traffic?limit=${limit}`,
  );
}

export async function clearTraffic(controlUrl: string): Promise<TrafficLog> {
  return request<TrafficLog>(`${base(controlUrl)}/api/harness/cursor/traffic`, {
    method: "DELETE",
  });
}

export async function fetchPorts(controlUrl: string): Promise<PortSettings> {
  return request<PortSettings>(`${base(controlUrl)}/api/settings/ports`);
}

export async function updatePorts(
  controlUrl: string,
  payload: PortSettings,
): Promise<PortSettings> {
  return request<PortSettings>(`${base(controlUrl)}/api/settings/ports`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}

export async function fetchProxy(controlUrl: string): Promise<ProxySettings> {
  return request<ProxySettings>(`${base(controlUrl)}/api/settings/proxy`);
}

export async function updateProxy(
  controlUrl: string,
  payload: ProxySettings,
): Promise<ProxySettings> {
  return request<ProxySettings>(`${base(controlUrl)}/api/settings/proxy`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}

export async function fetchDesktopSettings(controlUrl: string): Promise<DesktopSettings> {
  return request<DesktopSettings>(`${base(controlUrl)}/api/settings/desktop`);
}

export async function updateDesktopSettings(
  controlUrl: string,
  payload: DesktopSettings,
): Promise<DesktopSettings> {
  return request<DesktopSettings>(`${base(controlUrl)}/api/settings/desktop`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}

export async function fetchOverview(
  controlUrl: string,
  query?: { startMs?: number; endMs?: number; modelIds?: string[] },
): Promise<OverviewStats> {
  const params = new URLSearchParams();
  if (query?.startMs != null) params.set("start_ms", String(query.startMs));
  if (query?.endMs != null) params.set("end_ms", String(query.endMs));
  if (query?.modelIds?.length) params.set("model_ids", query.modelIds.join(","));
  const suffix = params.size ? `?${params}` : "";
  return request<OverviewStats>(`${base(controlUrl)}/api/overview${suffix}`);
}

export async function listCalls(controlUrl: string): Promise<CallSummary[]> {
  return request<CallSummary[]>(`${base(controlUrl)}/api/calls`);
}

export async function fetchCall(controlUrl: string, id: string): Promise<CallSummary> {
  return request<CallSummary>(`${base(controlUrl)}/api/calls/${encodeURIComponent(id)}`);
}

export async function discoverModels(
  controlUrl: string,
  payload: { provider_type: string; base_url: string; api_key: string; headers: Record<string, string> },
): Promise<string[]> {
  const result = await request<{ model_ids: string[] }>(`${base(controlUrl)}/api/models/discover`, {
    method: "POST",
    body: JSON.stringify(payload),
  });
  return result.model_ids;
}

export async function updateModelGroup(
  controlUrl: string,
  payload: { group_name: string; base_url?: string; api_key?: string },
): Promise<Model[]> {
  return request<Model[]>(`${base(controlUrl)}/api/models/group`, {
    method: "PUT",
    body: JSON.stringify(payload),
  });
}

export async function reorderModels(controlUrl: string, orderedIds: string[]): Promise<Model[]> {
  return request<Model[]>(`${base(controlUrl)}/api/models/order`, {
    method: "PUT",
    body: JSON.stringify({ ordered_ids: orderedIds }),
  });
}

async function getJson<T>(controlUrl: string, path: string): Promise<T> {
  return request<T>(`${base(controlUrl)}${path}`);
}

async function putJson<T>(controlUrl: string, path: string, payload: unknown): Promise<T> {
  return request<T>(`${base(controlUrl)}${path}`, { method: "PUT", body: JSON.stringify(payload) });
}

export const fetchObservation = (url: string) => getJson<{ detailed: boolean }>(url, "/api/settings/observation");
export const updateObservation = (url: string, detailed: boolean) =>
  putJson<{ detailed: boolean }>(url, "/api/settings/observation", { detailed });
export const fetchTab = (url: string) => getJson<TabSettings>(url, "/api/settings/tab");
export const updateTab = (url: string, payload: TabSettings) => putJson<TabSettings>(url, "/api/settings/tab", payload);
export const fetchCommit = (url: string) => getJson<{ model_id: string }>(url, "/api/settings/commit");
export const updateCommit = (url: string, modelId: string) =>
  putJson<{ model_id: string }>(url, "/api/settings/commit", { model_id: modelId });
export const fetchPricing = (url: string) => getJson<PricingSettings>(url, "/api/settings/pricing");
export const updatePricing = (url: string, payload: PricingSettings) =>
  putJson<PricingSettings>(url, "/api/settings/pricing", payload);
export const fetchStorage = (url: string) => getJson<StorageStats>(url, "/api/storage");
export const clearStorage = (url: string, scope: "details" | "all") =>
  request<StorageStats>(`${base(url)}/api/storage?scope=${scope}`, { method: "DELETE" });

export function emptyModelInput(): ModelInput {
  return {
    display_name: "",
    provider_type: "openai_responses",
    base_url: "",
    api_key: "",
    model_name: "",
    notes: "",
    context_tokens: 128_000,
    max_output_tokens: 8_192,
    enabled: true,
    sort_order: 0,
    extra: {},
    headers: {},
    group_name: "",
  };
}

export const controlUrl =
  (import.meta.env.VITE_CONTROL_URL as string | undefined) ?? "http://127.0.0.1:8787";
