"""Host and path routing rules for Cursor traffic."""

from __future__ import annotations

# MITM stamps the original Cursor URL so local handlers can re-fetch upstream.
UPSTREAM_URL_HEADER = "x-cursor-switch-upstream-url"

LOCAL_PATHS = frozenset(
    {
        "/agent/v1/run",  # modern Cursor agent WebSocket (wss)
        "/agent.v1.AgentService/RunSSE",
        "/aiserver.v1.InferenceService/RunInferenceSSE",
        "/aiserver.v1.BidiService/BidiAppend",

        "/aiserver.v1.AiService/AvailableDocs",
        "/aiserver.v1.DashboardService/GetEffectiveUserPlugins",
        "/aiserver.v1.DashboardService/GetUserPrivacyMode",
        "/agent.v1.AgentService/UpdateConversationMetadata",
        "/aiserver.v1.AiService/GetServerConfig",
        "/aiserver.v1.ServerConfigService/GetServerConfig",
        "/aiserver.v1.AiService/AvailableModels",
        "/agent.v1.AgentService/GetUsableModels",
        "/aiserver.v1.AiService/GetUsableModels",
        "/agent.v1.AgentService/GetDefaultModelForCli",
        "/aiserver.v1.AiService/GetDefaultModelForCli",
        "/aiserver.v1.AiService/GetDefaultModel",
        "/aiserver.v1.AiService/GetDefaultModelNudgeData",
        "/aiserver.v1.AuthService/GetEmail",
        "/aiserver.v1.AuthService/GetUserMeta",
        "/aiserver.v1.DashboardService/GetMe",
        "/aiserver.v1.DashboardService/GetTeams",
        "/aiserver.v1.DashboardService/GetUserProfile",
        "/aiserver.v1.DashboardService/GetCurrentPeriodUsage",
        "/aiserver.v1.DashboardService/GetUsageLimitStatusAndActiveGrants",
        "/aiserver.v1.AiService/KnowledgeBaseAdd",
        "/aiserver.v1.AiService/KnowledgeBaseList",
        "/aiserver.v1.AiService/KnowledgeBaseUpdate",
        "/aiserver.v1.AiService/KnowledgeBaseRemove",
        "/aiserver.v1.AiService/WriteGitCommitMessage",
        "/aiserver.v1.NetworkService/IsConnected",
        "/aiserver.v1.AnalyticsService/BootstrapStatsig",
        "/auth/full_stripe_profile",
        "/auth/stripe_profile",
    }
)

TAB_PATHS = frozenset(
    {
        "/aiserver.v1.AiService/StreamCpp",
        "/aiserver.v1.AiService/StreamNextCursorPrediction",
        "/aiserver.v1.AiService/GetCppEditClassification",
        "/aiserver.v1.AiService/RefreshTabContext",
        "/aiserver.v1.AiService/CppConfig",
        "/aiserver.v1.AiService/CppEditHistoryStatus",
        "/aiserver.v1.AiService/CppAppend",
        "/aiserver.v1.AiService/CppEditHistoryAppend",
        "/aiserver.v1.AiService/ReportAiCodeChangeMetrics",
        "/aiserver.v1.AiService/WriteGitBranchName",
        "/aiserver.v1.CppService/AvailableModels",
        "/aiserver.v1.CppService/RecordCppFate",
        "/aiserver.v1.FileSyncService/FSSyncFile",
        "/aiserver.v1.FileSyncService/FSIsEnabledForUser",
        "/aiserver.v1.FileSyncService/FSConfig",
        "/aiserver.v1.FileSyncService/FSUploadFile",
    }
)

def is_cursor_host(host: str) -> bool:
    host = host.strip(".").lower()
    return host in {"api2.cursor.sh", "api3.cursor.sh"} or host.endswith(".cursor.sh")


def should_route_locally(path: str) -> bool:
    """Tab always goes upstream; Agent and account paths stay local."""
    if path in TAB_PATHS:
        return False
    return path in LOCAL_PATHS


def upstream_url(
    path: str,
    host: str,
    *,
    local: bool,
    backend_host: str,
    backend_port: int,
    tab_mode: str = "direct",
    tab_address: str = "",
) -> str:
    """Pick the upstream for one MITM request.

    Tab modes: direct keeps the original Cursor host; custom rewrites to the
    configured address.
    """
    if local:
        return f"http://{backend_host}:{backend_port}{path}"
    route_path = path.split("?", 1)[0]
    if route_path in TAB_PATHS and tab_mode == "custom" and tab_address.strip():
        return f"{tab_address.rstrip('/')}{path}"
    return f"https://{host}{path}"
