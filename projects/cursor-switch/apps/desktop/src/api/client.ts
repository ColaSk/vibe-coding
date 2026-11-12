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

export type OverviewStats = {
  model_count: number;
  enabled_model_count: number;
  call_count: number;
  total_input_tokens: number;
  total_output_tokens: number;
  avg_first_token_ms: number | null;
};

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

export async function fetchOverview(controlUrl: string): Promise<OverviewStats> {
  return request<OverviewStats>(`${base(controlUrl)}/api/overview`);
}

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
  };
}
