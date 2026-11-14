import type { CommitPromptLocale, Locale } from "../i18n/runtime";

export type ModelType = "openai" | "anthropic";

export interface Model {
  model_hash: string;
  sort_order: number;
  display_name: string;
  group_name: string | null;
  type: ModelType;
  base_url: string;
  use_full_url: boolean;
  api_key: string;
  tooltip_data: string;
  model_id: string;
  reasoning_effort: string | null;
  openai_endpoint: string;
  openai_extra_params_enabled: boolean;
  openai_extra_params: Record<string, unknown>;
  custom_headers_enabled: boolean;
  custom_headers: Record<string, string>;
  anthropic_extra_params_enabled: boolean;
  anthropic_extra_params: Record<string, unknown>;
  context_window_tokens: number | null;
  max_completion_tokens: number | null;
  anthropic_max_tokens: number | null;
  anthropic_thinking_effort: string | null;
  thinking_budget_tokens: number | null;
  input_per_million: number;
  output_per_million: number;
  cache_read_per_million: number;
  cache_write_per_million: number;
  created_at_ms: number;
  updated_at_ms: number;
}

export interface ModelInput {
  sort_order: number;
  display_name: string;
  group_name: string | null;
  type: ModelType;
  base_url: string;
  use_full_url: boolean;
  api_key: string;
  tooltip_data: string;
  model_id: string;
  reasoning_effort: string | null;
  openai_endpoint: string;
  openai_extra_params_enabled: boolean;
  openai_extra_params: Record<string, unknown>;
  custom_headers_enabled: boolean;
  custom_headers: Record<string, string>;
  anthropic_extra_params_enabled: boolean;
  anthropic_extra_params: Record<string, unknown>;
  context_window_tokens: number | null;
  max_completion_tokens: number | null;
  anthropic_max_tokens: number | null;
  anthropic_thinking_effort: string | null;
  thinking_budget_tokens: number | null;
  input_per_million: number;
  output_per_million: number;
  cache_read_per_million: number;
  cache_write_per_million: number;
}

export interface ModelDiscoveryInput {
  type: ModelType;
  base_url: string;
  api_key: string;
  custom_headers_enabled: boolean;
  custom_headers: Record<string, string>;
}

export interface LegacyModelImportPreviewItem {
  model_hash: string;
  display_name: string;
  model_id: string;
  type: ModelType;
  existing: boolean;
}

export interface LegacyModelImportPreview {
  source: string;
  total: number;
  new_models: number;
  existing_models: number;
  models: LegacyModelImportPreviewItem[];
}

export interface LegacyModelImportResult {
  imported: number;
  skipped: number;
  total: number;
}

export interface ModelConnectivityResult {
  duration_ms: number;
  first_valid_response_ms: number | null;
  output_tokens: number;
  tokens_per_second: number;
  tokens_estimated: boolean;
  output: string;
}

export type CaState = "missing" | "untrusted" | "ready" | "invalid";
export type IntegrationState = "disabled" | "enabled" | "degraded";
export interface CursorHarnessStatus {
  platform: string;
  ca: CaState;
  configured_models: number;
  enabled_models: number;
  integration: IntegrationState;
  settings_applied: boolean;
  proxy_url: string | null;
  ca_install_command: string | null;
}

export interface PortSettings {
  proxy_port: number;
  service_port: number;
}

export interface ExternalApiSettings {
  enabled: boolean;
  api_key: string;
}

export interface StatisticsStorage {
  call_count: number;
  trace_count: number;
}

export type StatisticsStorageScope = "details" | "all";
export type ProxyMode = "default" | "custom";

export interface ProxySettings {
  mode: ProxyMode;
  address: string;
  auth_enabled: boolean;
  username: string;
  has_password: boolean;
}

export interface ProxySettingsInput {
  mode: ProxyMode;
  address: string;
  auth_enabled: boolean;
  username: string;
  password?: string;
}

export type TabMode = "direct" | "custom";

export interface TabSettings {
  mode: TabMode;
  address: string;
}

export interface CursorPathSettings {
  path: string;
  default_path: string;
  effective_path: string;
}

export interface DesktopSettings {
  silent_start: boolean;
  show_dock_icon: boolean;
}

export interface CommitSettings {
  model_id: string;
  prompt: string;
  prompt_locale: CommitPromptLocale;
}

export interface CommitSettingsView extends CommitSettings {
  default_prompt: string;
}

export interface TokenPricingSettings {
  input_per_million: number;
  output_per_million: number;
  cache_read_per_million: number;
  cache_write_per_million: number;
}

export type PluginRuntimeState = "uninitialized" | "initializing" | "ready" | "failed" | "unsupported";
export type PluginRuntimePhase = "checking" | "downloading" | "verifying" | "installing" | "validating";

export interface PluginRuntimeStatus {
  state: PluginRuntimeState;
  version: string;
  phase: PluginRuntimePhase | null;
  progress: number | null;
  error: string | null;
}

export interface PluginModelDescriptor {
  id: string;
  displayName: string;
  modelId: string;
  enabled: boolean;
  icon?: string | null;
  pluginName?: string;
  pluginId?: string;
  providerId?: string;
}

export interface PluginProviderDescriptor {
  id: string;
  displayName: Record<string, string> | string;
  configured: boolean;
  models: PluginModelDescriptor[];
}

export interface PluginDescriptor {
  id: string;
  name?: string;
  providers: PluginProviderDescriptor[];
}

export type PluginOAuthBegin = { sessionId: string; url: string };
export type PluginOAuthPoll = { status: string };
export type PluginImportFile = { name: string; content: string };
export type PluginImportResult = { imported: number };
export type PluginResourceActionResult = { ok: boolean };

export function pluginText(value: Record<string, string> | string | undefined, locale: Locale): string {
  if (!value) return "";
  if (typeof value === "string") return value;
  return value[locale] || value["zh-CN"] || value["en-US"] || Object.values(value)[0] || "";
}

export function configuredPluginModels(_plugins: PluginDescriptor[]): PluginModelDescriptor[] {
  return [];
}

export interface OverviewMetrics {
  llm_calls: number;
  successful_calls: number;
  failed_calls: number;
  token_usage: number;
  prompt_tokens: number;
  input_tokens: number;
  cache_read_tokens: number;
  cache_write_tokens: number;
  output_tokens: number;
}

export type TokenUsageGranularity = "minute" | "hour" | "day";

export interface OverviewTokenUsageBucket {
  bucket_start_ms: number;
  input_tokens: number;
  cache_read_tokens: number;
  cache_write_tokens: number;
  output_tokens: number;
}

export interface Overview {
  metrics: OverviewMetrics;
  token_usage_granularity: TokenUsageGranularity;
  token_usage_series: OverviewTokenUsageBucket[];
  estimated_value: number;
  estimated_cache_value: number;
}

export interface LlmCall {
  call_kind: "provider_llm" | "cursor_official";
  route: "local" | "cursor_official";
  call_id: string;
  run_id: string;
  conversation_id: string;
  provider_call_index: number;
  model_hash: string | null;
  provider_type: string;
  provider_url: string;
  request_type: string;
  request_url: string;
  model_id: string;
  display_name: string;
  reasoning_effort: string | null;
  fast: boolean | null;
  status: string;
  finish_reason: string | null;
  created_at_ms: number;
  ttfb_ms: number | null;
  ttft_ms: number | null;
  ttfr_ms: number | null;
  duration_ms: number | null;
  input_tokens: number | null;
  output_tokens: number | null;
  total_tokens: number | null;
  cache_read_tokens: number | null;
  cache_write_tokens: number | null;
  reasoning_tokens: number | null;
  message_count: number;
  tool_count: number;
  http_status: number | null;
  error_kind: string | null;
  error_message: string | null;
  detailed: boolean;
}

export interface CallDetail {
  call: LlmCall;
  request: { headers: unknown; body: unknown; byte_count: number } | null;
  response_chunks: Array<{ seq: number; received_offset_ms: number; data: string; byte_count: number }>;
  cursor_trace: {
    trace: {
      request_id: string;
      conversation_id: string | null;
      route: "local" | "cursor_official";
      model_id: string | null;
      status: string;
      request_bytes: number;
      response_bytes: number;
      response_event_count: number;
      http_status: number | null;
      received_at_ms: number;
      first_response_at_ms: number | null;
      finished_at_ms: number | null;
      error_message: string | null;
    };
    artifacts: Array<{
      seq: number;
      artifact_type: string;
      source: string;
      metadata: unknown;
      created_at_ms: number;
      byte_count: number;
      encoding: "utf8" | "base64";
      data: string;
    }>;
  } | null;
}

type SwitchModel = {
  id: string;
  display_name: string;
  provider_type: string;
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
  group_name?: string;
};

const CONTROL =
  (import.meta.env.VITE_CONTROL_URL as string | undefined) ?? "http://127.0.0.1:8787";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  let response: Response;
  try {
    response = await fetch(`${CONTROL}${path}`, {
      ...init,
      headers: init?.body
        ? { "content-type": "application/json", ...init.headers }
        : init?.headers,
    });
  } catch (cause) {
    throw new Error("无法连接本地管理服务", { cause });
  }
  if (!response.ok) {
    const body = await response.text();
    let message = body;
    try {
      const parsed = JSON.parse(body) as { detail?: unknown; message?: unknown };
      if (typeof parsed.detail === "string") message = parsed.detail;
      else if (typeof parsed.message === "string") message = parsed.message;
    } catch {
      // keep body
    }
    throw new Error(message || `${response.status} ${response.statusText}`);
  }
  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}

function providerToType(provider: string): ModelType {
  return provider === "anthropic" ? "anthropic" : "openai";
}

function typeToProvider(type: ModelType, endpoint: string): string {
  if (type === "anthropic") return "anthropic";
  return endpoint === "responses" ? "openai_responses" : "openai_chat";
}

const DEFAULT_MODEL_PRICING = {
  input_per_million: 5.0,
  output_per_million: 25.0,
  cache_read_per_million: 0.5,
  cache_write_per_million: 6.25,
};

function pricingFromExtra(extra: Record<string, unknown>, key: keyof typeof DEFAULT_MODEL_PRICING): number {
  const raw = extra[key];
  const value = typeof raw === "number" ? raw : Number(raw);
  return Number.isFinite(value) && value >= 0 ? value : DEFAULT_MODEL_PRICING[key];
}

function fromSwitch(row: SwitchModel): Model {
  const extra = row.extra ?? {};
  return {
    model_hash: row.id,
    sort_order: row.sort_order,
    display_name: row.display_name,
    group_name: row.group_name || (typeof extra.group_name === "string" ? extra.group_name : null),
    type: providerToType(row.provider_type),
    base_url: row.base_url,
    use_full_url: Boolean(extra.use_full_url),
    api_key: row.api_key,
    tooltip_data: row.notes || String(extra.tooltip_data ?? ""),
    model_id: row.model_name,
    reasoning_effort: (extra.reasoning_effort as string | null) ?? null,
    openai_endpoint: String(extra.openai_endpoint ?? (row.provider_type === "openai_responses" ? "responses" : "chat_completions")),
    openai_extra_params_enabled: Boolean(extra.openai_extra_params_enabled),
    openai_extra_params: (extra.openai_extra_params as Record<string, unknown>) ?? {},
    custom_headers_enabled: Object.keys(row.headers || {}).length > 0 || Boolean(extra.custom_headers_enabled),
    custom_headers: row.headers || {},
    anthropic_extra_params_enabled: Boolean(extra.anthropic_extra_params_enabled),
    anthropic_extra_params: (extra.anthropic_extra_params as Record<string, unknown>) ?? {},
    context_window_tokens: row.context_tokens,
    max_completion_tokens: row.max_output_tokens,
    anthropic_max_tokens: (extra.anthropic_max_tokens as number | null) ?? row.max_output_tokens,
    anthropic_thinking_effort: (extra.anthropic_thinking_effort as string | null) ?? null,
    thinking_budget_tokens: (extra.thinking_budget_tokens as number | null) ?? null,
    input_per_million: pricingFromExtra(extra, "input_per_million"),
    output_per_million: pricingFromExtra(extra, "output_per_million"),
    cache_read_per_million: pricingFromExtra(extra, "cache_read_per_million"),
    cache_write_per_million: pricingFromExtra(extra, "cache_write_per_million"),
    created_at_ms: 0,
    updated_at_ms: 0,
  };
}

function toSwitch(input: ModelInput): Omit<SwitchModel, "id"> {
  return {
    display_name: input.display_name,
    provider_type: typeToProvider(input.type, input.openai_endpoint),
    base_url: input.base_url,
    api_key: input.api_key,
    model_name: input.model_id,
    notes: input.tooltip_data,
    context_tokens: input.context_window_tokens ?? 128_000,
    max_output_tokens: input.max_completion_tokens ?? input.anthropic_max_tokens ?? 8_192,
    enabled: true,
    sort_order: input.sort_order,
    headers: input.custom_headers_enabled ? input.custom_headers : {},
    group_name: input.group_name ?? "",
    extra: {
      use_full_url: input.use_full_url,
      reasoning_effort: input.reasoning_effort,
      openai_endpoint: input.openai_endpoint,
      openai_extra_params_enabled: input.openai_extra_params_enabled,
      openai_extra_params: input.openai_extra_params,
      custom_headers_enabled: input.custom_headers_enabled,
      anthropic_extra_params_enabled: input.anthropic_extra_params_enabled,
      anthropic_extra_params: input.anthropic_extra_params,
      anthropic_max_tokens: input.anthropic_max_tokens,
      anthropic_thinking_effort: input.anthropic_thinking_effort,
      thinking_budget_tokens: input.thinking_budget_tokens,
      group_name: input.group_name,
      input_per_million: input.input_per_million,
      output_per_million: input.output_per_million,
      cache_read_per_million: input.cache_read_per_million,
      cache_write_per_million: input.cache_write_per_million,
    },
  };
}

function mapCall(row: Record<string, unknown>): LlmCall {
  const input = Number(row.input_tokens ?? 0);
  const output = Number(row.output_tokens ?? 0);
  return {
    call_kind: "provider_llm",
    route: "local",
    call_id: String(row.id ?? ""),
    run_id: "",
    conversation_id: "",
    provider_call_index: 0,
    model_hash: String(row.model_id ?? "") || null,
    provider_type: String(row.provider_type ?? ""),
    provider_url: "",
    request_type: "chat",
    request_url: "",
    model_id: String(row.model_name || row.model_id || ""),
    display_name: String(row.display_name ?? ""),
    reasoning_effort: null,
    fast: null,
    status: String(row.status ?? "ok") === "ok" ? "completed" : "failed",
    finish_reason: null,
    created_at_ms: Number(row.created_at_ms ?? 0),
    ttfb_ms: null,
    ttft_ms: row.first_token_ms == null ? null : Number(row.first_token_ms),
    ttfr_ms: null,
    duration_ms: row.duration_ms == null ? null : Number(row.duration_ms),
    input_tokens: input,
    output_tokens: output,
    total_tokens: input + output,
    cache_read_tokens: Number(row.cache_read_tokens ?? 0),
    cache_write_tokens: Number(row.cache_write_tokens ?? 0),
    reasoning_tokens: null,
    message_count: 0,
    tool_count: 0,
    http_status: null,
    error_kind: row.error_message ? "error" : null,
    error_message: String(row.error_message ?? "") || null,
    detailed: Boolean(row.detailed),
  };
}

function mapOverview(raw: Record<string, unknown>): Overview {
  const input = Number(raw.total_input_tokens ?? 0);
  const output = Number(raw.total_output_tokens ?? 0);
  const cacheRead = Number(raw.cache_read_tokens ?? 0);
  const cacheWrite = Number(raw.cache_write_tokens ?? 0);
  const series = Array.isArray(raw.token_usage_series)
    ? (raw.token_usage_series as Array<Record<string, number>>).map((bucket) => ({
      bucket_start_ms: Number(bucket.bucket_start_ms ?? 0),
      input_tokens: Number(bucket.input_tokens ?? 0),
      cache_read_tokens: Number(bucket.cache_read_tokens ?? 0),
      cache_write_tokens: Number(bucket.cache_write_tokens ?? 0),
      output_tokens: Number(bucket.output_tokens ?? 0),
    }))
    : [];
  return {
    metrics: {
      llm_calls: Number(raw.call_count ?? 0),
      successful_calls: Number(raw.successful_calls ?? 0),
      failed_calls: Number(raw.failed_calls ?? 0),
      token_usage: input + output + cacheRead + cacheWrite,
      prompt_tokens: input + cacheRead + cacheWrite,
      input_tokens: input,
      cache_read_tokens: cacheRead,
      cache_write_tokens: cacheWrite,
      output_tokens: output,
    },
    token_usage_granularity: (raw.token_usage_granularity as TokenUsageGranularity) || "day",
    token_usage_series: series,
    estimated_value: Number(raw.estimated_value ?? 0),
    estimated_cache_value: Number(raw.estimated_cache_value ?? 0),
  };
}

export const api = {
  ads: async () => ({ slots: [] }),
  dismissAd: async () => undefined,
  models: async () => (await request<SwitchModel[]>("/api/models")).map(fromSwitch),
  createModels: async (models: ModelInput[]) => {
    const created: Model[] = [];
    for (const model of models) {
      created.push(fromSwitch(await request<SwitchModel>("/api/models", { method: "POST", body: JSON.stringify(toSwitch(model)) })));
    }
    return created;
  },
  reorderModels: async (modelHashes: string[]) =>
    (await request<SwitchModel[]>("/api/models/order", {
      method: "PUT",
      body: JSON.stringify({ ordered_ids: modelHashes }),
    })).map(fromSwitch),
  discoverModels: async (input: ModelDiscoveryInput) => {
    const result = await request<{ model_ids: string[] }>("/api/models/discover", {
      method: "POST",
      body: JSON.stringify({
        provider_type: typeToProvider(input.type, "chat_completions"),
        base_url: input.base_url,
        api_key: input.api_key,
        headers: input.custom_headers_enabled ? input.custom_headers : {},
      }),
    });
    return { models: result.model_ids };
  },
  previewV0049Models: async (): Promise<LegacyModelImportPreview> => ({
    source: "",
    total: 0,
    new_models: 0,
    existing_models: 0,
    models: [],
  }),
  importV0049Models: async (): Promise<LegacyModelImportResult> => ({ imported: 0, skipped: 0, total: 0 }),
  updateModel: async (hash: string, model: ModelInput) =>
    fromSwitch(await request<SwitchModel>(`/api/models/${encodeURIComponent(hash)}`, {
      method: "PUT",
      body: JSON.stringify(toSwitch(model)),
    })),
  deleteModel: (hash: string) => request<void>(`/api/models/${encodeURIComponent(hash)}`, { method: "DELETE" }),
  testModel: async (hash: string, _testId: string, _signal?: AbortSignal) => {
    const result = await request<{
      ok: boolean;
      first_token_ms: number | null;
      total_ms: number;
      text: string;
      error: string | null;
      usage: Record<string, number> | null;
    }>(`/api/models/${encodeURIComponent(hash)}/test`, { method: "POST" });
    if (!result.ok) throw new Error(result.error || "测试失败");
    const outputTokens = result.usage?.output_tokens ?? 0;
    const duration = Math.max(1, result.total_ms);
    return {
      duration_ms: result.total_ms,
      first_valid_response_ms: result.first_token_ms,
      output_tokens: outputTokens,
      tokens_per_second: (outputTokens * 1000) / duration,
      tokens_estimated: false,
      output: result.text,
    } satisfies ModelConnectivityResult;
  },
  cancelModelTest: async (_hash?: string, _testId?: string) => undefined,
  overview: async (filter?: { startMs: number; endMs: number; modelHashes?: string[]; bucketMs?: number }) => {
    const params = new URLSearchParams();
    if (filter) {
      params.set("start_ms", String(filter.startMs));
      params.set("end_ms", String(filter.endMs));
      if (filter.modelHashes?.length) params.set("model_ids", filter.modelHashes.join(","));
    }
    const query = params.toString();
    return mapOverview(await request<Record<string, unknown>>(`/api/overview${query ? `?${query}` : ""}`));
  },
  cursorHarness: async () => {
    const [status, models] = await Promise.all([
      request<{
        enabled: boolean;
        ca: CaState;
        integration: string;
        proxy_url: string | null;
        ca_install_command: string | null;
      }>("/api/harness/cursor/status"),
      request<SwitchModel[]>("/api/models"),
    ]);
    return {
      platform: navigator.platform,
      ca: status.ca,
      configured_models: models.length,
      enabled_models: models.filter((model) => model.enabled).length,
      integration: status.enabled ? "enabled" : "disabled",
      settings_applied: status.enabled,
      proxy_url: status.proxy_url,
      ca_install_command: status.ca_install_command,
    } satisfies CursorHarnessStatus;
  },
  initializeCursorCa: async () => {
    await request("/api/harness/cursor/ca/initialize", { method: "POST" });
    return api.cursorHarness();
  },
  plugins: async () => [] as PluginDescriptor[],
  pluginOAuthBegin: async () => ({ sessionId: "", url: "" }),
  pluginOAuthPoll: async () => ({ status: "idle" }),
  importPluginResources: async () => ({ imported: 0 }),
  refreshPluginResource: async () => undefined,
  pluginResourceAction: async () => ({ ok: false }),
  deletePluginResource: async () => undefined,
  syncPluginModels: async () => ({ models: 0 }),
  setPluginModelEnabled: async () => undefined,
  pluginResourceExportUrl: () => "",
  removePluginConfiguration: async (_pluginId?: string) => undefined,
  pluginRuntime: async (): Promise<PluginRuntimeStatus> => ({
    state: "unsupported",
    version: "",
    phase: null,
    progress: null,
    error: null,
  }),
  initializePluginRuntime: async () => api.pluginRuntime(),
  cancelPluginRuntimeInitialization: async () => api.pluginRuntime(),
  openCursorCaInstallTerminal: async (command: string) => {
    await navigator.clipboard.writeText(command);
  },
  copyCursorText: async (text: string) => {
    await navigator.clipboard.writeText(text);
  },
  setCursorEnabled: async (enabled: boolean) => {
    await request("/api/harness/cursor/enabled", { method: "PUT", body: JSON.stringify({ enabled }) });
    return api.cursorHarness();
  },
  calls: async () => (await request<Record<string, unknown>[]>("/api/calls")).map(mapCall),
  call: async (id: string): Promise<CallDetail> => {
    const row = await request<Record<string, unknown>>(`/api/calls/${encodeURIComponent(id)}`);
    const call = mapCall(row);
    const requestJson = String(row.request_json ?? "");
    const responseText = String(row.response_text ?? "");
    let body: unknown = requestJson;
    try {
      body = requestJson ? JSON.parse(requestJson) : null;
    } catch {
      // keep raw
    }
    return {
      call,
      request: call.detailed && requestJson
        ? { headers: {}, body, byte_count: requestJson.length }
        : null,
      response_chunks: call.detailed && responseText
        ? [{ seq: 0, received_offset_ms: 0, data: responseText, byte_count: responseText.length }]
        : [],
      cursor_trace: null,
    };
  },
  openCallDetails: async (id: string) => {
    window.location.hash = `#/calls/${encodeURIComponent(id)}`;
  },
  openExternalUrl: async (url: string) => {
    window.open(url, "_blank", "noopener,noreferrer");
  },
  observability: () => request<{ detailed: boolean }>("/api/settings/observation"),
  setObservability: (detailed: boolean) =>
    request<{ detailed: boolean }>("/api/settings/observation", {
      method: "PUT",
      body: JSON.stringify({ detailed }),
    }),
  ports: () => request<PortSettings>("/api/settings/ports"),
  setPorts: (settings: PortSettings) =>
    request<PortSettings>("/api/settings/ports", { method: "PUT", body: JSON.stringify(settings) }),
  externalApiSettings: async (): Promise<ExternalApiSettings> => ({ enabled: false, api_key: "" }),
  setExternalApiSettings: async (settings: ExternalApiSettings) => settings,
  statisticsStorage: () => request<StatisticsStorage>("/api/storage"),
  clearStatisticsStorage: (scope: StatisticsStorageScope) =>
    request<StatisticsStorage>(`/api/storage?scope=${scope}`, { method: "DELETE" }),
  proxySettings: async () => {
    const proxy = await request<{
      mode: ProxyMode;
      address: string;
      auth_enabled: boolean;
      username: string;
      password: string;
    }>("/api/settings/proxy");
    return {
      mode: proxy.mode,
      address: proxy.address,
      auth_enabled: proxy.auth_enabled,
      username: proxy.username,
      has_password: Boolean(proxy.password),
    } satisfies ProxySettings;
  },
  setProxySettings: async (settings: ProxySettingsInput) => {
    await request("/api/settings/proxy", { method: "PUT", body: JSON.stringify(settings) });
    return api.proxySettings();
  },
  tabSettings: () => request<TabSettings>("/api/settings/tab"),
  setTabSettings: (settings: TabSettings) =>
    request<TabSettings>("/api/settings/tab", { method: "PUT", body: JSON.stringify(settings) }),
  cursorPathSettings: () => request<CursorPathSettings>("/api/settings/cursor-path"),
  setCursorPathSettings: (path: string) =>
    request<CursorPathSettings>("/api/settings/cursor-path", {
      method: "PUT",
      body: JSON.stringify({ path }),
    }),
  desktopSettings: () => request<DesktopSettings>("/api/settings/desktop"),
  setDesktopSettings: (settings: DesktopSettings) =>
    request<DesktopSettings>("/api/settings/desktop", { method: "PUT", body: JSON.stringify(settings) }),
  commitSettings: async (_locale: Locale): Promise<CommitSettingsView> => {
    const commit = await request<{ model_id: string }>("/api/settings/commit");
    return {
      model_id: commit.model_id,
      prompt: "",
      prompt_locale: "zh-CN",
      default_prompt: "",
    };
  },
  setCommitSettings: async (settings: CommitSettings): Promise<CommitSettingsView> => {
    await request("/api/settings/commit", {
      method: "PUT",
      body: JSON.stringify({ model_id: settings.model_id }),
    });
    return {
      ...settings,
      default_prompt: "",
    };
  },
  pricingSettings: () => request<TokenPricingSettings>("/api/settings/pricing"),
  setPricingSettings: (settings: TokenPricingSettings) =>
    request<TokenPricingSettings>("/api/settings/pricing", {
      method: "PUT",
      body: JSON.stringify(settings),
    }),
};
