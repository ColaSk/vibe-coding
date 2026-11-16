from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentHostBackgroundWorkKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_HOST_BACKGROUND_WORK_KIND_UNSPECIFIED: _ClassVar[AgentHostBackgroundWorkKind]
    AGENT_HOST_BACKGROUND_WORK_KIND_SHELL: _ClassVar[AgentHostBackgroundWorkKind]
    AGENT_HOST_BACKGROUND_WORK_KIND_SUBAGENT: _ClassVar[AgentHostBackgroundWorkKind]

class AgentHostBackgroundWorkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_HOST_BACKGROUND_WORK_STATE_UNSPECIFIED: _ClassVar[AgentHostBackgroundWorkState]
    AGENT_HOST_BACKGROUND_WORK_STATE_RUNNING: _ClassVar[AgentHostBackgroundWorkState]
    AGENT_HOST_BACKGROUND_WORK_STATE_QUEUED: _ClassVar[AgentHostBackgroundWorkState]

class AgentHostInteractionResponseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_HOST_INTERACTION_RESPONSE_STATUS_UNSPECIFIED: _ClassVar[AgentHostInteractionResponseStatus]
    AGENT_HOST_INTERACTION_RESPONSE_STATUS_ACCEPTED: _ClassVar[AgentHostInteractionResponseStatus]
    AGENT_HOST_INTERACTION_RESPONSE_STATUS_ALREADY_RESOLVED: _ClassVar[AgentHostInteractionResponseStatus]
    AGENT_HOST_INTERACTION_RESPONSE_STATUS_NOT_FOUND: _ClassVar[AgentHostInteractionResponseStatus]

class AgentHostSessionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_HOST_SESSION_STATUS_UNSPECIFIED: _ClassVar[AgentHostSessionStatus]
    AGENT_HOST_SESSION_STATUS_IDLE: _ClassVar[AgentHostSessionStatus]
    AGENT_HOST_SESSION_STATUS_RUNNING: _ClassVar[AgentHostSessionStatus]
    AGENT_HOST_SESSION_STATUS_AWAITING_INPUT: _ClassVar[AgentHostSessionStatus]

class AgentHostTurnOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_HOST_TURN_OUTCOME_UNSPECIFIED: _ClassVar[AgentHostTurnOutcome]
    AGENT_HOST_TURN_OUTCOME_COMPLETED: _ClassVar[AgentHostTurnOutcome]
    AGENT_HOST_TURN_OUTCOME_INTERRUPTED: _ClassVar[AgentHostTurnOutcome]
    AGENT_HOST_TURN_OUTCOME_FAILED: _ClassVar[AgentHostTurnOutcome]

class AgentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_MODE_UNSPECIFIED: _ClassVar[AgentMode]
    AGENT_MODE_AGENT: _ClassVar[AgentMode]
    AGENT_MODE_ASK: _ClassVar[AgentMode]
    AGENT_MODE_PLAN: _ClassVar[AgentMode]
    AGENT_MODE_DEBUG: _ClassVar[AgentMode]
    AGENT_MODE_TRIAGE: _ClassVar[AgentMode]
    AGENT_MODE_PROJECT: _ClassVar[AgentMode]
    AGENT_MODE_MULTITASK: _ClassVar[AgentMode]
    AGENT_MODE_CUSTOM: _ClassVar[AgentMode]

class AgentStoreClaimMountKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_STORE_CLAIM_MOUNT_KIND_UNSPECIFIED: _ClassVar[AgentStoreClaimMountKind]
    AGENT_STORE_CLAIM_MOUNT_KIND_SELF: _ClassVar[AgentStoreClaimMountKind]
    AGENT_STORE_CLAIM_MOUNT_KIND_USER: _ClassVar[AgentStoreClaimMountKind]
    AGENT_STORE_CLAIM_MOUNT_KIND_TEAM: _ClassVar[AgentStoreClaimMountKind]
    AGENT_STORE_CLAIM_MOUNT_KIND_AUTOMATION: _ClassVar[AgentStoreClaimMountKind]
    AGENT_STORE_CLAIM_MOUNT_KIND_CLOUD_PEER: _ClassVar[AgentStoreClaimMountKind]

class ArtifactPathErrorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_PATH_ERROR_KIND_UNSPECIFIED: _ClassVar[ArtifactPathErrorKind]
    ARTIFACT_PATH_ERROR_KIND_MISSING: _ClassVar[ArtifactPathErrorKind]
    ARTIFACT_PATH_ERROR_KIND_PERMISSION: _ClassVar[ArtifactPathErrorKind]
    ARTIFACT_PATH_ERROR_KIND_NOT_A_FILE: _ClassVar[ArtifactPathErrorKind]
    ARTIFACT_PATH_ERROR_KIND_INVALID_PATH: _ClassVar[ArtifactPathErrorKind]
    ARTIFACT_PATH_ERROR_KIND_UNKNOWN: _ClassVar[ArtifactPathErrorKind]

class ArtifactRestoreStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_RESTORE_STATUS_UNSPECIFIED: _ClassVar[ArtifactRestoreStatus]
    ARTIFACT_RESTORE_STATUS_RESTORED: _ClassVar[ArtifactRestoreStatus]
    ARTIFACT_RESTORE_STATUS_SKIPPED_ALREADY_EXISTS: _ClassVar[ArtifactRestoreStatus]
    ARTIFACT_RESTORE_STATUS_REJECTED: _ClassVar[ArtifactRestoreStatus]

class ArtifactUploadDispatchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_UPLOAD_DISPATCH_STATUS_UNSPECIFIED: _ClassVar[ArtifactUploadDispatchStatus]
    ARTIFACT_UPLOAD_DISPATCH_STATUS_ACCEPTED: _ClassVar[ArtifactUploadDispatchStatus]
    ARTIFACT_UPLOAD_DISPATCH_STATUS_REJECTED: _ClassVar[ArtifactUploadDispatchStatus]
    ARTIFACT_UPLOAD_DISPATCH_STATUS_SKIPPED_ALREADY_IN_PROGRESS: _ClassVar[ArtifactUploadDispatchStatus]

class ArtifactUploadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_UPLOAD_STATUS_UNSPECIFIED: _ClassVar[ArtifactUploadStatus]
    ARTIFACT_UPLOAD_STATUS_NOT_STARTED: _ClassVar[ArtifactUploadStatus]
    ARTIFACT_UPLOAD_STATUS_IN_PROGRESS: _ClassVar[ArtifactUploadStatus]
    ARTIFACT_UPLOAD_STATUS_COMPLETED: _ClassVar[ArtifactUploadStatus]
    ARTIFACT_UPLOAD_STATUS_FAILED: _ClassVar[ArtifactUploadStatus]

class BackgroundTaskCompletionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_TASK_COMPLETION_REASON_UNSPECIFIED: _ClassVar[BackgroundTaskCompletionReason]
    BACKGROUND_TASK_COMPLETION_REASON_TASK_FINISHED: _ClassVar[BackgroundTaskCompletionReason]
    BACKGROUND_TASK_COMPLETION_REASON_TASK_PROGRESS: _ClassVar[BackgroundTaskCompletionReason]

class BackgroundTaskKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_TASK_KIND_UNSPECIFIED: _ClassVar[BackgroundTaskKind]
    BACKGROUND_TASK_KIND_SHELL: _ClassVar[BackgroundTaskKind]
    BACKGROUND_TASK_KIND_SUBAGENT: _ClassVar[BackgroundTaskKind]

class BackgroundTaskNotificationContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_TASK_NOTIFICATION_CONTEXT_UNSPECIFIED: _ClassVar[BackgroundTaskNotificationContext]
    BACKGROUND_TASK_NOTIFICATION_CONTEXT_USER_DRIVEN_INTERACTIVE_CHILD: _ClassVar[BackgroundTaskNotificationContext]

class BackgroundTaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BACKGROUND_TASK_STATUS_UNSPECIFIED: _ClassVar[BackgroundTaskStatus]
    BACKGROUND_TASK_STATUS_SUCCESS: _ClassVar[BackgroundTaskStatus]
    BACKGROUND_TASK_STATUS_ERROR: _ClassVar[BackgroundTaskStatus]
    BACKGROUND_TASK_STATUS_ABORTED: _ClassVar[BackgroundTaskStatus]

class BatchGetDiffErrorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATCH_GET_DIFF_ERROR_KIND_UNSPECIFIED: _ClassVar[BatchGetDiffErrorKind]
    BATCH_GET_DIFF_ERROR_KIND_FETCH_FAILED: _ClassVar[BatchGetDiffErrorKind]
    BATCH_GET_DIFF_ERROR_KIND_DIFF_FAILED: _ClassVar[BatchGetDiffErrorKind]
    BATCH_GET_DIFF_ERROR_KIND_UNAUTHENTICATED: _ClassVar[BatchGetDiffErrorKind]
    BATCH_GET_DIFF_ERROR_KIND_NOT_FOUND: _ClassVar[BatchGetDiffErrorKind]
    BATCH_GET_DIFF_ERROR_KIND_INTERNAL: _ClassVar[BatchGetDiffErrorKind]

class BugfixVerdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUGFIX_VERDICT_UNSPECIFIED: _ClassVar[BugfixVerdict]
    BUGFIX_VERDICT_FIXED: _ClassVar[BugfixVerdict]
    BUGFIX_VERDICT_FALSE_POSITIVE: _ClassVar[BugfixVerdict]
    BUGFIX_VERDICT_COULD_NOT_FIX: _ClassVar[BugfixVerdict]
    BUGFIX_VERDICT_RESOLVED_BY_OTHER_FIX: _ClassVar[BugfixVerdict]

class ClickType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLICK_TYPE_UNSPECIFIED: _ClassVar[ClickType]
    CLICK_TYPE_SINGLE: _ClassVar[ClickType]
    CLICK_TYPE_DOUBLE: _ClassVar[ClickType]
    CLICK_TYPE_TRIPLE: _ClassVar[ClickType]
    CLICK_TYPE_RIGHT: _ClassVar[ClickType]
    CLICK_TYPE_MIDDLE: _ClassVar[ClickType]

class ConversationSearchSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONVERSATION_SEARCH_SOURCE_UNSPECIFIED: _ClassVar[ConversationSearchSource]
    CONVERSATION_SEARCH_SOURCE_LOCAL: _ClassVar[ConversationSearchSource]
    CONVERSATION_SEARCH_SOURCE_CLOUD_CACHE: _ClassVar[ConversationSearchSource]

class CursorRuleSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURSOR_RULE_SOURCE_UNSPECIFIED: _ClassVar[CursorRuleSource]
    CURSOR_RULE_SOURCE_TEAM: _ClassVar[CursorRuleSource]
    CURSOR_RULE_SOURCE_USER: _ClassVar[CursorRuleSource]

class CursorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURSOR_TYPE_UNSPECIFIED: _ClassVar[CursorType]
    CURSOR_TYPE_ARROW: _ClassVar[CursorType]
    CURSOR_TYPE_POINTER: _ClassVar[CursorType]
    CURSOR_TYPE_TEXT: _ClassVar[CursorType]
    CURSOR_TYPE_WAIT: _ClassVar[CursorType]
    CURSOR_TYPE_CROSSHAIR: _ClassVar[CursorType]
    CURSOR_TYPE_MOVE: _ClassVar[CursorType]
    CURSOR_TYPE_RESIZE_NS: _ClassVar[CursorType]
    CURSOR_TYPE_RESIZE_EW: _ClassVar[CursorType]
    CURSOR_TYPE_RESIZE_NWSE: _ClassVar[CursorType]
    CURSOR_TYPE_RESIZE_NESW: _ClassVar[CursorType]
    CURSOR_TYPE_NOT_ALLOWED: _ClassVar[CursorType]
    CURSOR_TYPE_GRAB: _ClassVar[CursorType]
    CURSOR_TYPE_GRABBING: _ClassVar[CursorType]

class CustomModeSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOM_MODE_SOURCE_UNSPECIFIED: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_AGENT_SKILL: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_PLUGIN_SKILL: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_REPO_SKILL: _ClassVar[CustomModeSource]
    CUSTOM_MODE_SOURCE_MANAGED_SKILL: _ClassVar[CustomModeSource]

class CustomSubagentPermissionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOM_SUBAGENT_PERMISSION_MODE_UNSPECIFIED: _ClassVar[CustomSubagentPermissionMode]
    CUSTOM_SUBAGENT_PERMISSION_MODE_DEFAULT: _ClassVar[CustomSubagentPermissionMode]
    CUSTOM_SUBAGENT_PERMISSION_MODE_READONLY: _ClassVar[CustomSubagentPermissionMode]
    CUSTOM_SUBAGENT_PERMISSION_MODE_AGENT_ONLY: _ClassVar[CustomSubagentPermissionMode]

class DiagnosticSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIAGNOSTIC_SEVERITY_UNSPECIFIED: _ClassVar[DiagnosticSeverity]
    DIAGNOSTIC_SEVERITY_ERROR: _ClassVar[DiagnosticSeverity]
    DIAGNOSTIC_SEVERITY_WARNING: _ClassVar[DiagnosticSeverity]
    DIAGNOSTIC_SEVERITY_INFORMATION: _ClassVar[DiagnosticSeverity]
    DIAGNOSTIC_SEVERITY_HINT: _ClassVar[DiagnosticSeverity]

class EntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTRY_TYPE_UNSPECIFIED: _ClassVar[EntryType]
    ENTRY_TYPE_FILE: _ClassVar[EntryType]
    ENTRY_TYPE_DIRECTORY: _ClassVar[EntryType]
    ENTRY_TYPE_SYMLINK: _ClassVar[EntryType]

class ForceBackgroundShellStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORCE_BACKGROUND_SHELL_STATUS_UNSPECIFIED: _ClassVar[ForceBackgroundShellStatus]
    FORCE_BACKGROUND_SHELL_STATUS_ACCEPTED: _ClassVar[ForceBackgroundShellStatus]
    FORCE_BACKGROUND_SHELL_STATUS_NOT_FOUND: _ClassVar[ForceBackgroundShellStatus]

class ForceBackgroundSubagentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORCE_BACKGROUND_SUBAGENT_STATUS_UNSPECIFIED: _ClassVar[ForceBackgroundSubagentStatus]
    FORCE_BACKGROUND_SUBAGENT_STATUS_ACCEPTED: _ClassVar[ForceBackgroundSubagentStatus]
    FORCE_BACKGROUND_SUBAGENT_STATUS_NOT_FOUND: _ClassVar[ForceBackgroundSubagentStatus]

class GoalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GOAL_STATUS_UNSPECIFIED: _ClassVar[GoalStatus]
    GOAL_STATUS_ACTIVE: _ClassVar[GoalStatus]
    GOAL_STATUS_PAUSED: _ClassVar[GoalStatus]
    GOAL_STATUS_COMPLETE: _ClassVar[GoalStatus]
    GOAL_STATUS_CLEARED: _ClassVar[GoalStatus]

class IdleClassification(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDLE_CLASSIFICATION_UNSPECIFIED: _ClassVar[IdleClassification]
    IDLE_CLASSIFICATION_LOADING_WAIT: _ClassVar[IdleClassification]
    IDLE_CLASSIFICATION_VIEWING_RESULT: _ClassVar[IdleClassification]
    IDLE_CLASSIFICATION_THINKING_PAUSE: _ClassVar[IdleClassification]
    IDLE_CLASSIFICATION_LONG_OPERATION: _ClassVar[IdleClassification]

class KeystrokeEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEYSTROKE_EVENT_TYPE_UNSPECIFIED: _ClassVar[KeystrokeEventType]
    KEYSTROKE_EVENT_TYPE_KEY_COMBO: _ClassVar[KeystrokeEventType]
    KEYSTROKE_EVENT_TYPE_KEY_SINGLE: _ClassVar[KeystrokeEventType]
    KEYSTROKE_EVENT_TYPE_TEXT_TYPED: _ClassVar[KeystrokeEventType]

class LocalPromptQualityInvocationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_UNSPECIFIED: _ClassVar[LocalPromptQualityInvocationStatus]
    LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_SUCCESS: _ClassVar[LocalPromptQualityInvocationStatus]
    LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_ERRORED: _ClassVar[LocalPromptQualityInvocationStatus]
    LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_ABORTED: _ClassVar[LocalPromptQualityInvocationStatus]

class MotionStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOTION_STYLE_UNSPECIFIED: _ClassVar[MotionStyle]
    MOTION_STYLE_SLOW: _ClassVar[MotionStyle]
    MOTION_STYLE_MELLOW: _ClassVar[MotionStyle]
    MOTION_STYLE_QUICK: _ClassVar[MotionStyle]
    MOTION_STYLE_RAPID: _ClassVar[MotionStyle]

class MountedAgentStoreKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOUNTED_AGENT_STORE_KIND_UNSPECIFIED: _ClassVar[MountedAgentStoreKind]
    MOUNTED_AGENT_STORE_KIND_SELF: _ClassVar[MountedAgentStoreKind]
    MOUNTED_AGENT_STORE_KIND_PEER: _ClassVar[MountedAgentStoreKind]
    MOUNTED_AGENT_STORE_KIND_SHARE: _ClassVar[MountedAgentStoreKind]
    MOUNTED_AGENT_STORE_KIND_PRINCIPAL: _ClassVar[MountedAgentStoreKind]

class MouseButton(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOUSE_BUTTON_UNSPECIFIED: _ClassVar[MouseButton]
    MOUSE_BUTTON_LEFT: _ClassVar[MouseButton]
    MOUSE_BUTTON_RIGHT: _ClassVar[MouseButton]
    MOUSE_BUTTON_MIDDLE: _ClassVar[MouseButton]
    MOUSE_BUTTON_BACK: _ClassVar[MouseButton]
    MOUSE_BUTTON_FORWARD: _ClassVar[MouseButton]

class PackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKAGE_TYPE_UNSPECIFIED: _ClassVar[PackageType]
    PACKAGE_TYPE_CURSOR_PROJECT: _ClassVar[PackageType]
    PACKAGE_TYPE_CURSOR_PERSONAL: _ClassVar[PackageType]
    PACKAGE_TYPE_CLAUDE_SKILL: _ClassVar[PackageType]
    PACKAGE_TYPE_CLAUDE_PLUGIN: _ClassVar[PackageType]

class PrivateWorkerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRIVATE_WORKER_STATUS_UNSPECIFIED: _ClassVar[PrivateWorkerStatus]
    PRIVATE_WORKER_STATUS_DISCONNECTED: _ClassVar[PrivateWorkerStatus]
    PRIVATE_WORKER_STATUS_READY: _ClassVar[PrivateWorkerStatus]
    PRIVATE_WORKER_STATUS_CLAIMED: _ClassVar[PrivateWorkerStatus]

class PullRequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PULL_REQUEST_STATUS_UNSPECIFIED: _ClassVar[PullRequestStatus]
    PULL_REQUEST_STATUS_OPEN: _ClassVar[PullRequestStatus]
    PULL_REQUEST_STATUS_CLOSED: _ClassVar[PullRequestStatus]

class RecordingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECORDING_MODE_UNSPECIFIED: _ClassVar[RecordingMode]
    RECORDING_MODE_START_RECORDING: _ClassVar[RecordingMode]
    RECORDING_MODE_SAVE_RECORDING: _ClassVar[RecordingMode]
    RECORDING_MODE_DISCARD_RECORDING: _ClassVar[RecordingMode]

class ReplaceEnvMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLACE_ENV_MODE_UNSPECIFIED: _ClassVar[ReplaceEnvMode]
    REPLACE_ENV_MODE_CUSTOM: _ClassVar[ReplaceEnvMode]
    REPLACE_ENV_MODE_CLEAN_SLATE: _ClassVar[ReplaceEnvMode]
    REPLACE_ENV_MODE_DEFAULT: _ClassVar[ReplaceEnvMode]

class RequestedFilePathRejectedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REQUESTED_FILE_PATH_REJECTED_REASON_UNSPECIFIED: _ClassVar[RequestedFilePathRejectedReason]
    REQUESTED_FILE_PATH_REJECTED_REASON_SLASHES_NOT_ALLOWED: _ClassVar[RequestedFilePathRejectedReason]

class ResponseComparisonDisplayOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_COMPARISON_DISPLAY_ORDER_UNSPECIFIED: _ClassVar[ResponseComparisonDisplayOrder]
    RESPONSE_COMPARISON_DISPLAY_ORDER_PARENT_FIRST: _ClassVar[ResponseComparisonDisplayOrder]
    RESPONSE_COMPARISON_DISPLAY_ORDER_ALTERNATE_FIRST: _ClassVar[ResponseComparisonDisplayOrder]

class ResponseComparisonSkipReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_COMPARISON_SKIP_REASON_UNSPECIFIED: _ClassVar[ResponseComparisonSkipReason]
    RESPONSE_COMPARISON_SKIP_REASON_ALTERNATE_TOOL_CALL: _ClassVar[ResponseComparisonSkipReason]
    RESPONSE_COMPARISON_SKIP_REASON_INFERENCE_ERROR: _ClassVar[ResponseComparisonSkipReason]
    RESPONSE_COMPARISON_SKIP_REASON_TIMEOUT: _ClassVar[ResponseComparisonSkipReason]
    RESPONSE_COMPARISON_SKIP_REASON_CANCELLED: _ClassVar[ResponseComparisonSkipReason]

class ScrollDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCROLL_DIRECTION_UNSPECIFIED: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_UP: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_DOWN: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_LEFT: _ClassVar[ScrollDirection]
    SCROLL_DIRECTION_RIGHT: _ClassVar[ScrollDirection]

class SelectedPluginCapabilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SELECTED_PLUGIN_CAPABILITY_TYPE_UNSPECIFIED: _ClassVar[SelectedPluginCapabilityType]
    SELECTED_PLUGIN_CAPABILITY_TYPE_COMMAND: _ClassVar[SelectedPluginCapabilityType]
    SELECTED_PLUGIN_CAPABILITY_TYPE_SKILL: _ClassVar[SelectedPluginCapabilityType]
    SELECTED_PLUGIN_CAPABILITY_TYPE_SUBAGENT: _ClassVar[SelectedPluginCapabilityType]

class ShellAbortReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHELL_ABORT_REASON_UNSPECIFIED: _ClassVar[ShellAbortReason]
    SHELL_ABORT_REASON_USER_ABORT: _ClassVar[ShellAbortReason]
    SHELL_ABORT_REASON_TIMEOUT: _ClassVar[ShellAbortReason]

class ShellBackgroundReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHELL_BACKGROUND_REASON_UNSPECIFIED: _ClassVar[ShellBackgroundReason]
    SHELL_BACKGROUND_REASON_TIMEOUT: _ClassVar[ShellBackgroundReason]
    SHELL_BACKGROUND_REASON_USER_REQUEST: _ClassVar[ShellBackgroundReason]

class SimulatedMsgReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIMULATED_MSG_REASON_UNSPECIFIED: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_PLAN_EXECUTION: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_COMMIT_REMINDER: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_BACKGROUND_TASK_COMPLETION: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_COMMIT: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_COMMIT_AND_PUSH: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_PUSH: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_CREATE_PR: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_FIX_MERGE_CONFLICTS: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_USER_SENT_TO_SUBAGENT: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_USER_INTERRUPTED_SUBAGENT: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_USER_QUEUED_TO_SUBAGENT: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_BABYSIT_PR_IN_CLOUD: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_CI_PANEL_INVESTIGATE_FAILURE: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_MULTITASK: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_BUILD_IN_PARALLEL: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_MULTITASK_SPLIT_PRS: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_APPLY_LOCALLY: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_CHECKOUT_BRANCH: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_UPDATE_BRANCH: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_PR_TAB_BUGBOT_FIX: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_RUN_BUGBOT_REVIEW: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_RUN_SECURITY_REVIEW: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_FSD_APPLY_FINDING: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_FSD_UNDO_FINDING: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_FSD_START: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_FSD_PR_INTERRUPT: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_SUBSCRIPTION: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_DIFF_TAB_CREATE_BRANCH: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_AGENT_STORE_CONFLICT: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_GOAL_CONTINUATION: _ClassVar[SimulatedMsgReason]
    SIMULATED_MSG_REASON_PROJECT_KICKOFF: _ClassVar[SimulatedMsgReason]

class SmartModeClassifierDecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMART_MODE_CLASSIFIER_DECISION_UNSPECIFIED: _ClassVar[SmartModeClassifierDecision]
    SMART_MODE_CLASSIFIER_DECISION_ALLOW: _ClassVar[SmartModeClassifierDecision]
    SMART_MODE_CLASSIFIER_DECISION_BLOCK: _ClassVar[SmartModeClassifierDecision]

class SubagentBackgroundReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBAGENT_BACKGROUND_REASON_UNSPECIFIED: _ClassVar[SubagentBackgroundReason]
    SUBAGENT_BACKGROUND_REASON_AGENT_REQUEST: _ClassVar[SubagentBackgroundReason]
    SUBAGENT_BACKGROUND_REASON_USER_REQUEST: _ClassVar[SubagentBackgroundReason]
    SUBAGENT_BACKGROUND_REASON_QUEUED_FOLLOW_UP: _ClassVar[SubagentBackgroundReason]

class SubagentExecutionEnvironment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBAGENT_EXECUTION_ENVIRONMENT_UNSPECIFIED: _ClassVar[SubagentExecutionEnvironment]
    SUBAGENT_EXECUTION_ENVIRONMENT_LOCAL: _ClassVar[SubagentExecutionEnvironment]
    SUBAGENT_EXECUTION_ENVIRONMENT_CLOUD: _ClassVar[SubagentExecutionEnvironment]

class SubagentInteractionPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBAGENT_INTERACTION_POLICY_UNSPECIFIED: _ClassVar[SubagentInteractionPolicy]
    SUBAGENT_INTERACTION_POLICY_AUTO_REJECT: _ClassVar[SubagentInteractionPolicy]
    SUBAGENT_INTERACTION_POLICY_BUBBLE_TO_PARENT: _ClassVar[SubagentInteractionPolicy]
    SUBAGENT_INTERACTION_POLICY_SURFACE_TO_USER: _ClassVar[SubagentInteractionPolicy]

class SubagentRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBAGENT_RUN_STATUS_UNSPECIFIED: _ClassVar[SubagentRunStatus]
    SUBAGENT_RUN_STATUS_RUNNING: _ClassVar[SubagentRunStatus]
    SUBAGENT_RUN_STATUS_BACKGROUNDED: _ClassVar[SubagentRunStatus]
    SUBAGENT_RUN_STATUS_SUCCESS: _ClassVar[SubagentRunStatus]
    SUBAGENT_RUN_STATUS_ERROR: _ClassVar[SubagentRunStatus]
    SUBAGENT_RUN_STATUS_ABORTED: _ClassVar[SubagentRunStatus]

class SubscriptionSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_SOURCE_UNSPECIFIED: _ClassVar[SubscriptionSource]
    SUBSCRIPTION_SOURCE_SLACK: _ClassVar[SubscriptionSource]
    SUBSCRIPTION_SOURCE_GITHUB: _ClassVar[SubscriptionSource]
    SUBSCRIPTION_SOURCE_LINEAR: _ClassVar[SubscriptionSource]

class TaskMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_MODE_UNSPECIFIED: _ClassVar[TaskMode]
    TASK_MODE_AGENT: _ClassVar[TaskMode]
    TASK_MODE_PLAN: _ClassVar[TaskMode]

class ThinkingStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    THINKING_STYLE_UNSPECIFIED: _ClassVar[ThinkingStyle]
    THINKING_STYLE_DEFAULT: _ClassVar[ThinkingStyle]
    THINKING_STYLE_CODEX: _ClassVar[ThinkingStyle]
    THINKING_STYLE_GPT5: _ClassVar[ThinkingStyle]

class TimeoutBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIMEOUT_BEHAVIOR_UNSPECIFIED: _ClassVar[TimeoutBehavior]
    TIMEOUT_BEHAVIOR_CANCEL: _ClassVar[TimeoutBehavior]
    TIMEOUT_BEHAVIOR_BACKGROUND: _ClassVar[TimeoutBehavior]

class TmuxSessionKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TMUX_SESSION_KIND_UNSPECIFIED: _ClassVar[TmuxSessionKind]
    TMUX_SESSION_KIND_USER_MANUAL: _ClassVar[TmuxSessionKind]
    TMUX_SESSION_KIND_AGENT_BACKGROUND: _ClassVar[TmuxSessionKind]
    TMUX_SESSION_KIND_AGENT_INTERACTIVE: _ClassVar[TmuxSessionKind]

class TodoStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TODO_STATUS_UNSPECIFIED: _ClassVar[TodoStatus]
    TODO_STATUS_PENDING: _ClassVar[TodoStatus]
    TODO_STATUS_IN_PROGRESS: _ClassVar[TodoStatus]
    TODO_STATUS_COMPLETED: _ClassVar[TodoStatus]
    TODO_STATUS_CANCELLED: _ClassVar[TodoStatus]
AGENT_HOST_BACKGROUND_WORK_KIND_UNSPECIFIED: AgentHostBackgroundWorkKind
AGENT_HOST_BACKGROUND_WORK_KIND_SHELL: AgentHostBackgroundWorkKind
AGENT_HOST_BACKGROUND_WORK_KIND_SUBAGENT: AgentHostBackgroundWorkKind
AGENT_HOST_BACKGROUND_WORK_STATE_UNSPECIFIED: AgentHostBackgroundWorkState
AGENT_HOST_BACKGROUND_WORK_STATE_RUNNING: AgentHostBackgroundWorkState
AGENT_HOST_BACKGROUND_WORK_STATE_QUEUED: AgentHostBackgroundWorkState
AGENT_HOST_INTERACTION_RESPONSE_STATUS_UNSPECIFIED: AgentHostInteractionResponseStatus
AGENT_HOST_INTERACTION_RESPONSE_STATUS_ACCEPTED: AgentHostInteractionResponseStatus
AGENT_HOST_INTERACTION_RESPONSE_STATUS_ALREADY_RESOLVED: AgentHostInteractionResponseStatus
AGENT_HOST_INTERACTION_RESPONSE_STATUS_NOT_FOUND: AgentHostInteractionResponseStatus
AGENT_HOST_SESSION_STATUS_UNSPECIFIED: AgentHostSessionStatus
AGENT_HOST_SESSION_STATUS_IDLE: AgentHostSessionStatus
AGENT_HOST_SESSION_STATUS_RUNNING: AgentHostSessionStatus
AGENT_HOST_SESSION_STATUS_AWAITING_INPUT: AgentHostSessionStatus
AGENT_HOST_TURN_OUTCOME_UNSPECIFIED: AgentHostTurnOutcome
AGENT_HOST_TURN_OUTCOME_COMPLETED: AgentHostTurnOutcome
AGENT_HOST_TURN_OUTCOME_INTERRUPTED: AgentHostTurnOutcome
AGENT_HOST_TURN_OUTCOME_FAILED: AgentHostTurnOutcome
AGENT_MODE_UNSPECIFIED: AgentMode
AGENT_MODE_AGENT: AgentMode
AGENT_MODE_ASK: AgentMode
AGENT_MODE_PLAN: AgentMode
AGENT_MODE_DEBUG: AgentMode
AGENT_MODE_TRIAGE: AgentMode
AGENT_MODE_PROJECT: AgentMode
AGENT_MODE_MULTITASK: AgentMode
AGENT_MODE_CUSTOM: AgentMode
AGENT_STORE_CLAIM_MOUNT_KIND_UNSPECIFIED: AgentStoreClaimMountKind
AGENT_STORE_CLAIM_MOUNT_KIND_SELF: AgentStoreClaimMountKind
AGENT_STORE_CLAIM_MOUNT_KIND_USER: AgentStoreClaimMountKind
AGENT_STORE_CLAIM_MOUNT_KIND_TEAM: AgentStoreClaimMountKind
AGENT_STORE_CLAIM_MOUNT_KIND_AUTOMATION: AgentStoreClaimMountKind
AGENT_STORE_CLAIM_MOUNT_KIND_CLOUD_PEER: AgentStoreClaimMountKind
ARTIFACT_PATH_ERROR_KIND_UNSPECIFIED: ArtifactPathErrorKind
ARTIFACT_PATH_ERROR_KIND_MISSING: ArtifactPathErrorKind
ARTIFACT_PATH_ERROR_KIND_PERMISSION: ArtifactPathErrorKind
ARTIFACT_PATH_ERROR_KIND_NOT_A_FILE: ArtifactPathErrorKind
ARTIFACT_PATH_ERROR_KIND_INVALID_PATH: ArtifactPathErrorKind
ARTIFACT_PATH_ERROR_KIND_UNKNOWN: ArtifactPathErrorKind
ARTIFACT_RESTORE_STATUS_UNSPECIFIED: ArtifactRestoreStatus
ARTIFACT_RESTORE_STATUS_RESTORED: ArtifactRestoreStatus
ARTIFACT_RESTORE_STATUS_SKIPPED_ALREADY_EXISTS: ArtifactRestoreStatus
ARTIFACT_RESTORE_STATUS_REJECTED: ArtifactRestoreStatus
ARTIFACT_UPLOAD_DISPATCH_STATUS_UNSPECIFIED: ArtifactUploadDispatchStatus
ARTIFACT_UPLOAD_DISPATCH_STATUS_ACCEPTED: ArtifactUploadDispatchStatus
ARTIFACT_UPLOAD_DISPATCH_STATUS_REJECTED: ArtifactUploadDispatchStatus
ARTIFACT_UPLOAD_DISPATCH_STATUS_SKIPPED_ALREADY_IN_PROGRESS: ArtifactUploadDispatchStatus
ARTIFACT_UPLOAD_STATUS_UNSPECIFIED: ArtifactUploadStatus
ARTIFACT_UPLOAD_STATUS_NOT_STARTED: ArtifactUploadStatus
ARTIFACT_UPLOAD_STATUS_IN_PROGRESS: ArtifactUploadStatus
ARTIFACT_UPLOAD_STATUS_COMPLETED: ArtifactUploadStatus
ARTIFACT_UPLOAD_STATUS_FAILED: ArtifactUploadStatus
BACKGROUND_TASK_COMPLETION_REASON_UNSPECIFIED: BackgroundTaskCompletionReason
BACKGROUND_TASK_COMPLETION_REASON_TASK_FINISHED: BackgroundTaskCompletionReason
BACKGROUND_TASK_COMPLETION_REASON_TASK_PROGRESS: BackgroundTaskCompletionReason
BACKGROUND_TASK_KIND_UNSPECIFIED: BackgroundTaskKind
BACKGROUND_TASK_KIND_SHELL: BackgroundTaskKind
BACKGROUND_TASK_KIND_SUBAGENT: BackgroundTaskKind
BACKGROUND_TASK_NOTIFICATION_CONTEXT_UNSPECIFIED: BackgroundTaskNotificationContext
BACKGROUND_TASK_NOTIFICATION_CONTEXT_USER_DRIVEN_INTERACTIVE_CHILD: BackgroundTaskNotificationContext
BACKGROUND_TASK_STATUS_UNSPECIFIED: BackgroundTaskStatus
BACKGROUND_TASK_STATUS_SUCCESS: BackgroundTaskStatus
BACKGROUND_TASK_STATUS_ERROR: BackgroundTaskStatus
BACKGROUND_TASK_STATUS_ABORTED: BackgroundTaskStatus
BATCH_GET_DIFF_ERROR_KIND_UNSPECIFIED: BatchGetDiffErrorKind
BATCH_GET_DIFF_ERROR_KIND_FETCH_FAILED: BatchGetDiffErrorKind
BATCH_GET_DIFF_ERROR_KIND_DIFF_FAILED: BatchGetDiffErrorKind
BATCH_GET_DIFF_ERROR_KIND_UNAUTHENTICATED: BatchGetDiffErrorKind
BATCH_GET_DIFF_ERROR_KIND_NOT_FOUND: BatchGetDiffErrorKind
BATCH_GET_DIFF_ERROR_KIND_INTERNAL: BatchGetDiffErrorKind
BUGFIX_VERDICT_UNSPECIFIED: BugfixVerdict
BUGFIX_VERDICT_FIXED: BugfixVerdict
BUGFIX_VERDICT_FALSE_POSITIVE: BugfixVerdict
BUGFIX_VERDICT_COULD_NOT_FIX: BugfixVerdict
BUGFIX_VERDICT_RESOLVED_BY_OTHER_FIX: BugfixVerdict
CLICK_TYPE_UNSPECIFIED: ClickType
CLICK_TYPE_SINGLE: ClickType
CLICK_TYPE_DOUBLE: ClickType
CLICK_TYPE_TRIPLE: ClickType
CLICK_TYPE_RIGHT: ClickType
CLICK_TYPE_MIDDLE: ClickType
CONVERSATION_SEARCH_SOURCE_UNSPECIFIED: ConversationSearchSource
CONVERSATION_SEARCH_SOURCE_LOCAL: ConversationSearchSource
CONVERSATION_SEARCH_SOURCE_CLOUD_CACHE: ConversationSearchSource
CURSOR_RULE_SOURCE_UNSPECIFIED: CursorRuleSource
CURSOR_RULE_SOURCE_TEAM: CursorRuleSource
CURSOR_RULE_SOURCE_USER: CursorRuleSource
CURSOR_TYPE_UNSPECIFIED: CursorType
CURSOR_TYPE_ARROW: CursorType
CURSOR_TYPE_POINTER: CursorType
CURSOR_TYPE_TEXT: CursorType
CURSOR_TYPE_WAIT: CursorType
CURSOR_TYPE_CROSSHAIR: CursorType
CURSOR_TYPE_MOVE: CursorType
CURSOR_TYPE_RESIZE_NS: CursorType
CURSOR_TYPE_RESIZE_EW: CursorType
CURSOR_TYPE_RESIZE_NWSE: CursorType
CURSOR_TYPE_RESIZE_NESW: CursorType
CURSOR_TYPE_NOT_ALLOWED: CursorType
CURSOR_TYPE_GRAB: CursorType
CURSOR_TYPE_GRABBING: CursorType
CUSTOM_MODE_SOURCE_UNSPECIFIED: CustomModeSource
CUSTOM_MODE_SOURCE_AGENT_SKILL: CustomModeSource
CUSTOM_MODE_SOURCE_PLUGIN_SKILL: CustomModeSource
CUSTOM_MODE_SOURCE_REPO_SKILL: CustomModeSource
CUSTOM_MODE_SOURCE_MANAGED_SKILL: CustomModeSource
CUSTOM_SUBAGENT_PERMISSION_MODE_UNSPECIFIED: CustomSubagentPermissionMode
CUSTOM_SUBAGENT_PERMISSION_MODE_DEFAULT: CustomSubagentPermissionMode
CUSTOM_SUBAGENT_PERMISSION_MODE_READONLY: CustomSubagentPermissionMode
CUSTOM_SUBAGENT_PERMISSION_MODE_AGENT_ONLY: CustomSubagentPermissionMode
DIAGNOSTIC_SEVERITY_UNSPECIFIED: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_ERROR: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_WARNING: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_INFORMATION: DiagnosticSeverity
DIAGNOSTIC_SEVERITY_HINT: DiagnosticSeverity
ENTRY_TYPE_UNSPECIFIED: EntryType
ENTRY_TYPE_FILE: EntryType
ENTRY_TYPE_DIRECTORY: EntryType
ENTRY_TYPE_SYMLINK: EntryType
FORCE_BACKGROUND_SHELL_STATUS_UNSPECIFIED: ForceBackgroundShellStatus
FORCE_BACKGROUND_SHELL_STATUS_ACCEPTED: ForceBackgroundShellStatus
FORCE_BACKGROUND_SHELL_STATUS_NOT_FOUND: ForceBackgroundShellStatus
FORCE_BACKGROUND_SUBAGENT_STATUS_UNSPECIFIED: ForceBackgroundSubagentStatus
FORCE_BACKGROUND_SUBAGENT_STATUS_ACCEPTED: ForceBackgroundSubagentStatus
FORCE_BACKGROUND_SUBAGENT_STATUS_NOT_FOUND: ForceBackgroundSubagentStatus
GOAL_STATUS_UNSPECIFIED: GoalStatus
GOAL_STATUS_ACTIVE: GoalStatus
GOAL_STATUS_PAUSED: GoalStatus
GOAL_STATUS_COMPLETE: GoalStatus
GOAL_STATUS_CLEARED: GoalStatus
IDLE_CLASSIFICATION_UNSPECIFIED: IdleClassification
IDLE_CLASSIFICATION_LOADING_WAIT: IdleClassification
IDLE_CLASSIFICATION_VIEWING_RESULT: IdleClassification
IDLE_CLASSIFICATION_THINKING_PAUSE: IdleClassification
IDLE_CLASSIFICATION_LONG_OPERATION: IdleClassification
KEYSTROKE_EVENT_TYPE_UNSPECIFIED: KeystrokeEventType
KEYSTROKE_EVENT_TYPE_KEY_COMBO: KeystrokeEventType
KEYSTROKE_EVENT_TYPE_KEY_SINGLE: KeystrokeEventType
KEYSTROKE_EVENT_TYPE_TEXT_TYPED: KeystrokeEventType
LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_UNSPECIFIED: LocalPromptQualityInvocationStatus
LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_SUCCESS: LocalPromptQualityInvocationStatus
LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_ERRORED: LocalPromptQualityInvocationStatus
LOCAL_PROMPT_QUALITY_INVOCATION_STATUS_ABORTED: LocalPromptQualityInvocationStatus
MOTION_STYLE_UNSPECIFIED: MotionStyle
MOTION_STYLE_SLOW: MotionStyle
MOTION_STYLE_MELLOW: MotionStyle
MOTION_STYLE_QUICK: MotionStyle
MOTION_STYLE_RAPID: MotionStyle
MOUNTED_AGENT_STORE_KIND_UNSPECIFIED: MountedAgentStoreKind
MOUNTED_AGENT_STORE_KIND_SELF: MountedAgentStoreKind
MOUNTED_AGENT_STORE_KIND_PEER: MountedAgentStoreKind
MOUNTED_AGENT_STORE_KIND_SHARE: MountedAgentStoreKind
MOUNTED_AGENT_STORE_KIND_PRINCIPAL: MountedAgentStoreKind
MOUSE_BUTTON_UNSPECIFIED: MouseButton
MOUSE_BUTTON_LEFT: MouseButton
MOUSE_BUTTON_RIGHT: MouseButton
MOUSE_BUTTON_MIDDLE: MouseButton
MOUSE_BUTTON_BACK: MouseButton
MOUSE_BUTTON_FORWARD: MouseButton
PACKAGE_TYPE_UNSPECIFIED: PackageType
PACKAGE_TYPE_CURSOR_PROJECT: PackageType
PACKAGE_TYPE_CURSOR_PERSONAL: PackageType
PACKAGE_TYPE_CLAUDE_SKILL: PackageType
PACKAGE_TYPE_CLAUDE_PLUGIN: PackageType
PRIVATE_WORKER_STATUS_UNSPECIFIED: PrivateWorkerStatus
PRIVATE_WORKER_STATUS_DISCONNECTED: PrivateWorkerStatus
PRIVATE_WORKER_STATUS_READY: PrivateWorkerStatus
PRIVATE_WORKER_STATUS_CLAIMED: PrivateWorkerStatus
PULL_REQUEST_STATUS_UNSPECIFIED: PullRequestStatus
PULL_REQUEST_STATUS_OPEN: PullRequestStatus
PULL_REQUEST_STATUS_CLOSED: PullRequestStatus
RECORDING_MODE_UNSPECIFIED: RecordingMode
RECORDING_MODE_START_RECORDING: RecordingMode
RECORDING_MODE_SAVE_RECORDING: RecordingMode
RECORDING_MODE_DISCARD_RECORDING: RecordingMode
REPLACE_ENV_MODE_UNSPECIFIED: ReplaceEnvMode
REPLACE_ENV_MODE_CUSTOM: ReplaceEnvMode
REPLACE_ENV_MODE_CLEAN_SLATE: ReplaceEnvMode
REPLACE_ENV_MODE_DEFAULT: ReplaceEnvMode
REQUESTED_FILE_PATH_REJECTED_REASON_UNSPECIFIED: RequestedFilePathRejectedReason
REQUESTED_FILE_PATH_REJECTED_REASON_SLASHES_NOT_ALLOWED: RequestedFilePathRejectedReason
RESPONSE_COMPARISON_DISPLAY_ORDER_UNSPECIFIED: ResponseComparisonDisplayOrder
RESPONSE_COMPARISON_DISPLAY_ORDER_PARENT_FIRST: ResponseComparisonDisplayOrder
RESPONSE_COMPARISON_DISPLAY_ORDER_ALTERNATE_FIRST: ResponseComparisonDisplayOrder
RESPONSE_COMPARISON_SKIP_REASON_UNSPECIFIED: ResponseComparisonSkipReason
RESPONSE_COMPARISON_SKIP_REASON_ALTERNATE_TOOL_CALL: ResponseComparisonSkipReason
RESPONSE_COMPARISON_SKIP_REASON_INFERENCE_ERROR: ResponseComparisonSkipReason
RESPONSE_COMPARISON_SKIP_REASON_TIMEOUT: ResponseComparisonSkipReason
RESPONSE_COMPARISON_SKIP_REASON_CANCELLED: ResponseComparisonSkipReason
SCROLL_DIRECTION_UNSPECIFIED: ScrollDirection
SCROLL_DIRECTION_UP: ScrollDirection
SCROLL_DIRECTION_DOWN: ScrollDirection
SCROLL_DIRECTION_LEFT: ScrollDirection
SCROLL_DIRECTION_RIGHT: ScrollDirection
SELECTED_PLUGIN_CAPABILITY_TYPE_UNSPECIFIED: SelectedPluginCapabilityType
SELECTED_PLUGIN_CAPABILITY_TYPE_COMMAND: SelectedPluginCapabilityType
SELECTED_PLUGIN_CAPABILITY_TYPE_SKILL: SelectedPluginCapabilityType
SELECTED_PLUGIN_CAPABILITY_TYPE_SUBAGENT: SelectedPluginCapabilityType
SHELL_ABORT_REASON_UNSPECIFIED: ShellAbortReason
SHELL_ABORT_REASON_USER_ABORT: ShellAbortReason
SHELL_ABORT_REASON_TIMEOUT: ShellAbortReason
SHELL_BACKGROUND_REASON_UNSPECIFIED: ShellBackgroundReason
SHELL_BACKGROUND_REASON_TIMEOUT: ShellBackgroundReason
SHELL_BACKGROUND_REASON_USER_REQUEST: ShellBackgroundReason
SIMULATED_MSG_REASON_UNSPECIFIED: SimulatedMsgReason
SIMULATED_MSG_REASON_PLAN_EXECUTION: SimulatedMsgReason
SIMULATED_MSG_REASON_COMMIT_REMINDER: SimulatedMsgReason
SIMULATED_MSG_REASON_BACKGROUND_TASK_COMPLETION: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_COMMIT: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_COMMIT_AND_PUSH: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_PUSH: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_CREATE_PR: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_FIX_MERGE_CONFLICTS: SimulatedMsgReason
SIMULATED_MSG_REASON_USER_SENT_TO_SUBAGENT: SimulatedMsgReason
SIMULATED_MSG_REASON_USER_INTERRUPTED_SUBAGENT: SimulatedMsgReason
SIMULATED_MSG_REASON_USER_QUEUED_TO_SUBAGENT: SimulatedMsgReason
SIMULATED_MSG_REASON_BABYSIT_PR_IN_CLOUD: SimulatedMsgReason
SIMULATED_MSG_REASON_CI_PANEL_INVESTIGATE_FAILURE: SimulatedMsgReason
SIMULATED_MSG_REASON_MULTITASK: SimulatedMsgReason
SIMULATED_MSG_REASON_BUILD_IN_PARALLEL: SimulatedMsgReason
SIMULATED_MSG_REASON_MULTITASK_SPLIT_PRS: SimulatedMsgReason
SIMULATED_MSG_REASON_APPLY_LOCALLY: SimulatedMsgReason
SIMULATED_MSG_REASON_CHECKOUT_BRANCH: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_UPDATE_BRANCH: SimulatedMsgReason
SIMULATED_MSG_REASON_PR_TAB_BUGBOT_FIX: SimulatedMsgReason
SIMULATED_MSG_REASON_RUN_BUGBOT_REVIEW: SimulatedMsgReason
SIMULATED_MSG_REASON_RUN_SECURITY_REVIEW: SimulatedMsgReason
SIMULATED_MSG_REASON_FSD_APPLY_FINDING: SimulatedMsgReason
SIMULATED_MSG_REASON_FSD_UNDO_FINDING: SimulatedMsgReason
SIMULATED_MSG_REASON_FSD_START: SimulatedMsgReason
SIMULATED_MSG_REASON_FSD_PR_INTERRUPT: SimulatedMsgReason
SIMULATED_MSG_REASON_SUBSCRIPTION: SimulatedMsgReason
SIMULATED_MSG_REASON_DIFF_TAB_CREATE_BRANCH: SimulatedMsgReason
SIMULATED_MSG_REASON_AGENT_STORE_CONFLICT: SimulatedMsgReason
SIMULATED_MSG_REASON_GOAL_CONTINUATION: SimulatedMsgReason
SIMULATED_MSG_REASON_PROJECT_KICKOFF: SimulatedMsgReason
SMART_MODE_CLASSIFIER_DECISION_UNSPECIFIED: SmartModeClassifierDecision
SMART_MODE_CLASSIFIER_DECISION_ALLOW: SmartModeClassifierDecision
SMART_MODE_CLASSIFIER_DECISION_BLOCK: SmartModeClassifierDecision
SUBAGENT_BACKGROUND_REASON_UNSPECIFIED: SubagentBackgroundReason
SUBAGENT_BACKGROUND_REASON_AGENT_REQUEST: SubagentBackgroundReason
SUBAGENT_BACKGROUND_REASON_USER_REQUEST: SubagentBackgroundReason
SUBAGENT_BACKGROUND_REASON_QUEUED_FOLLOW_UP: SubagentBackgroundReason
SUBAGENT_EXECUTION_ENVIRONMENT_UNSPECIFIED: SubagentExecutionEnvironment
SUBAGENT_EXECUTION_ENVIRONMENT_LOCAL: SubagentExecutionEnvironment
SUBAGENT_EXECUTION_ENVIRONMENT_CLOUD: SubagentExecutionEnvironment
SUBAGENT_INTERACTION_POLICY_UNSPECIFIED: SubagentInteractionPolicy
SUBAGENT_INTERACTION_POLICY_AUTO_REJECT: SubagentInteractionPolicy
SUBAGENT_INTERACTION_POLICY_BUBBLE_TO_PARENT: SubagentInteractionPolicy
SUBAGENT_INTERACTION_POLICY_SURFACE_TO_USER: SubagentInteractionPolicy
SUBAGENT_RUN_STATUS_UNSPECIFIED: SubagentRunStatus
SUBAGENT_RUN_STATUS_RUNNING: SubagentRunStatus
SUBAGENT_RUN_STATUS_BACKGROUNDED: SubagentRunStatus
SUBAGENT_RUN_STATUS_SUCCESS: SubagentRunStatus
SUBAGENT_RUN_STATUS_ERROR: SubagentRunStatus
SUBAGENT_RUN_STATUS_ABORTED: SubagentRunStatus
SUBSCRIPTION_SOURCE_UNSPECIFIED: SubscriptionSource
SUBSCRIPTION_SOURCE_SLACK: SubscriptionSource
SUBSCRIPTION_SOURCE_GITHUB: SubscriptionSource
SUBSCRIPTION_SOURCE_LINEAR: SubscriptionSource
TASK_MODE_UNSPECIFIED: TaskMode
TASK_MODE_AGENT: TaskMode
TASK_MODE_PLAN: TaskMode
THINKING_STYLE_UNSPECIFIED: ThinkingStyle
THINKING_STYLE_DEFAULT: ThinkingStyle
THINKING_STYLE_CODEX: ThinkingStyle
THINKING_STYLE_GPT5: ThinkingStyle
TIMEOUT_BEHAVIOR_UNSPECIFIED: TimeoutBehavior
TIMEOUT_BEHAVIOR_CANCEL: TimeoutBehavior
TIMEOUT_BEHAVIOR_BACKGROUND: TimeoutBehavior
TMUX_SESSION_KIND_UNSPECIFIED: TmuxSessionKind
TMUX_SESSION_KIND_USER_MANUAL: TmuxSessionKind
TMUX_SESSION_KIND_AGENT_BACKGROUND: TmuxSessionKind
TMUX_SESSION_KIND_AGENT_INTERACTIVE: TmuxSessionKind
TODO_STATUS_UNSPECIFIED: TodoStatus
TODO_STATUS_PENDING: TodoStatus
TODO_STATUS_IN_PROGRESS: TodoStatus
TODO_STATUS_COMPLETED: TodoStatus
TODO_STATUS_CANCELLED: TodoStatus

class AbortAgentHostBackgroundWorkRequest(_message.Message):
    __slots__ = ("session_id", "work_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORK_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    work_id: str
    def __init__(self, session_id: _Optional[str] = ..., work_id: _Optional[str] = ...) -> None: ...

class AbortAgentHostBackgroundWorkResponse(_message.Message):
    __slots__ = ("aborted",)
    ABORTED_FIELD_NUMBER: _ClassVar[int]
    aborted: bool
    def __init__(self, aborted: _Optional[bool] = ...) -> None: ...

class AbortAllAgentHostBackgroundWorkRequest(_message.Message):
    __slots__ = ("session_id", "kind", "state", "owner_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    kind: AgentHostBackgroundWorkKind
    state: AgentHostBackgroundWorkState
    owner_id: str
    def __init__(self, session_id: _Optional[str] = ..., kind: _Optional[_Union[AgentHostBackgroundWorkKind, str]] = ..., state: _Optional[_Union[AgentHostBackgroundWorkState, str]] = ..., owner_id: _Optional[str] = ...) -> None: ...

class AbortAllAgentHostBackgroundWorkResponse(_message.Message):
    __slots__ = ("aborted_count",)
    ABORTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    aborted_count: int
    def __init__(self, aborted_count: _Optional[int] = ...) -> None: ...

class AbortArgs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AbortResult(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ActiveBranchChange(_message.Message):
    __slots__ = ("path", "branch_name")
    PATH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    branch_name: str
    def __init__(self, path: _Optional[str] = ..., branch_name: _Optional[str] = ...) -> None: ...

class AfterAgentResponseRequestQuery(_message.Message):
    __slots__ = ("text", "conversation_id", "generation_id", "model", "model_id", "model_params", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    text: str
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    def __init__(self, text: _Optional[str] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ...) -> None: ...

class AfterAgentResponseRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AfterAgentThoughtRequestQuery(_message.Message):
    __slots__ = ("text", "duration_ms", "conversation_id", "generation_id", "model", "model_id", "model_params")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    text: str
    duration_ms: int
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, text: _Optional[str] = ..., duration_ms: _Optional[int] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class AfterAgentThoughtRequestResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgentClientMessage(_message.Message):
    __slots__ = ("run_request", "exec_client_message", "exec_client_control_message", "kv_client_message", "conversation_action", "interaction_response", "client_heartbeat", "prewarm_request")
    RUN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXEC_CLIENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXEC_CLIENT_CONTROL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KV_CLIENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    PREWARM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    run_request: AgentRunRequest
    exec_client_message: ExecClientMessage
    exec_client_control_message: ExecClientControlMessage
    kv_client_message: KvClientMessage
    conversation_action: ConversationAction
    interaction_response: InteractionResponse
    client_heartbeat: ClientHeartbeat
    prewarm_request: PrewarmRequest
    def __init__(self, run_request: _Optional[_Union[AgentRunRequest, _Mapping]] = ..., exec_client_message: _Optional[_Union[ExecClientMessage, _Mapping]] = ..., exec_client_control_message: _Optional[_Union[ExecClientControlMessage, _Mapping]] = ..., kv_client_message: _Optional[_Union[KvClientMessage, _Mapping]] = ..., conversation_action: _Optional[_Union[ConversationAction, _Mapping]] = ..., interaction_response: _Optional[_Union[InteractionResponse, _Mapping]] = ..., client_heartbeat: _Optional[_Union[ClientHeartbeat, _Mapping]] = ..., prewarm_request: _Optional[_Union[PrewarmRequest, _Mapping]] = ...) -> None: ...

class AgentConversationTurn(_message.Message):
    __slots__ = ("user_message", "steps", "request_id")
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    user_message: UserMessage
    steps: _containers.RepeatedCompositeFieldContainer[ConversationStep]
    request_id: str
    def __init__(self, user_message: _Optional[_Union[UserMessage, _Mapping]] = ..., steps: _Optional[_Iterable[_Union[ConversationStep, _Mapping]]] = ..., request_id: _Optional[str] = ...) -> None: ...

class AgentConversationTurnStructure(_message.Message):
    __slots__ = ("user_message", "steps", "request_id", "encrypted_model", "dynamic_tool_count", "send_message_step_indices")
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_MODEL_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_TOOL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_STEP_INDICES_FIELD_NUMBER: _ClassVar[int]
    user_message: bytes
    steps: _containers.RepeatedScalarFieldContainer[bytes]
    request_id: str
    encrypted_model: str
    dynamic_tool_count: int
    send_message_step_indices: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user_message: _Optional[bytes] = ..., steps: _Optional[_Iterable[bytes]] = ..., request_id: _Optional[str] = ..., encrypted_model: _Optional[str] = ..., dynamic_tool_count: _Optional[int] = ..., send_message_step_indices: _Optional[_Iterable[int]] = ...) -> None: ...

class AgentHostBackgroundWork(_message.Message):
    __slots__ = ("id", "kind", "state", "owner_id", "has_abort", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_ABORT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: AgentHostBackgroundWorkKind
    state: AgentHostBackgroundWorkState
    owner_id: str
    has_abort: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[AgentHostBackgroundWorkKind, str]] = ..., state: _Optional[_Union[AgentHostBackgroundWorkState, str]] = ..., owner_id: _Optional[str] = ..., has_abort: _Optional[bool] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AgentHostInteractionCancelled(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class AgentHostInteractionFailed(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class AgentHostInteractionResolved(_message.Message):
    __slots__ = ("turn_id", "interaction_id", "responded", "cancelled", "failed")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONDED_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    interaction_id: str
    responded: InteractionResponse
    cancelled: AgentHostInteractionCancelled
    failed: AgentHostInteractionFailed
    def __init__(self, turn_id: _Optional[str] = ..., interaction_id: _Optional[str] = ..., responded: _Optional[_Union[InteractionResponse, _Mapping]] = ..., cancelled: _Optional[_Union[AgentHostInteractionCancelled, _Mapping]] = ..., failed: _Optional[_Union[AgentHostInteractionFailed, _Mapping]] = ...) -> None: ...

class AgentHostPendingInteraction(_message.Message):
    __slots__ = ("interaction_id", "turn_id", "query")
    INTERACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    interaction_id: str
    turn_id: str
    query: InteractionQuery
    def __init__(self, interaction_id: _Optional[str] = ..., turn_id: _Optional[str] = ..., query: _Optional[_Union[InteractionQuery, _Mapping]] = ...) -> None: ...

class AgentHostSession(_message.Message):
    __slots__ = ("session_id", "status", "last_event_id", "forked_from_session_id", "parent")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    FORKED_FROM_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    status: AgentHostSessionStatus
    last_event_id: int
    forked_from_session_id: str
    parent: SessionParent
    def __init__(self, session_id: _Optional[str] = ..., status: _Optional[_Union[AgentHostSessionStatus, str]] = ..., last_event_id: _Optional[int] = ..., forked_from_session_id: _Optional[str] = ..., parent: _Optional[_Union[SessionParent, _Mapping]] = ...) -> None: ...

class AgentHostSessionAdded(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: AgentHostSession
    def __init__(self, session: _Optional[_Union[AgentHostSession, _Mapping]] = ...) -> None: ...

class AgentHostSessionBackgroundWorkSnapshot(_message.Message):
    __slots__ = ("work",)
    WORK_FIELD_NUMBER: _ClassVar[int]
    work: _containers.RepeatedCompositeFieldContainer[AgentHostBackgroundWork]
    def __init__(self, work: _Optional[_Iterable[_Union[AgentHostBackgroundWork, _Mapping]]] = ...) -> None: ...

class AgentHostSessionBackgroundWorkState(_message.Message):
    __slots__ = ("work",)
    WORK_FIELD_NUMBER: _ClassVar[int]
    work: _containers.RepeatedCompositeFieldContainer[AgentHostBackgroundWork]
    def __init__(self, work: _Optional[_Iterable[_Union[AgentHostBackgroundWork, _Mapping]]] = ...) -> None: ...

class AgentHostSessionDeleted(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class AgentHostSessionEvent(_message.Message):
    __slots__ = ("event_id", "interaction_update", "conversation_state", "turn_started", "turn_awaiting_input", "turn_settled", "interaction_resolved", "subagent_started")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    TURN_STARTED_FIELD_NUMBER: _ClassVar[int]
    TURN_AWAITING_INPUT_FIELD_NUMBER: _ClassVar[int]
    TURN_SETTLED_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_STARTED_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    interaction_update: InteractionUpdate
    conversation_state: ConversationStateStructure
    turn_started: AgentHostTurnStarted
    turn_awaiting_input: AgentHostTurnAwaitingInput
    turn_settled: AgentHostTurnSettled
    interaction_resolved: AgentHostInteractionResolved
    subagent_started: AgentHostSubagentStarted
    def __init__(self, event_id: _Optional[int] = ..., interaction_update: _Optional[_Union[InteractionUpdate, _Mapping]] = ..., conversation_state: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., turn_started: _Optional[_Union[AgentHostTurnStarted, _Mapping]] = ..., turn_awaiting_input: _Optional[_Union[AgentHostTurnAwaitingInput, _Mapping]] = ..., turn_settled: _Optional[_Union[AgentHostTurnSettled, _Mapping]] = ..., interaction_resolved: _Optional[_Union[AgentHostInteractionResolved, _Mapping]] = ..., subagent_started: _Optional[_Union[AgentHostSubagentStarted, _Mapping]] = ...) -> None: ...

class AgentHostSessionInteractionsSnapshot(_message.Message):
    __slots__ = ("interactions",)
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    interactions: _containers.RepeatedCompositeFieldContainer[AgentHostPendingInteraction]
    def __init__(self, interactions: _Optional[_Iterable[_Union[AgentHostPendingInteraction, _Mapping]]] = ...) -> None: ...

class AgentHostSessionInteractionsState(_message.Message):
    __slots__ = ("interactions",)
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    interactions: _containers.RepeatedCompositeFieldContainer[AgentHostPendingInteraction]
    def __init__(self, interactions: _Optional[_Iterable[_Union[AgentHostPendingInteraction, _Mapping]]] = ...) -> None: ...

class AgentHostSessionOptions(_message.Message):
    __slots__ = ("workspace_paths", "worktree_main_path", "is_glass_root", "interaction_policy")
    WORKSPACE_PATHS_FIELD_NUMBER: _ClassVar[int]
    WORKTREE_MAIN_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_GLASS_ROOT_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    workspace_paths: _containers.RepeatedScalarFieldContainer[str]
    worktree_main_path: str
    is_glass_root: bool
    interaction_policy: SubagentInteractionPolicy
    def __init__(self, workspace_paths: _Optional[_Iterable[str]] = ..., worktree_main_path: _Optional[str] = ..., is_glass_root: _Optional[bool] = ..., interaction_policy: _Optional[_Union[SubagentInteractionPolicy, str]] = ...) -> None: ...

class AgentHostSessionUpdated(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: AgentHostSession
    def __init__(self, session: _Optional[_Union[AgentHostSession, _Mapping]] = ...) -> None: ...

class AgentHostSessionsSnapshot(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[AgentHostSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[AgentHostSession, _Mapping]]] = ...) -> None: ...

class AgentHostSubagentStarted(_message.Message):
    __slots__ = ("turn_id", "parent_tool_call_id", "child_session_id", "root_session_id")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    parent_tool_call_id: str
    child_session_id: str
    root_session_id: str
    def __init__(self, turn_id: _Optional[str] = ..., parent_tool_call_id: _Optional[str] = ..., child_session_id: _Optional[str] = ..., root_session_id: _Optional[str] = ...) -> None: ...

class AgentHostTurnAwaitingInput(_message.Message):
    __slots__ = ("turn_id", "request_id", "interaction_id", "query")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    request_id: str
    interaction_id: str
    query: InteractionQuery
    def __init__(self, turn_id: _Optional[str] = ..., request_id: _Optional[str] = ..., interaction_id: _Optional[str] = ..., query: _Optional[_Union[InteractionQuery, _Mapping]] = ...) -> None: ...

class AgentHostTurnOptions(_message.Message):
    __slots__ = ("generation_uuid", "custom_system_prompt", "exclude_workspace_context", "enable_agent_retries", "fixed_retry_delay_ms", "endless_retries", "agent_session_id")
    GENERATION_UUID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_WORKSPACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AGENT_RETRIES_FIELD_NUMBER: _ClassVar[int]
    FIXED_RETRY_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    ENDLESS_RETRIES_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    generation_uuid: str
    custom_system_prompt: str
    exclude_workspace_context: bool
    enable_agent_retries: bool
    fixed_retry_delay_ms: int
    endless_retries: bool
    agent_session_id: str
    def __init__(self, generation_uuid: _Optional[str] = ..., custom_system_prompt: _Optional[str] = ..., exclude_workspace_context: _Optional[bool] = ..., enable_agent_retries: _Optional[bool] = ..., fixed_retry_delay_ms: _Optional[int] = ..., endless_retries: _Optional[bool] = ..., agent_session_id: _Optional[str] = ...) -> None: ...

class AgentHostTurnSettled(_message.Message):
    __slots__ = ("turn_id", "outcome", "detail")
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    outcome: AgentHostTurnOutcome
    detail: str
    def __init__(self, turn_id: _Optional[str] = ..., outcome: _Optional[_Union[AgentHostTurnOutcome, str]] = ..., detail: _Optional[str] = ...) -> None: ...

class AgentHostTurnStarted(_message.Message):
    __slots__ = ("turn_id",)
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    def __init__(self, turn_id: _Optional[str] = ...) -> None: ...

class AgentRunRequest(_message.Message):
    __slots__ = ("conversation_state", "action", "model_details", "requested_model", "mcp_tools", "conversation_id", "mcp_file_system_options", "skill_options", "custom_system_prompt", "suggest_next_prompt", "subagent_type_name", "exclude_workspace_context", "harness", "selected_subagent_models", "selected_subagent_model_details", "conversation_group_id", "pre_fetched_blobs", "dev_raw_model_slug", "client_supports_inline_images", "subagent_model_overrides", "can_create_cloud_subagents", "suppress_subagent_progress_update_tool", "client_supports_send_to_user", "computer_use_coordinate_mode", "run_id", "agent_session_id", "client_supports_prompt_context_usage_rpc")
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_MODEL_FIELD_NUMBER: _ClassVar[int]
    MCP_TOOLS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MCP_FILE_SYSTEM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SKILL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_NEXT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_WORKSPACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUBAGENT_MODELS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUBAGENT_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_FETCHED_BLOBS_FIELD_NUMBER: _ClassVar[int]
    DEV_RAW_MODEL_SLUG_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPORTS_INLINE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_MODEL_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_CLOUD_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_SUBAGENT_PROGRESS_UPDATE_TOOL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPORTS_SEND_TO_USER_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_COORDINATE_MODE_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPORTS_PROMPT_CONTEXT_USAGE_RPC_FIELD_NUMBER: _ClassVar[int]
    conversation_state: ConversationStateStructure
    action: ConversationAction
    model_details: ModelDetails
    requested_model: RequestedModel
    mcp_tools: McpTools
    conversation_id: str
    mcp_file_system_options: McpFileSystemOptions
    skill_options: SkillOptions
    custom_system_prompt: str
    suggest_next_prompt: bool
    subagent_type_name: str
    exclude_workspace_context: bool
    harness: str
    selected_subagent_models: _containers.RepeatedCompositeFieldContainer[RequestedModel]
    selected_subagent_model_details: _containers.RepeatedCompositeFieldContainer[ModelDetails]
    conversation_group_id: str
    pre_fetched_blobs: _containers.RepeatedCompositeFieldContainer[PreFetchedBlob]
    dev_raw_model_slug: str
    client_supports_inline_images: bool
    subagent_model_overrides: _containers.RepeatedCompositeFieldContainer[SubagentModelOverride]
    can_create_cloud_subagents: bool
    suppress_subagent_progress_update_tool: bool
    client_supports_send_to_user: bool
    computer_use_coordinate_mode: str
    run_id: str
    agent_session_id: str
    client_supports_prompt_context_usage_rpc: bool
    def __init__(self, conversation_state: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., action: _Optional[_Union[ConversationAction, _Mapping]] = ..., model_details: _Optional[_Union[ModelDetails, _Mapping]] = ..., requested_model: _Optional[_Union[RequestedModel, _Mapping]] = ..., mcp_tools: _Optional[_Union[McpTools, _Mapping]] = ..., conversation_id: _Optional[str] = ..., mcp_file_system_options: _Optional[_Union[McpFileSystemOptions, _Mapping]] = ..., skill_options: _Optional[_Union[SkillOptions, _Mapping]] = ..., custom_system_prompt: _Optional[str] = ..., suggest_next_prompt: _Optional[bool] = ..., subagent_type_name: _Optional[str] = ..., exclude_workspace_context: _Optional[bool] = ..., harness: _Optional[str] = ..., selected_subagent_models: _Optional[_Iterable[_Union[RequestedModel, _Mapping]]] = ..., selected_subagent_model_details: _Optional[_Iterable[_Union[ModelDetails, _Mapping]]] = ..., conversation_group_id: _Optional[str] = ..., pre_fetched_blobs: _Optional[_Iterable[_Union[PreFetchedBlob, _Mapping]]] = ..., dev_raw_model_slug: _Optional[str] = ..., client_supports_inline_images: _Optional[bool] = ..., subagent_model_overrides: _Optional[_Iterable[_Union[SubagentModelOverride, _Mapping]]] = ..., can_create_cloud_subagents: _Optional[bool] = ..., suppress_subagent_progress_update_tool: _Optional[bool] = ..., client_supports_send_to_user: _Optional[bool] = ..., computer_use_coordinate_mode: _Optional[str] = ..., run_id: _Optional[str] = ..., agent_session_id: _Optional[str] = ..., client_supports_prompt_context_usage_rpc: _Optional[bool] = ...) -> None: ...

class AgentServerMessage(_message.Message):
    __slots__ = ("ttft_breakdown", "interaction_update", "exec_server_message", "exec_server_control_message", "conversation_checkpoint_update", "kv_server_message", "interaction_query")
    TTFT_BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    EXEC_SERVER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXEC_SERVER_CONTROL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CHECKPOINT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    KV_SERVER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_QUERY_FIELD_NUMBER: _ClassVar[int]
    ttft_breakdown: TtftBreakdown
    interaction_update: InteractionUpdate
    exec_server_message: ExecServerMessage
    exec_server_control_message: ExecServerControlMessage
    conversation_checkpoint_update: ConversationStateStructure
    kv_server_message: KvServerMessage
    interaction_query: InteractionQuery
    def __init__(self, ttft_breakdown: _Optional[_Union[TtftBreakdown, _Mapping]] = ..., interaction_update: _Optional[_Union[InteractionUpdate, _Mapping]] = ..., exec_server_message: _Optional[_Union[ExecServerMessage, _Mapping]] = ..., exec_server_control_message: _Optional[_Union[ExecServerControlMessage, _Mapping]] = ..., conversation_checkpoint_update: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., kv_server_message: _Optional[_Union[KvServerMessage, _Mapping]] = ..., interaction_query: _Optional[_Union[InteractionQuery, _Mapping]] = ...) -> None: ...

class AgentSkill(_message.Message):
    __slots__ = ("full_path", "content", "description", "parse_error", "environments", "disabled_environments", "git_remote_origin", "disable_model_invocation", "plugin", "marketplace", "plugin_id", "marketplace_id", "globs", "scoped_to")
    FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    GIT_REMOTE_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MODEL_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBS_FIELD_NUMBER: _ClassVar[int]
    SCOPED_TO_FIELD_NUMBER: _ClassVar[int]
    full_path: str
    content: str
    description: str
    parse_error: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    disabled_environments: _containers.RepeatedScalarFieldContainer[str]
    git_remote_origin: str
    disable_model_invocation: bool
    plugin: str
    marketplace: str
    plugin_id: str
    marketplace_id: str
    globs: _containers.RepeatedScalarFieldContainer[str]
    scoped_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, full_path: _Optional[str] = ..., content: _Optional[str] = ..., description: _Optional[str] = ..., parse_error: _Optional[str] = ..., environments: _Optional[_Iterable[str]] = ..., disabled_environments: _Optional[_Iterable[str]] = ..., git_remote_origin: _Optional[str] = ..., disable_model_invocation: _Optional[bool] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., plugin_id: _Optional[str] = ..., marketplace_id: _Optional[str] = ..., globs: _Optional[_Iterable[str]] = ..., scoped_to: _Optional[_Iterable[str]] = ...) -> None: ...

class AgentSkillMetadata(_message.Message):
    __slots__ = ("full_path", "description", "parse_error", "environments", "disabled_environments", "git_remote_origin", "disable_model_invocation", "plugin", "marketplace", "plugin_id", "marketplace_id", "globs", "scoped_to")
    FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    GIT_REMOTE_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MODEL_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBS_FIELD_NUMBER: _ClassVar[int]
    SCOPED_TO_FIELD_NUMBER: _ClassVar[int]
    full_path: str
    description: str
    parse_error: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    disabled_environments: _containers.RepeatedScalarFieldContainer[str]
    git_remote_origin: str
    disable_model_invocation: bool
    plugin: str
    marketplace: str
    plugin_id: str
    marketplace_id: str
    globs: _containers.RepeatedScalarFieldContainer[str]
    scoped_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, full_path: _Optional[str] = ..., description: _Optional[str] = ..., parse_error: _Optional[str] = ..., environments: _Optional[_Iterable[str]] = ..., disabled_environments: _Optional[_Iterable[str]] = ..., git_remote_origin: _Optional[str] = ..., disable_model_invocation: _Optional[bool] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., plugin_id: _Optional[str] = ..., marketplace_id: _Optional[str] = ..., globs: _Optional[_Iterable[str]] = ..., scoped_to: _Optional[_Iterable[str]] = ...) -> None: ...

class AgentStoreClaimConfig(_message.Message):
    __slots__ = ("self", "mounts", "store_backed_artifacts_enabled")
    SELF_FIELD_NUMBER: _ClassVar[int]
    MOUNTS_FIELD_NUMBER: _ClassVar[int]
    STORE_BACKED_ARTIFACTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    self: AgentStoreSelfClaimConfig
    mounts: _containers.RepeatedCompositeFieldContainer[AgentStoreClaimMount]
    store_backed_artifacts_enabled: bool
    def __init__(self_, self: _Optional[_Union[AgentStoreSelfClaimConfig, _Mapping]] = ..., mounts: _Optional[_Iterable[_Union[AgentStoreClaimMount, _Mapping]]] = ..., store_backed_artifacts_enabled: _Optional[bool] = ...) -> None: ...

class AgentStoreClaimMount(_message.Message):
    __slots__ = ("kind", "source_id")
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    kind: AgentStoreClaimMountKind
    source_id: str
    def __init__(self, kind: _Optional[_Union[AgentStoreClaimMountKind, str]] = ..., source_id: _Optional[str] = ...) -> None: ...

class AgentStoreConflictArgs(_message.Message):
    __slots__ = ("cursor", "advance")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ADVANCE_FIELD_NUMBER: _ClassVar[int]
    cursor: AgentStoreConflictCursor
    advance: bool
    def __init__(self, cursor: _Optional[_Union[AgentStoreConflictCursor, _Mapping]] = ..., advance: _Optional[bool] = ...) -> None: ...

class AgentStoreConflictCursor(_message.Message):
    __slots__ = ("journal_epoch", "seq", "last_event_id")
    JOURNAL_EPOCH_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    journal_epoch: str
    seq: int
    last_event_id: str
    def __init__(self, journal_epoch: _Optional[str] = ..., seq: _Optional[int] = ..., last_event_id: _Optional[str] = ...) -> None: ...

class AgentStoreConflictError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class AgentStoreConflictEvent(_message.Message):
    __slots__ = ("v", "event_id", "journal_epoch", "seq", "ts_ms", "kind", "store_id", "original_rel_path", "conflict_rel_path", "original_abs_path", "conflict_abs_path", "preserved_bytes")
    V_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    JOURNAL_EPOCH_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    TS_MS_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_REL_PATH_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ABS_PATH_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_ABS_PATH_FIELD_NUMBER: _ClassVar[int]
    PRESERVED_BYTES_FIELD_NUMBER: _ClassVar[int]
    v: int
    event_id: str
    journal_epoch: str
    seq: int
    ts_ms: int
    kind: str
    store_id: str
    original_rel_path: str
    conflict_rel_path: str
    original_abs_path: str
    conflict_abs_path: str
    preserved_bytes: int
    def __init__(self, v: _Optional[int] = ..., event_id: _Optional[str] = ..., journal_epoch: _Optional[str] = ..., seq: _Optional[int] = ..., ts_ms: _Optional[int] = ..., kind: _Optional[str] = ..., store_id: _Optional[str] = ..., original_rel_path: _Optional[str] = ..., conflict_rel_path: _Optional[str] = ..., original_abs_path: _Optional[str] = ..., conflict_abs_path: _Optional[str] = ..., preserved_bytes: _Optional[int] = ...) -> None: ...

class AgentStoreConflictResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: AgentStoreConflictSuccess
    error: AgentStoreConflictError
    def __init__(self, success: _Optional[_Union[AgentStoreConflictSuccess, _Mapping]] = ..., error: _Optional[_Union[AgentStoreConflictError, _Mapping]] = ...) -> None: ...

class AgentStoreConflictSuccess(_message.Message):
    __slots__ = ("events", "next_cursor", "gap")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    GAP_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AgentStoreConflictEvent]
    next_cursor: AgentStoreConflictCursor
    gap: bool
    def __init__(self, events: _Optional[_Iterable[_Union[AgentStoreConflictEvent, _Mapping]]] = ..., next_cursor: _Optional[_Union[AgentStoreConflictCursor, _Mapping]] = ..., gap: _Optional[bool] = ...) -> None: ...

class AgentStoreSelfClaimConfig(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AiAttributionArgs(_message.Message):
    __slots__ = ("file_paths", "start_line", "end_line", "commit_hashes", "output_mode", "max_commits", "include_line_ranges")
    FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    END_LINE_FIELD_NUMBER: _ClassVar[int]
    COMMIT_HASHES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_COMMITS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LINE_RANGES_FIELD_NUMBER: _ClassVar[int]
    file_paths: _containers.RepeatedScalarFieldContainer[str]
    start_line: int
    end_line: int
    commit_hashes: _containers.RepeatedScalarFieldContainer[str]
    output_mode: str
    max_commits: int
    include_line_ranges: bool
    def __init__(self, file_paths: _Optional[_Iterable[str]] = ..., start_line: _Optional[int] = ..., end_line: _Optional[int] = ..., commit_hashes: _Optional[_Iterable[str]] = ..., output_mode: _Optional[str] = ..., max_commits: _Optional[int] = ..., include_line_ranges: _Optional[bool] = ...) -> None: ...

class AiAttributionError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class AiAttributionResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: AiAttributionSuccess
    error: AiAttributionError
    def __init__(self, success: _Optional[_Union[AiAttributionSuccess, _Mapping]] = ..., error: _Optional[_Union[AiAttributionError, _Mapping]] = ...) -> None: ...

class AiAttributionSuccess(_message.Message):
    __slots__ = ("attribution_text", "output_location")
    ATTRIBUTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    attribution_text: str
    output_location: OutputLocation
    def __init__(self, attribution_text: _Optional[str] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ...) -> None: ...

class AiAttributionToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: AiAttributionArgs
    result: AiAttributionResult
    def __init__(self, args: _Optional[_Union[AiAttributionArgs, _Mapping]] = ..., result: _Optional[_Union[AiAttributionResult, _Mapping]] = ...) -> None: ...

class ApiKeyCredentials(_message.Message):
    __slots__ = ("api_key", "base_url")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    base_url: str
    def __init__(self, api_key: _Optional[str] = ..., base_url: _Optional[str] = ...) -> None: ...

class AppliedAgentChange(_message.Message):
    __slots__ = ("path", "change_type", "before_content", "after_content", "error", "message_for_model")
    class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANGE_TYPE_UNSPECIFIED: _ClassVar[AppliedAgentChange.ChangeType]
        CHANGE_TYPE_CREATED: _ClassVar[AppliedAgentChange.ChangeType]
        CHANGE_TYPE_MODIFIED: _ClassVar[AppliedAgentChange.ChangeType]
        CHANGE_TYPE_DELETED: _ClassVar[AppliedAgentChange.ChangeType]
    CHANGE_TYPE_UNSPECIFIED: AppliedAgentChange.ChangeType
    CHANGE_TYPE_CREATED: AppliedAgentChange.ChangeType
    CHANGE_TYPE_MODIFIED: AppliedAgentChange.ChangeType
    CHANGE_TYPE_DELETED: AppliedAgentChange.ChangeType
    PATH_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    AFTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FOR_MODEL_FIELD_NUMBER: _ClassVar[int]
    path: str
    change_type: AppliedAgentChange.ChangeType
    before_content: str
    after_content: str
    error: str
    message_for_model: str
    def __init__(self, path: _Optional[str] = ..., change_type: _Optional[_Union[AppliedAgentChange.ChangeType, str]] = ..., before_content: _Optional[str] = ..., after_content: _Optional[str] = ..., error: _Optional[str] = ..., message_for_model: _Optional[str] = ...) -> None: ...

class ApplyAgentDiffArgs(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class ApplyAgentDiffError(_message.Message):
    __slots__ = ("error", "applied_changes")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    error: str
    applied_changes: _containers.RepeatedCompositeFieldContainer[AppliedAgentChange]
    def __init__(self, error: _Optional[str] = ..., applied_changes: _Optional[_Iterable[_Union[AppliedAgentChange, _Mapping]]] = ...) -> None: ...

class ApplyAgentDiffResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ApplyAgentDiffSuccess
    error: ApplyAgentDiffError
    def __init__(self, success: _Optional[_Union[ApplyAgentDiffSuccess, _Mapping]] = ..., error: _Optional[_Union[ApplyAgentDiffError, _Mapping]] = ...) -> None: ...

class ApplyAgentDiffSuccess(_message.Message):
    __slots__ = ("applied_changes",)
    APPLIED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    applied_changes: _containers.RepeatedCompositeFieldContainer[AppliedAgentChange]
    def __init__(self, applied_changes: _Optional[_Iterable[_Union[AppliedAgentChange, _Mapping]]] = ...) -> None: ...

class ApplyAgentDiffToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ApplyAgentDiffArgs
    result: ApplyAgentDiffResult
    def __init__(self, args: _Optional[_Union[ApplyAgentDiffArgs, _Mapping]] = ..., result: _Optional[_Union[ApplyAgentDiffResult, _Mapping]] = ...) -> None: ...

class ArtifactPathError(_message.Message):
    __slots__ = ("kind", "code", "message")
    KIND_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kind: ArtifactPathErrorKind
    code: str
    message: str
    def __init__(self, kind: _Optional[_Union[ArtifactPathErrorKind, str]] = ..., code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ArtifactUploadDispatchResult(_message.Message):
    __slots__ = ("absolute_path", "status", "message", "slack_file_id")
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SLACK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    absolute_path: str
    status: ArtifactUploadDispatchStatus
    message: str
    slack_file_id: str
    def __init__(self, absolute_path: _Optional[str] = ..., status: _Optional[_Union[ArtifactUploadDispatchStatus, str]] = ..., message: _Optional[str] = ..., slack_file_id: _Optional[str] = ...) -> None: ...

class ArtifactUploadInstruction(_message.Message):
    __slots__ = ("absolute_path", "upload_url", "method", "headers", "content_type", "slack_upload_url", "slack_file_id")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLACK_UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    SLACK_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    absolute_path: str
    upload_url: str
    method: str
    headers: _containers.ScalarMap[str, str]
    content_type: str
    slack_upload_url: str
    slack_file_id: str
    def __init__(self, absolute_path: _Optional[str] = ..., upload_url: _Optional[str] = ..., method: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., content_type: _Optional[str] = ..., slack_upload_url: _Optional[str] = ..., slack_file_id: _Optional[str] = ...) -> None: ...

class ArtifactUploadMetadata(_message.Message):
    __slots__ = ("absolute_path", "size_bytes", "updated_at_unix_ms", "status", "bytes_uploaded", "last_error", "upload_attempts", "last_started_at_unix_ms", "last_finished_at_unix_ms", "upload_id")
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BYTES_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    LAST_STARTED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_FINISHED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    absolute_path: str
    size_bytes: int
    updated_at_unix_ms: int
    status: ArtifactUploadStatus
    bytes_uploaded: int
    last_error: str
    upload_attempts: int
    last_started_at_unix_ms: int
    last_finished_at_unix_ms: int
    upload_id: str
    def __init__(self, absolute_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., updated_at_unix_ms: _Optional[int] = ..., status: _Optional[_Union[ArtifactUploadStatus, str]] = ..., bytes_uploaded: _Optional[int] = ..., last_error: _Optional[str] = ..., upload_attempts: _Optional[int] = ..., last_started_at_unix_ms: _Optional[int] = ..., last_finished_at_unix_ms: _Optional[int] = ..., upload_id: _Optional[str] = ...) -> None: ...

class AskQuestionArgs(_message.Message):
    __slots__ = ("title", "questions", "run_async", "async_original_tool_call_id")
    class Option(_message.Message):
        __slots__ = ("id", "label")
        ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        id: str
        label: str
        def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...
    class Question(_message.Message):
        __slots__ = ("id", "prompt", "options", "allow_multiple")
        ID_FIELD_NUMBER: _ClassVar[int]
        PROMPT_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MULTIPLE_FIELD_NUMBER: _ClassVar[int]
        id: str
        prompt: str
        options: _containers.RepeatedCompositeFieldContainer[AskQuestionArgs.Option]
        allow_multiple: bool
        def __init__(self, id: _Optional[str] = ..., prompt: _Optional[str] = ..., options: _Optional[_Iterable[_Union[AskQuestionArgs.Option, _Mapping]]] = ..., allow_multiple: _Optional[bool] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    QUESTIONS_FIELD_NUMBER: _ClassVar[int]
    RUN_ASYNC_FIELD_NUMBER: _ClassVar[int]
    ASYNC_ORIGINAL_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    questions: _containers.RepeatedCompositeFieldContainer[AskQuestionArgs.Question]
    run_async: bool
    async_original_tool_call_id: str
    def __init__(self, title: _Optional[str] = ..., questions: _Optional[_Iterable[_Union[AskQuestionArgs.Question, _Mapping]]] = ..., run_async: _Optional[bool] = ..., async_original_tool_call_id: _Optional[str] = ...) -> None: ...

class AskQuestionAsync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AskQuestionError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class AskQuestionInteractionQuery(_message.Message):
    __slots__ = ("args", "tool_call_id")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    args: AskQuestionArgs
    tool_call_id: str
    def __init__(self, args: _Optional[_Union[AskQuestionArgs, _Mapping]] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class AskQuestionInteractionResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: AskQuestionResult
    def __init__(self, result: _Optional[_Union[AskQuestionResult, _Mapping]] = ...) -> None: ...

class AskQuestionRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class AskQuestionResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    ASYNC_FIELD_NUMBER: _ClassVar[int]
    success: AskQuestionSuccess
    error: AskQuestionError
    rejected: AskQuestionRejected
    def __init__(self, success: _Optional[_Union[AskQuestionSuccess, _Mapping]] = ..., error: _Optional[_Union[AskQuestionError, _Mapping]] = ..., rejected: _Optional[_Union[AskQuestionRejected, _Mapping]] = ..., **kwargs) -> None: ...

class AskQuestionSuccess(_message.Message):
    __slots__ = ("answers",)
    class Answer(_message.Message):
        __slots__ = ("question_id", "selected_option_ids", "freeform_text")
        QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
        SELECTED_OPTION_IDS_FIELD_NUMBER: _ClassVar[int]
        FREEFORM_TEXT_FIELD_NUMBER: _ClassVar[int]
        question_id: str
        selected_option_ids: _containers.RepeatedScalarFieldContainer[str]
        freeform_text: str
        def __init__(self, question_id: _Optional[str] = ..., selected_option_ids: _Optional[_Iterable[str]] = ..., freeform_text: _Optional[str] = ...) -> None: ...
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    answers: _containers.RepeatedCompositeFieldContainer[AskQuestionSuccess.Answer]
    def __init__(self, answers: _Optional[_Iterable[_Union[AskQuestionSuccess.Answer, _Mapping]]] = ...) -> None: ...

class AskQuestionToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: AskQuestionArgs
    result: AskQuestionResult
    def __init__(self, args: _Optional[_Union[AskQuestionArgs, _Mapping]] = ..., result: _Optional[_Union[AskQuestionResult, _Mapping]] = ...) -> None: ...

class AssistantMessage(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class AsyncAskQuestionCompletionAction(_message.Message):
    __slots__ = ("original_tool_call_id", "original_args", "result")
    ORIGINAL_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    original_tool_call_id: str
    original_args: AskQuestionArgs
    result: AskQuestionResult
    def __init__(self, original_tool_call_id: _Optional[str] = ..., original_args: _Optional[_Union[AskQuestionArgs, _Mapping]] = ..., result: _Optional[_Union[AskQuestionResult, _Mapping]] = ...) -> None: ...

class AttachAgentHostSessionRequest(_message.Message):
    __slots__ = ("session_id", "last_event_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    last_event_id: int
    def __init__(self, session_id: _Optional[str] = ..., last_event_id: _Optional[int] = ...) -> None: ...

class AttachPtyRequest(_message.Message):
    __slots__ = ("pty_id", "last_event_id")
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    last_event_id: str
    def __init__(self, pty_id: _Optional[str] = ..., last_event_id: _Optional[str] = ...) -> None: ...

class AttachTmuxSessionRequest(_message.Message):
    __slots__ = ("session_id", "cols", "rows")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    cols: int
    rows: int
    def __init__(self, session_id: _Optional[str] = ..., cols: _Optional[int] = ..., rows: _Optional[int] = ...) -> None: ...

class AttachTmuxSessionResponse(_message.Message):
    __slots__ = ("pty_id", "session")
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    session: TmuxSession
    def __init__(self, pty_id: _Optional[str] = ..., session: _Optional[_Union[TmuxSession, _Mapping]] = ...) -> None: ...

class AwaitArgs(_message.Message):
    __slots__ = ("task_id", "block_until_ms", "regex")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_UNTIL_MS_FIELD_NUMBER: _ClassVar[int]
    REGEX_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    block_until_ms: int
    regex: str
    def __init__(self, task_id: _Optional[str] = ..., block_until_ms: _Optional[int] = ..., regex: _Optional[str] = ...) -> None: ...

class AwaitError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class AwaitResult(_message.Message):
    __slots__ = ("complete", "still_running", "error", "success")
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    STILL_RUNNING_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    complete: AwaitTaskComplete
    still_running: AwaitTaskStillRunning
    error: AwaitError
    success: AwaitSuccess
    def __init__(self, complete: _Optional[_Union[AwaitTaskComplete, _Mapping]] = ..., still_running: _Optional[_Union[AwaitTaskStillRunning, _Mapping]] = ..., error: _Optional[_Union[AwaitError, _Mapping]] = ..., success: _Optional[_Union[AwaitSuccess, _Mapping]] = ...) -> None: ...

class AwaitSuccess(_message.Message):
    __slots__ = ("complete", "still_running")
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    STILL_RUNNING_FIELD_NUMBER: _ClassVar[int]
    complete: AwaitTaskComplete
    still_running: AwaitTaskStillRunning
    def __init__(self, complete: _Optional[_Union[AwaitTaskComplete, _Mapping]] = ..., still_running: _Optional[_Union[AwaitTaskStillRunning, _Mapping]] = ...) -> None: ...

class AwaitTaskComplete(_message.Message):
    __slots__ = ("task_id", "runtime_ms", "output_file_path", "output_length", "regex_requested", "regex_match", "exit_code", "wake_reason")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_MS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REGEX_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    REGEX_MATCH_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    WAKE_REASON_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    runtime_ms: int
    output_file_path: str
    output_length: int
    regex_requested: bool
    regex_match: str
    exit_code: int
    wake_reason: str
    def __init__(self, task_id: _Optional[str] = ..., runtime_ms: _Optional[int] = ..., output_file_path: _Optional[str] = ..., output_length: _Optional[int] = ..., regex_requested: _Optional[bool] = ..., regex_match: _Optional[str] = ..., exit_code: _Optional[int] = ..., wake_reason: _Optional[str] = ...) -> None: ...

class AwaitTaskStillRunning(_message.Message):
    __slots__ = ("task_id", "runtime_ms", "output_file_path", "output_length", "regex_requested", "regex_match", "wake_reason")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_MS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REGEX_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    REGEX_MATCH_FIELD_NUMBER: _ClassVar[int]
    WAKE_REASON_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    runtime_ms: int
    output_file_path: str
    output_length: int
    regex_requested: bool
    regex_match: str
    wake_reason: str
    def __init__(self, task_id: _Optional[str] = ..., runtime_ms: _Optional[int] = ..., output_file_path: _Optional[str] = ..., output_length: _Optional[int] = ..., regex_requested: _Optional[bool] = ..., regex_match: _Optional[str] = ..., wake_reason: _Optional[str] = ...) -> None: ...

class AwaitToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: AwaitArgs
    result: AwaitResult
    def __init__(self, args: _Optional[_Union[AwaitArgs, _Mapping]] = ..., result: _Optional[_Union[AwaitResult, _Mapping]] = ...) -> None: ...

class AzureCredentials(_message.Message):
    __slots__ = ("api_key", "base_url", "deployment")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    base_url: str
    deployment: str
    def __init__(self, api_key: _Optional[str] = ..., base_url: _Optional[str] = ..., deployment: _Optional[str] = ...) -> None: ...

class BackgroundShellAction(_message.Message):
    __slots__ = ("tool_call_id",)
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    def __init__(self, tool_call_id: _Optional[str] = ...) -> None: ...

class BackgroundShellSpawnArgs(_message.Message):
    __slots__ = ("command", "working_directory", "tool_call_id", "parsing_result", "sandbox_policy", "enable_write_shell_stdin_tool", "description", "classifier_result", "output_notification", "smart_mode_approval", "hook_approval_requirement", "skip_approval", "conversation_id", "admin_command_denylist")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    PARSING_RESULT_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_POLICY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WRITE_SHELL_STDIN_TOOL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIER_RESULT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    HOOK_APPROVAL_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    SKIP_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_COMMAND_DENYLIST_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    tool_call_id: str
    parsing_result: ShellCommandParsingResult
    sandbox_policy: SandboxPolicy
    enable_write_shell_stdin_tool: bool
    description: str
    classifier_result: CommandClassifierResult
    output_notification: ShellOutputNotificationConfig
    smart_mode_approval: SmartModeApproval
    hook_approval_requirement: ShellHookApprovalRequirement
    skip_approval: bool
    conversation_id: str
    admin_command_denylist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., parsing_result: _Optional[_Union[ShellCommandParsingResult, _Mapping]] = ..., sandbox_policy: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., enable_write_shell_stdin_tool: _Optional[bool] = ..., description: _Optional[str] = ..., classifier_result: _Optional[_Union[CommandClassifierResult, _Mapping]] = ..., output_notification: _Optional[_Union[ShellOutputNotificationConfig, _Mapping]] = ..., smart_mode_approval: _Optional[_Union[SmartModeApproval, _Mapping]] = ..., hook_approval_requirement: _Optional[_Union[ShellHookApprovalRequirement, _Mapping]] = ..., skip_approval: _Optional[bool] = ..., conversation_id: _Optional[str] = ..., admin_command_denylist: _Optional[_Iterable[str]] = ...) -> None: ...

class BackgroundShellSpawnError(_message.Message):
    __slots__ = ("command", "working_directory", "error")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    error: str
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class BackgroundShellSpawnResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "permission_denied", "sandbox_unsupported")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_UNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    success: BackgroundShellSpawnSuccess
    error: BackgroundShellSpawnError
    rejected: ShellRejected
    permission_denied: ShellPermissionDenied
    sandbox_unsupported: ShellSandboxUnsupported
    def __init__(self, success: _Optional[_Union[BackgroundShellSpawnSuccess, _Mapping]] = ..., error: _Optional[_Union[BackgroundShellSpawnError, _Mapping]] = ..., rejected: _Optional[_Union[ShellRejected, _Mapping]] = ..., permission_denied: _Optional[_Union[ShellPermissionDenied, _Mapping]] = ..., sandbox_unsupported: _Optional[_Union[ShellSandboxUnsupported, _Mapping]] = ...) -> None: ...

class BackgroundShellSpawnSuccess(_message.Message):
    __slots__ = ("shell_id", "command", "working_directory", "pid")
    SHELL_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    shell_id: int
    command: str
    working_directory: str
    pid: int
    def __init__(self, shell_id: _Optional[int] = ..., command: _Optional[str] = ..., working_directory: _Optional[str] = ..., pid: _Optional[int] = ...) -> None: ...

class BackgroundSubagentAction(_message.Message):
    __slots__ = ("tool_call_id",)
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    def __init__(self, tool_call_id: _Optional[str] = ...) -> None: ...

class BackgroundTaskCompletion(_message.Message):
    __slots__ = ("task_id", "kind", "status", "title", "detail", "output_path", "thread_id", "reason", "subagent_id", "tool_call_id", "notification_context")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    kind: BackgroundTaskKind
    status: BackgroundTaskStatus
    title: str
    detail: str
    output_path: str
    thread_id: str
    reason: BackgroundTaskCompletionReason
    subagent_id: str
    tool_call_id: str
    notification_context: BackgroundTaskNotificationContext
    def __init__(self, task_id: _Optional[str] = ..., kind: _Optional[_Union[BackgroundTaskKind, str]] = ..., status: _Optional[_Union[BackgroundTaskStatus, str]] = ..., title: _Optional[str] = ..., detail: _Optional[str] = ..., output_path: _Optional[str] = ..., thread_id: _Optional[str] = ..., reason: _Optional[_Union[BackgroundTaskCompletionReason, str]] = ..., subagent_id: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., notification_context: _Optional[_Union[BackgroundTaskNotificationContext, str]] = ...) -> None: ...

class BackgroundTaskCompletionAction(_message.Message):
    __slots__ = ("completions",)
    COMPLETIONS_FIELD_NUMBER: _ClassVar[int]
    completions: _containers.RepeatedCompositeFieldContainer[BackgroundTaskCompletion]
    def __init__(self, completions: _Optional[_Iterable[_Union[BackgroundTaskCompletion, _Mapping]]] = ...) -> None: ...

class BatchGetDiffError(_message.Message):
    __slots__ = ("kind", "message")
    KIND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    kind: BatchGetDiffErrorKind
    message: str
    def __init__(self, kind: _Optional[_Union[BatchGetDiffErrorKind, str]] = ..., message: _Optional[str] = ...) -> None: ...

class BatchGetDiffItem(_message.Message):
    __slots__ = ("diff_request", "fetch_branches")
    DIFF_REQUEST_FIELD_NUMBER: _ClassVar[int]
    FETCH_BRANCHES_FIELD_NUMBER: _ClassVar[int]
    diff_request: GetDiffRequest
    fetch_branches: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, diff_request: _Optional[_Union[GetDiffRequest, _Mapping]] = ..., fetch_branches: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchGetDiffRequest(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BatchGetDiffItem]
    def __init__(self, items: _Optional[_Iterable[_Union[BatchGetDiffItem, _Mapping]]] = ...) -> None: ...

class BatchGetDiffResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[BatchGetDiffResult]
    def __init__(self, results: _Optional[_Iterable[_Union[BatchGetDiffResult, _Mapping]]] = ...) -> None: ...

class BatchGetDiffResult(_message.Message):
    __slots__ = ("item_index", "fetched_branches", "failed_branches", "diff", "error")
    ITEM_INDEX_FIELD_NUMBER: _ClassVar[int]
    FETCHED_BRANCHES_FIELD_NUMBER: _ClassVar[int]
    FAILED_BRANCHES_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    item_index: int
    fetched_branches: _containers.RepeatedScalarFieldContainer[str]
    failed_branches: _containers.RepeatedScalarFieldContainer[str]
    diff: GetDiffResponse
    error: BatchGetDiffError
    def __init__(self, item_index: _Optional[int] = ..., fetched_branches: _Optional[_Iterable[str]] = ..., failed_branches: _Optional[_Iterable[str]] = ..., diff: _Optional[_Union[GetDiffResponse, _Mapping]] = ..., error: _Optional[_Union[BatchGetDiffError, _Mapping]] = ...) -> None: ...

class BedrockCredentials(_message.Message):
    __slots__ = ("access_key", "secret_key", "region", "session_token")
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    secret_key: str
    region: str
    session_token: str
    def __init__(self, access_key: _Optional[str] = ..., secret_key: _Optional[str] = ..., region: _Optional[str] = ..., session_token: _Optional[str] = ...) -> None: ...

class BeforeSubmitPromptAttachment(_message.Message):
    __slots__ = ("type", "file_path")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    type: str
    file_path: str
    def __init__(self, type: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class BeforeSubmitPromptRequestQuery(_message.Message):
    __slots__ = ("prompt", "attachments", "composer_mode", "conversation_id", "generation_id", "model", "model_id", "model_params")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMPOSER_MODE_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    attachments: _containers.RepeatedCompositeFieldContainer[BeforeSubmitPromptAttachment]
    composer_mode: str
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, prompt: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[BeforeSubmitPromptAttachment, _Mapping]]] = ..., composer_mode: _Optional[str] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class BeforeSubmitPromptRequestResponse(_message.Message):
    __slots__ = ("user_message", "additional_context")
    CONTINUE_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_message: str
    additional_context: str
    def __init__(self, user_message: _Optional[str] = ..., additional_context: _Optional[str] = ..., **kwargs) -> None: ...

class BidiPollRequest(_message.Message):
    __slots__ = ("request_id", "start_request")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    START_REQUEST_FIELD_NUMBER: _ClassVar[int]
    request_id: BidiRequestId
    start_request: bool
    def __init__(self, request_id: _Optional[_Union[BidiRequestId, _Mapping]] = ..., start_request: _Optional[bool] = ...) -> None: ...

class BidiPollResponse(_message.Message):
    __slots__ = ("seqno", "data", "eof")
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EOF_FIELD_NUMBER: _ClassVar[int]
    seqno: int
    data: str
    eof: bool
    def __init__(self, seqno: _Optional[int] = ..., data: _Optional[str] = ..., eof: _Optional[bool] = ...) -> None: ...

class BidiRequestId(_message.Message):
    __slots__ = ("request_id",)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    def __init__(self, request_id: _Optional[str] = ...) -> None: ...

class BlameByFilePathArgs(_message.Message):
    __slots__ = ("file_path", "start_line", "end_line")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    END_LINE_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    start_line: int
    end_line: int
    def __init__(self, file_path: _Optional[str] = ..., start_line: _Optional[int] = ..., end_line: _Optional[int] = ...) -> None: ...

class BlameByFilePathError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class BlameByFilePathResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: BlameByFilePathSuccess
    error: BlameByFilePathError
    def __init__(self, success: _Optional[_Union[BlameByFilePathSuccess, _Mapping]] = ..., error: _Optional[_Union[BlameByFilePathError, _Mapping]] = ...) -> None: ...

class BlameByFilePathSuccess(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class BlameByFilePathToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: BlameByFilePathArgs
    result: BlameByFilePathResult
    def __init__(self, args: _Optional[_Union[BlameByFilePathArgs, _Mapping]] = ..., result: _Optional[_Union[BlameByFilePathResult, _Mapping]] = ...) -> None: ...

class BlobEntry(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    value: bytes
    def __init__(self, id: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class BugfixResultItem(_message.Message):
    __slots__ = ("bug_id", "bug_title", "verdict", "explanation", "severity")
    BUG_ID_FIELD_NUMBER: _ClassVar[int]
    BUG_TITLE_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    bug_id: str
    bug_title: str
    verdict: BugfixVerdict
    explanation: str
    severity: str
    def __init__(self, bug_id: _Optional[str] = ..., bug_title: _Optional[str] = ..., verdict: _Optional[_Union[BugfixVerdict, str]] = ..., explanation: _Optional[str] = ..., severity: _Optional[str] = ...) -> None: ...

class CallFrame(_message.Message):
    __slots__ = ("function_name", "url", "line_number", "column_number")
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    function_name: str
    url: str
    line_number: int
    column_number: int
    def __init__(self, function_name: _Optional[str] = ..., url: _Optional[str] = ..., line_number: _Optional[int] = ..., column_number: _Optional[int] = ...) -> None: ...

class CancelAction(_message.Message):
    __slots__ = ("reason", "interrupted_pending_tool_call_resolutions")
    REASON_FIELD_NUMBER: _ClassVar[int]
    INTERRUPTED_PENDING_TOOL_CALL_RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    reason: str
    interrupted_pending_tool_call_resolutions: InterruptedPendingToolCallResolutions
    def __init__(self, reason: _Optional[str] = ..., interrupted_pending_tool_call_resolutions: _Optional[_Union[InterruptedPendingToolCallResolutions, _Mapping]] = ...) -> None: ...

class CancelQueuedAgentHostTurnRequest(_message.Message):
    __slots__ = ("session_id", "turn_id", "reason")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    turn_id: str
    reason: str
    def __init__(self, session_id: _Optional[str] = ..., turn_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelQueuedAgentHostTurnResponse(_message.Message):
    __slots__ = ("cancelled",)
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    cancelled: bool
    def __init__(self, cancelled: _Optional[bool] = ...) -> None: ...

class CancelSubagentAction(_message.Message):
    __slots__ = ("subagent_id",)
    SUBAGENT_ID_FIELD_NUMBER: _ClassVar[int]
    subagent_id: str
    def __init__(self, subagent_id: _Optional[str] = ...) -> None: ...

class CanvasDiagnosticsArgs(_message.Message):
    __slots__ = ("path", "tool_call_id")
    PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    path: str
    tool_call_id: str
    def __init__(self, path: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class CanvasDiagnosticsError(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class CanvasDiagnosticsResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CanvasDiagnosticsSuccess
    error: CanvasDiagnosticsError
    def __init__(self, success: _Optional[_Union[CanvasDiagnosticsSuccess, _Mapping]] = ..., error: _Optional[_Union[CanvasDiagnosticsError, _Mapping]] = ...) -> None: ...

class CanvasDiagnosticsSuccess(_message.Message):
    __slots__ = ("path", "diagnostics")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    path: str
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    def __init__(self, path: _Optional[str] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ...) -> None: ...

class ClaimWorkerRequest(_message.Message):
    __slots__ = ("http_mcp_config_json", "mcp_config_json", "bc_id", "agent_store_claim_config")
    HTTP_MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    BC_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_STORE_CLAIM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    http_mcp_config_json: str
    mcp_config_json: str
    bc_id: str
    agent_store_claim_config: AgentStoreClaimConfig
    def __init__(self, http_mcp_config_json: _Optional[str] = ..., mcp_config_json: _Optional[str] = ..., bc_id: _Optional[str] = ..., agent_store_claim_config: _Optional[_Union[AgentStoreClaimConfig, _Mapping]] = ...) -> None: ...

class ClickAction(_message.Message):
    __slots__ = ("coordinate", "button", "count", "modifier_keys")
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_KEYS_FIELD_NUMBER: _ClassVar[int]
    coordinate: Coordinate
    button: MouseButton
    count: int
    modifier_keys: str
    def __init__(self, coordinate: _Optional[_Union[Coordinate, _Mapping]] = ..., button: _Optional[_Union[MouseButton, str]] = ..., count: _Optional[int] = ..., modifier_keys: _Optional[str] = ...) -> None: ...

class ClickEffectKeyframe(_message.Message):
    __slots__ = ("video_timestamp_ms", "x", "y", "click_type", "action_index", "has_modifiers")
    VIDEO_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    CLICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    HAS_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    video_timestamp_ms: int
    x: int
    y: int
    click_type: ClickType
    action_index: int
    has_modifiers: bool
    def __init__(self, video_timestamp_ms: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., click_type: _Optional[_Union[ClickType, str]] = ..., action_index: _Optional[int] = ..., has_modifiers: _Optional[bool] = ...) -> None: ...

class ClientContinuationConfig(_message.Message):
    __slots__ = ("idle_threshold", "max_loops", "nudge_message", "escape_message_template", "collect_background_children", "children_completed_message_template", "continuation_round_delay_ms")
    IDLE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_LOOPS_FIELD_NUMBER: _ClassVar[int]
    NUDGE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ESCAPE_MESSAGE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    COLLECT_BACKGROUND_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_COMPLETED_MESSAGE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_ROUND_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    idle_threshold: int
    max_loops: int
    nudge_message: str
    escape_message_template: str
    collect_background_children: bool
    children_completed_message_template: str
    continuation_round_delay_ms: int
    def __init__(self, idle_threshold: _Optional[int] = ..., max_loops: _Optional[int] = ..., nudge_message: _Optional[str] = ..., escape_message_template: _Optional[str] = ..., collect_background_children: _Optional[bool] = ..., children_completed_message_template: _Optional[str] = ..., continuation_round_delay_ms: _Optional[int] = ...) -> None: ...

class ClientHeartbeat(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloudSubagentReference(_message.Message):
    __slots__ = ("bc_id", "transcript_path")
    BC_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    bc_id: str
    transcript_path: str
    def __init__(self, bc_id: _Optional[str] = ..., transcript_path: _Optional[str] = ...) -> None: ...

class CodeBlock(_message.Message):
    __slots__ = ("relative_workspace_path", "file_contents", "file_contents_length", "range", "contents", "signatures", "override_contents", "original_contents", "detailed_lines", "file_git_context")
    class Signatures(_message.Message):
        __slots__ = ("ranges",)
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[CursorRange]
        def __init__(self, ranges: _Optional[_Iterable[_Union[CursorRange, _Mapping]]] = ...) -> None: ...
    RELATIVE_WORKSPACE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENTS_LENGTH_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    DETAILED_LINES_FIELD_NUMBER: _ClassVar[int]
    FILE_GIT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    relative_workspace_path: str
    file_contents: str
    file_contents_length: int
    range: CursorRange
    contents: str
    signatures: CodeBlock.Signatures
    override_contents: str
    original_contents: str
    detailed_lines: _containers.RepeatedCompositeFieldContainer[DetailedLine]
    file_git_context: FileGit
    def __init__(self, relative_workspace_path: _Optional[str] = ..., file_contents: _Optional[str] = ..., file_contents_length: _Optional[int] = ..., range: _Optional[_Union[CursorRange, _Mapping]] = ..., contents: _Optional[str] = ..., signatures: _Optional[_Union[CodeBlock.Signatures, _Mapping]] = ..., override_contents: _Optional[str] = ..., original_contents: _Optional[str] = ..., detailed_lines: _Optional[_Iterable[_Union[DetailedLine, _Mapping]]] = ..., file_git_context: _Optional[_Union[FileGit, _Mapping]] = ...) -> None: ...

class CodeResult(_message.Message):
    __slots__ = ("code_block", "score")
    CODE_BLOCK_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    code_block: CodeBlock
    score: float
    def __init__(self, code_block: _Optional[_Union[CodeBlock, _Mapping]] = ..., score: _Optional[float] = ...) -> None: ...

class CommandClassifierResult(_message.Message):
    __slots__ = ("commands", "suggested_sandbox_mode", "classification_failed")
    class SuggestedSandboxMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUGGESTED_SANDBOX_MODE_UNSPECIFIED: _ClassVar[CommandClassifierResult.SuggestedSandboxMode]
        SUGGESTED_SANDBOX_MODE_SANDBOX: _ClassVar[CommandClassifierResult.SuggestedSandboxMode]
        SUGGESTED_SANDBOX_MODE_NO_SANDBOX: _ClassVar[CommandClassifierResult.SuggestedSandboxMode]
        SUGGESTED_SANDBOX_MODE_UNDETERMINED: _ClassVar[CommandClassifierResult.SuggestedSandboxMode]
    SUGGESTED_SANDBOX_MODE_UNSPECIFIED: CommandClassifierResult.SuggestedSandboxMode
    SUGGESTED_SANDBOX_MODE_SANDBOX: CommandClassifierResult.SuggestedSandboxMode
    SUGGESTED_SANDBOX_MODE_NO_SANDBOX: CommandClassifierResult.SuggestedSandboxMode
    SUGGESTED_SANDBOX_MODE_UNDETERMINED: CommandClassifierResult.SuggestedSandboxMode
    class ClassifiedCommand(_message.Message):
        __slots__ = ("name", "arguments", "suggested_allowlist_entry", "subcommand_tokens")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_ALLOWLIST_ENTRY_FIELD_NUMBER: _ClassVar[int]
        SUBCOMMAND_TOKENS_FIELD_NUMBER: _ClassVar[int]
        name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        suggested_allowlist_entry: str
        subcommand_tokens: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ..., suggested_allowlist_entry: _Optional[str] = ..., subcommand_tokens: _Optional[_Iterable[str]] = ...) -> None: ...
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_SANDBOX_MODE_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[CommandClassifierResult.ClassifiedCommand]
    suggested_sandbox_mode: CommandClassifierResult.SuggestedSandboxMode
    classification_failed: bool
    def __init__(self, commands: _Optional[_Iterable[_Union[CommandClassifierResult.ClassifiedCommand, _Mapping]]] = ..., suggested_sandbox_mode: _Optional[_Union[CommandClassifierResult.SuggestedSandboxMode, str]] = ..., classification_failed: _Optional[bool] = ...) -> None: ...

class CommunicateUpdateArgs(_message.Message):
    __slots__ = ("current_step", "final_summary", "completed_subtitle")
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    FINAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    current_step: str
    final_summary: str
    completed_subtitle: str
    def __init__(self, current_step: _Optional[str] = ..., final_summary: _Optional[str] = ..., completed_subtitle: _Optional[str] = ...) -> None: ...

class CommunicateUpdateError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class CommunicateUpdateHistoryEntry(_message.Message):
    __slots__ = ("step", "message_index")
    STEP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    step: str
    message_index: int
    def __init__(self, step: _Optional[str] = ..., message_index: _Optional[int] = ...) -> None: ...

class CommunicateUpdateResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CommunicateUpdateSuccess
    error: CommunicateUpdateError
    def __init__(self, success: _Optional[_Union[CommunicateUpdateSuccess, _Mapping]] = ..., error: _Optional[_Union[CommunicateUpdateError, _Mapping]] = ...) -> None: ...

class CommunicateUpdateSuccess(_message.Message):
    __slots__ = ("current_step", "message_index")
    CURRENT_STEP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    current_step: str
    message_index: int
    def __init__(self, current_step: _Optional[str] = ..., message_index: _Optional[int] = ...) -> None: ...

class CommunicateUpdateToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: CommunicateUpdateArgs
    result: CommunicateUpdateResult
    def __init__(self, args: _Optional[_Union[CommunicateUpdateArgs, _Mapping]] = ..., result: _Optional[_Union[CommunicateUpdateResult, _Mapping]] = ...) -> None: ...

class CommunicateUpdateTurnState(_message.Message):
    __slots__ = ("history", "final_summary", "completed_subtitle")
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    FINAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[CommunicateUpdateHistoryEntry]
    final_summary: str
    completed_subtitle: str
    def __init__(self, history: _Optional[_Iterable[_Union[CommunicateUpdateHistoryEntry, _Mapping]]] = ..., final_summary: _Optional[str] = ..., completed_subtitle: _Optional[str] = ...) -> None: ...

class ComputerUseAction(_message.Message):
    __slots__ = ("mouse_move", "click", "mouse_down", "mouse_up", "drag", "scroll", "type", "key", "wait", "screenshot", "cursor_position")
    MOUSE_MOVE_FIELD_NUMBER: _ClassVar[int]
    CLICK_FIELD_NUMBER: _ClassVar[int]
    MOUSE_DOWN_FIELD_NUMBER: _ClassVar[int]
    MOUSE_UP_FIELD_NUMBER: _ClassVar[int]
    DRAG_FIELD_NUMBER: _ClassVar[int]
    SCROLL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    mouse_move: MouseMoveAction
    click: ClickAction
    mouse_down: MouseDownAction
    mouse_up: MouseUpAction
    drag: DragAction
    scroll: ScrollAction
    type: TypeAction
    key: KeyAction
    wait: WaitAction
    screenshot: ScreenshotAction
    cursor_position: CursorPositionAction
    def __init__(self, mouse_move: _Optional[_Union[MouseMoveAction, _Mapping]] = ..., click: _Optional[_Union[ClickAction, _Mapping]] = ..., mouse_down: _Optional[_Union[MouseDownAction, _Mapping]] = ..., mouse_up: _Optional[_Union[MouseUpAction, _Mapping]] = ..., drag: _Optional[_Union[DragAction, _Mapping]] = ..., scroll: _Optional[_Union[ScrollAction, _Mapping]] = ..., type: _Optional[_Union[TypeAction, _Mapping]] = ..., key: _Optional[_Union[KeyAction, _Mapping]] = ..., wait: _Optional[_Union[WaitAction, _Mapping]] = ..., screenshot: _Optional[_Union[ScreenshotAction, _Mapping]] = ..., cursor_position: _Optional[_Union[CursorPositionAction, _Mapping]] = ...) -> None: ...

class ComputerUseArgs(_message.Message):
    __slots__ = ("tool_call_id", "actions", "description")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    actions: _containers.RepeatedCompositeFieldContainer[ComputerUseAction]
    description: str
    def __init__(self, tool_call_id: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[ComputerUseAction, _Mapping]]] = ..., description: _Optional[str] = ...) -> None: ...

class ComputerUseError(_message.Message):
    __slots__ = ("error", "action_count", "duration_ms", "log", "screenshot", "screenshot_path")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    error: str
    action_count: int
    duration_ms: int
    log: str
    screenshot: str
    screenshot_path: str
    def __init__(self, error: _Optional[str] = ..., action_count: _Optional[int] = ..., duration_ms: _Optional[int] = ..., log: _Optional[str] = ..., screenshot: _Optional[str] = ..., screenshot_path: _Optional[str] = ...) -> None: ...

class ComputerUseResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ComputerUseSuccess
    error: ComputerUseError
    def __init__(self, success: _Optional[_Union[ComputerUseSuccess, _Mapping]] = ..., error: _Optional[_Union[ComputerUseError, _Mapping]] = ...) -> None: ...

class ComputerUseSuccess(_message.Message):
    __slots__ = ("action_count", "duration_ms", "screenshot", "log", "screenshot_path", "cursor_position")
    ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_PATH_FIELD_NUMBER: _ClassVar[int]
    CURSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    action_count: int
    duration_ms: int
    screenshot: str
    log: str
    screenshot_path: str
    cursor_position: Coordinate
    def __init__(self, action_count: _Optional[int] = ..., duration_ms: _Optional[int] = ..., screenshot: _Optional[str] = ..., log: _Optional[str] = ..., screenshot_path: _Optional[str] = ..., cursor_position: _Optional[_Union[Coordinate, _Mapping]] = ...) -> None: ...

class ComputerUseToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ComputerUseArgs
    result: ComputerUseResult
    def __init__(self, args: _Optional[_Union[ComputerUseArgs, _Mapping]] = ..., result: _Optional[_Union[ComputerUseResult, _Mapping]] = ...) -> None: ...

class ConnectScmArgs(_message.Message):
    __slots__ = ("tool_call_id", "github")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    GITHUB_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    github: ConnectScmGithub
    def __init__(self, tool_call_id: _Optional[str] = ..., github: _Optional[_Union[ConnectScmGithub, _Mapping]] = ...) -> None: ...

class ConnectScmError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ConnectScmGithub(_message.Message):
    __slots__ = ("repository", "ghe_application")
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    GHE_APPLICATION_FIELD_NUMBER: _ClassVar[int]
    repository: ConnectScmGithubRepository
    ghe_application: str
    def __init__(self, repository: _Optional[_Union[ConnectScmGithubRepository, _Mapping]] = ..., ghe_application: _Optional[str] = ...) -> None: ...

class ConnectScmGithubRepository(_message.Message):
    __slots__ = ("owner", "repo")
    OWNER_FIELD_NUMBER: _ClassVar[int]
    REPO_FIELD_NUMBER: _ClassVar[int]
    owner: str
    repo: str
    def __init__(self, owner: _Optional[str] = ..., repo: _Optional[str] = ...) -> None: ...

class ConnectScmRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class ConnectScmRequestQuery(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: ConnectScmArgs
    def __init__(self, args: _Optional[_Union[ConnectScmArgs, _Mapping]] = ...) -> None: ...

class ConnectScmRequestResponse(_message.Message):
    __slots__ = ("approved", "rejected", "failed")
    class Approved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Failed(_message.Message):
        __slots__ = ("error",)
        ERROR_FIELD_NUMBER: _ClassVar[int]
        error: str
        def __init__(self, error: _Optional[str] = ...) -> None: ...
    class Rejected(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    approved: ConnectScmRequestResponse.Approved
    rejected: ConnectScmRequestResponse.Rejected
    failed: ConnectScmRequestResponse.Failed
    def __init__(self, approved: _Optional[_Union[ConnectScmRequestResponse.Approved, _Mapping]] = ..., rejected: _Optional[_Union[ConnectScmRequestResponse.Rejected, _Mapping]] = ..., failed: _Optional[_Union[ConnectScmRequestResponse.Failed, _Mapping]] = ...) -> None: ...

class ConnectScmResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: ConnectScmSuccess
    error: ConnectScmError
    rejected: ConnectScmRejected
    def __init__(self, success: _Optional[_Union[ConnectScmSuccess, _Mapping]] = ..., error: _Optional[_Union[ConnectScmError, _Mapping]] = ..., rejected: _Optional[_Union[ConnectScmRejected, _Mapping]] = ...) -> None: ...

class ConnectScmSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConnectScmToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ConnectScmArgs
    result: ConnectScmResult
    def __init__(self, args: _Optional[_Union[ConnectScmArgs, _Mapping]] = ..., result: _Optional[_Union[ConnectScmResult, _Mapping]] = ...) -> None: ...

class ContextInjectionCancelled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContextInjectionDelivered(_message.Message):
    __slots__ = ("step", "delivery_batch_id", "delivered_at_ms")
    STEP_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    step: int
    delivery_batch_id: str
    delivered_at_ms: int
    def __init__(self, step: _Optional[int] = ..., delivery_batch_id: _Optional[str] = ..., delivered_at_ms: _Optional[int] = ...) -> None: ...

class ContextInjectionQueued(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContextInjectionQueuedForNextTurn(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ContextInjectionRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class ContextInjectionState(_message.Message):
    __slots__ = ("queued", "delivered", "queued_for_next_turn", "cancelled", "rejected")
    QUEUED_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    QUEUED_FOR_NEXT_TURN_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    queued: ContextInjectionQueued
    delivered: ContextInjectionDelivered
    queued_for_next_turn: ContextInjectionQueuedForNextTurn
    cancelled: ContextInjectionCancelled
    rejected: ContextInjectionRejected
    def __init__(self, queued: _Optional[_Union[ContextInjectionQueued, _Mapping]] = ..., delivered: _Optional[_Union[ContextInjectionDelivered, _Mapping]] = ..., queued_for_next_turn: _Optional[_Union[ContextInjectionQueuedForNextTurn, _Mapping]] = ..., cancelled: _Optional[_Union[ContextInjectionCancelled, _Mapping]] = ..., rejected: _Optional[_Union[ContextInjectionRejected, _Mapping]] = ...) -> None: ...

class ContextInjectionStateUpdate(_message.Message):
    __slots__ = ("injection_id", "state")
    INJECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    injection_id: str
    state: ContextInjectionState
    def __init__(self, injection_id: _Optional[str] = ..., state: _Optional[_Union[ContextInjectionState, _Mapping]] = ...) -> None: ...

class ConversationAction(_message.Message):
    __slots__ = ("triggering_auth_id", "triggering_user_info", "request_context_parts", "user_message_action", "resume_action", "cancel_action", "summarize_action", "shell_command_action", "start_plan_action", "execute_plan_action", "async_ask_question_completion_action", "cancel_subagent_action", "background_task_completion_action", "background_shell_action", "background_subagent_action", "subscription_notification_action", "goal_continuation_action", "inject_context_action")
    TRIGGERING_AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    TRIGGERING_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_PARTS_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
    RESUME_ACTION_FIELD_NUMBER: _ClassVar[int]
    CANCEL_ACTION_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SHELL_COMMAND_ACTION_FIELD_NUMBER: _ClassVar[int]
    START_PLAN_ACTION_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_PLAN_ACTION_FIELD_NUMBER: _ClassVar[int]
    ASYNC_ASK_QUESTION_COMPLETION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CANCEL_SUBAGENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_TASK_COMPLETION_ACTION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SHELL_ACTION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SUBAGENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NOTIFICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    GOAL_CONTINUATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INJECT_CONTEXT_ACTION_FIELD_NUMBER: _ClassVar[int]
    triggering_auth_id: str
    triggering_user_info: TriggeringUserInfo
    request_context_parts: RequestContextPartReferences
    user_message_action: UserMessageAction
    resume_action: ResumeAction
    cancel_action: CancelAction
    summarize_action: SummarizeAction
    shell_command_action: ShellCommandAction
    start_plan_action: StartPlanAction
    execute_plan_action: ExecutePlanAction
    async_ask_question_completion_action: AsyncAskQuestionCompletionAction
    cancel_subagent_action: CancelSubagentAction
    background_task_completion_action: BackgroundTaskCompletionAction
    background_shell_action: BackgroundShellAction
    background_subagent_action: BackgroundSubagentAction
    subscription_notification_action: SubscriptionNotificationAction
    goal_continuation_action: GoalContinuationAction
    inject_context_action: InjectContextAction
    def __init__(self, triggering_auth_id: _Optional[str] = ..., triggering_user_info: _Optional[_Union[TriggeringUserInfo, _Mapping]] = ..., request_context_parts: _Optional[_Union[RequestContextPartReferences, _Mapping]] = ..., user_message_action: _Optional[_Union[UserMessageAction, _Mapping]] = ..., resume_action: _Optional[_Union[ResumeAction, _Mapping]] = ..., cancel_action: _Optional[_Union[CancelAction, _Mapping]] = ..., summarize_action: _Optional[_Union[SummarizeAction, _Mapping]] = ..., shell_command_action: _Optional[_Union[ShellCommandAction, _Mapping]] = ..., start_plan_action: _Optional[_Union[StartPlanAction, _Mapping]] = ..., execute_plan_action: _Optional[_Union[ExecutePlanAction, _Mapping]] = ..., async_ask_question_completion_action: _Optional[_Union[AsyncAskQuestionCompletionAction, _Mapping]] = ..., cancel_subagent_action: _Optional[_Union[CancelSubagentAction, _Mapping]] = ..., background_task_completion_action: _Optional[_Union[BackgroundTaskCompletionAction, _Mapping]] = ..., background_shell_action: _Optional[_Union[BackgroundShellAction, _Mapping]] = ..., background_subagent_action: _Optional[_Union[BackgroundSubagentAction, _Mapping]] = ..., subscription_notification_action: _Optional[_Union[SubscriptionNotificationAction, _Mapping]] = ..., goal_continuation_action: _Optional[_Union[GoalContinuationAction, _Mapping]] = ..., inject_context_action: _Optional[_Union[InjectContextAction, _Mapping]] = ...) -> None: ...

class ConversationHistory(_message.Message):
    __slots__ = ("messages", "replace_user_info")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[ConversationHistoryMessage]
    replace_user_info: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[ConversationHistoryMessage, _Mapping]]] = ..., replace_user_info: _Optional[bool] = ...) -> None: ...

class ConversationHistoryAssistantContent(_message.Message):
    __slots__ = ("text", "reasoning", "redacted_reasoning", "tool_call")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    REASONING_FIELD_NUMBER: _ClassVar[int]
    REDACTED_REASONING_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    text: ConversationHistoryTextContent
    reasoning: ConversationHistoryReasoningContent
    redacted_reasoning: ConversationHistoryRedactedReasoningContent
    tool_call: ConversationHistoryToolCall
    def __init__(self, text: _Optional[_Union[ConversationHistoryTextContent, _Mapping]] = ..., reasoning: _Optional[_Union[ConversationHistoryReasoningContent, _Mapping]] = ..., redacted_reasoning: _Optional[_Union[ConversationHistoryRedactedReasoningContent, _Mapping]] = ..., tool_call: _Optional[_Union[ConversationHistoryToolCall, _Mapping]] = ...) -> None: ...

class ConversationHistoryAssistantMessage(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[ConversationHistoryAssistantContent]
    def __init__(self, content: _Optional[_Iterable[_Union[ConversationHistoryAssistantContent, _Mapping]]] = ...) -> None: ...

class ConversationHistoryImageContent(_message.Message):
    __slots__ = ("data", "mime_type")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    data: str
    mime_type: str
    def __init__(self, data: _Optional[str] = ..., mime_type: _Optional[str] = ...) -> None: ...

class ConversationHistoryMessage(_message.Message):
    __slots__ = ("user", "assistant", "tool")
    USER_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_FIELD_NUMBER: _ClassVar[int]
    TOOL_FIELD_NUMBER: _ClassVar[int]
    user: ConversationHistoryUserMessage
    assistant: ConversationHistoryAssistantMessage
    tool: ConversationHistoryToolMessage
    def __init__(self, user: _Optional[_Union[ConversationHistoryUserMessage, _Mapping]] = ..., assistant: _Optional[_Union[ConversationHistoryAssistantMessage, _Mapping]] = ..., tool: _Optional[_Union[ConversationHistoryToolMessage, _Mapping]] = ...) -> None: ...

class ConversationHistoryReasoningContent(_message.Message):
    __slots__ = ("text", "signature")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    text: str
    signature: str
    def __init__(self, text: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class ConversationHistoryRedactedReasoningContent(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class ConversationHistoryTextContent(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ConversationHistoryToolCall(_message.Message):
    __slots__ = ("tool_call_id", "tool_name", "args_json")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_JSON_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    tool_name: str
    args_json: str
    def __init__(self, tool_call_id: _Optional[str] = ..., tool_name: _Optional[str] = ..., args_json: _Optional[str] = ...) -> None: ...

class ConversationHistoryToolMessage(_message.Message):
    __slots__ = ("tool_call_id", "tool_name", "content", "is_error", "hook_additional_contexts")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    HOOK_ADDITIONAL_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    tool_name: str
    content: _containers.RepeatedCompositeFieldContainer[ConversationHistoryToolResultContent]
    is_error: bool
    hook_additional_contexts: _containers.RepeatedCompositeFieldContainer[HookAdditionalContext]
    def __init__(self, tool_call_id: _Optional[str] = ..., tool_name: _Optional[str] = ..., content: _Optional[_Iterable[_Union[ConversationHistoryToolResultContent, _Mapping]]] = ..., is_error: _Optional[bool] = ..., hook_additional_contexts: _Optional[_Iterable[_Union[HookAdditionalContext, _Mapping]]] = ...) -> None: ...

class ConversationHistoryToolResultContent(_message.Message):
    __slots__ = ("text", "image")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    text: ConversationHistoryTextContent
    image: ConversationHistoryImageContent
    def __init__(self, text: _Optional[_Union[ConversationHistoryTextContent, _Mapping]] = ..., image: _Optional[_Union[ConversationHistoryImageContent, _Mapping]] = ...) -> None: ...

class ConversationHistoryUserContent(_message.Message):
    __slots__ = ("text", "image")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    text: ConversationHistoryTextContent
    image: ConversationHistoryImageContent
    def __init__(self, text: _Optional[_Union[ConversationHistoryTextContent, _Mapping]] = ..., image: _Optional[_Union[ConversationHistoryImageContent, _Mapping]] = ...) -> None: ...

class ConversationHistoryUserMessage(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[ConversationHistoryUserContent]
    def __init__(self, content: _Optional[_Iterable[_Union[ConversationHistoryUserContent, _Mapping]]] = ...) -> None: ...

class ConversationPlan(_message.Message):
    __slots__ = ("plan",)
    PLAN_FIELD_NUMBER: _ClassVar[int]
    plan: str
    def __init__(self, plan: _Optional[str] = ...) -> None: ...

class ConversationSearchArgs(_message.Message):
    __slots__ = ("query", "tool_call_id", "limit")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    query: str
    tool_call_id: str
    limit: int
    def __init__(self, query: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ConversationSearchError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ConversationSearchHit(_message.Message):
    __slots__ = ("conversation_id", "title", "source", "updated_at_ms", "snippet")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SNIPPET_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    title: str
    source: ConversationSearchSource
    updated_at_ms: int
    snippet: str
    def __init__(self, conversation_id: _Optional[str] = ..., title: _Optional[str] = ..., source: _Optional[_Union[ConversationSearchSource, str]] = ..., updated_at_ms: _Optional[int] = ..., snippet: _Optional[str] = ...) -> None: ...

class ConversationSearchResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ConversationSearchSuccess
    error: ConversationSearchError
    def __init__(self, success: _Optional[_Union[ConversationSearchSuccess, _Mapping]] = ..., error: _Optional[_Union[ConversationSearchError, _Mapping]] = ...) -> None: ...

class ConversationSearchSuccess(_message.Message):
    __slots__ = ("hits", "truncated", "partial", "rebuilding")
    HITS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    REBUILDING_FIELD_NUMBER: _ClassVar[int]
    hits: _containers.RepeatedCompositeFieldContainer[ConversationSearchHit]
    truncated: bool
    partial: bool
    rebuilding: bool
    def __init__(self, hits: _Optional[_Iterable[_Union[ConversationSearchHit, _Mapping]]] = ..., truncated: _Optional[bool] = ..., partial: _Optional[bool] = ..., rebuilding: _Optional[bool] = ...) -> None: ...

class ConversationState(_message.Message):
    __slots__ = ("root_prompt_messages_json", "turns", "todos", "pending_tool_calls", "token_details", "summary", "plan", "summary_archive", "file_states", "summary_archives", "plans", "communicate_update_history", "communicate_update_final_summary", "communicate_update_completed_subtitle", "communicate_update_states_by_parent_tool_call_id")
    class FileStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FileState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FileState, _Mapping]] = ...) -> None: ...
    class PlansEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PlanRegistryEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PlanRegistryEntry, _Mapping]] = ...) -> None: ...
    class CommunicateUpdateStatesByParentToolCallIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CommunicateUpdateTurnState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CommunicateUpdateTurnState, _Mapping]] = ...) -> None: ...
    ROOT_PROMPT_MESSAGES_JSON_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    PENDING_TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    FILE_STATES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    PLANS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_FINAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_COMPLETED_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_STATES_BY_PARENT_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    root_prompt_messages_json: _containers.RepeatedScalarFieldContainer[str]
    turns: _containers.RepeatedCompositeFieldContainer[ConversationTurn]
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    pending_tool_calls: _containers.RepeatedScalarFieldContainer[str]
    token_details: ConversationTokenDetails
    summary: ConversationSummary
    plan: ConversationPlan
    summary_archive: ConversationSummaryArchive
    file_states: _containers.MessageMap[str, FileState]
    summary_archives: _containers.RepeatedCompositeFieldContainer[ConversationSummaryArchive]
    plans: _containers.MessageMap[str, PlanRegistryEntry]
    communicate_update_history: _containers.RepeatedCompositeFieldContainer[CommunicateUpdateHistoryEntry]
    communicate_update_final_summary: str
    communicate_update_completed_subtitle: str
    communicate_update_states_by_parent_tool_call_id: _containers.MessageMap[str, CommunicateUpdateTurnState]
    def __init__(self, root_prompt_messages_json: _Optional[_Iterable[str]] = ..., turns: _Optional[_Iterable[_Union[ConversationTurn, _Mapping]]] = ..., todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ..., pending_tool_calls: _Optional[_Iterable[str]] = ..., token_details: _Optional[_Union[ConversationTokenDetails, _Mapping]] = ..., summary: _Optional[_Union[ConversationSummary, _Mapping]] = ..., plan: _Optional[_Union[ConversationPlan, _Mapping]] = ..., summary_archive: _Optional[_Union[ConversationSummaryArchive, _Mapping]] = ..., file_states: _Optional[_Mapping[str, FileState]] = ..., summary_archives: _Optional[_Iterable[_Union[ConversationSummaryArchive, _Mapping]]] = ..., plans: _Optional[_Mapping[str, PlanRegistryEntry]] = ..., communicate_update_history: _Optional[_Iterable[_Union[CommunicateUpdateHistoryEntry, _Mapping]]] = ..., communicate_update_final_summary: _Optional[str] = ..., communicate_update_completed_subtitle: _Optional[str] = ..., communicate_update_states_by_parent_tool_call_id: _Optional[_Mapping[str, CommunicateUpdateTurnState]] = ...) -> None: ...

class ConversationStateStructure(_message.Message):
    __slots__ = ("root_prompt_messages_json", "turns", "todos", "pending_tool_calls", "token_details", "summary", "plan", "previous_workspace_uris", "mode", "summary_archive", "file_states", "file_states_v2", "summary_archives", "turn_timings", "subagent_states", "self_summary_count", "read_paths", "active_branch_name", "plans", "tracked_git_repo_branches", "agent_type", "communicate_update_history", "subagent_threads", "communicate_update_final_summary", "communicate_update_completed_subtitle", "communicate_update_states_by_parent_tool_call_id", "subagent_runs_by_parent_tool_call_id", "conversation_started_timestamp_ms", "conversation_started_time_zone", "subagent_state_refs", "goal_state", "is_root_project_conversation")
    class FileStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class FileStatesV2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FileStateStructure
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[FileStateStructure, _Mapping]] = ...) -> None: ...
    class SubagentStatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SubagentPersistedState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SubagentPersistedState, _Mapping]] = ...) -> None: ...
    class PlansEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PlanRegistryEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PlanRegistryEntry, _Mapping]] = ...) -> None: ...
    class SubagentThreadsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class CommunicateUpdateStatesByParentToolCallIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CommunicateUpdateTurnState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[CommunicateUpdateTurnState, _Mapping]] = ...) -> None: ...
    class SubagentRunsByParentToolCallIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SubagentRunState
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SubagentRunState, _Mapping]] = ...) -> None: ...
    class SubagentStateRefsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    ROOT_PROMPT_MESSAGES_JSON_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    PENDING_TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_WORKSPACE_URIS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    FILE_STATES_FIELD_NUMBER: _ClassVar[int]
    FILE_STATES_V2_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ARCHIVES_FIELD_NUMBER: _ClassVar[int]
    TURN_TIMINGS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_STATES_FIELD_NUMBER: _ClassVar[int]
    SELF_SUMMARY_COUNT_FIELD_NUMBER: _ClassVar[int]
    READ_PATHS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANS_FIELD_NUMBER: _ClassVar[int]
    TRACKED_GIT_REPO_BRANCHES_FIELD_NUMBER: _ClassVar[int]
    AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_THREADS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_FINAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_COMPLETED_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_STATES_BY_PARENT_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_RUNS_BY_PARENT_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STARTED_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STARTED_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_STATE_REFS_FIELD_NUMBER: _ClassVar[int]
    GOAL_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_ROOT_PROJECT_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    root_prompt_messages_json: _containers.RepeatedScalarFieldContainer[bytes]
    turns: _containers.RepeatedScalarFieldContainer[bytes]
    todos: _containers.RepeatedScalarFieldContainer[bytes]
    pending_tool_calls: _containers.RepeatedScalarFieldContainer[str]
    token_details: ConversationTokenDetails
    summary: bytes
    plan: bytes
    previous_workspace_uris: _containers.RepeatedScalarFieldContainer[str]
    mode: AgentMode
    summary_archive: bytes
    file_states: _containers.ScalarMap[str, bytes]
    file_states_v2: _containers.MessageMap[str, FileStateStructure]
    summary_archives: _containers.RepeatedScalarFieldContainer[bytes]
    turn_timings: _containers.RepeatedCompositeFieldContainer[StepTiming]
    subagent_states: _containers.MessageMap[str, SubagentPersistedState]
    self_summary_count: int
    read_paths: _containers.RepeatedScalarFieldContainer[str]
    active_branch_name: str
    plans: _containers.MessageMap[str, PlanRegistryEntry]
    tracked_git_repo_branches: _containers.RepeatedCompositeFieldContainer[TrackedGitRepo]
    agent_type: str
    communicate_update_history: _containers.RepeatedCompositeFieldContainer[CommunicateUpdateHistoryEntry]
    subagent_threads: _containers.ScalarMap[str, str]
    communicate_update_final_summary: str
    communicate_update_completed_subtitle: str
    communicate_update_states_by_parent_tool_call_id: _containers.MessageMap[str, CommunicateUpdateTurnState]
    subagent_runs_by_parent_tool_call_id: _containers.MessageMap[str, SubagentRunState]
    conversation_started_timestamp_ms: int
    conversation_started_time_zone: str
    subagent_state_refs: _containers.ScalarMap[str, bytes]
    goal_state: GoalState
    is_root_project_conversation: bool
    def __init__(self, root_prompt_messages_json: _Optional[_Iterable[bytes]] = ..., turns: _Optional[_Iterable[bytes]] = ..., todos: _Optional[_Iterable[bytes]] = ..., pending_tool_calls: _Optional[_Iterable[str]] = ..., token_details: _Optional[_Union[ConversationTokenDetails, _Mapping]] = ..., summary: _Optional[bytes] = ..., plan: _Optional[bytes] = ..., previous_workspace_uris: _Optional[_Iterable[str]] = ..., mode: _Optional[_Union[AgentMode, str]] = ..., summary_archive: _Optional[bytes] = ..., file_states: _Optional[_Mapping[str, bytes]] = ..., file_states_v2: _Optional[_Mapping[str, FileStateStructure]] = ..., summary_archives: _Optional[_Iterable[bytes]] = ..., turn_timings: _Optional[_Iterable[_Union[StepTiming, _Mapping]]] = ..., subagent_states: _Optional[_Mapping[str, SubagentPersistedState]] = ..., self_summary_count: _Optional[int] = ..., read_paths: _Optional[_Iterable[str]] = ..., active_branch_name: _Optional[str] = ..., plans: _Optional[_Mapping[str, PlanRegistryEntry]] = ..., tracked_git_repo_branches: _Optional[_Iterable[_Union[TrackedGitRepo, _Mapping]]] = ..., agent_type: _Optional[str] = ..., communicate_update_history: _Optional[_Iterable[_Union[CommunicateUpdateHistoryEntry, _Mapping]]] = ..., subagent_threads: _Optional[_Mapping[str, str]] = ..., communicate_update_final_summary: _Optional[str] = ..., communicate_update_completed_subtitle: _Optional[str] = ..., communicate_update_states_by_parent_tool_call_id: _Optional[_Mapping[str, CommunicateUpdateTurnState]] = ..., subagent_runs_by_parent_tool_call_id: _Optional[_Mapping[str, SubagentRunState]] = ..., conversation_started_timestamp_ms: _Optional[int] = ..., conversation_started_time_zone: _Optional[str] = ..., subagent_state_refs: _Optional[_Mapping[str, bytes]] = ..., goal_state: _Optional[_Union[GoalState, _Mapping]] = ..., is_root_project_conversation: _Optional[bool] = ...) -> None: ...

class ConversationStep(_message.Message):
    __slots__ = ("assistant_message", "tool_call", "thinking_message")
    ASSISTANT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    THINKING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    assistant_message: AssistantMessage
    tool_call: ToolCall
    thinking_message: ThinkingMessage
    def __init__(self, assistant_message: _Optional[_Union[AssistantMessage, _Mapping]] = ..., tool_call: _Optional[_Union[ToolCall, _Mapping]] = ..., thinking_message: _Optional[_Union[ThinkingMessage, _Mapping]] = ...) -> None: ...

class ConversationSummary(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: str
    def __init__(self, summary: _Optional[str] = ...) -> None: ...

class ConversationSummaryArchive(_message.Message):
    __slots__ = ("summarized_messages", "summary", "window_tail", "summary_message")
    SUMMARIZED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TAIL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    summarized_messages: _containers.RepeatedScalarFieldContainer[bytes]
    summary: str
    window_tail: int
    summary_message: bytes
    def __init__(self, summarized_messages: _Optional[_Iterable[bytes]] = ..., summary: _Optional[str] = ..., window_tail: _Optional[int] = ..., summary_message: _Optional[bytes] = ...) -> None: ...

class ConversationTokenDetails(_message.Message):
    __slots__ = ("used_tokens", "max_tokens", "breakdown", "prompt_context_usage_tree", "prompt_context_usage_snapshot_blob_id")
    USED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CONTEXT_USAGE_TREE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_CONTEXT_USAGE_SNAPSHOT_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    used_tokens: int
    max_tokens: int
    breakdown: PromptTokenBreakdownSnapshot
    prompt_context_usage_tree: PromptContextUsageTree
    prompt_context_usage_snapshot_blob_id: bytes
    def __init__(self, used_tokens: _Optional[int] = ..., max_tokens: _Optional[int] = ..., breakdown: _Optional[_Union[PromptTokenBreakdownSnapshot, _Mapping]] = ..., prompt_context_usage_tree: _Optional[_Union[PromptContextUsageTree, _Mapping]] = ..., prompt_context_usage_snapshot_blob_id: _Optional[bytes] = ...) -> None: ...

class ConversationTurn(_message.Message):
    __slots__ = ("agent_conversation_turn", "shell_conversation_turn")
    AGENT_CONVERSATION_TURN_FIELD_NUMBER: _ClassVar[int]
    SHELL_CONVERSATION_TURN_FIELD_NUMBER: _ClassVar[int]
    agent_conversation_turn: AgentConversationTurn
    shell_conversation_turn: ShellConversationTurn
    def __init__(self, agent_conversation_turn: _Optional[_Union[AgentConversationTurn, _Mapping]] = ..., shell_conversation_turn: _Optional[_Union[ShellConversationTurn, _Mapping]] = ...) -> None: ...

class ConversationTurnStructure(_message.Message):
    __slots__ = ("agent_conversation_turn", "shell_conversation_turn")
    AGENT_CONVERSATION_TURN_FIELD_NUMBER: _ClassVar[int]
    SHELL_CONVERSATION_TURN_FIELD_NUMBER: _ClassVar[int]
    agent_conversation_turn: AgentConversationTurnStructure
    shell_conversation_turn: ShellConversationTurnStructure
    def __init__(self, agent_conversation_turn: _Optional[_Union[AgentConversationTurnStructure, _Mapping]] = ..., shell_conversation_turn: _Optional[_Union[ShellConversationTurnStructure, _Mapping]] = ...) -> None: ...

class Coordinate(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class CreateAgentHostSessionRequest(_message.Message):
    __slots__ = ("session_id", "initial_history", "session_options")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_HISTORY_FIELD_NUMBER: _ClassVar[int]
    SESSION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    initial_history: ConversationStateStructure
    session_options: AgentHostSessionOptions
    def __init__(self, session_id: _Optional[str] = ..., initial_history: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., session_options: _Optional[_Union[AgentHostSessionOptions, _Mapping]] = ...) -> None: ...

class CreateAgentHostSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateGoalArgs(_message.Message):
    __slots__ = ("objective",)
    OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    objective: str
    def __init__(self, objective: _Optional[str] = ...) -> None: ...

class CreateGoalResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: CreateGoalSuccess
    error: GoalError
    def __init__(self, success: _Optional[_Union[CreateGoalSuccess, _Mapping]] = ..., error: _Optional[_Union[GoalError, _Mapping]] = ...) -> None: ...

class CreateGoalSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateGoalToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: CreateGoalArgs
    result: CreateGoalResult
    def __init__(self, args: _Optional[_Union[CreateGoalArgs, _Mapping]] = ..., result: _Optional[_Union[CreateGoalResult, _Mapping]] = ...) -> None: ...

class CreatePlanArgs(_message.Message):
    __slots__ = ("plan", "todos", "overview", "name", "is_project", "phases")
    PLAN_FIELD_NUMBER: _ClassVar[int]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PROJECT_FIELD_NUMBER: _ClassVar[int]
    PHASES_FIELD_NUMBER: _ClassVar[int]
    plan: str
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    overview: str
    name: str
    is_project: bool
    phases: _containers.RepeatedCompositeFieldContainer[Phase]
    def __init__(self, plan: _Optional[str] = ..., todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ..., overview: _Optional[str] = ..., name: _Optional[str] = ..., is_project: _Optional[bool] = ..., phases: _Optional[_Iterable[_Union[Phase, _Mapping]]] = ...) -> None: ...

class CreatePlanError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class CreatePlanRequestQuery(_message.Message):
    __slots__ = ("args", "tool_call_id")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    args: CreatePlanArgs
    tool_call_id: str
    def __init__(self, args: _Optional[_Union[CreatePlanArgs, _Mapping]] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class CreatePlanRequestResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: CreatePlanResult
    def __init__(self, result: _Optional[_Union[CreatePlanResult, _Mapping]] = ...) -> None: ...

class CreatePlanResult(_message.Message):
    __slots__ = ("plan_uri", "success", "error")
    PLAN_URI_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    plan_uri: str
    success: CreatePlanSuccess
    error: CreatePlanError
    def __init__(self, plan_uri: _Optional[str] = ..., success: _Optional[_Union[CreatePlanSuccess, _Mapping]] = ..., error: _Optional[_Union[CreatePlanError, _Mapping]] = ...) -> None: ...

class CreatePlanSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePlanToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: CreatePlanArgs
    result: CreatePlanResult
    def __init__(self, args: _Optional[_Union[CreatePlanArgs, _Mapping]] = ..., result: _Optional[_Union[CreatePlanResult, _Mapping]] = ...) -> None: ...

class CreatePrAction(_message.Message):
    __slots__ = ("title", "body", "base_branch", "draft", "branch_name", "add_labels", "repo_url", "skip_branch_prefix_check", "stack_on_pr_number")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_LABELS_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    SKIP_BRANCH_PREFIX_CHECK_FIELD_NUMBER: _ClassVar[int]
    STACK_ON_PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    base_branch: str
    draft: bool
    branch_name: str
    add_labels: _containers.RepeatedScalarFieldContainer[str]
    repo_url: str
    skip_branch_prefix_check: bool
    stack_on_pr_number: int
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., base_branch: _Optional[str] = ..., draft: _Optional[bool] = ..., branch_name: _Optional[str] = ..., add_labels: _Optional[_Iterable[str]] = ..., repo_url: _Optional[str] = ..., skip_branch_prefix_check: _Optional[bool] = ..., stack_on_pr_number: _Optional[int] = ...) -> None: ...

class CreateTmuxSessionRequest(_message.Message):
    __slots__ = ("session_name", "display_name", "kind", "process", "cwd", "env")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    session_name: str
    display_name: str
    kind: TmuxSessionKind
    process: Process
    cwd: str
    env: _containers.ScalarMap[str, str]
    def __init__(self, session_name: _Optional[str] = ..., display_name: _Optional[str] = ..., kind: _Optional[_Union[TmuxSessionKind, str]] = ..., process: _Optional[_Union[Process, _Mapping]] = ..., cwd: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateTmuxSessionResponse(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: TmuxSession
    def __init__(self, session: _Optional[_Union[TmuxSession, _Mapping]] = ...) -> None: ...

class CreateTranscriptOverviewRequest(_message.Message):
    __slots__ = ("formatted_conversation",)
    FORMATTED_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    formatted_conversation: str
    def __init__(self, formatted_conversation: _Optional[str] = ...) -> None: ...

class CreateTranscriptOverviewResponse(_message.Message):
    __slots__ = ("overview",)
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    overview: str
    def __init__(self, overview: _Optional[str] = ...) -> None: ...

class CursorPackage(_message.Message):
    __slots__ = ("name", "description", "folder_path", "enabled", "parse_error", "prompts", "readme_file_path", "package_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    PROMPTS_FIELD_NUMBER: _ClassVar[int]
    README_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    folder_path: str
    enabled: bool
    parse_error: str
    prompts: _containers.RepeatedCompositeFieldContainer[CursorPackagePrompt]
    readme_file_path: str
    package_type: PackageType
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., folder_path: _Optional[str] = ..., enabled: _Optional[bool] = ..., parse_error: _Optional[str] = ..., prompts: _Optional[_Iterable[_Union[CursorPackagePrompt, _Mapping]]] = ..., readme_file_path: _Optional[str] = ..., package_type: _Optional[_Union[PackageType, str]] = ...) -> None: ...

class CursorPackagePrompt(_message.Message):
    __slots__ = ("name", "file_path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    file_path: str
    def __init__(self, name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class CursorPath(_message.Message):
    __slots__ = ("style", "keyframes")
    STYLE_FIELD_NUMBER: _ClassVar[int]
    KEYFRAMES_FIELD_NUMBER: _ClassVar[int]
    style: MotionStyle
    keyframes: _containers.RepeatedCompositeFieldContainer[CursorPathKeyframe]
    def __init__(self, style: _Optional[_Union[MotionStyle, str]] = ..., keyframes: _Optional[_Iterable[_Union[CursorPathKeyframe, _Mapping]]] = ...) -> None: ...

class CursorPathKeyframe(_message.Message):
    __slots__ = ("video_timestamp_ms", "x", "y", "cursor_type", "velocity")
    VIDEO_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    CURSOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    video_timestamp_ms: int
    x: int
    y: int
    cursor_type: CursorType
    velocity: float
    def __init__(self, video_timestamp_ms: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., cursor_type: _Optional[_Union[CursorType, str]] = ..., velocity: _Optional[float] = ...) -> None: ...

class CursorPosition(_message.Message):
    __slots__ = ("line", "column")
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    line: int
    column: int
    def __init__(self, line: _Optional[int] = ..., column: _Optional[int] = ...) -> None: ...

class CursorPositionAction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CursorRange(_message.Message):
    __slots__ = ("start_position", "end_position")
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    END_POSITION_FIELD_NUMBER: _ClassVar[int]
    start_position: CursorPosition
    end_position: CursorPosition
    def __init__(self, start_position: _Optional[_Union[CursorPosition, _Mapping]] = ..., end_position: _Optional[_Union[CursorPosition, _Mapping]] = ...) -> None: ...

class CursorRule(_message.Message):
    __slots__ = ("full_path", "content", "type", "source", "git_remote_origin", "parse_error", "environments", "disabled_environments", "plugin", "marketplace", "plugin_id", "marketplace_id", "scoped_to", "frontmatter", "is_required")
    FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    GIT_REMOTE_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPED_TO_FIELD_NUMBER: _ClassVar[int]
    FRONTMATTER_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    full_path: str
    content: str
    type: CursorRuleType
    source: CursorRuleSource
    git_remote_origin: str
    parse_error: str
    environments: _containers.RepeatedScalarFieldContainer[str]
    disabled_environments: _containers.RepeatedScalarFieldContainer[str]
    plugin: str
    marketplace: str
    plugin_id: str
    marketplace_id: str
    scoped_to: _containers.RepeatedScalarFieldContainer[str]
    frontmatter: str
    is_required: bool
    def __init__(self, full_path: _Optional[str] = ..., content: _Optional[str] = ..., type: _Optional[_Union[CursorRuleType, _Mapping]] = ..., source: _Optional[_Union[CursorRuleSource, str]] = ..., git_remote_origin: _Optional[str] = ..., parse_error: _Optional[str] = ..., environments: _Optional[_Iterable[str]] = ..., disabled_environments: _Optional[_Iterable[str]] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., plugin_id: _Optional[str] = ..., marketplace_id: _Optional[str] = ..., scoped_to: _Optional[_Iterable[str]] = ..., frontmatter: _Optional[str] = ..., is_required: _Optional[bool] = ...) -> None: ...

class CursorRuleType(_message.Message):
    __slots__ = ("file_globbed", "agent_fetched", "manually_attached")
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    FILE_GLOBBED_FIELD_NUMBER: _ClassVar[int]
    AGENT_FETCHED_FIELD_NUMBER: _ClassVar[int]
    MANUALLY_ATTACHED_FIELD_NUMBER: _ClassVar[int]
    file_globbed: CursorRuleTypeFileGlobs
    agent_fetched: CursorRuleTypeAgentFetched
    manually_attached: CursorRuleTypeManuallyAttached
    def __init__(self, file_globbed: _Optional[_Union[CursorRuleTypeFileGlobs, _Mapping]] = ..., agent_fetched: _Optional[_Union[CursorRuleTypeAgentFetched, _Mapping]] = ..., manually_attached: _Optional[_Union[CursorRuleTypeManuallyAttached, _Mapping]] = ..., **kwargs) -> None: ...

class CursorRuleTypeAgentFetched(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class CursorRuleTypeFileGlobs(_message.Message):
    __slots__ = ("globs",)
    GLOBS_FIELD_NUMBER: _ClassVar[int]
    globs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, globs: _Optional[_Iterable[str]] = ...) -> None: ...

class CursorRuleTypeGlobal(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CursorRuleTypeManuallyAttached(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomModeDescriptor(_message.Message):
    __slots__ = ("id", "label", "description", "icon", "color", "source", "source_path", "source_hash", "managed_skill_id", "plugin_id", "plugin_snapshot_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    MANAGED_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_SNAPSHOT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    description: str
    icon: str
    color: str
    source: CustomModeSource
    source_path: str
    source_hash: str
    managed_skill_id: str
    plugin_id: str
    plugin_snapshot_token: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., description: _Optional[str] = ..., icon: _Optional[str] = ..., color: _Optional[str] = ..., source: _Optional[_Union[CustomModeSource, str]] = ..., source_path: _Optional[str] = ..., source_hash: _Optional[str] = ..., managed_skill_id: _Optional[str] = ..., plugin_id: _Optional[str] = ..., plugin_snapshot_token: _Optional[str] = ...) -> None: ...

class CustomModeExitIntent(_message.Message):
    __slots__ = ("next_mode", "exited_mode")
    NEXT_MODE_FIELD_NUMBER: _ClassVar[int]
    EXITED_MODE_FIELD_NUMBER: _ClassVar[int]
    next_mode: AgentMode
    exited_mode: SubmittedExitedCustomMode
    def __init__(self, next_mode: _Optional[_Union[AgentMode, str]] = ..., exited_mode: _Optional[_Union[SubmittedExitedCustomMode, _Mapping]] = ...) -> None: ...

class CustomModeIntent(_message.Message):
    __slots__ = ("enter", "exit")
    ENTER_FIELD_NUMBER: _ClassVar[int]
    EXIT_FIELD_NUMBER: _ClassVar[int]
    enter: SubmittedCustomMode
    exit: CustomModeExitIntent
    def __init__(self, enter: _Optional[_Union[SubmittedCustomMode, _Mapping]] = ..., exit: _Optional[_Union[CustomModeExitIntent, _Mapping]] = ...) -> None: ...

class CustomSubagent(_message.Message):
    __slots__ = ("full_path", "name", "description", "tools", "model", "prompt", "permission_mode", "is_background", "plugin", "marketplace", "plugin_id", "marketplace_id", "force_default_model", "source")
    FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_DEFAULT_MODEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    full_path: str
    name: str
    description: str
    tools: _containers.RepeatedScalarFieldContainer[str]
    model: str
    prompt: str
    permission_mode: CustomSubagentPermissionMode
    is_background: bool
    plugin: str
    marketplace: str
    plugin_id: str
    marketplace_id: str
    force_default_model: bool
    source: str
    def __init__(self, full_path: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tools: _Optional[_Iterable[str]] = ..., model: _Optional[str] = ..., prompt: _Optional[str] = ..., permission_mode: _Optional[_Union[CustomSubagentPermissionMode, str]] = ..., is_background: _Optional[bool] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., plugin_id: _Optional[str] = ..., marketplace_id: _Optional[str] = ..., force_default_model: _Optional[bool] = ..., source: _Optional[str] = ...) -> None: ...

class DebugModeConfig(_message.Message):
    __slots__ = ("log_path", "server_endpoint", "session_id")
    LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    SERVER_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    log_path: str
    server_endpoint: str
    session_id: str
    def __init__(self, log_path: _Optional[str] = ..., server_endpoint: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...

class DecisionInput(_message.Message):
    __slots__ = ("video_path", "video_duration_ms", "video_width", "video_height", "action_count", "zoom_candidates", "idle_periods", "click_effects", "keystroke_events", "cursor_paths")
    VIDEO_PATH_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIDEO_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ZOOM_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    IDLE_PERIODS_FIELD_NUMBER: _ClassVar[int]
    CLICK_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    KEYSTROKE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_PATHS_FIELD_NUMBER: _ClassVar[int]
    video_path: str
    video_duration_ms: int
    video_width: int
    video_height: int
    action_count: int
    zoom_candidates: _containers.RepeatedCompositeFieldContainer[ZoomCandidate]
    idle_periods: _containers.RepeatedCompositeFieldContainer[IdlePeriod]
    click_effects: _containers.RepeatedCompositeFieldContainer[ClickEffectKeyframe]
    keystroke_events: _containers.RepeatedCompositeFieldContainer[KeystrokeEvent]
    cursor_paths: _containers.RepeatedCompositeFieldContainer[CursorPath]
    def __init__(self, video_path: _Optional[str] = ..., video_duration_ms: _Optional[int] = ..., video_width: _Optional[int] = ..., video_height: _Optional[int] = ..., action_count: _Optional[int] = ..., zoom_candidates: _Optional[_Iterable[_Union[ZoomCandidate, _Mapping]]] = ..., idle_periods: _Optional[_Iterable[_Union[IdlePeriod, _Mapping]]] = ..., click_effects: _Optional[_Iterable[_Union[ClickEffectKeyframe, _Mapping]]] = ..., keystroke_events: _Optional[_Iterable[_Union[KeystrokeEvent, _Mapping]]] = ..., cursor_paths: _Optional[_Iterable[_Union[CursorPath, _Mapping]]] = ...) -> None: ...

class DecisionOutput(_message.Message):
    __slots__ = ("cursor_style", "selected_zooms", "selected_speedups", "show_click_effects", "selected_click_effects", "show_keystrokes", "cuts")
    CURSOR_STYLE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ZOOMS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SPEEDUPS_FIELD_NUMBER: _ClassVar[int]
    SHOW_CLICK_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_CLICK_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_KEYSTROKES_FIELD_NUMBER: _ClassVar[int]
    CUTS_FIELD_NUMBER: _ClassVar[int]
    cursor_style: MotionStyle
    selected_zooms: _containers.RepeatedCompositeFieldContainer[ZoomSelection]
    selected_speedups: _containers.RepeatedCompositeFieldContainer[SpeedupSelection]
    show_click_effects: bool
    selected_click_effects: _containers.RepeatedScalarFieldContainer[int]
    show_keystrokes: bool
    cuts: _containers.RepeatedCompositeFieldContainer[VideoCut]
    def __init__(self, cursor_style: _Optional[_Union[MotionStyle, str]] = ..., selected_zooms: _Optional[_Iterable[_Union[ZoomSelection, _Mapping]]] = ..., selected_speedups: _Optional[_Iterable[_Union[SpeedupSelection, _Mapping]]] = ..., show_click_effects: _Optional[bool] = ..., selected_click_effects: _Optional[_Iterable[int]] = ..., show_keystrokes: _Optional[bool] = ..., cuts: _Optional[_Iterable[_Union[VideoCut, _Mapping]]] = ...) -> None: ...

class DeleteAgentHostSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class DeleteAgentHostSessionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteArgs(_message.Message):
    __slots__ = ("path", "tool_call_id")
    PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    path: str
    tool_call_id: str
    def __init__(self, path: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class DeleteError(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class DeleteFileBusy(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class DeleteFileNotFound(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class DeleteNotFile(_message.Message):
    __slots__ = ("path", "actual_type")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    path: str
    actual_type: str
    def __init__(self, path: _Optional[str] = ..., actual_type: _Optional[str] = ...) -> None: ...

class DeletePermissionDenied(_message.Message):
    __slots__ = ("path", "client_visible_error", "is_readonly")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VISIBLE_ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    path: str
    client_visible_error: str
    is_readonly: bool
    def __init__(self, path: _Optional[str] = ..., client_visible_error: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class DeleteRejected(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeleteResult(_message.Message):
    __slots__ = ("success", "file_not_found", "not_file", "permission_denied", "file_busy", "rejected", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FILE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    NOT_FILE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    FILE_BUSY_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: DeleteSuccess
    file_not_found: DeleteFileNotFound
    not_file: DeleteNotFile
    permission_denied: DeletePermissionDenied
    file_busy: DeleteFileBusy
    rejected: DeleteRejected
    error: DeleteError
    def __init__(self, success: _Optional[_Union[DeleteSuccess, _Mapping]] = ..., file_not_found: _Optional[_Union[DeleteFileNotFound, _Mapping]] = ..., not_file: _Optional[_Union[DeleteNotFile, _Mapping]] = ..., permission_denied: _Optional[_Union[DeletePermissionDenied, _Mapping]] = ..., file_busy: _Optional[_Union[DeleteFileBusy, _Mapping]] = ..., rejected: _Optional[_Union[DeleteRejected, _Mapping]] = ..., error: _Optional[_Union[DeleteError, _Mapping]] = ...) -> None: ...

class DeleteSuccess(_message.Message):
    __slots__ = ("path", "deleted_file", "file_size", "prev_content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DELETED_FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PREV_CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    deleted_file: str
    file_size: int
    prev_content: str
    def __init__(self, path: _Optional[str] = ..., deleted_file: _Optional[str] = ..., file_size: _Optional[int] = ..., prev_content: _Optional[str] = ...) -> None: ...

class DeleteToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: DeleteArgs
    result: DeleteResult
    def __init__(self, args: _Optional[_Union[DeleteArgs, _Mapping]] = ..., result: _Optional[_Union[DeleteResult, _Mapping]] = ...) -> None: ...

class DetailedLine(_message.Message):
    __slots__ = ("text", "line_number", "is_signature")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    IS_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    text: str
    line_number: float
    is_signature: bool
    def __init__(self, text: _Optional[str] = ..., line_number: _Optional[float] = ..., is_signature: _Optional[bool] = ...) -> None: ...

class Diagnostic(_message.Message):
    __slots__ = ("severity", "range", "message", "source", "code", "is_stale")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    IS_STALE_FIELD_NUMBER: _ClassVar[int]
    severity: DiagnosticSeverity
    range: Range
    message: str
    source: str
    code: str
    is_stale: bool
    def __init__(self, severity: _Optional[_Union[DiagnosticSeverity, str]] = ..., range: _Optional[_Union[Range, _Mapping]] = ..., message: _Optional[str] = ..., source: _Optional[str] = ..., code: _Optional[str] = ..., is_stale: _Optional[bool] = ...) -> None: ...

class DiagnosticItem(_message.Message):
    __slots__ = ("severity", "range", "message", "source", "code", "is_stale")
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    IS_STALE_FIELD_NUMBER: _ClassVar[int]
    severity: DiagnosticSeverity
    range: DiagnosticRange
    message: str
    source: str
    code: str
    is_stale: bool
    def __init__(self, severity: _Optional[_Union[DiagnosticSeverity, str]] = ..., range: _Optional[_Union[DiagnosticRange, _Mapping]] = ..., message: _Optional[str] = ..., source: _Optional[str] = ..., code: _Optional[str] = ..., is_stale: _Optional[bool] = ...) -> None: ...

class DiagnosticRange(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: Position
    end: Position
    def __init__(self, start: _Optional[_Union[Position, _Mapping]] = ..., end: _Optional[_Union[Position, _Mapping]] = ...) -> None: ...

class DiagnosticsArgs(_message.Message):
    __slots__ = ("path", "tool_call_id")
    PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    path: str
    tool_call_id: str
    def __init__(self, path: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class DiagnosticsError(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class DiagnosticsFileNotFound(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class DiagnosticsPermissionDenied(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class DiagnosticsRejected(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DiagnosticsResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "file_not_found", "permission_denied")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    FILE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    success: DiagnosticsSuccess
    error: DiagnosticsError
    rejected: DiagnosticsRejected
    file_not_found: DiagnosticsFileNotFound
    permission_denied: DiagnosticsPermissionDenied
    def __init__(self, success: _Optional[_Union[DiagnosticsSuccess, _Mapping]] = ..., error: _Optional[_Union[DiagnosticsError, _Mapping]] = ..., rejected: _Optional[_Union[DiagnosticsRejected, _Mapping]] = ..., file_not_found: _Optional[_Union[DiagnosticsFileNotFound, _Mapping]] = ..., permission_denied: _Optional[_Union[DiagnosticsPermissionDenied, _Mapping]] = ...) -> None: ...

class DiagnosticsSuccess(_message.Message):
    __slots__ = ("path", "diagnostics", "total_diagnostics")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    path: str
    diagnostics: _containers.RepeatedCompositeFieldContainer[Diagnostic]
    total_diagnostics: int
    def __init__(self, path: _Optional[str] = ..., diagnostics: _Optional[_Iterable[_Union[Diagnostic, _Mapping]]] = ..., total_diagnostics: _Optional[int] = ...) -> None: ...

class DirectoryEntry(_message.Message):
    __slots__ = ("name", "path", "type", "size_bytes", "modified_at_unix_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    type: EntryType
    size_bytes: int
    modified_at_unix_ms: int
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., type: _Optional[_Union[EntryType, str]] = ..., size_bytes: _Optional[int] = ..., modified_at_unix_ms: _Optional[int] = ...) -> None: ...

class DownloadCursorServerRequest(_message.Message):
    __slots__ = ("commit",)
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    commit: str
    def __init__(self, commit: _Optional[str] = ...) -> None: ...

class DownloadCursorServerResponse(_message.Message):
    __slots__ = ("already_downloaded",)
    ALREADY_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    already_downloaded: bool
    def __init__(self, already_downloaded: _Optional[bool] = ...) -> None: ...

class DragAction(_message.Message):
    __slots__ = ("path", "button", "modifier_keys")
    PATH_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_KEYS_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedCompositeFieldContainer[Coordinate]
    button: MouseButton
    modifier_keys: str
    def __init__(self, path: _Optional[_Iterable[_Union[Coordinate, _Mapping]]] = ..., button: _Optional[_Union[MouseButton, str]] = ..., modifier_keys: _Optional[str] = ...) -> None: ...

class EditArgs(_message.Message):
    __slots__ = ("path", "stream_content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    STREAM_CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    stream_content: str
    def __init__(self, path: _Optional[str] = ..., stream_content: _Optional[str] = ...) -> None: ...

class EditError(_message.Message):
    __slots__ = ("path", "error", "model_visible_error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MODEL_VISIBLE_ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    model_visible_error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ..., model_visible_error: _Optional[str] = ...) -> None: ...

class EditFileNotFound(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class EditPrLabelsArgs(_message.Message):
    __slots__ = ("tool_call_id", "pr_url", "add_labels", "remove_labels")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    ADD_LABELS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LABELS_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    pr_url: str
    add_labels: _containers.RepeatedScalarFieldContainer[str]
    remove_labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tool_call_id: _Optional[str] = ..., pr_url: _Optional[str] = ..., add_labels: _Optional[_Iterable[str]] = ..., remove_labels: _Optional[_Iterable[str]] = ...) -> None: ...

class EditPrLabelsError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class EditPrLabelsResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: EditPrLabelsSuccess
    error: EditPrLabelsError
    def __init__(self, success: _Optional[_Union[EditPrLabelsSuccess, _Mapping]] = ..., error: _Optional[_Union[EditPrLabelsError, _Mapping]] = ...) -> None: ...

class EditPrLabelsSuccess(_message.Message):
    __slots__ = ("pr_url", "pr_number", "message")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    pr_number: int
    message: str
    def __init__(self, pr_url: _Optional[str] = ..., pr_number: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class EditPrLabelsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: EditPrLabelsArgs
    result: EditPrLabelsResult
    def __init__(self, args: _Optional[_Union[EditPrLabelsArgs, _Mapping]] = ..., result: _Optional[_Union[EditPrLabelsResult, _Mapping]] = ...) -> None: ...

class EditReadPermissionDenied(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class EditRejected(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class EditResult(_message.Message):
    __slots__ = ("success", "file_not_found", "read_permission_denied", "write_permission_denied", "rejected", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FILE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    READ_PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    WRITE_PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: EditSuccess
    file_not_found: EditFileNotFound
    read_permission_denied: EditReadPermissionDenied
    write_permission_denied: EditWritePermissionDenied
    rejected: EditRejected
    error: EditError
    def __init__(self, success: _Optional[_Union[EditSuccess, _Mapping]] = ..., file_not_found: _Optional[_Union[EditFileNotFound, _Mapping]] = ..., read_permission_denied: _Optional[_Union[EditReadPermissionDenied, _Mapping]] = ..., write_permission_denied: _Optional[_Union[EditWritePermissionDenied, _Mapping]] = ..., rejected: _Optional[_Union[EditRejected, _Mapping]] = ..., error: _Optional[_Union[EditError, _Mapping]] = ...) -> None: ...

class EditSuccess(_message.Message):
    __slots__ = ("path", "lines_added", "lines_removed", "diff_string", "before_full_file_content", "after_full_file_content", "message")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LINES_ADDED_FIELD_NUMBER: _ClassVar[int]
    LINES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    DIFF_STRING_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FULL_FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    AFTER_FULL_FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    lines_added: int
    lines_removed: int
    diff_string: str
    before_full_file_content: str
    after_full_file_content: str
    message: str
    def __init__(self, path: _Optional[str] = ..., lines_added: _Optional[int] = ..., lines_removed: _Optional[int] = ..., diff_string: _Optional[str] = ..., before_full_file_content: _Optional[str] = ..., after_full_file_content: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class EditToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: EditArgs
    result: EditResult
    def __init__(self, args: _Optional[_Union[EditArgs, _Mapping]] = ..., result: _Optional[_Union[EditResult, _Mapping]] = ...) -> None: ...

class EditToolCallDelta(_message.Message):
    __slots__ = ("stream_content_delta",)
    STREAM_CONTENT_DELTA_FIELD_NUMBER: _ClassVar[int]
    stream_content_delta: str
    def __init__(self, stream_content_delta: _Optional[str] = ...) -> None: ...

class EditWritePermissionDenied(_message.Message):
    __slots__ = ("path", "error", "is_readonly")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    is_readonly: bool
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Error(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ExecClientControlMessage(_message.Message):
    __slots__ = ("stream_close", "throw", "heartbeat")
    STREAM_CLOSE_FIELD_NUMBER: _ClassVar[int]
    THROW_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    stream_close: ExecClientStreamClose
    throw: ExecClientThrow
    heartbeat: ExecClientHeartbeat
    def __init__(self, stream_close: _Optional[_Union[ExecClientStreamClose, _Mapping]] = ..., throw: _Optional[_Union[ExecClientThrow, _Mapping]] = ..., heartbeat: _Optional[_Union[ExecClientHeartbeat, _Mapping]] = ...) -> None: ...

class ExecClientHeartbeat(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ExecClientMessage(_message.Message):
    __slots__ = ("id", "exec_id", "local_execution_time_ms", "hook_additional_contexts", "shell_result", "write_result", "delete_result", "grep_result", "read_result", "redacted_read_result", "ls_result", "diagnostics_result", "request_context_result", "mcp_result", "shell_stream", "background_shell_spawn_result", "list_mcp_resources_exec_result", "read_mcp_resource_exec_result", "mcp_state_exec_result", "fetch_result", "record_screen_result", "computer_use_result", "write_shell_stdin_result", "execute_hook_result", "subagent_result", "force_background_shell_result", "force_background_subagent_result", "subagent_await_result", "smart_mode_classifier_result", "canvas_diagnostics_result", "shell_allowlist_precheck_result", "mcp_allowlist_precheck_result", "web_fetch_allowlist_precheck_result", "git_diff_response", "pi_read_result", "pi_bash_result", "pi_edit_result", "pi_write_result", "pi_grep_result", "pi_find_result", "pi_ls_result", "conversation_search_result", "agent_store_conflict_result", "mini_swe_agent_bash_result")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    HOOK_ADDITIONAL_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    SHELL_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELETE_RESULT_FIELD_NUMBER: _ClassVar[int]
    GREP_RESULT_FIELD_NUMBER: _ClassVar[int]
    READ_RESULT_FIELD_NUMBER: _ClassVar[int]
    REDACTED_READ_RESULT_FIELD_NUMBER: _ClassVar[int]
    LS_RESULT_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_RESULT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_RESULT_FIELD_NUMBER: _ClassVar[int]
    MCP_RESULT_FIELD_NUMBER: _ClassVar[int]
    SHELL_STREAM_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SHELL_SPAWN_RESULT_FIELD_NUMBER: _ClassVar[int]
    LIST_MCP_RESOURCES_EXEC_RESULT_FIELD_NUMBER: _ClassVar[int]
    READ_MCP_RESOURCE_EXEC_RESULT_FIELD_NUMBER: _ClassVar[int]
    MCP_STATE_EXEC_RESULT_FIELD_NUMBER: _ClassVar[int]
    FETCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    RECORD_SCREEN_RESULT_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_RESULT_FIELD_NUMBER: _ClassVar[int]
    WRITE_SHELL_STDIN_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_HOOK_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    FORCE_BACKGROUND_SHELL_RESULT_FIELD_NUMBER: _ClassVar[int]
    FORCE_BACKGROUND_SUBAGENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_AWAIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_CLASSIFIER_RESULT_FIELD_NUMBER: _ClassVar[int]
    CANVAS_DIAGNOSTICS_RESULT_FIELD_NUMBER: _ClassVar[int]
    SHELL_ALLOWLIST_PRECHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    MCP_ALLOWLIST_PRECHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    WEB_FETCH_ALLOWLIST_PRECHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    GIT_DIFF_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PI_READ_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_BASH_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_EDIT_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_WRITE_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_GREP_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_FIND_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_LS_RESULT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SEARCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    AGENT_STORE_CONFLICT_RESULT_FIELD_NUMBER: _ClassVar[int]
    MINI_SWE_AGENT_BASH_RESULT_FIELD_NUMBER: _ClassVar[int]
    id: int
    exec_id: str
    local_execution_time_ms: int
    hook_additional_contexts: _containers.RepeatedCompositeFieldContainer[HookAdditionalContext]
    shell_result: ShellResult
    write_result: WriteResult
    delete_result: DeleteResult
    grep_result: GrepResult
    read_result: ReadResult
    redacted_read_result: ReadResult
    ls_result: LsResult
    diagnostics_result: DiagnosticsResult
    request_context_result: RequestContextResult
    mcp_result: McpResult
    shell_stream: ShellStream
    background_shell_spawn_result: BackgroundShellSpawnResult
    list_mcp_resources_exec_result: ListMcpResourcesExecResult
    read_mcp_resource_exec_result: ReadMcpResourceExecResult
    mcp_state_exec_result: McpStateExecResult
    fetch_result: FetchResult
    record_screen_result: RecordScreenResult
    computer_use_result: ComputerUseResult
    write_shell_stdin_result: WriteShellStdinResult
    execute_hook_result: ExecuteHookResult
    subagent_result: SubagentResult
    force_background_shell_result: ForceBackgroundShellResult
    force_background_subagent_result: ForceBackgroundSubagentResult
    subagent_await_result: SubagentAwaitResult
    smart_mode_classifier_result: SmartModeClassifierResult
    canvas_diagnostics_result: CanvasDiagnosticsResult
    shell_allowlist_precheck_result: ShellAllowlistPrecheckResult
    mcp_allowlist_precheck_result: McpAllowlistPrecheckResult
    web_fetch_allowlist_precheck_result: WebFetchAllowlistPrecheckResult
    git_diff_response: GetDiffResponse
    pi_read_result: PiReadExecResult
    pi_bash_result: PiBashExecResult
    pi_edit_result: PiEditExecResult
    pi_write_result: PiWriteExecResult
    pi_grep_result: PiGrepExecResult
    pi_find_result: PiFindExecResult
    pi_ls_result: PiLsExecResult
    conversation_search_result: ConversationSearchResult
    agent_store_conflict_result: AgentStoreConflictResult
    mini_swe_agent_bash_result: ShellResult
    def __init__(self, id: _Optional[int] = ..., exec_id: _Optional[str] = ..., local_execution_time_ms: _Optional[int] = ..., hook_additional_contexts: _Optional[_Iterable[_Union[HookAdditionalContext, _Mapping]]] = ..., shell_result: _Optional[_Union[ShellResult, _Mapping]] = ..., write_result: _Optional[_Union[WriteResult, _Mapping]] = ..., delete_result: _Optional[_Union[DeleteResult, _Mapping]] = ..., grep_result: _Optional[_Union[GrepResult, _Mapping]] = ..., read_result: _Optional[_Union[ReadResult, _Mapping]] = ..., redacted_read_result: _Optional[_Union[ReadResult, _Mapping]] = ..., ls_result: _Optional[_Union[LsResult, _Mapping]] = ..., diagnostics_result: _Optional[_Union[DiagnosticsResult, _Mapping]] = ..., request_context_result: _Optional[_Union[RequestContextResult, _Mapping]] = ..., mcp_result: _Optional[_Union[McpResult, _Mapping]] = ..., shell_stream: _Optional[_Union[ShellStream, _Mapping]] = ..., background_shell_spawn_result: _Optional[_Union[BackgroundShellSpawnResult, _Mapping]] = ..., list_mcp_resources_exec_result: _Optional[_Union[ListMcpResourcesExecResult, _Mapping]] = ..., read_mcp_resource_exec_result: _Optional[_Union[ReadMcpResourceExecResult, _Mapping]] = ..., mcp_state_exec_result: _Optional[_Union[McpStateExecResult, _Mapping]] = ..., fetch_result: _Optional[_Union[FetchResult, _Mapping]] = ..., record_screen_result: _Optional[_Union[RecordScreenResult, _Mapping]] = ..., computer_use_result: _Optional[_Union[ComputerUseResult, _Mapping]] = ..., write_shell_stdin_result: _Optional[_Union[WriteShellStdinResult, _Mapping]] = ..., execute_hook_result: _Optional[_Union[ExecuteHookResult, _Mapping]] = ..., subagent_result: _Optional[_Union[SubagentResult, _Mapping]] = ..., force_background_shell_result: _Optional[_Union[ForceBackgroundShellResult, _Mapping]] = ..., force_background_subagent_result: _Optional[_Union[ForceBackgroundSubagentResult, _Mapping]] = ..., subagent_await_result: _Optional[_Union[SubagentAwaitResult, _Mapping]] = ..., smart_mode_classifier_result: _Optional[_Union[SmartModeClassifierResult, _Mapping]] = ..., canvas_diagnostics_result: _Optional[_Union[CanvasDiagnosticsResult, _Mapping]] = ..., shell_allowlist_precheck_result: _Optional[_Union[ShellAllowlistPrecheckResult, _Mapping]] = ..., mcp_allowlist_precheck_result: _Optional[_Union[McpAllowlistPrecheckResult, _Mapping]] = ..., web_fetch_allowlist_precheck_result: _Optional[_Union[WebFetchAllowlistPrecheckResult, _Mapping]] = ..., git_diff_response: _Optional[_Union[GetDiffResponse, _Mapping]] = ..., pi_read_result: _Optional[_Union[PiReadExecResult, _Mapping]] = ..., pi_bash_result: _Optional[_Union[PiBashExecResult, _Mapping]] = ..., pi_edit_result: _Optional[_Union[PiEditExecResult, _Mapping]] = ..., pi_write_result: _Optional[_Union[PiWriteExecResult, _Mapping]] = ..., pi_grep_result: _Optional[_Union[PiGrepExecResult, _Mapping]] = ..., pi_find_result: _Optional[_Union[PiFindExecResult, _Mapping]] = ..., pi_ls_result: _Optional[_Union[PiLsExecResult, _Mapping]] = ..., conversation_search_result: _Optional[_Union[ConversationSearchResult, _Mapping]] = ..., agent_store_conflict_result: _Optional[_Union[AgentStoreConflictResult, _Mapping]] = ..., mini_swe_agent_bash_result: _Optional[_Union[ShellResult, _Mapping]] = ...) -> None: ...

class ExecClientStreamClose(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ExecClientThrow(_message.Message):
    __slots__ = ("id", "error", "stack_trace", "error_code")
    ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    id: int
    error: str
    stack_trace: str
    error_code: str
    def __init__(self, id: _Optional[int] = ..., error: _Optional[str] = ..., stack_trace: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...

class ExecRequest(_message.Message):
    __slots__ = ("command", "cwd", "args", "environment")
    class EnvironmentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    command: str
    cwd: str
    args: _containers.RepeatedScalarFieldContainer[str]
    environment: _containers.ScalarMap[str, str]
    def __init__(self, command: _Optional[str] = ..., cwd: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ..., environment: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ExecResponse(_message.Message):
    __slots__ = ("stdout_event", "stderr_event", "exit_event")
    STDOUT_EVENT_FIELD_NUMBER: _ClassVar[int]
    STDERR_EVENT_FIELD_NUMBER: _ClassVar[int]
    EXIT_EVENT_FIELD_NUMBER: _ClassVar[int]
    stdout_event: StdoutEvent
    stderr_event: StderrEvent
    exit_event: ExitEvent
    def __init__(self, stdout_event: _Optional[_Union[StdoutEvent, _Mapping]] = ..., stderr_event: _Optional[_Union[StderrEvent, _Mapping]] = ..., exit_event: _Optional[_Union[ExitEvent, _Mapping]] = ...) -> None: ...

class ExecServerAbort(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ExecServerControlMessage(_message.Message):
    __slots__ = ("abort",)
    ABORT_FIELD_NUMBER: _ClassVar[int]
    abort: ExecServerAbort
    def __init__(self, abort: _Optional[_Union[ExecServerAbort, _Mapping]] = ...) -> None: ...

class ExecServerMessage(_message.Message):
    __slots__ = ("id", "exec_id", "span_context", "accept_hook_additional_contexts", "shell_args", "write_args", "delete_args", "grep_args", "read_args", "redacted_read_args", "ls_args", "diagnostics_args", "request_context_args", "mcp_args", "shell_stream_args", "background_shell_spawn_args", "list_mcp_resources_exec_args", "read_mcp_resource_exec_args", "mcp_state_exec_args", "fetch_args", "record_screen_args", "computer_use_args", "write_shell_stdin_args", "execute_hook_args", "subagent_args", "force_background_shell_args", "force_background_subagent_args", "subagent_await_args", "smart_mode_classifier_args", "canvas_diagnostics_args", "shell_allowlist_precheck_args", "mcp_allowlist_precheck_args", "web_fetch_allowlist_precheck_args", "git_diff_request", "pi_read_args", "pi_bash_args", "pi_edit_args", "pi_write_args", "pi_grep_args", "pi_find_args", "pi_ls_args", "mini_swe_agent_bash_args", "conversation_search_args", "agent_store_conflict_args")
    ID_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_HOOK_ADDITIONAL_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    SHELL_ARGS_FIELD_NUMBER: _ClassVar[int]
    WRITE_ARGS_FIELD_NUMBER: _ClassVar[int]
    DELETE_ARGS_FIELD_NUMBER: _ClassVar[int]
    GREP_ARGS_FIELD_NUMBER: _ClassVar[int]
    READ_ARGS_FIELD_NUMBER: _ClassVar[int]
    REDACTED_READ_ARGS_FIELD_NUMBER: _ClassVar[int]
    LS_ARGS_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_ARGS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_ARGS_FIELD_NUMBER: _ClassVar[int]
    MCP_ARGS_FIELD_NUMBER: _ClassVar[int]
    SHELL_STREAM_ARGS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SHELL_SPAWN_ARGS_FIELD_NUMBER: _ClassVar[int]
    LIST_MCP_RESOURCES_EXEC_ARGS_FIELD_NUMBER: _ClassVar[int]
    READ_MCP_RESOURCE_EXEC_ARGS_FIELD_NUMBER: _ClassVar[int]
    MCP_STATE_EXEC_ARGS_FIELD_NUMBER: _ClassVar[int]
    FETCH_ARGS_FIELD_NUMBER: _ClassVar[int]
    RECORD_SCREEN_ARGS_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_ARGS_FIELD_NUMBER: _ClassVar[int]
    WRITE_SHELL_STDIN_ARGS_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_HOOK_ARGS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_ARGS_FIELD_NUMBER: _ClassVar[int]
    FORCE_BACKGROUND_SHELL_ARGS_FIELD_NUMBER: _ClassVar[int]
    FORCE_BACKGROUND_SUBAGENT_ARGS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_AWAIT_ARGS_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_CLASSIFIER_ARGS_FIELD_NUMBER: _ClassVar[int]
    CANVAS_DIAGNOSTICS_ARGS_FIELD_NUMBER: _ClassVar[int]
    SHELL_ALLOWLIST_PRECHECK_ARGS_FIELD_NUMBER: _ClassVar[int]
    MCP_ALLOWLIST_PRECHECK_ARGS_FIELD_NUMBER: _ClassVar[int]
    WEB_FETCH_ALLOWLIST_PRECHECK_ARGS_FIELD_NUMBER: _ClassVar[int]
    GIT_DIFF_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PI_READ_ARGS_FIELD_NUMBER: _ClassVar[int]
    PI_BASH_ARGS_FIELD_NUMBER: _ClassVar[int]
    PI_EDIT_ARGS_FIELD_NUMBER: _ClassVar[int]
    PI_WRITE_ARGS_FIELD_NUMBER: _ClassVar[int]
    PI_GREP_ARGS_FIELD_NUMBER: _ClassVar[int]
    PI_FIND_ARGS_FIELD_NUMBER: _ClassVar[int]
    PI_LS_ARGS_FIELD_NUMBER: _ClassVar[int]
    MINI_SWE_AGENT_BASH_ARGS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_SEARCH_ARGS_FIELD_NUMBER: _ClassVar[int]
    AGENT_STORE_CONFLICT_ARGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    exec_id: str
    span_context: SpanContext
    accept_hook_additional_contexts: bool
    shell_args: ShellArgs
    write_args: WriteArgs
    delete_args: DeleteArgs
    grep_args: GrepArgs
    read_args: ReadArgs
    redacted_read_args: ReadArgs
    ls_args: LsArgs
    diagnostics_args: DiagnosticsArgs
    request_context_args: RequestContextArgs
    mcp_args: McpArgs
    shell_stream_args: ShellArgs
    background_shell_spawn_args: BackgroundShellSpawnArgs
    list_mcp_resources_exec_args: ListMcpResourcesExecArgs
    read_mcp_resource_exec_args: ReadMcpResourceExecArgs
    mcp_state_exec_args: McpStateExecArgs
    fetch_args: FetchArgs
    record_screen_args: RecordScreenArgs
    computer_use_args: ComputerUseArgs
    write_shell_stdin_args: WriteShellStdinArgs
    execute_hook_args: ExecuteHookArgs
    subagent_args: SubagentArgs
    force_background_shell_args: ForceBackgroundShellArgs
    force_background_subagent_args: ForceBackgroundSubagentArgs
    subagent_await_args: SubagentAwaitArgs
    smart_mode_classifier_args: SmartModeClassifierArgs
    canvas_diagnostics_args: CanvasDiagnosticsArgs
    shell_allowlist_precheck_args: ShellAllowlistPrecheckArgs
    mcp_allowlist_precheck_args: McpAllowlistPrecheckArgs
    web_fetch_allowlist_precheck_args: WebFetchAllowlistPrecheckArgs
    git_diff_request: GetDiffRequest
    pi_read_args: PiReadExecArgs
    pi_bash_args: PiBashExecArgs
    pi_edit_args: PiEditExecArgs
    pi_write_args: PiWriteExecArgs
    pi_grep_args: PiGrepExecArgs
    pi_find_args: PiFindExecArgs
    pi_ls_args: PiLsExecArgs
    mini_swe_agent_bash_args: ShellArgs
    conversation_search_args: ConversationSearchArgs
    agent_store_conflict_args: AgentStoreConflictArgs
    def __init__(self, id: _Optional[int] = ..., exec_id: _Optional[str] = ..., span_context: _Optional[_Union[SpanContext, _Mapping]] = ..., accept_hook_additional_contexts: _Optional[bool] = ..., shell_args: _Optional[_Union[ShellArgs, _Mapping]] = ..., write_args: _Optional[_Union[WriteArgs, _Mapping]] = ..., delete_args: _Optional[_Union[DeleteArgs, _Mapping]] = ..., grep_args: _Optional[_Union[GrepArgs, _Mapping]] = ..., read_args: _Optional[_Union[ReadArgs, _Mapping]] = ..., redacted_read_args: _Optional[_Union[ReadArgs, _Mapping]] = ..., ls_args: _Optional[_Union[LsArgs, _Mapping]] = ..., diagnostics_args: _Optional[_Union[DiagnosticsArgs, _Mapping]] = ..., request_context_args: _Optional[_Union[RequestContextArgs, _Mapping]] = ..., mcp_args: _Optional[_Union[McpArgs, _Mapping]] = ..., shell_stream_args: _Optional[_Union[ShellArgs, _Mapping]] = ..., background_shell_spawn_args: _Optional[_Union[BackgroundShellSpawnArgs, _Mapping]] = ..., list_mcp_resources_exec_args: _Optional[_Union[ListMcpResourcesExecArgs, _Mapping]] = ..., read_mcp_resource_exec_args: _Optional[_Union[ReadMcpResourceExecArgs, _Mapping]] = ..., mcp_state_exec_args: _Optional[_Union[McpStateExecArgs, _Mapping]] = ..., fetch_args: _Optional[_Union[FetchArgs, _Mapping]] = ..., record_screen_args: _Optional[_Union[RecordScreenArgs, _Mapping]] = ..., computer_use_args: _Optional[_Union[ComputerUseArgs, _Mapping]] = ..., write_shell_stdin_args: _Optional[_Union[WriteShellStdinArgs, _Mapping]] = ..., execute_hook_args: _Optional[_Union[ExecuteHookArgs, _Mapping]] = ..., subagent_args: _Optional[_Union[SubagentArgs, _Mapping]] = ..., force_background_shell_args: _Optional[_Union[ForceBackgroundShellArgs, _Mapping]] = ..., force_background_subagent_args: _Optional[_Union[ForceBackgroundSubagentArgs, _Mapping]] = ..., subagent_await_args: _Optional[_Union[SubagentAwaitArgs, _Mapping]] = ..., smart_mode_classifier_args: _Optional[_Union[SmartModeClassifierArgs, _Mapping]] = ..., canvas_diagnostics_args: _Optional[_Union[CanvasDiagnosticsArgs, _Mapping]] = ..., shell_allowlist_precheck_args: _Optional[_Union[ShellAllowlistPrecheckArgs, _Mapping]] = ..., mcp_allowlist_precheck_args: _Optional[_Union[McpAllowlistPrecheckArgs, _Mapping]] = ..., web_fetch_allowlist_precheck_args: _Optional[_Union[WebFetchAllowlistPrecheckArgs, _Mapping]] = ..., git_diff_request: _Optional[_Union[GetDiffRequest, _Mapping]] = ..., pi_read_args: _Optional[_Union[PiReadExecArgs, _Mapping]] = ..., pi_bash_args: _Optional[_Union[PiBashExecArgs, _Mapping]] = ..., pi_edit_args: _Optional[_Union[PiEditExecArgs, _Mapping]] = ..., pi_write_args: _Optional[_Union[PiWriteExecArgs, _Mapping]] = ..., pi_grep_args: _Optional[_Union[PiGrepExecArgs, _Mapping]] = ..., pi_find_args: _Optional[_Union[PiFindExecArgs, _Mapping]] = ..., pi_ls_args: _Optional[_Union[PiLsExecArgs, _Mapping]] = ..., mini_swe_agent_bash_args: _Optional[_Union[ShellArgs, _Mapping]] = ..., conversation_search_args: _Optional[_Union[ConversationSearchArgs, _Mapping]] = ..., agent_store_conflict_args: _Optional[_Union[AgentStoreConflictArgs, _Mapping]] = ...) -> None: ...

class ExecStreamElement(_message.Message):
    __slots__ = ("exec_client_message", "exec_client_control_message")
    EXEC_CLIENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXEC_CLIENT_CONTROL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    exec_client_message: ExecClientMessage
    exec_client_control_message: ExecClientControlMessage
    def __init__(self, exec_client_message: _Optional[_Union[ExecClientMessage, _Mapping]] = ..., exec_client_control_message: _Optional[_Union[ExecClientControlMessage, _Mapping]] = ...) -> None: ...

class ExecuteHookArgs(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: ExecuteHookRequest
    def __init__(self, request: _Optional[_Union[ExecuteHookRequest, _Mapping]] = ...) -> None: ...

class ExecuteHookRequest(_message.Message):
    __slots__ = ("pre_compact", "subagent_start", "subagent_stop", "pre_tool_use", "post_tool_use", "post_tool_use_failure", "before_submit_prompt", "after_agent_response", "after_agent_thought", "stop")
    PRE_COMPACT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_START_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_STOP_FIELD_NUMBER: _ClassVar[int]
    PRE_TOOL_USE_FIELD_NUMBER: _ClassVar[int]
    POST_TOOL_USE_FIELD_NUMBER: _ClassVar[int]
    POST_TOOL_USE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_SUBMIT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    AFTER_AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    AFTER_AGENT_THOUGHT_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    pre_compact: PreCompactRequestQuery
    subagent_start: SubagentStartRequestQuery
    subagent_stop: SubagentStopRequestQuery
    pre_tool_use: PreToolUseRequestQuery
    post_tool_use: PostToolUseRequestQuery
    post_tool_use_failure: PostToolUseFailureRequestQuery
    before_submit_prompt: BeforeSubmitPromptRequestQuery
    after_agent_response: AfterAgentResponseRequestQuery
    after_agent_thought: AfterAgentThoughtRequestQuery
    stop: StopRequestQuery
    def __init__(self, pre_compact: _Optional[_Union[PreCompactRequestQuery, _Mapping]] = ..., subagent_start: _Optional[_Union[SubagentStartRequestQuery, _Mapping]] = ..., subagent_stop: _Optional[_Union[SubagentStopRequestQuery, _Mapping]] = ..., pre_tool_use: _Optional[_Union[PreToolUseRequestQuery, _Mapping]] = ..., post_tool_use: _Optional[_Union[PostToolUseRequestQuery, _Mapping]] = ..., post_tool_use_failure: _Optional[_Union[PostToolUseFailureRequestQuery, _Mapping]] = ..., before_submit_prompt: _Optional[_Union[BeforeSubmitPromptRequestQuery, _Mapping]] = ..., after_agent_response: _Optional[_Union[AfterAgentResponseRequestQuery, _Mapping]] = ..., after_agent_thought: _Optional[_Union[AfterAgentThoughtRequestQuery, _Mapping]] = ..., stop: _Optional[_Union[StopRequestQuery, _Mapping]] = ...) -> None: ...

class ExecuteHookResponse(_message.Message):
    __slots__ = ("pre_compact", "subagent_start", "subagent_stop", "pre_tool_use", "post_tool_use", "post_tool_use_failure", "before_submit_prompt", "after_agent_response", "after_agent_thought", "stop")
    PRE_COMPACT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_START_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_STOP_FIELD_NUMBER: _ClassVar[int]
    PRE_TOOL_USE_FIELD_NUMBER: _ClassVar[int]
    POST_TOOL_USE_FIELD_NUMBER: _ClassVar[int]
    POST_TOOL_USE_FAILURE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_SUBMIT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    AFTER_AGENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    AFTER_AGENT_THOUGHT_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    pre_compact: PreCompactRequestResponse
    subagent_start: SubagentStartRequestResponse
    subagent_stop: SubagentStopRequestResponse
    pre_tool_use: PreToolUseRequestResponse
    post_tool_use: PostToolUseRequestResponse
    post_tool_use_failure: PostToolUseFailureRequestResponse
    before_submit_prompt: BeforeSubmitPromptRequestResponse
    after_agent_response: AfterAgentResponseRequestResponse
    after_agent_thought: AfterAgentThoughtRequestResponse
    stop: StopRequestResponse
    def __init__(self, pre_compact: _Optional[_Union[PreCompactRequestResponse, _Mapping]] = ..., subagent_start: _Optional[_Union[SubagentStartRequestResponse, _Mapping]] = ..., subagent_stop: _Optional[_Union[SubagentStopRequestResponse, _Mapping]] = ..., pre_tool_use: _Optional[_Union[PreToolUseRequestResponse, _Mapping]] = ..., post_tool_use: _Optional[_Union[PostToolUseRequestResponse, _Mapping]] = ..., post_tool_use_failure: _Optional[_Union[PostToolUseFailureRequestResponse, _Mapping]] = ..., before_submit_prompt: _Optional[_Union[BeforeSubmitPromptRequestResponse, _Mapping]] = ..., after_agent_response: _Optional[_Union[AfterAgentResponseRequestResponse, _Mapping]] = ..., after_agent_thought: _Optional[_Union[AfterAgentThoughtRequestResponse, _Mapping]] = ..., stop: _Optional[_Union[StopRequestResponse, _Mapping]] = ...) -> None: ...

class ExecuteHookResult(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: ExecuteHookResponse
    def __init__(self, response: _Optional[_Union[ExecuteHookResponse, _Mapping]] = ...) -> None: ...

class ExecutePlanAction(_message.Message):
    __slots__ = ("request_context", "plan", "plan_file_uri", "plan_file_content", "execution_mode", "kickoff_message_id", "plan_id", "plan_file_path")
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    PLAN_FILE_URI_FIELD_NUMBER: _ClassVar[int]
    PLAN_FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_MODE_FIELD_NUMBER: _ClassVar[int]
    KICKOFF_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    request_context: RequestContext
    plan: ConversationPlan
    plan_file_uri: str
    plan_file_content: str
    execution_mode: AgentMode
    kickoff_message_id: str
    plan_id: str
    plan_file_path: str
    def __init__(self, request_context: _Optional[_Union[RequestContext, _Mapping]] = ..., plan: _Optional[_Union[ConversationPlan, _Mapping]] = ..., plan_file_uri: _Optional[str] = ..., plan_file_content: _Optional[str] = ..., execution_mode: _Optional[_Union[AgentMode, str]] = ..., kickoff_message_id: _Optional[str] = ..., plan_id: _Optional[str] = ..., plan_file_path: _Optional[str] = ...) -> None: ...

class ExecutePlanInfo(_message.Message):
    __slots__ = ("plan_id", "plan_title")
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_TITLE_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    plan_title: str
    def __init__(self, plan_id: _Optional[str] = ..., plan_title: _Optional[str] = ...) -> None: ...

class ExitEvent(_message.Message):
    __slots__ = ("exit_code",)
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_code: int
    def __init__(self, exit_code: _Optional[int] = ...) -> None: ...

class ExportFileMetadata(_message.Message):
    __slots__ = ("total_bytes",)
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_bytes: int
    def __init__(self, total_bytes: _Optional[int] = ...) -> None: ...

class ExportFileRequest(_message.Message):
    __slots__ = ("path", "workspace_root_path")
    PATH_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    workspace_root_path: str
    def __init__(self, path: _Optional[str] = ..., workspace_root_path: _Optional[str] = ...) -> None: ...

class ExportFileResponse(_message.Message):
    __slots__ = ("content_chunk", "metadata")
    CONTENT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    content_chunk: bytes
    metadata: ExportFileMetadata
    def __init__(self, content_chunk: _Optional[bytes] = ..., metadata: _Optional[_Union[ExportFileMetadata, _Mapping]] = ...) -> None: ...

class ExtraContextEntry(_message.Message):
    __slots__ = ("data", "blob_id")
    DATA_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    data: str
    blob_id: bytes
    def __init__(self, data: _Optional[str] = ..., blob_id: _Optional[bytes] = ...) -> None: ...

class FeedbackRequestCategory(_message.Message):
    __slots__ = ("id", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class FeedbackRequestCategoryGroup(_message.Message):
    __slots__ = ("id", "prompt", "categories")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    prompt: str
    categories: _containers.RepeatedCompositeFieldContainer[FeedbackRequestCategory]
    def __init__(self, id: _Optional[str] = ..., prompt: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[FeedbackRequestCategory, _Mapping]]] = ...) -> None: ...

class FeedbackRequestUpdate(_message.Message):
    __slots__ = ("request_id", "canonical_model_name", "categories", "category_groups", "show_form_immediately", "title", "negative_title", "comment_placeholder")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SHOW_FORM_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_TITLE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    canonical_model_name: str
    categories: _containers.RepeatedCompositeFieldContainer[FeedbackRequestCategory]
    category_groups: _containers.RepeatedCompositeFieldContainer[FeedbackRequestCategoryGroup]
    show_form_immediately: bool
    title: str
    negative_title: str
    comment_placeholder: str
    def __init__(self, request_id: _Optional[str] = ..., canonical_model_name: _Optional[str] = ..., categories: _Optional[_Iterable[_Union[FeedbackRequestCategory, _Mapping]]] = ..., category_groups: _Optional[_Iterable[_Union[FeedbackRequestCategoryGroup, _Mapping]]] = ..., show_form_immediately: _Optional[bool] = ..., title: _Optional[str] = ..., negative_title: _Optional[str] = ..., comment_placeholder: _Optional[str] = ...) -> None: ...

class FetchArgs(_message.Message):
    __slots__ = ("url", "tool_call_id")
    URL_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    tool_call_id: str
    def __init__(self, url: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class FetchCloudAgentDataArgs(_message.Message):
    __slots__ = ("bc_ids", "sources", "statuses", "include_team_wide", "include_archived", "limit", "include_transcript", "active_since")
    BC_IDS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TEAM_WIDE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SINCE_FIELD_NUMBER: _ClassVar[int]
    bc_ids: _containers.RepeatedScalarFieldContainer[str]
    sources: _containers.RepeatedScalarFieldContainer[str]
    statuses: _containers.RepeatedScalarFieldContainer[str]
    include_team_wide: bool
    include_archived: bool
    limit: int
    include_transcript: bool
    active_since: str
    def __init__(self, bc_ids: _Optional[_Iterable[str]] = ..., sources: _Optional[_Iterable[str]] = ..., statuses: _Optional[_Iterable[str]] = ..., include_team_wide: _Optional[bool] = ..., include_archived: _Optional[bool] = ..., limit: _Optional[int] = ..., include_transcript: _Optional[bool] = ..., active_since: _Optional[str] = ...) -> None: ...

class FetchCloudAgentDataError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class FetchCloudAgentDataResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: FetchCloudAgentDataSuccess
    error: FetchCloudAgentDataError
    def __init__(self, success: _Optional[_Union[FetchCloudAgentDataSuccess, _Mapping]] = ..., error: _Optional[_Union[FetchCloudAgentDataError, _Mapping]] = ...) -> None: ...

class FetchCloudAgentDataSuccess(_message.Message):
    __slots__ = ("summary", "agent_count", "written_paths", "unavailable_bc_ids")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    WRITTEN_PATHS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE_BC_IDS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    agent_count: int
    written_paths: _containers.RepeatedScalarFieldContainer[str]
    unavailable_bc_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, summary: _Optional[str] = ..., agent_count: _Optional[int] = ..., written_paths: _Optional[_Iterable[str]] = ..., unavailable_bc_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchCloudAgentDataToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: FetchCloudAgentDataArgs
    result: FetchCloudAgentDataResult
    def __init__(self, args: _Optional[_Union[FetchCloudAgentDataArgs, _Mapping]] = ..., result: _Optional[_Union[FetchCloudAgentDataResult, _Mapping]] = ...) -> None: ...

class FetchError(_message.Message):
    __slots__ = ("url", "error")
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    url: str
    error: str
    def __init__(self, url: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class FetchResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: FetchSuccess
    error: FetchError
    def __init__(self, success: _Optional[_Union[FetchSuccess, _Mapping]] = ..., error: _Optional[_Union[FetchError, _Mapping]] = ...) -> None: ...

class FetchSuccess(_message.Message):
    __slots__ = ("url", "content", "status_code", "content_type")
    URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    url: str
    content: str
    status_code: int
    content_type: str
    def __init__(self, url: _Optional[str] = ..., content: _Optional[str] = ..., status_code: _Optional[int] = ..., content_type: _Optional[str] = ...) -> None: ...

class FetchToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: FetchArgs
    result: FetchResult
    def __init__(self, args: _Optional[_Union[FetchArgs, _Mapping]] = ..., result: _Optional[_Union[FetchResult, _Mapping]] = ...) -> None: ...

class FileDiagnostics(_message.Message):
    __slots__ = ("path", "diagnostics", "diagnostics_count")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_COUNT_FIELD_NUMBER: _ClassVar[int]
    path: str
    diagnostics: _containers.RepeatedCompositeFieldContainer[DiagnosticItem]
    diagnostics_count: int
    def __init__(self, path: _Optional[str] = ..., diagnostics: _Optional[_Iterable[_Union[DiagnosticItem, _Mapping]]] = ..., diagnostics_count: _Optional[int] = ...) -> None: ...

class FileDiff(_message.Message):
    __slots__ = ("added", "removed", "to", "chunks", "before_file_contents", "after_file_contents", "is_generated")
    class Chunk(_message.Message):
        __slots__ = ("content", "lines", "old_start", "old_lines", "new_start", "new_lines")
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        LINES_FIELD_NUMBER: _ClassVar[int]
        OLD_START_FIELD_NUMBER: _ClassVar[int]
        OLD_LINES_FIELD_NUMBER: _ClassVar[int]
        NEW_START_FIELD_NUMBER: _ClassVar[int]
        NEW_LINES_FIELD_NUMBER: _ClassVar[int]
        content: str
        lines: _containers.RepeatedScalarFieldContainer[str]
        old_start: int
        old_lines: int
        new_start: int
        new_lines: int
        def __init__(self, content: _Optional[str] = ..., lines: _Optional[_Iterable[str]] = ..., old_start: _Optional[int] = ..., old_lines: _Optional[int] = ..., new_start: _Optional[int] = ..., new_lines: _Optional[int] = ...) -> None: ...
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    AFTER_FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    IS_GENERATED_FIELD_NUMBER: _ClassVar[int]
    added: int
    removed: int
    to: str
    chunks: _containers.RepeatedCompositeFieldContainer[FileDiff.Chunk]
    before_file_contents: str
    after_file_contents: str
    is_generated: bool
    def __init__(self, added: _Optional[int] = ..., removed: _Optional[int] = ..., to: _Optional[str] = ..., chunks: _Optional[_Iterable[_Union[FileDiff.Chunk, _Mapping]]] = ..., before_file_contents: _Optional[str] = ..., after_file_contents: _Optional[str] = ..., is_generated: _Optional[bool] = ..., **kwargs) -> None: ...

class FileGit(_message.Message):
    __slots__ = ("commits",)
    COMMITS_FIELD_NUMBER: _ClassVar[int]
    commits: _containers.RepeatedCompositeFieldContainer[GitCommit]
    def __init__(self, commits: _Optional[_Iterable[_Union[GitCommit, _Mapping]]] = ...) -> None: ...

class FileState(_message.Message):
    __slots__ = ("content", "initial_content")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    initial_content: str
    def __init__(self, content: _Optional[str] = ..., initial_content: _Optional[str] = ...) -> None: ...

class FileStateStructure(_message.Message):
    __slots__ = ("content", "initial_content")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    initial_content: bytes
    def __init__(self, content: _Optional[bytes] = ..., initial_content: _Optional[bytes] = ...) -> None: ...

class ForceBackgroundShellArgs(_message.Message):
    __slots__ = ("tool_call_id",)
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    def __init__(self, tool_call_id: _Optional[str] = ...) -> None: ...

class ForceBackgroundShellResult(_message.Message):
    __slots__ = ("status", "shell_result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHELL_RESULT_FIELD_NUMBER: _ClassVar[int]
    status: ForceBackgroundShellStatus
    shell_result: ShellResult
    def __init__(self, status: _Optional[_Union[ForceBackgroundShellStatus, str]] = ..., shell_result: _Optional[_Union[ShellResult, _Mapping]] = ...) -> None: ...

class ForceBackgroundSubagentArgs(_message.Message):
    __slots__ = ("tool_call_id",)
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    def __init__(self, tool_call_id: _Optional[str] = ...) -> None: ...

class ForceBackgroundSubagentResult(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ForceBackgroundSubagentStatus
    def __init__(self, status: _Optional[_Union[ForceBackgroundSubagentStatus, str]] = ...) -> None: ...

class ForkAgentHostSessionRequest(_message.Message):
    __slots__ = ("session_id", "last_turn_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_TURN_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    last_turn_id: str
    def __init__(self, session_id: _Optional[str] = ..., last_turn_id: _Optional[str] = ...) -> None: ...

class ForkAgentHostSessionResponse(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class Frame(_message.Message):
    __slots__ = ("id", "method", "data", "kind", "error")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[Frame.Kind]
        KIND_REQUEST: _ClassVar[Frame.Kind]
        KIND_RESPONSE: _ClassVar[Frame.Kind]
        KIND_ERROR: _ClassVar[Frame.Kind]
    KIND_UNSPECIFIED: Frame.Kind
    KIND_REQUEST: Frame.Kind
    KIND_RESPONSE: Frame.Kind
    KIND_ERROR: Frame.Kind
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    method: str
    data: bytes
    kind: Frame.Kind
    error: str
    def __init__(self, id: _Optional[str] = ..., method: _Optional[str] = ..., data: _Optional[bytes] = ..., kind: _Optional[_Union[Frame.Kind, str]] = ..., error: _Optional[str] = ...) -> None: ...

class GenerateImageArgs(_message.Message):
    __slots__ = ("description", "file_path", "reference_image_paths", "aspect_ratio")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_IMAGE_PATHS_FIELD_NUMBER: _ClassVar[int]
    ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    description: str
    file_path: str
    reference_image_paths: _containers.RepeatedScalarFieldContainer[str]
    aspect_ratio: str
    def __init__(self, description: _Optional[str] = ..., file_path: _Optional[str] = ..., reference_image_paths: _Optional[_Iterable[str]] = ..., aspect_ratio: _Optional[str] = ...) -> None: ...

class GenerateImageError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GenerateImageRequestQuery(_message.Message):
    __slots__ = ("args", "tool_call_id")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    args: GenerateImageArgs
    tool_call_id: str
    def __init__(self, args: _Optional[_Union[GenerateImageArgs, _Mapping]] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class GenerateImageRequestResponse(_message.Message):
    __slots__ = ("approved", "rejected")
    class Approved(_message.Message):
        __slots__ = ("description",)
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        description: str
        def __init__(self, description: _Optional[str] = ...) -> None: ...
    class Rejected(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    approved: GenerateImageRequestResponse.Approved
    rejected: GenerateImageRequestResponse.Rejected
    def __init__(self, approved: _Optional[_Union[GenerateImageRequestResponse.Approved, _Mapping]] = ..., rejected: _Optional[_Union[GenerateImageRequestResponse.Rejected, _Mapping]] = ...) -> None: ...

class GenerateImageResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GenerateImageSuccess
    error: GenerateImageError
    def __init__(self, success: _Optional[_Union[GenerateImageSuccess, _Mapping]] = ..., error: _Optional[_Union[GenerateImageError, _Mapping]] = ...) -> None: ...

class GenerateImageSuccess(_message.Message):
    __slots__ = ("file_path", "image_data")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    image_data: str
    def __init__(self, file_path: _Optional[str] = ..., image_data: _Optional[str] = ...) -> None: ...

class GenerateImageToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: GenerateImageArgs
    result: GenerateImageResult
    def __init__(self, args: _Optional[_Union[GenerateImageArgs, _Mapping]] = ..., result: _Optional[_Union[GenerateImageResult, _Mapping]] = ...) -> None: ...

class GetAllowedModelIntentsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAllowedModelIntentsResponse(_message.Message):
    __slots__ = ("model_intents",)
    MODEL_INTENTS_FIELD_NUMBER: _ClassVar[int]
    model_intents: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model_intents: _Optional[_Iterable[str]] = ...) -> None: ...

class GetBlobArgs(_message.Message):
    __slots__ = ("blob_id",)
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    blob_id: bytes
    def __init__(self, blob_id: _Optional[bytes] = ...) -> None: ...

class GetBlobResult(_message.Message):
    __slots__ = ("blob_data", "error")
    BLOB_DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    blob_data: bytes
    error: Error
    def __init__(self, blob_data: _Optional[bytes] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class GetCapabilitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCapabilitiesResponse(_message.Message):
    __slots__ = ("computer_use_supported", "install_plugin_artifact_supported")
    COMPUTER_USE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    INSTALL_PLUGIN_ARTIFACT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    computer_use_supported: bool
    install_plugin_artifact_supported: bool
    def __init__(self, computer_use_supported: _Optional[bool] = ..., install_plugin_artifact_supported: _Optional[bool] = ...) -> None: ...

class GetCiStatusAction(_message.Message):
    __slots__ = ("pr_url", "branch_name", "repo_url")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    branch_name: str
    repo_url: str
    def __init__(self, pr_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., repo_url: _Optional[str] = ...) -> None: ...

class GetDefaultModelForCliRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultModelForCliResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: ModelDetails
    def __init__(self, model: _Optional[_Union[ModelDetails, _Mapping]] = ...) -> None: ...

class GetDiffRequest(_message.Message):
    __slots__ = ("cwd", "ref", "base_ref", "merge_base", "target_paths", "unified_context_lines", "max_untracked_files", "submodule_recurse_depth", "include_space_changes", "committed_only", "compute_patch_id", "return_head_sha", "max_response_bytes", "output_format")
    class OutputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OUTPUT_FORMAT_UNSPECIFIED: _ClassVar[GetDiffRequest.OutputFormat]
        OUTPUT_FORMAT_NAME_STATUS: _ClassVar[GetDiffRequest.OutputFormat]
        OUTPUT_FORMAT_NAME_STATUS_AND_NUMSTAT: _ClassVar[GetDiffRequest.OutputFormat]
        OUTPUT_FORMAT_FILE_DIFFS: _ClassVar[GetDiffRequest.OutputFormat]
        OUTPUT_FORMAT_DIFFS_WITH_BEFORE_AND_AFTER: _ClassVar[GetDiffRequest.OutputFormat]
    OUTPUT_FORMAT_UNSPECIFIED: GetDiffRequest.OutputFormat
    OUTPUT_FORMAT_NAME_STATUS: GetDiffRequest.OutputFormat
    OUTPUT_FORMAT_NAME_STATUS_AND_NUMSTAT: GetDiffRequest.OutputFormat
    OUTPUT_FORMAT_FILE_DIFFS: GetDiffRequest.OutputFormat
    OUTPUT_FORMAT_DIFFS_WITH_BEFORE_AND_AFTER: GetDiffRequest.OutputFormat
    CWD_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    BASE_REF_FIELD_NUMBER: _ClassVar[int]
    MERGE_BASE_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATHS_FIELD_NUMBER: _ClassVar[int]
    UNIFIED_CONTEXT_LINES_FIELD_NUMBER: _ClassVar[int]
    MAX_UNTRACKED_FILES_FIELD_NUMBER: _ClassVar[int]
    SUBMODULE_RECURSE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SPACE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_ONLY_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    RETURN_HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    MAX_RESPONSE_BYTES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    cwd: str
    ref: str
    base_ref: str
    merge_base: bool
    target_paths: _containers.RepeatedScalarFieldContainer[str]
    unified_context_lines: int
    max_untracked_files: int
    submodule_recurse_depth: int
    include_space_changes: bool
    committed_only: bool
    compute_patch_id: bool
    return_head_sha: bool
    max_response_bytes: int
    output_format: GetDiffRequest.OutputFormat
    def __init__(self, cwd: _Optional[str] = ..., ref: _Optional[str] = ..., base_ref: _Optional[str] = ..., merge_base: _Optional[bool] = ..., target_paths: _Optional[_Iterable[str]] = ..., unified_context_lines: _Optional[int] = ..., max_untracked_files: _Optional[int] = ..., submodule_recurse_depth: _Optional[int] = ..., include_space_changes: _Optional[bool] = ..., committed_only: _Optional[bool] = ..., compute_patch_id: _Optional[bool] = ..., return_head_sha: _Optional[bool] = ..., max_response_bytes: _Optional[int] = ..., output_format: _Optional[_Union[GetDiffRequest.OutputFormat, str]] = ...) -> None: ...

class GetDiffResponse(_message.Message):
    __slots__ = ("diff", "submodule_diffs", "patch_id", "head_sha", "has_uncommitted_changes")
    class SubmoduleDiff(_message.Message):
        __slots__ = ("relative_path", "diff", "errored")
        RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        DIFF_FIELD_NUMBER: _ClassVar[int]
        ERRORED_FIELD_NUMBER: _ClassVar[int]
        relative_path: str
        diff: GitDiff
        errored: bool
        def __init__(self, relative_path: _Optional[str] = ..., diff: _Optional[_Union[GitDiff, _Mapping]] = ..., errored: _Optional[bool] = ...) -> None: ...
    DIFF_FIELD_NUMBER: _ClassVar[int]
    SUBMODULE_DIFFS_FIELD_NUMBER: _ClassVar[int]
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    HEAD_SHA_FIELD_NUMBER: _ClassVar[int]
    HAS_UNCOMMITTED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    diff: GitDiff
    submodule_diffs: _containers.RepeatedCompositeFieldContainer[GetDiffResponse.SubmoduleDiff]
    patch_id: str
    head_sha: str
    has_uncommitted_changes: bool
    def __init__(self, diff: _Optional[_Union[GitDiff, _Mapping]] = ..., submodule_diffs: _Optional[_Iterable[_Union[GetDiffResponse.SubmoduleDiff, _Mapping]]] = ..., patch_id: _Optional[str] = ..., head_sha: _Optional[str] = ..., has_uncommitted_changes: _Optional[bool] = ...) -> None: ...

class GetMcpRefreshTokensRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMcpRefreshTokensResponse(_message.Message):
    __slots__ = ("refresh_tokens",)
    class RefreshTokensEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.ScalarMap[str, str]
    def __init__(self, refresh_tokens: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetMcpToolsAgentResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetMcpToolsSuccess
    error: GetMcpToolsError
    def __init__(self, success: _Optional[_Union[GetMcpToolsSuccess, _Mapping]] = ..., error: _Optional[_Union[GetMcpToolsError, _Mapping]] = ...) -> None: ...

class GetMcpToolsArgs(_message.Message):
    __slots__ = ("server", "tool_name", "pattern", "tool_call_id")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    server: str
    tool_name: str
    pattern: str
    tool_call_id: str
    def __init__(self, server: _Optional[str] = ..., tool_name: _Optional[str] = ..., pattern: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class GetMcpToolsError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GetMcpToolsSuccess(_message.Message):
    __slots__ = ("content", "output_file_path")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    content: str
    output_file_path: str
    def __init__(self, content: _Optional[str] = ..., output_file_path: _Optional[str] = ...) -> None: ...

class GetMcpToolsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: GetMcpToolsArgs
    result: GetMcpToolsAgentResult
    def __init__(self, args: _Optional[_Union[GetMcpToolsArgs, _Mapping]] = ..., result: _Optional[_Union[GetMcpToolsAgentResult, _Mapping]] = ...) -> None: ...

class GetNewChatNudgeLegacyModelPickerRequest(_message.Message):
    __slots__ = ("current_model", "max_mode")
    CURRENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    MAX_MODE_FIELD_NUMBER: _ClassVar[int]
    current_model: str
    max_mode: bool
    def __init__(self, current_model: _Optional[str] = ..., max_mode: _Optional[bool] = ...) -> None: ...

class GetNewChatNudgeLegacyModelPickerResponse(_message.Message):
    __slots__ = ("nudge",)
    NUDGE_FIELD_NUMBER: _ClassVar[int]
    nudge: NewChatNudge
    def __init__(self, nudge: _Optional[_Union[NewChatNudge, _Mapping]] = ...) -> None: ...

class GetNewChatNudgeParameterizedModelPickerRequest(_message.Message):
    __slots__ = ("current_model",)
    CURRENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    current_model: RequestedModel
    def __init__(self, current_model: _Optional[_Union[RequestedModel, _Mapping]] = ...) -> None: ...

class GetNewChatNudgeParameterizedModelPickerResponse(_message.Message):
    __slots__ = ("nudge",)
    NUDGE_FIELD_NUMBER: _ClassVar[int]
    nudge: NewChatNudgeV2
    def __init__(self, nudge: _Optional[_Union[NewChatNudgeV2, _Mapping]] = ...) -> None: ...

class GetPromptContextUsageRequest(_message.Message):
    __slots__ = ("conversation_id", "snapshot_blob_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    snapshot_blob_id: bytes
    def __init__(self, conversation_id: _Optional[str] = ..., snapshot_blob_id: _Optional[bytes] = ...) -> None: ...

class GetPromptContextUsageResponse(_message.Message):
    __slots__ = ("snapshot",)
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: PromptContextUsageSnapshot
    def __init__(self, snapshot: _Optional[_Union[PromptContextUsageSnapshot, _Mapping]] = ...) -> None: ...

class GetSignedUrlForAttachedMediaRequest(_message.Message):
    __slots__ = ("conversation_id", "key", "mime_type", "content_length_bytes")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    key: str
    mime_type: str
    content_length_bytes: int
    def __init__(self, conversation_id: _Optional[str] = ..., key: _Optional[str] = ..., mime_type: _Optional[str] = ..., content_length_bytes: _Optional[int] = ...) -> None: ...

class GetSignedUrlForAttachedMediaResponse(_message.Message):
    __slots__ = ("key", "post_url", "get_url", "expires_at_unix_ms", "refresh_after_unix_ms", "post_fields", "put_url")
    class PostFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_FIELD_NUMBER: _ClassVar[int]
    POST_URL_FIELD_NUMBER: _ClassVar[int]
    GET_URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_AFTER_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    POST_FIELDS_FIELD_NUMBER: _ClassVar[int]
    PUT_URL_FIELD_NUMBER: _ClassVar[int]
    key: str
    post_url: str
    get_url: str
    expires_at_unix_ms: int
    refresh_after_unix_ms: int
    post_fields: _containers.ScalarMap[str, str]
    put_url: str
    def __init__(self, key: _Optional[str] = ..., post_url: _Optional[str] = ..., get_url: _Optional[str] = ..., expires_at_unix_ms: _Optional[int] = ..., refresh_after_unix_ms: _Optional[int] = ..., post_fields: _Optional[_Mapping[str, str]] = ..., put_url: _Optional[str] = ...) -> None: ...

class GetUsableModelsRequest(_message.Message):
    __slots__ = ("custom_model_ids",)
    CUSTOM_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    custom_model_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, custom_model_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetUsableModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[ModelDetails]
    def __init__(self, models: _Optional[_Iterable[_Union[ModelDetails, _Mapping]]] = ...) -> None: ...

class GetWorkerIdResponse(_message.Message):
    __slots__ = ("worker_id",)
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    worker_id: str
    def __init__(self, worker_id: _Optional[str] = ...) -> None: ...

class GetWorkspaceChangesHashRequest(_message.Message):
    __slots__ = ("root_path", "base_ref")
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    BASE_REF_FIELD_NUMBER: _ClassVar[int]
    root_path: str
    base_ref: str
    def __init__(self, root_path: _Optional[str] = ..., base_ref: _Optional[str] = ...) -> None: ...

class GetWorkspaceChangesHashResponse(_message.Message):
    __slots__ = ("hash",)
    HASH_FIELD_NUMBER: _ClassVar[int]
    hash: str
    def __init__(self, hash: _Optional[str] = ...) -> None: ...

class GitCommit(_message.Message):
    __slots__ = ("commit", "author", "date", "message")
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    commit: str
    author: str
    date: str
    message: str
    def __init__(self, commit: _Optional[str] = ..., author: _Optional[str] = ..., date: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GitDiff(_message.Message):
    __slots__ = ("diffs", "diff_type")
    class DiffType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIFF_TYPE_UNSPECIFIED: _ClassVar[GitDiff.DiffType]
        DIFF_TYPE_DIFF_TO_HEAD: _ClassVar[GitDiff.DiffType]
        DIFF_TYPE_DIFF_FROM_BRANCH_TO_MAIN: _ClassVar[GitDiff.DiffType]
    DIFF_TYPE_UNSPECIFIED: GitDiff.DiffType
    DIFF_TYPE_DIFF_TO_HEAD: GitDiff.DiffType
    DIFF_TYPE_DIFF_FROM_BRANCH_TO_MAIN: GitDiff.DiffType
    DIFFS_FIELD_NUMBER: _ClassVar[int]
    DIFF_TYPE_FIELD_NUMBER: _ClassVar[int]
    diffs: _containers.RepeatedCompositeFieldContainer[FileDiff]
    diff_type: GitDiff.DiffType
    def __init__(self, diffs: _Optional[_Iterable[_Union[FileDiff, _Mapping]]] = ..., diff_type: _Optional[_Union[GitDiff.DiffType, str]] = ...) -> None: ...

class GitRepoInfo(_message.Message):
    __slots__ = ("path", "status", "branch_name", "remote_url", "previous_branch_is_ancestor", "is_origin_backed")
    PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_BRANCH_IS_ANCESTOR_FIELD_NUMBER: _ClassVar[int]
    IS_ORIGIN_BACKED_FIELD_NUMBER: _ClassVar[int]
    path: str
    status: str
    branch_name: str
    remote_url: str
    previous_branch_is_ancestor: bool
    is_origin_backed: bool
    def __init__(self, path: _Optional[str] = ..., status: _Optional[str] = ..., branch_name: _Optional[str] = ..., remote_url: _Optional[str] = ..., previous_branch_is_ancestor: _Optional[bool] = ..., is_origin_backed: _Optional[bool] = ...) -> None: ...

class GlobToolArgs(_message.Message):
    __slots__ = ("target_directory", "glob_pattern")
    TARGET_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    GLOB_PATTERN_FIELD_NUMBER: _ClassVar[int]
    target_directory: str
    glob_pattern: str
    def __init__(self, target_directory: _Optional[str] = ..., glob_pattern: _Optional[str] = ...) -> None: ...

class GlobToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: GlobToolArgs
    result: GlobToolResult
    def __init__(self, args: _Optional[_Union[GlobToolArgs, _Mapping]] = ..., result: _Optional[_Union[GlobToolResult, _Mapping]] = ...) -> None: ...

class GlobToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GlobToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GlobToolSuccess
    error: GlobToolError
    def __init__(self, success: _Optional[_Union[GlobToolSuccess, _Mapping]] = ..., error: _Optional[_Union[GlobToolError, _Mapping]] = ...) -> None: ...

class GlobToolSuccess(_message.Message):
    __slots__ = ("pattern", "path", "files", "total_files", "client_truncated", "ripgrep_truncated")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    RIPGREP_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    files: _containers.RepeatedScalarFieldContainer[str]
    total_files: int
    client_truncated: bool
    ripgrep_truncated: bool
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., files: _Optional[_Iterable[str]] = ..., total_files: _Optional[int] = ..., client_truncated: _Optional[bool] = ..., ripgrep_truncated: _Optional[bool] = ...) -> None: ...

class GoalContinuationAction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GoalError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GoalState(_message.Message):
    __slots__ = ("conversation_id", "goal_id", "objective", "status", "idle_continuations_without_tool_calls", "active_duration_ms", "last_accrued_at_ms", "continuation_count", "agent_session_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IDLE_CONTINUATIONS_WITHOUT_TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCRUED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    goal_id: str
    objective: str
    status: GoalStatus
    idle_continuations_without_tool_calls: int
    active_duration_ms: int
    last_accrued_at_ms: int
    continuation_count: int
    agent_session_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., goal_id: _Optional[str] = ..., objective: _Optional[str] = ..., status: _Optional[_Union[GoalStatus, str]] = ..., idle_continuations_without_tool_calls: _Optional[int] = ..., active_duration_ms: _Optional[int] = ..., last_accrued_at_ms: _Optional[int] = ..., continuation_count: _Optional[int] = ..., agent_session_id: _Optional[str] = ...) -> None: ...

class GrepArgs(_message.Message):
    __slots__ = ("pattern", "path", "glob", "output_mode", "context_before", "context_after", "context", "case_insensitive", "type", "head_limit", "multiline", "sort", "sort_ascending", "tool_call_id", "sandbox_policy", "offset")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    GLOB_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_AFTER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEAD_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MULTILINE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    SORT_ASCENDING_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_POLICY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    glob: str
    output_mode: str
    context_before: int
    context_after: int
    context: int
    case_insensitive: bool
    type: str
    head_limit: int
    multiline: bool
    sort: str
    sort_ascending: bool
    tool_call_id: str
    sandbox_policy: SandboxPolicy
    offset: int
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., glob: _Optional[str] = ..., output_mode: _Optional[str] = ..., context_before: _Optional[int] = ..., context_after: _Optional[int] = ..., context: _Optional[int] = ..., case_insensitive: _Optional[bool] = ..., type: _Optional[str] = ..., head_limit: _Optional[int] = ..., multiline: _Optional[bool] = ..., sort: _Optional[str] = ..., sort_ascending: _Optional[bool] = ..., tool_call_id: _Optional[str] = ..., sandbox_policy: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., offset: _Optional[int] = ...) -> None: ...

class GrepContentMatch(_message.Message):
    __slots__ = ("line_number", "content", "content_truncated", "is_context_line")
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    IS_CONTEXT_LINE_FIELD_NUMBER: _ClassVar[int]
    line_number: int
    content: str
    content_truncated: bool
    is_context_line: bool
    def __init__(self, line_number: _Optional[int] = ..., content: _Optional[str] = ..., content_truncated: _Optional[bool] = ..., is_context_line: _Optional[bool] = ...) -> None: ...

class GrepContentResult(_message.Message):
    __slots__ = ("matches", "total_lines", "total_matched_lines", "client_truncated", "ripgrep_truncated", "head_limit_applied", "offset_applied")
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LINES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHED_LINES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    RIPGREP_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    HEAD_LIMIT_APPLIED_FIELD_NUMBER: _ClassVar[int]
    OFFSET_APPLIED_FIELD_NUMBER: _ClassVar[int]
    matches: _containers.RepeatedCompositeFieldContainer[GrepFileMatch]
    total_lines: int
    total_matched_lines: int
    client_truncated: bool
    ripgrep_truncated: bool
    head_limit_applied: int
    offset_applied: int
    def __init__(self, matches: _Optional[_Iterable[_Union[GrepFileMatch, _Mapping]]] = ..., total_lines: _Optional[int] = ..., total_matched_lines: _Optional[int] = ..., client_truncated: _Optional[bool] = ..., ripgrep_truncated: _Optional[bool] = ..., head_limit_applied: _Optional[int] = ..., offset_applied: _Optional[int] = ...) -> None: ...

class GrepCountResult(_message.Message):
    __slots__ = ("counts", "total_files", "total_matches", "client_truncated", "ripgrep_truncated", "head_limit_applied", "offset_applied")
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    RIPGREP_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    HEAD_LIMIT_APPLIED_FIELD_NUMBER: _ClassVar[int]
    OFFSET_APPLIED_FIELD_NUMBER: _ClassVar[int]
    counts: _containers.RepeatedCompositeFieldContainer[GrepFileCount]
    total_files: int
    total_matches: int
    client_truncated: bool
    ripgrep_truncated: bool
    head_limit_applied: int
    offset_applied: int
    def __init__(self, counts: _Optional[_Iterable[_Union[GrepFileCount, _Mapping]]] = ..., total_files: _Optional[int] = ..., total_matches: _Optional[int] = ..., client_truncated: _Optional[bool] = ..., ripgrep_truncated: _Optional[bool] = ..., head_limit_applied: _Optional[int] = ..., offset_applied: _Optional[int] = ...) -> None: ...

class GrepError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class GrepFileCount(_message.Message):
    __slots__ = ("file", "count")
    FILE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    file: str
    count: int
    def __init__(self, file: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GrepFileMatch(_message.Message):
    __slots__ = ("file", "matches")
    FILE_FIELD_NUMBER: _ClassVar[int]
    MATCHES_FIELD_NUMBER: _ClassVar[int]
    file: str
    matches: _containers.RepeatedCompositeFieldContainer[GrepContentMatch]
    def __init__(self, file: _Optional[str] = ..., matches: _Optional[_Iterable[_Union[GrepContentMatch, _Mapping]]] = ...) -> None: ...

class GrepFilesResult(_message.Message):
    __slots__ = ("files", "total_files", "client_truncated", "ripgrep_truncated", "head_limit_applied", "offset_applied")
    FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    RIPGREP_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    HEAD_LIMIT_APPLIED_FIELD_NUMBER: _ClassVar[int]
    OFFSET_APPLIED_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedScalarFieldContainer[str]
    total_files: int
    client_truncated: bool
    ripgrep_truncated: bool
    head_limit_applied: int
    offset_applied: int
    def __init__(self, files: _Optional[_Iterable[str]] = ..., total_files: _Optional[int] = ..., client_truncated: _Optional[bool] = ..., ripgrep_truncated: _Optional[bool] = ..., head_limit_applied: _Optional[int] = ..., offset_applied: _Optional[int] = ...) -> None: ...

class GrepResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GrepSuccess
    error: GrepError
    def __init__(self, success: _Optional[_Union[GrepSuccess, _Mapping]] = ..., error: _Optional[_Union[GrepError, _Mapping]] = ...) -> None: ...

class GrepStream(_message.Message):
    __slots__ = ("pattern",)
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    def __init__(self, pattern: _Optional[str] = ...) -> None: ...

class GrepSuccess(_message.Message):
    __slots__ = ("pattern", "path", "output_mode", "workspace_results", "active_editor_result")
    class WorkspaceResultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GrepUnionResult
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GrepUnionResult, _Mapping]] = ...) -> None: ...
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_EDITOR_RESULT_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    output_mode: str
    workspace_results: _containers.MessageMap[str, GrepUnionResult]
    active_editor_result: GrepUnionResult
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., output_mode: _Optional[str] = ..., workspace_results: _Optional[_Mapping[str, GrepUnionResult]] = ..., active_editor_result: _Optional[_Union[GrepUnionResult, _Mapping]] = ...) -> None: ...

class GrepToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: GrepArgs
    result: GrepResult
    def __init__(self, args: _Optional[_Union[GrepArgs, _Mapping]] = ..., result: _Optional[_Union[GrepResult, _Mapping]] = ...) -> None: ...

class GrepUnionResult(_message.Message):
    __slots__ = ("count", "files", "content")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    count: GrepCountResult
    files: GrepFilesResult
    content: GrepContentResult
    def __init__(self, count: _Optional[_Union[GrepCountResult, _Mapping]] = ..., files: _Optional[_Union[GrepFilesResult, _Mapping]] = ..., content: _Optional[_Union[GrepContentResult, _Mapping]] = ...) -> None: ...

class HeartbeatUpdate(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HookAdditionalContext(_message.Message):
    __slots__ = ("hook_event_name", "content")
    HOOK_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    hook_event_name: str
    content: str
    def __init__(self, hook_event_name: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class HooksConfigInfo(_message.Message):
    __slots__ = ("configured_steps",)
    CONFIGURED_STEPS_FIELD_NUMBER: _ClassVar[int]
    configured_steps: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, configured_steps: _Optional[_Iterable[str]] = ...) -> None: ...

class IdeEditorsStateFile(_message.Message):
    __slots__ = ("relative_path", "absolute_path", "is_currently_focused", "current_line_number", "current_line_text", "line_count")
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENTLY_FOCUSED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LINE_TEXT_FIELD_NUMBER: _ClassVar[int]
    LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    relative_path: str
    absolute_path: str
    is_currently_focused: bool
    current_line_number: int
    current_line_text: str
    line_count: int
    def __init__(self, relative_path: _Optional[str] = ..., absolute_path: _Optional[str] = ..., is_currently_focused: _Optional[bool] = ..., current_line_number: _Optional[int] = ..., current_line_text: _Optional[str] = ..., line_count: _Optional[int] = ...) -> None: ...

class IdeEditorsStateLite(_message.Message):
    __slots__ = ("recently_viewed_files",)
    RECENTLY_VIEWED_FILES_FIELD_NUMBER: _ClassVar[int]
    recently_viewed_files: _containers.RepeatedCompositeFieldContainer[IdeEditorsStateFile]
    def __init__(self, recently_viewed_files: _Optional[_Iterable[_Union[IdeEditorsStateFile, _Mapping]]] = ...) -> None: ...

class IdlePeriod(_message.Message):
    __slots__ = ("start_ms", "end_ms", "duration_ms", "classification", "suggested_speed", "preceding_action_type", "following_action_type")
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CLASSIFICATION_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_SPEED_FIELD_NUMBER: _ClassVar[int]
    PRECEDING_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    start_ms: int
    end_ms: int
    duration_ms: int
    classification: IdleClassification
    suggested_speed: float
    preceding_action_type: str
    following_action_type: str
    def __init__(self, start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., classification: _Optional[_Union[IdleClassification, str]] = ..., suggested_speed: _Optional[float] = ..., preceding_action_type: _Optional[str] = ..., following_action_type: _Optional[str] = ...) -> None: ...

class ImageProto(_message.Message):
    __slots__ = ("data", "uuid", "path", "dimension", "task_specific_description", "mime_type")
    class Dimension(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    TASK_SPECIFIC_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    uuid: str
    path: str
    dimension: ImageProto.Dimension
    task_specific_description: str
    mime_type: str
    def __init__(self, data: _Optional[bytes] = ..., uuid: _Optional[str] = ..., path: _Optional[str] = ..., dimension: _Optional[_Union[ImageProto.Dimension, _Mapping]] = ..., task_specific_description: _Optional[str] = ..., mime_type: _Optional[str] = ...) -> None: ...

class InjectContextAction(_message.Message):
    __slots__ = ("injection_id", "expected_run_id", "user_context", "system_context")
    INJECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    injection_id: str
    expected_run_id: str
    user_context: UserContextInjection
    system_context: SystemContextInjection
    def __init__(self, injection_id: _Optional[str] = ..., expected_run_id: _Optional[str] = ..., user_context: _Optional[_Union[UserContextInjection, _Mapping]] = ..., system_context: _Optional[_Union[SystemContextInjection, _Mapping]] = ...) -> None: ...

class InputEvent(_message.Message):
    __slots__ = ("execution_timestamp_ms", "action", "command_duration_ms", "position_before", "position_after", "cursor_type_after")
    EXECUTION_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    COMMAND_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    POSITION_BEFORE_FIELD_NUMBER: _ClassVar[int]
    POSITION_AFTER_FIELD_NUMBER: _ClassVar[int]
    CURSOR_TYPE_AFTER_FIELD_NUMBER: _ClassVar[int]
    execution_timestamp_ms: int
    action: ComputerUseAction
    command_duration_ms: int
    position_before: Coordinate
    position_after: Coordinate
    cursor_type_after: CursorType
    def __init__(self, execution_timestamp_ms: _Optional[int] = ..., action: _Optional[_Union[ComputerUseAction, _Mapping]] = ..., command_duration_ms: _Optional[int] = ..., position_before: _Optional[_Union[Coordinate, _Mapping]] = ..., position_after: _Optional[_Union[Coordinate, _Mapping]] = ..., cursor_type_after: _Optional[_Union[CursorType, str]] = ...) -> None: ...

class InstallPluginArtifactRequest(_message.Message):
    __slots__ = ("download_url", "target_root", "artifact_digest")
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    TARGET_ROOT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    target_root: str
    artifact_digest: str
    def __init__(self, download_url: _Optional[str] = ..., target_root: _Optional[str] = ..., artifact_digest: _Optional[str] = ...) -> None: ...

class InstallPluginArtifactResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InteractionQuery(_message.Message):
    __slots__ = ("id", "web_search_request_query", "ask_question_interaction_query", "switch_mode_request_query", "create_plan_request_query", "setup_vm_environment_args", "web_fetch_request_query", "pr_management_request_query", "mcp_auth_request_query", "generate_image_request_query", "replace_env_args", "connect_scm_request_query")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    ASK_QUESTION_INTERACTION_QUERY_FIELD_NUMBER: _ClassVar[int]
    SWITCH_MODE_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    CREATE_PLAN_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_ENVIRONMENT_ARGS_FIELD_NUMBER: _ClassVar[int]
    WEB_FETCH_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    PR_MANAGEMENT_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    MCP_AUTH_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    GENERATE_IMAGE_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ENV_ARGS_FIELD_NUMBER: _ClassVar[int]
    CONNECT_SCM_REQUEST_QUERY_FIELD_NUMBER: _ClassVar[int]
    id: int
    web_search_request_query: WebSearchRequestQuery
    ask_question_interaction_query: AskQuestionInteractionQuery
    switch_mode_request_query: SwitchModeRequestQuery
    create_plan_request_query: CreatePlanRequestQuery
    setup_vm_environment_args: SetupVmEnvironmentArgs
    web_fetch_request_query: WebFetchRequestQuery
    pr_management_request_query: PrManagementRequestQuery
    mcp_auth_request_query: McpAuthRequestQuery
    generate_image_request_query: GenerateImageRequestQuery
    replace_env_args: ReplaceEnvArgs
    connect_scm_request_query: ConnectScmRequestQuery
    def __init__(self, id: _Optional[int] = ..., web_search_request_query: _Optional[_Union[WebSearchRequestQuery, _Mapping]] = ..., ask_question_interaction_query: _Optional[_Union[AskQuestionInteractionQuery, _Mapping]] = ..., switch_mode_request_query: _Optional[_Union[SwitchModeRequestQuery, _Mapping]] = ..., create_plan_request_query: _Optional[_Union[CreatePlanRequestQuery, _Mapping]] = ..., setup_vm_environment_args: _Optional[_Union[SetupVmEnvironmentArgs, _Mapping]] = ..., web_fetch_request_query: _Optional[_Union[WebFetchRequestQuery, _Mapping]] = ..., pr_management_request_query: _Optional[_Union[PrManagementRequestQuery, _Mapping]] = ..., mcp_auth_request_query: _Optional[_Union[McpAuthRequestQuery, _Mapping]] = ..., generate_image_request_query: _Optional[_Union[GenerateImageRequestQuery, _Mapping]] = ..., replace_env_args: _Optional[_Union[ReplaceEnvArgs, _Mapping]] = ..., connect_scm_request_query: _Optional[_Union[ConnectScmRequestQuery, _Mapping]] = ...) -> None: ...

class InteractionResponse(_message.Message):
    __slots__ = ("id", "web_search_request_response", "ask_question_interaction_response", "switch_mode_request_response", "create_plan_request_response", "setup_vm_environment_result", "web_fetch_request_response", "pr_management_result", "mcp_auth_request_response", "generate_image_request_response", "replace_env_result", "connect_scm_request_response")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ASK_QUESTION_INTERACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SWITCH_MODE_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CREATE_PLAN_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_ENVIRONMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    WEB_FETCH_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PR_MANAGEMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    MCP_AUTH_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_IMAGE_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ENV_RESULT_FIELD_NUMBER: _ClassVar[int]
    CONNECT_SCM_REQUEST_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    id: int
    web_search_request_response: WebSearchRequestResponse
    ask_question_interaction_response: AskQuestionInteractionResponse
    switch_mode_request_response: SwitchModeRequestResponse
    create_plan_request_response: CreatePlanRequestResponse
    setup_vm_environment_result: SetupVmEnvironmentResult
    web_fetch_request_response: WebFetchRequestResponse
    pr_management_result: PrManagementResult
    mcp_auth_request_response: McpAuthRequestResponse
    generate_image_request_response: GenerateImageRequestResponse
    replace_env_result: ReplaceEnvResult
    connect_scm_request_response: ConnectScmRequestResponse
    def __init__(self, id: _Optional[int] = ..., web_search_request_response: _Optional[_Union[WebSearchRequestResponse, _Mapping]] = ..., ask_question_interaction_response: _Optional[_Union[AskQuestionInteractionResponse, _Mapping]] = ..., switch_mode_request_response: _Optional[_Union[SwitchModeRequestResponse, _Mapping]] = ..., create_plan_request_response: _Optional[_Union[CreatePlanRequestResponse, _Mapping]] = ..., setup_vm_environment_result: _Optional[_Union[SetupVmEnvironmentResult, _Mapping]] = ..., web_fetch_request_response: _Optional[_Union[WebFetchRequestResponse, _Mapping]] = ..., pr_management_result: _Optional[_Union[PrManagementResult, _Mapping]] = ..., mcp_auth_request_response: _Optional[_Union[McpAuthRequestResponse, _Mapping]] = ..., generate_image_request_response: _Optional[_Union[GenerateImageRequestResponse, _Mapping]] = ..., replace_env_result: _Optional[_Union[ReplaceEnvResult, _Mapping]] = ..., connect_scm_request_response: _Optional[_Union[ConnectScmRequestResponse, _Mapping]] = ...) -> None: ...

class InteractionUpdate(_message.Message):
    __slots__ = ("text_delta", "partial_tool_call", "tool_call_delta", "tool_call_started", "tool_call_completed", "thinking_delta", "thinking_completed", "user_message_appended", "token_delta", "summary", "summary_started", "summary_completed", "shell_output_delta", "heartbeat", "turn_ended", "step_started", "step_completed", "prompt_suggestion", "post_request_prompt", "active_branch_change", "feedback_request", "response_comparison", "context_injection_state")
    TEXT_DELTA_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_DELTA_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_STARTED_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    THINKING_DELTA_FIELD_NUMBER: _ClassVar[int]
    THINKING_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_APPENDED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_DELTA_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_STARTED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    SHELL_OUTPUT_DELTA_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    TURN_ENDED_FIELD_NUMBER: _ClassVar[int]
    STEP_STARTED_FIELD_NUMBER: _ClassVar[int]
    STEP_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    PROMPT_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    POST_REQUEST_PROMPT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_BRANCH_CHANGE_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_COMPARISON_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_INJECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    text_delta: TextDeltaUpdate
    partial_tool_call: PartialToolCallUpdate
    tool_call_delta: ToolCallDeltaUpdate
    tool_call_started: ToolCallStartedUpdate
    tool_call_completed: ToolCallCompletedUpdate
    thinking_delta: ThinkingDeltaUpdate
    thinking_completed: ThinkingCompletedUpdate
    user_message_appended: UserMessageAppendedUpdate
    token_delta: TokenDeltaUpdate
    summary: SummaryUpdate
    summary_started: SummaryStartedUpdate
    summary_completed: SummaryCompletedUpdate
    shell_output_delta: ShellOutputDeltaUpdate
    heartbeat: HeartbeatUpdate
    turn_ended: TurnEndedUpdate
    step_started: StepStartedUpdate
    step_completed: StepCompletedUpdate
    prompt_suggestion: PromptSuggestionUpdate
    post_request_prompt: PostRequestPromptUpdate
    active_branch_change: ActiveBranchChange
    feedback_request: FeedbackRequestUpdate
    response_comparison: ResponseComparisonUpdate
    context_injection_state: ContextInjectionStateUpdate
    def __init__(self, text_delta: _Optional[_Union[TextDeltaUpdate, _Mapping]] = ..., partial_tool_call: _Optional[_Union[PartialToolCallUpdate, _Mapping]] = ..., tool_call_delta: _Optional[_Union[ToolCallDeltaUpdate, _Mapping]] = ..., tool_call_started: _Optional[_Union[ToolCallStartedUpdate, _Mapping]] = ..., tool_call_completed: _Optional[_Union[ToolCallCompletedUpdate, _Mapping]] = ..., thinking_delta: _Optional[_Union[ThinkingDeltaUpdate, _Mapping]] = ..., thinking_completed: _Optional[_Union[ThinkingCompletedUpdate, _Mapping]] = ..., user_message_appended: _Optional[_Union[UserMessageAppendedUpdate, _Mapping]] = ..., token_delta: _Optional[_Union[TokenDeltaUpdate, _Mapping]] = ..., summary: _Optional[_Union[SummaryUpdate, _Mapping]] = ..., summary_started: _Optional[_Union[SummaryStartedUpdate, _Mapping]] = ..., summary_completed: _Optional[_Union[SummaryCompletedUpdate, _Mapping]] = ..., shell_output_delta: _Optional[_Union[ShellOutputDeltaUpdate, _Mapping]] = ..., heartbeat: _Optional[_Union[HeartbeatUpdate, _Mapping]] = ..., turn_ended: _Optional[_Union[TurnEndedUpdate, _Mapping]] = ..., step_started: _Optional[_Union[StepStartedUpdate, _Mapping]] = ..., step_completed: _Optional[_Union[StepCompletedUpdate, _Mapping]] = ..., prompt_suggestion: _Optional[_Union[PromptSuggestionUpdate, _Mapping]] = ..., post_request_prompt: _Optional[_Union[PostRequestPromptUpdate, _Mapping]] = ..., active_branch_change: _Optional[_Union[ActiveBranchChange, _Mapping]] = ..., feedback_request: _Optional[_Union[FeedbackRequestUpdate, _Mapping]] = ..., response_comparison: _Optional[_Union[ResponseComparisonUpdate, _Mapping]] = ..., context_injection_state: _Optional[_Union[ContextInjectionStateUpdate, _Mapping]] = ...) -> None: ...

class InterruptAgentHostTurnRequest(_message.Message):
    __slots__ = ("session_id", "turn_id", "reason")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    turn_id: str
    reason: str
    def __init__(self, session_id: _Optional[str] = ..., turn_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class InterruptAgentHostTurnResponse(_message.Message):
    __slots__ = ("interrupted",)
    INTERRUPTED_FIELD_NUMBER: _ClassVar[int]
    interrupted: bool
    def __init__(self, interrupted: _Optional[bool] = ...) -> None: ...

class InterruptedPendingToolCallResolution(_message.Message):
    __slots__ = ("tool_call_id", "shell_result", "task_result")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SHELL_RESULT_FIELD_NUMBER: _ClassVar[int]
    TASK_RESULT_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    shell_result: ShellResult
    task_result: TaskResult
    def __init__(self, tool_call_id: _Optional[str] = ..., shell_result: _Optional[_Union[ShellResult, _Mapping]] = ..., task_result: _Optional[_Union[TaskResult, _Mapping]] = ...) -> None: ...

class InterruptedPendingToolCallResolutions(_message.Message):
    __slots__ = ("resolutions",)
    RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    resolutions: _containers.RepeatedCompositeFieldContainer[InterruptedPendingToolCallResolution]
    def __init__(self, resolutions: _Optional[_Iterable[_Union[InterruptedPendingToolCallResolution, _Mapping]]] = ...) -> None: ...

class InvocationContext(_message.Message):
    __slots__ = ("slack_thread", "github_pr", "ide_state", "microsoft_teams_thread", "blob_id")
    class GithubPR(_message.Message):
        __slots__ = ("title", "description", "comments", "ci_failures")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        COMMENTS_FIELD_NUMBER: _ClassVar[int]
        CI_FAILURES_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        comments: str
        ci_failures: str
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., comments: _Optional[str] = ..., ci_failures: _Optional[str] = ...) -> None: ...
    class IdeState(_message.Message):
        __slots__ = ("visible_files", "recently_viewed_files", "currently_viewed_prs")
        class File(_message.Message):
            __slots__ = ("path", "relative_path", "cursor_position", "total_lines", "active_command")
            class CursorPosition(_message.Message):
                __slots__ = ("line", "text")
                LINE_FIELD_NUMBER: _ClassVar[int]
                TEXT_FIELD_NUMBER: _ClassVar[int]
                line: int
                text: str
                def __init__(self, line: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...
            PATH_FIELD_NUMBER: _ClassVar[int]
            RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
            CURSOR_POSITION_FIELD_NUMBER: _ClassVar[int]
            TOTAL_LINES_FIELD_NUMBER: _ClassVar[int]
            ACTIVE_COMMAND_FIELD_NUMBER: _ClassVar[int]
            path: str
            relative_path: str
            cursor_position: InvocationContext.IdeState.File.CursorPosition
            total_lines: int
            active_command: str
            def __init__(self, path: _Optional[str] = ..., relative_path: _Optional[str] = ..., cursor_position: _Optional[_Union[InvocationContext.IdeState.File.CursorPosition, _Mapping]] = ..., total_lines: _Optional[int] = ..., active_command: _Optional[str] = ...) -> None: ...
        class ViewedPullRequest(_message.Message):
            __slots__ = ("number", "url", "title", "folder_path", "summary_json", "description")
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            URL_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
            SUMMARY_JSON_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            number: int
            url: str
            title: str
            folder_path: str
            summary_json: str
            description: str
            def __init__(self, number: _Optional[int] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., folder_path: _Optional[str] = ..., summary_json: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
        VISIBLE_FILES_FIELD_NUMBER: _ClassVar[int]
        RECENTLY_VIEWED_FILES_FIELD_NUMBER: _ClassVar[int]
        CURRENTLY_VIEWED_PRS_FIELD_NUMBER: _ClassVar[int]
        visible_files: _containers.RepeatedCompositeFieldContainer[InvocationContext.IdeState.File]
        recently_viewed_files: _containers.RepeatedCompositeFieldContainer[InvocationContext.IdeState.File]
        currently_viewed_prs: _containers.RepeatedCompositeFieldContainer[InvocationContext.IdeState.ViewedPullRequest]
        def __init__(self, visible_files: _Optional[_Iterable[_Union[InvocationContext.IdeState.File, _Mapping]]] = ..., recently_viewed_files: _Optional[_Iterable[_Union[InvocationContext.IdeState.File, _Mapping]]] = ..., currently_viewed_prs: _Optional[_Iterable[_Union[InvocationContext.IdeState.ViewedPullRequest, _Mapping]]] = ...) -> None: ...
    class MicrosoftTeamsThread(_message.Message):
        __slots__ = ("thread", "channel_name", "team_name", "channel_description", "team_description")
        THREAD_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TEAM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        thread: str
        channel_name: str
        team_name: str
        channel_description: str
        team_description: str
        def __init__(self, thread: _Optional[str] = ..., channel_name: _Optional[str] = ..., team_name: _Optional[str] = ..., channel_description: _Optional[str] = ..., team_description: _Optional[str] = ...) -> None: ...
    class SlackThread(_message.Message):
        __slots__ = ("thread", "channel_name", "channel_purpose", "channel_topic", "sender_name", "sender_id", "sender_type", "is_directly_addressed")
        THREAD_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_PURPOSE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_TOPIC_FIELD_NUMBER: _ClassVar[int]
        SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
        SENDER_ID_FIELD_NUMBER: _ClassVar[int]
        SENDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_DIRECTLY_ADDRESSED_FIELD_NUMBER: _ClassVar[int]
        thread: str
        channel_name: str
        channel_purpose: str
        channel_topic: str
        sender_name: str
        sender_id: str
        sender_type: str
        is_directly_addressed: bool
        def __init__(self, thread: _Optional[str] = ..., channel_name: _Optional[str] = ..., channel_purpose: _Optional[str] = ..., channel_topic: _Optional[str] = ..., sender_name: _Optional[str] = ..., sender_id: _Optional[str] = ..., sender_type: _Optional[str] = ..., is_directly_addressed: _Optional[bool] = ...) -> None: ...
    SLACK_THREAD_FIELD_NUMBER: _ClassVar[int]
    GITHUB_PR_FIELD_NUMBER: _ClassVar[int]
    IDE_STATE_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT_TEAMS_THREAD_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    slack_thread: InvocationContext.SlackThread
    github_pr: InvocationContext.GithubPR
    ide_state: InvocationContext.IdeState
    microsoft_teams_thread: InvocationContext.MicrosoftTeamsThread
    blob_id: bytes
    def __init__(self, slack_thread: _Optional[_Union[InvocationContext.SlackThread, _Mapping]] = ..., github_pr: _Optional[_Union[InvocationContext.GithubPR, _Mapping]] = ..., ide_state: _Optional[_Union[InvocationContext.IdeState, _Mapping]] = ..., microsoft_teams_thread: _Optional[_Union[InvocationContext.MicrosoftTeamsThread, _Mapping]] = ..., blob_id: _Optional[bytes] = ...) -> None: ...

class KeyAction(_message.Message):
    __slots__ = ("key", "hold_duration_ms")
    KEY_FIELD_NUMBER: _ClassVar[int]
    HOLD_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    key: str
    hold_duration_ms: int
    def __init__(self, key: _Optional[str] = ..., hold_duration_ms: _Optional[int] = ...) -> None: ...

class KeystrokeEvent(_message.Message):
    __slots__ = ("video_timestamp_ms", "display_text", "event_type", "display_duration_ms", "action_index")
    VIDEO_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ACTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    video_timestamp_ms: int
    display_text: str
    event_type: KeystrokeEventType
    display_duration_ms: int
    action_index: int
    def __init__(self, video_timestamp_ms: _Optional[int] = ..., display_text: _Optional[str] = ..., event_type: _Optional[_Union[KeystrokeEventType, str]] = ..., display_duration_ms: _Optional[int] = ..., action_index: _Optional[int] = ...) -> None: ...

class KillTmuxSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class KillTmuxSessionResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class KvClientMessage(_message.Message):
    __slots__ = ("id", "get_blob_result", "set_blob_result")
    ID_FIELD_NUMBER: _ClassVar[int]
    GET_BLOB_RESULT_FIELD_NUMBER: _ClassVar[int]
    SET_BLOB_RESULT_FIELD_NUMBER: _ClassVar[int]
    id: int
    get_blob_result: GetBlobResult
    set_blob_result: SetBlobResult
    def __init__(self, id: _Optional[int] = ..., get_blob_result: _Optional[_Union[GetBlobResult, _Mapping]] = ..., set_blob_result: _Optional[_Union[SetBlobResult, _Mapping]] = ...) -> None: ...

class KvServerMessage(_message.Message):
    __slots__ = ("id", "span_context", "get_blob_args", "set_blob_args")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    GET_BLOB_ARGS_FIELD_NUMBER: _ClassVar[int]
    SET_BLOB_ARGS_FIELD_NUMBER: _ClassVar[int]
    id: int
    span_context: SpanContext
    get_blob_args: GetBlobArgs
    set_blob_args: SetBlobArgs
    def __init__(self, id: _Optional[int] = ..., span_context: _Optional[_Union[SpanContext, _Mapping]] = ..., get_blob_args: _Optional[_Union[GetBlobArgs, _Mapping]] = ..., set_blob_args: _Optional[_Union[SetBlobArgs, _Mapping]] = ...) -> None: ...

class ListAgentHostSessionsRequest(_message.Message):
    __slots__ = ("include_children", "parent_session_id")
    INCLUDE_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    PARENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    include_children: bool
    parent_session_id: str
    def __init__(self, include_children: _Optional[bool] = ..., parent_session_id: _Optional[str] = ...) -> None: ...

class ListAgentHostSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[AgentHostSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[AgentHostSession, _Mapping]]] = ...) -> None: ...

class ListArtifactsRequest(_message.Message):
    __slots__ = ("extra_paths",)
    EXTRA_PATHS_FIELD_NUMBER: _ClassVar[int]
    extra_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, extra_paths: _Optional[_Iterable[str]] = ...) -> None: ...

class ListArtifactsResponse(_message.Message):
    __slots__ = ("artifacts", "path_errors")
    class PathErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ArtifactPathError
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ArtifactPathError, _Mapping]] = ...) -> None: ...
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    PATH_ERRORS_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[ArtifactUploadMetadata]
    path_errors: _containers.MessageMap[str, ArtifactPathError]
    def __init__(self, artifacts: _Optional[_Iterable[_Union[ArtifactUploadMetadata, _Mapping]]] = ..., path_errors: _Optional[_Mapping[str, ArtifactPathError]] = ...) -> None: ...

class ListDirectoryRequest(_message.Message):
    __slots__ = ("path", "include_hidden")
    PATH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    path: str
    include_hidden: bool
    def __init__(self, path: _Optional[str] = ..., include_hidden: _Optional[bool] = ...) -> None: ...

class ListDirectoryResponse(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[DirectoryEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[DirectoryEntry, _Mapping]]] = ...) -> None: ...

class ListMcpResourcesError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ListMcpResourcesExecArgs(_message.Message):
    __slots__ = ("server",)
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: str
    def __init__(self, server: _Optional[str] = ...) -> None: ...

class ListMcpResourcesExecResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    class McpResource(_message.Message):
        __slots__ = ("uri", "name", "description", "mime_type", "server", "annotations")
        class AnnotationsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        URI_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        SERVER_FIELD_NUMBER: _ClassVar[int]
        ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
        uri: str
        name: str
        description: str
        mime_type: str
        server: str
        annotations: _containers.ScalarMap[str, str]
        def __init__(self, uri: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., server: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: ListMcpResourcesSuccess
    error: ListMcpResourcesError
    rejected: ListMcpResourcesRejected
    def __init__(self, success: _Optional[_Union[ListMcpResourcesSuccess, _Mapping]] = ..., error: _Optional[_Union[ListMcpResourcesError, _Mapping]] = ..., rejected: _Optional[_Union[ListMcpResourcesRejected, _Mapping]] = ...) -> None: ...

class ListMcpResourcesRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class ListMcpResourcesSuccess(_message.Message):
    __slots__ = ("resources",)
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[ListMcpResourcesExecResult.McpResource]
    def __init__(self, resources: _Optional[_Iterable[_Union[ListMcpResourcesExecResult.McpResource, _Mapping]]] = ...) -> None: ...

class ListMcpResourcesToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ListMcpResourcesExecArgs
    result: ListMcpResourcesExecResult
    def __init__(self, args: _Optional[_Union[ListMcpResourcesExecArgs, _Mapping]] = ..., result: _Optional[_Union[ListMcpResourcesExecResult, _Mapping]] = ...) -> None: ...

class ListPtysRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPtysResponse(_message.Message):
    __slots__ = ("ptys",)
    PTYS_FIELD_NUMBER: _ClassVar[int]
    ptys: _containers.RepeatedCompositeFieldContainer[PtyInfo]
    def __init__(self, ptys: _Optional[_Iterable[_Union[PtyInfo, _Mapping]]] = ...) -> None: ...

class ListTmuxSessionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTmuxSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[TmuxSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[TmuxSession, _Mapping]]] = ...) -> None: ...

class LoadMcpServersRequest(_message.Message):
    __slots__ = ("mcp_config_json", "remove_missing")
    MCP_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    REMOVE_MISSING_FIELD_NUMBER: _ClassVar[int]
    mcp_config_json: str
    remove_missing: bool
    def __init__(self, mcp_config_json: _Optional[str] = ..., remove_missing: _Optional[bool] = ...) -> None: ...

class LoadMcpServersResponse(_message.Message):
    __slots__ = ("loaded_server_names",)
    LOADED_SERVER_NAMES_FIELD_NUMBER: _ClassVar[int]
    loaded_server_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, loaded_server_names: _Optional[_Iterable[str]] = ...) -> None: ...

class LocalPromptQualityInvocation(_message.Message):
    __slots__ = ("invocation_id", "attempt_request_id", "attempt", "started_at", "completed_at", "model_id", "provider_name", "status", "messages", "response_messages", "tools_json", "prompt_tokens", "completion_tokens", "total_tokens", "token_limit", "error_message")
    INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOOLS_JSON_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    invocation_id: str
    attempt_request_id: str
    attempt: int
    started_at: str
    completed_at: str
    model_id: str
    provider_name: str
    status: LocalPromptQualityInvocationStatus
    messages: _containers.RepeatedScalarFieldContainer[bytes]
    response_messages: _containers.RepeatedScalarFieldContainer[bytes]
    tools_json: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    token_limit: int
    error_message: str
    def __init__(self, invocation_id: _Optional[str] = ..., attempt_request_id: _Optional[str] = ..., attempt: _Optional[int] = ..., started_at: _Optional[str] = ..., completed_at: _Optional[str] = ..., model_id: _Optional[str] = ..., provider_name: _Optional[str] = ..., status: _Optional[_Union[LocalPromptQualityInvocationStatus, str]] = ..., messages: _Optional[_Iterable[bytes]] = ..., response_messages: _Optional[_Iterable[bytes]] = ..., tools_json: _Optional[str] = ..., prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., token_limit: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class LsArgs(_message.Message):
    __slots__ = ("path", "ignore", "tool_call_id", "sandbox_policy", "timeout_ms")
    PATH_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_POLICY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    path: str
    ignore: _containers.RepeatedScalarFieldContainer[str]
    tool_call_id: str
    sandbox_policy: SandboxPolicy
    timeout_ms: int
    def __init__(self, path: _Optional[str] = ..., ignore: _Optional[_Iterable[str]] = ..., tool_call_id: _Optional[str] = ..., sandbox_policy: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class LsDirectoryTreeNode(_message.Message):
    __slots__ = ("abs_path", "children_dirs", "children_files", "children_were_processed", "full_subtree_extension_counts", "num_files")
    class File(_message.Message):
        __slots__ = ("name", "terminal_metadata")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TERMINAL_METADATA_FIELD_NUMBER: _ClassVar[int]
        name: str
        terminal_metadata: TerminalMetadata
        def __init__(self, name: _Optional[str] = ..., terminal_metadata: _Optional[_Union[TerminalMetadata, _Mapping]] = ...) -> None: ...
    class FullSubtreeExtensionCountsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ABS_PATH_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_DIRS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FILES_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_WERE_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    FULL_SUBTREE_EXTENSION_COUNTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    abs_path: str
    children_dirs: _containers.RepeatedCompositeFieldContainer[LsDirectoryTreeNode]
    children_files: _containers.RepeatedCompositeFieldContainer[LsDirectoryTreeNode.File]
    children_were_processed: bool
    full_subtree_extension_counts: _containers.ScalarMap[str, int]
    num_files: int
    def __init__(self, abs_path: _Optional[str] = ..., children_dirs: _Optional[_Iterable[_Union[LsDirectoryTreeNode, _Mapping]]] = ..., children_files: _Optional[_Iterable[_Union[LsDirectoryTreeNode.File, _Mapping]]] = ..., children_were_processed: _Optional[bool] = ..., full_subtree_extension_counts: _Optional[_Mapping[str, int]] = ..., num_files: _Optional[int] = ...) -> None: ...

class LsError(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class LsRejected(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class LsResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "timeout")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    success: LsSuccess
    error: LsError
    rejected: LsRejected
    timeout: LsTimeout
    def __init__(self, success: _Optional[_Union[LsSuccess, _Mapping]] = ..., error: _Optional[_Union[LsError, _Mapping]] = ..., rejected: _Optional[_Union[LsRejected, _Mapping]] = ..., timeout: _Optional[_Union[LsTimeout, _Mapping]] = ...) -> None: ...

class LsSuccess(_message.Message):
    __slots__ = ("directory_tree_root",)
    DIRECTORY_TREE_ROOT_FIELD_NUMBER: _ClassVar[int]
    directory_tree_root: LsDirectoryTreeNode
    def __init__(self, directory_tree_root: _Optional[_Union[LsDirectoryTreeNode, _Mapping]] = ...) -> None: ...

class LsTimeout(_message.Message):
    __slots__ = ("directory_tree_root",)
    DIRECTORY_TREE_ROOT_FIELD_NUMBER: _ClassVar[int]
    directory_tree_root: LsDirectoryTreeNode
    def __init__(self, directory_tree_root: _Optional[_Union[LsDirectoryTreeNode, _Mapping]] = ...) -> None: ...

class LsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: LsArgs
    result: LsResult
    def __init__(self, args: _Optional[_Union[LsArgs, _Mapping]] = ..., result: _Optional[_Union[LsResult, _Mapping]] = ...) -> None: ...

class MatchedInstalledPlugin(_message.Message):
    __slots__ = ("display_name", "description", "matched_keyword", "skills", "subagents", "hooks", "rules", "commands", "mcp_servers")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MATCHED_KEYWORD_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    matched_keyword: str
    skills: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    subagents: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    hooks: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    rules: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    commands: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    mcp_servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., matched_keyword: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., subagents: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., commands: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., mcp_servers: _Optional[_Iterable[str]] = ...) -> None: ...

class McpAllowlistPrecheckArgs(_message.Message):
    __slots__ = ("provider_identifier", "tool_name", "tool_call_id")
    PROVIDER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    provider_identifier: str
    tool_name: str
    tool_call_id: str
    def __init__(self, provider_identifier: _Optional[str] = ..., tool_name: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class McpAllowlistPrecheckResult(_message.Message):
    __slots__ = ("allowlisted",)
    ALLOWLISTED_FIELD_NUMBER: _ClassVar[int]
    allowlisted: bool
    def __init__(self, allowlisted: _Optional[bool] = ...) -> None: ...

class McpApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class McpArgs(_message.Message):
    __slots__ = ("name", "args", "tool_call_id", "provider_identifier", "tool_name", "smart_mode_approval", "smart_mode_approval_only", "skip_approval", "server_identifier")
    class ArgsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_APPROVAL_ONLY_FIELD_NUMBER: _ClassVar[int]
    SKIP_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    name: str
    args: _containers.MessageMap[str, _struct_pb2.Value]
    tool_call_id: str
    provider_identifier: str
    tool_name: str
    smart_mode_approval: SmartModeApproval
    smart_mode_approval_only: bool
    skip_approval: bool
    server_identifier: str
    def __init__(self, name: _Optional[str] = ..., args: _Optional[_Mapping[str, _struct_pb2.Value]] = ..., tool_call_id: _Optional[str] = ..., provider_identifier: _Optional[str] = ..., tool_name: _Optional[str] = ..., smart_mode_approval: _Optional[_Union[SmartModeApproval, _Mapping]] = ..., smart_mode_approval_only: _Optional[bool] = ..., skip_approval: _Optional[bool] = ..., server_identifier: _Optional[str] = ...) -> None: ...

class McpAuthArgs(_message.Message):
    __slots__ = ("server_identifier", "tool_call_id")
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    server_identifier: str
    tool_call_id: str
    def __init__(self, server_identifier: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class McpAuthError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class McpAuthRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class McpAuthRequestQuery(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: McpAuthArgs
    def __init__(self, args: _Optional[_Union[McpAuthArgs, _Mapping]] = ...) -> None: ...

class McpAuthRequestResponse(_message.Message):
    __slots__ = ("approved", "rejected")
    class Approved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Rejected(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    approved: McpAuthRequestResponse.Approved
    rejected: McpAuthRequestResponse.Rejected
    def __init__(self, approved: _Optional[_Union[McpAuthRequestResponse.Approved, _Mapping]] = ..., rejected: _Optional[_Union[McpAuthRequestResponse.Rejected, _Mapping]] = ...) -> None: ...

class McpAuthResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: McpAuthSuccess
    error: McpAuthError
    rejected: McpAuthRejected
    def __init__(self, success: _Optional[_Union[McpAuthSuccess, _Mapping]] = ..., error: _Optional[_Union[McpAuthError, _Mapping]] = ..., rejected: _Optional[_Union[McpAuthRejected, _Mapping]] = ...) -> None: ...

class McpAuthSuccess(_message.Message):
    __slots__ = ("server_identifier",)
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    server_identifier: str
    def __init__(self, server_identifier: _Optional[str] = ...) -> None: ...

class McpAuthToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: McpAuthArgs
    result: McpAuthResult
    def __init__(self, args: _Optional[_Union[McpAuthArgs, _Mapping]] = ..., result: _Optional[_Union[McpAuthResult, _Mapping]] = ...) -> None: ...

class McpDescriptor(_message.Message):
    __slots__ = ("server_name", "server_identifier", "folder_path", "server_use_instructions", "tools", "plugin", "marketplace", "plugin_db_id", "marketplace_id")
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    SERVER_USE_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_DB_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    server_identifier: str
    folder_path: str
    server_use_instructions: str
    tools: _containers.RepeatedCompositeFieldContainer[McpToolDescriptor]
    plugin: str
    marketplace: str
    plugin_db_id: str
    marketplace_id: str
    def __init__(self, server_name: _Optional[str] = ..., server_identifier: _Optional[str] = ..., folder_path: _Optional[str] = ..., server_use_instructions: _Optional[str] = ..., tools: _Optional[_Iterable[_Union[McpToolDescriptor, _Mapping]]] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., plugin_db_id: _Optional[str] = ..., marketplace_id: _Optional[str] = ...) -> None: ...

class McpError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class McpFileSystemOptions(_message.Message):
    __slots__ = ("enabled", "workspace_project_dir", "mcp_descriptors")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_PROJECT_DIR_FIELD_NUMBER: _ClassVar[int]
    MCP_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    workspace_project_dir: str
    mcp_descriptors: _containers.RepeatedCompositeFieldContainer[McpDescriptor]
    def __init__(self, enabled: _Optional[bool] = ..., workspace_project_dir: _Optional[str] = ..., mcp_descriptors: _Optional[_Iterable[_Union[McpDescriptor, _Mapping]]] = ...) -> None: ...

class McpImageContent(_message.Message):
    __slots__ = ("data", "mime_type")
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    mime_type: str
    def __init__(self, data: _Optional[bytes] = ..., mime_type: _Optional[str] = ...) -> None: ...

class McpInstructions(_message.Message):
    __slots__ = ("server_name", "instructions", "server_identifier")
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    instructions: str
    server_identifier: str
    def __init__(self, server_name: _Optional[str] = ..., instructions: _Optional[str] = ..., server_identifier: _Optional[str] = ...) -> None: ...

class McpMetaToolOptions(_message.Message):
    __slots__ = ("enabled", "mcp_descriptors")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MCP_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    mcp_descriptors: _containers.RepeatedCompositeFieldContainer[McpDescriptor]
    def __init__(self, enabled: _Optional[bool] = ..., mcp_descriptors: _Optional[_Iterable[_Union[McpDescriptor, _Mapping]]] = ...) -> None: ...

class McpPermissionDenied(_message.Message):
    __slots__ = ("error", "is_readonly")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    error: str
    is_readonly: bool
    def __init__(self, error: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class McpRejected(_message.Message):
    __slots__ = ("reason", "is_readonly")
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    reason: str
    is_readonly: bool
    def __init__(self, reason: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class McpResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "permission_denied", "tool_not_found", "server_not_found", "approved")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    TOOL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    SERVER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    success: McpSuccess
    error: McpError
    rejected: McpRejected
    permission_denied: McpPermissionDenied
    tool_not_found: McpToolNotFound
    server_not_found: McpServerNotFound
    approved: McpApproved
    def __init__(self, success: _Optional[_Union[McpSuccess, _Mapping]] = ..., error: _Optional[_Union[McpError, _Mapping]] = ..., rejected: _Optional[_Union[McpRejected, _Mapping]] = ..., permission_denied: _Optional[_Union[McpPermissionDenied, _Mapping]] = ..., tool_not_found: _Optional[_Union[McpToolNotFound, _Mapping]] = ..., server_not_found: _Optional[_Union[McpServerNotFound, _Mapping]] = ..., approved: _Optional[_Union[McpApproved, _Mapping]] = ...) -> None: ...

class McpServerNotFound(_message.Message):
    __slots__ = ("name", "available_servers")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SERVERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    available_servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., available_servers: _Optional[_Iterable[str]] = ...) -> None: ...

class McpStateError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class McpStateExecArgs(_message.Message):
    __slots__ = ("server_identifiers", "kick_only")
    SERVER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    KICK_ONLY_FIELD_NUMBER: _ClassVar[int]
    server_identifiers: _containers.RepeatedScalarFieldContainer[str]
    kick_only: bool
    def __init__(self, server_identifiers: _Optional[_Iterable[str]] = ..., kick_only: _Optional[bool] = ...) -> None: ...

class McpStateExecResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: McpStateSuccess
    error: McpStateError
    rejected: McpStateRejected
    def __init__(self, success: _Optional[_Union[McpStateSuccess, _Mapping]] = ..., error: _Optional[_Union[McpStateError, _Mapping]] = ..., rejected: _Optional[_Union[McpStateRejected, _Mapping]] = ...) -> None: ...

class McpStateRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class McpStateServer(_message.Message):
    __slots__ = ("server_name", "server_identifier", "plugin", "marketplace", "tools", "instructions", "status")
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    server_name: str
    server_identifier: str
    plugin: str
    marketplace: str
    tools: _containers.RepeatedCompositeFieldContainer[McpToolDefinition]
    instructions: _containers.RepeatedCompositeFieldContainer[McpInstructions]
    status: str
    def __init__(self, server_name: _Optional[str] = ..., server_identifier: _Optional[str] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., tools: _Optional[_Iterable[_Union[McpToolDefinition, _Mapping]]] = ..., instructions: _Optional[_Iterable[_Union[McpInstructions, _Mapping]]] = ..., status: _Optional[str] = ...) -> None: ...

class McpStateSuccess(_message.Message):
    __slots__ = ("servers",)
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[McpStateServer]
    def __init__(self, servers: _Optional[_Iterable[_Union[McpStateServer, _Mapping]]] = ...) -> None: ...

class McpSuccess(_message.Message):
    __slots__ = ("content", "is_error", "structured_content")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_ERROR_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[McpToolResultContentItem]
    is_error: bool
    structured_content: _struct_pb2.Struct
    def __init__(self, content: _Optional[_Iterable[_Union[McpToolResultContentItem, _Mapping]]] = ..., is_error: _Optional[bool] = ..., structured_content: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class McpTextContent(_message.Message):
    __slots__ = ("text", "output_location")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    text: str
    output_location: OutputLocation
    def __init__(self, text: _Optional[str] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ...) -> None: ...

class McpToolCall(_message.Message):
    __slots__ = ("args", "result", "description")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    args: McpArgs
    result: McpToolResult
    description: str
    def __init__(self, args: _Optional[_Union[McpArgs, _Mapping]] = ..., result: _Optional[_Union[McpToolResult, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class McpToolDefinition(_message.Message):
    __slots__ = ("name", "provider_identifier", "tool_name", "description", "input_schema", "input_schema_json")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    name: str
    provider_identifier: str
    tool_name: str
    description: str
    input_schema: _struct_pb2.Value
    input_schema_json: str
    def __init__(self, name: _Optional[str] = ..., provider_identifier: _Optional[str] = ..., tool_name: _Optional[str] = ..., description: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., input_schema_json: _Optional[str] = ...) -> None: ...

class McpToolDescriptor(_message.Message):
    __slots__ = ("tool_name", "definition_path", "description", "input_schema", "input_schema_json", "annotations_json")
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_PATH_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    INPUT_SCHEMA_JSON_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_JSON_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    definition_path: str
    description: str
    input_schema: _struct_pb2.Value
    input_schema_json: str
    annotations_json: str
    def __init__(self, tool_name: _Optional[str] = ..., definition_path: _Optional[str] = ..., description: _Optional[str] = ..., input_schema: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ..., input_schema_json: _Optional[str] = ..., annotations_json: _Optional[str] = ...) -> None: ...

class McpToolError(_message.Message):
    __slots__ = ("error", "read_tool_def_reminder")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    READ_TOOL_DEF_REMINDER_FIELD_NUMBER: _ClassVar[int]
    error: str
    read_tool_def_reminder: str
    def __init__(self, error: _Optional[str] = ..., read_tool_def_reminder: _Optional[str] = ...) -> None: ...

class McpToolNotFound(_message.Message):
    __slots__ = ("name", "available_tools")
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TOOLS_FIELD_NUMBER: _ClassVar[int]
    name: str
    available_tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., available_tools: _Optional[_Iterable[str]] = ...) -> None: ...

class McpToolResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "permission_denied")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    success: McpSuccess
    error: McpToolError
    rejected: McpRejected
    permission_denied: McpPermissionDenied
    def __init__(self, success: _Optional[_Union[McpSuccess, _Mapping]] = ..., error: _Optional[_Union[McpToolError, _Mapping]] = ..., rejected: _Optional[_Union[McpRejected, _Mapping]] = ..., permission_denied: _Optional[_Union[McpPermissionDenied, _Mapping]] = ...) -> None: ...

class McpToolResultContentItem(_message.Message):
    __slots__ = ("text", "image")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    text: McpTextContent
    image: McpImageContent
    def __init__(self, text: _Optional[_Union[McpTextContent, _Mapping]] = ..., image: _Optional[_Union[McpImageContent, _Mapping]] = ...) -> None: ...

class McpTools(_message.Message):
    __slots__ = ("mcp_tools",)
    MCP_TOOLS_FIELD_NUMBER: _ClassVar[int]
    mcp_tools: _containers.RepeatedCompositeFieldContainer[McpToolDefinition]
    def __init__(self, mcp_tools: _Optional[_Iterable[_Union[McpToolDefinition, _Mapping]]] = ...) -> None: ...

class ModelDetails(_message.Message):
    __slots__ = ("model_id", "display_model_id", "display_name", "display_name_short", "aliases", "thinking_details", "max_mode", "api_key_credentials", "azure_credentials", "bedrock_credentials")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_SHORT_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    THINKING_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MAX_MODE_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    display_model_id: str
    display_name: str
    display_name_short: str
    aliases: _containers.RepeatedScalarFieldContainer[str]
    thinking_details: ThinkingDetails
    max_mode: bool
    api_key_credentials: ApiKeyCredentials
    azure_credentials: AzureCredentials
    bedrock_credentials: BedrockCredentials
    def __init__(self, model_id: _Optional[str] = ..., display_model_id: _Optional[str] = ..., display_name: _Optional[str] = ..., display_name_short: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ..., thinking_details: _Optional[_Union[ThinkingDetails, _Mapping]] = ..., max_mode: _Optional[bool] = ..., api_key_credentials: _Optional[_Union[ApiKeyCredentials, _Mapping]] = ..., azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]] = ..., bedrock_credentials: _Optional[_Union[BedrockCredentials, _Mapping]] = ...) -> None: ...

class MountedAgentStore(_message.Message):
    __slots__ = ("path", "kind", "alias", "read_only")
    PATH_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_FIELD_NUMBER: _ClassVar[int]
    path: str
    kind: MountedAgentStoreKind
    alias: str
    read_only: bool
    def __init__(self, path: _Optional[str] = ..., kind: _Optional[_Union[MountedAgentStoreKind, str]] = ..., alias: _Optional[str] = ..., read_only: _Optional[bool] = ...) -> None: ...

class MouseDownAction(_message.Message):
    __slots__ = ("button",)
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    button: MouseButton
    def __init__(self, button: _Optional[_Union[MouseButton, str]] = ...) -> None: ...

class MouseMoveAction(_message.Message):
    __slots__ = ("coordinate",)
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    coordinate: Coordinate
    def __init__(self, coordinate: _Optional[_Union[Coordinate, _Mapping]] = ...) -> None: ...

class MouseUpAction(_message.Message):
    __slots__ = ("button",)
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    button: MouseButton
    def __init__(self, button: _Optional[_Union[MouseButton, str]] = ...) -> None: ...

class NameAgentRequest(_message.Message):
    __slots__ = ("user_message",)
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user_message: str
    def __init__(self, user_message: _Optional[str] = ...) -> None: ...

class NameAgentResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class NetworkPolicy(_message.Message):
    __slots__ = ("version", "default_action", "deny", "allow", "logging")
    class DefaultAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_ACTION_UNSPECIFIED: _ClassVar[NetworkPolicy.DefaultAction]
        DEFAULT_ACTION_ALLOW: _ClassVar[NetworkPolicy.DefaultAction]
        DEFAULT_ACTION_DENY: _ClassVar[NetworkPolicy.DefaultAction]
    DEFAULT_ACTION_UNSPECIFIED: NetworkPolicy.DefaultAction
    DEFAULT_ACTION_ALLOW: NetworkPolicy.DefaultAction
    DEFAULT_ACTION_DENY: NetworkPolicy.DefaultAction
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ACTION_FIELD_NUMBER: _ClassVar[int]
    DENY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    LOGGING_FIELD_NUMBER: _ClassVar[int]
    version: int
    default_action: NetworkPolicy.DefaultAction
    deny: _containers.RepeatedScalarFieldContainer[str]
    allow: _containers.RepeatedScalarFieldContainer[str]
    logging: NetworkPolicyLoggingConfig
    def __init__(self, version: _Optional[int] = ..., default_action: _Optional[_Union[NetworkPolicy.DefaultAction, str]] = ..., deny: _Optional[_Iterable[str]] = ..., allow: _Optional[_Iterable[str]] = ..., logging: _Optional[_Union[NetworkPolicyLoggingConfig, _Mapping]] = ...) -> None: ...

class NetworkPolicyLoggingConfig(_message.Message):
    __slots__ = ("decision_log_path", "log_format")
    DECISION_LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    LOG_FORMAT_FIELD_NUMBER: _ClassVar[int]
    decision_log_path: str
    log_format: str
    def __init__(self, decision_log_path: _Optional[str] = ..., log_format: _Optional[str] = ...) -> None: ...

class NewChatNudge(_message.Message):
    __slots__ = ("nudge_id", "target_model", "experiment_name", "bump", "ask", "silent_switch")
    NUDGE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODEL_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    BUMP_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    SILENT_SWITCH_FIELD_NUMBER: _ClassVar[int]
    nudge_id: str
    target_model: str
    experiment_name: str
    bump: NudgeBumpVariant
    ask: NudgeAskVariant
    silent_switch: NudgeSilentSwitchVariant
    def __init__(self, nudge_id: _Optional[str] = ..., target_model: _Optional[str] = ..., experiment_name: _Optional[str] = ..., bump: _Optional[_Union[NudgeBumpVariant, _Mapping]] = ..., ask: _Optional[_Union[NudgeAskVariant, _Mapping]] = ..., silent_switch: _Optional[_Union[NudgeSilentSwitchVariant, _Mapping]] = ...) -> None: ...

class NewChatNudgeV2(_message.Message):
    __slots__ = ("nudge_id", "target_model", "experiment_name", "bump", "ask", "silent_switch")
    NUDGE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODEL_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    BUMP_FIELD_NUMBER: _ClassVar[int]
    ASK_FIELD_NUMBER: _ClassVar[int]
    SILENT_SWITCH_FIELD_NUMBER: _ClassVar[int]
    nudge_id: str
    target_model: RequestedModel
    experiment_name: str
    bump: NudgeBumpVariant
    ask: NudgeAskVariant
    silent_switch: NudgeSilentSwitchVariant
    def __init__(self, nudge_id: _Optional[str] = ..., target_model: _Optional[_Union[RequestedModel, _Mapping]] = ..., experiment_name: _Optional[str] = ..., bump: _Optional[_Union[NudgeBumpVariant, _Mapping]] = ..., ask: _Optional[_Union[NudgeAskVariant, _Mapping]] = ..., silent_switch: _Optional[_Union[NudgeSilentSwitchVariant, _Mapping]] = ...) -> None: ...

class NewCloudVmTarget(_message.Message):
    __slots__ = ("environment_build_id", "base_branch")
    ENVIRONMENT_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    environment_build_id: str
    base_branch: str
    def __init__(self, environment_build_id: _Optional[str] = ..., base_branch: _Optional[str] = ...) -> None: ...

class NotifyConversationCloneRequest(_message.Message):
    __slots__ = ("conversation_id", "source_conversation_id", "source_request_id")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    source_conversation_id: str
    source_request_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., source_conversation_id: _Optional[str] = ..., source_request_id: _Optional[str] = ...) -> None: ...

class NotifyConversationCloneResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NudgeAskVariant(_message.Message):
    __slots__ = ("popup_message", "accept_label")
    POPUP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_LABEL_FIELD_NUMBER: _ClassVar[int]
    popup_message: str
    accept_label: str
    def __init__(self, popup_message: _Optional[str] = ..., accept_label: _Optional[str] = ...) -> None: ...

class NudgeBumpVariant(_message.Message):
    __slots__ = ("banner_message",)
    BANNER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    banner_message: str
    def __init__(self, banner_message: _Optional[str] = ...) -> None: ...

class NudgeSilentSwitchVariant(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OutputLocation(_message.Message):
    __slots__ = ("file_path", "size_bytes", "line_count")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    LINE_COUNT_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    size_bytes: int
    line_count: int
    def __init__(self, file_path: _Optional[str] = ..., size_bytes: _Optional[int] = ..., line_count: _Optional[int] = ...) -> None: ...

class PartialToolCallUpdate(_message.Message):
    __slots__ = ("call_id", "tool_call", "args_text_delta", "model_call_id")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    ARGS_TEXT_DELTA_FIELD_NUMBER: _ClassVar[int]
    MODEL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    tool_call: ToolCall
    args_text_delta: str
    model_call_id: str
    def __init__(self, call_id: _Optional[str] = ..., tool_call: _Optional[_Union[ToolCall, _Mapping]] = ..., args_text_delta: _Optional[str] = ..., model_call_id: _Optional[str] = ...) -> None: ...

class PermissionsAutoRunInstructions(_message.Message):
    __slots__ = ("allow_instructions", "block_instructions")
    ALLOW_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    allow_instructions: _containers.RepeatedScalarFieldContainer[str]
    block_instructions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allow_instructions: _Optional[_Iterable[str]] = ..., block_instructions: _Optional[_Iterable[str]] = ...) -> None: ...

class Phase(_message.Message):
    __slots__ = ("name", "todos")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    name: str
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    def __init__(self, name: _Optional[str] = ..., todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ...) -> None: ...

class PiBashExecArgs(_message.Message):
    __slots__ = ("command", "timeout")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    command: str
    timeout: float
    def __init__(self, command: _Optional[str] = ..., timeout: _Optional[float] = ...) -> None: ...

class PiBashExecError(_message.Message):
    __slots__ = ("error", "truncation", "full_output_path")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    FULL_OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    error: str
    truncation: PiTruncation
    full_output_path: str
    def __init__(self, error: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., full_output_path: _Optional[str] = ...) -> None: ...

class PiBashExecResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiBashExecSuccess
    error: PiBashExecError
    def __init__(self, success: _Optional[_Union[PiBashExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiBashExecError, _Mapping]] = ...) -> None: ...

class PiBashExecSuccess(_message.Message):
    __slots__ = ("output", "truncation", "full_output_path")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    FULL_OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    full_output_path: str
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., full_output_path: _Optional[str] = ...) -> None: ...

class PiBashToolArgs(_message.Message):
    __slots__ = ("command", "timeout")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    command: str
    timeout: float
    def __init__(self, command: _Optional[str] = ..., timeout: _Optional[float] = ...) -> None: ...

class PiBashToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiBashToolArgs
    result: PiBashToolResult
    def __init__(self, args: _Optional[_Union[PiBashToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiBashToolResult, _Mapping]] = ...) -> None: ...

class PiBashToolError(_message.Message):
    __slots__ = ("error", "truncation", "full_output_path")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    FULL_OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    error: str
    truncation: PiTruncation
    full_output_path: str
    def __init__(self, error: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., full_output_path: _Optional[str] = ...) -> None: ...

class PiBashToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiBashToolSuccess
    error: PiBashToolError
    def __init__(self, success: _Optional[_Union[PiBashToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiBashToolError, _Mapping]] = ...) -> None: ...

class PiBashToolSuccess(_message.Message):
    __slots__ = ("output", "truncation", "full_output_path")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    FULL_OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    full_output_path: str
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., full_output_path: _Optional[str] = ...) -> None: ...

class PiEditExecArgs(_message.Message):
    __slots__ = ("path", "edits")
    PATH_FIELD_NUMBER: _ClassVar[int]
    EDITS_FIELD_NUMBER: _ClassVar[int]
    path: str
    edits: _containers.RepeatedCompositeFieldContainer[PiEditReplacement]
    def __init__(self, path: _Optional[str] = ..., edits: _Optional[_Iterable[_Union[PiEditReplacement, _Mapping]]] = ...) -> None: ...

class PiEditExecError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiEditExecRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class PiEditExecResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: PiEditExecSuccess
    error: PiEditExecError
    rejected: PiEditExecRejected
    def __init__(self, success: _Optional[_Union[PiEditExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiEditExecError, _Mapping]] = ..., rejected: _Optional[_Union[PiEditExecRejected, _Mapping]] = ...) -> None: ...

class PiEditExecSuccess(_message.Message):
    __slots__ = ("output", "diff", "patch", "first_changed_line")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    FIRST_CHANGED_LINE_FIELD_NUMBER: _ClassVar[int]
    output: str
    diff: str
    patch: str
    first_changed_line: int
    def __init__(self, output: _Optional[str] = ..., diff: _Optional[str] = ..., patch: _Optional[str] = ..., first_changed_line: _Optional[int] = ...) -> None: ...

class PiEditReplacement(_message.Message):
    __slots__ = ("old_text", "new_text")
    OLD_TEXT_FIELD_NUMBER: _ClassVar[int]
    NEW_TEXT_FIELD_NUMBER: _ClassVar[int]
    old_text: str
    new_text: str
    def __init__(self, old_text: _Optional[str] = ..., new_text: _Optional[str] = ...) -> None: ...

class PiEditToolArgs(_message.Message):
    __slots__ = ("path", "edits")
    PATH_FIELD_NUMBER: _ClassVar[int]
    EDITS_FIELD_NUMBER: _ClassVar[int]
    path: str
    edits: _containers.RepeatedCompositeFieldContainer[PiEditReplacement]
    def __init__(self, path: _Optional[str] = ..., edits: _Optional[_Iterable[_Union[PiEditReplacement, _Mapping]]] = ...) -> None: ...

class PiEditToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiEditToolArgs
    result: PiEditToolResult
    def __init__(self, args: _Optional[_Union[PiEditToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiEditToolResult, _Mapping]] = ...) -> None: ...

class PiEditToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiEditToolRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class PiEditToolResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: PiEditToolSuccess
    error: PiEditToolError
    rejected: PiEditToolRejected
    def __init__(self, success: _Optional[_Union[PiEditToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiEditToolError, _Mapping]] = ..., rejected: _Optional[_Union[PiEditToolRejected, _Mapping]] = ...) -> None: ...

class PiEditToolSuccess(_message.Message):
    __slots__ = ("output", "diff", "patch", "first_changed_line")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    FIRST_CHANGED_LINE_FIELD_NUMBER: _ClassVar[int]
    output: str
    diff: str
    patch: str
    first_changed_line: int
    def __init__(self, output: _Optional[str] = ..., diff: _Optional[str] = ..., patch: _Optional[str] = ..., first_changed_line: _Optional[int] = ...) -> None: ...

class PiFindExecArgs(_message.Message):
    __slots__ = ("pattern", "path", "limit")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    limit: int
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class PiFindExecError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiFindExecResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiFindExecSuccess
    error: PiFindExecError
    def __init__(self, success: _Optional[_Union[PiFindExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiFindExecError, _Mapping]] = ...) -> None: ...

class PiFindExecSuccess(_message.Message):
    __slots__ = ("output", "truncation", "result_limit_reached")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    RESULT_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    result_limit_reached: int
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., result_limit_reached: _Optional[int] = ...) -> None: ...

class PiFindToolArgs(_message.Message):
    __slots__ = ("pattern", "path", "limit")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    limit: int
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class PiFindToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiFindToolArgs
    result: PiFindToolResult
    def __init__(self, args: _Optional[_Union[PiFindToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiFindToolResult, _Mapping]] = ...) -> None: ...

class PiFindToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiFindToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiFindToolSuccess
    error: PiFindToolError
    def __init__(self, success: _Optional[_Union[PiFindToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiFindToolError, _Mapping]] = ...) -> None: ...

class PiFindToolSuccess(_message.Message):
    __slots__ = ("output", "truncation", "result_limit_reached")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    RESULT_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    result_limit_reached: int
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., result_limit_reached: _Optional[int] = ...) -> None: ...

class PiGrepExecArgs(_message.Message):
    __slots__ = ("pattern", "path", "glob", "ignore_case", "literal", "context", "limit")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    GLOB_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CASE_FIELD_NUMBER: _ClassVar[int]
    LITERAL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    glob: str
    ignore_case: bool
    literal: bool
    context: int
    limit: int
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., glob: _Optional[str] = ..., ignore_case: _Optional[bool] = ..., literal: _Optional[bool] = ..., context: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class PiGrepExecError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiGrepExecResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiGrepExecSuccess
    error: PiGrepExecError
    def __init__(self, success: _Optional[_Union[PiGrepExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiGrepExecError, _Mapping]] = ...) -> None: ...

class PiGrepExecSuccess(_message.Message):
    __slots__ = ("output", "truncation", "match_limit_reached", "lines_truncated")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
    LINES_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    match_limit_reached: int
    lines_truncated: bool
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., match_limit_reached: _Optional[int] = ..., lines_truncated: _Optional[bool] = ...) -> None: ...

class PiGrepToolArgs(_message.Message):
    __slots__ = ("pattern", "path", "glob", "ignore_case", "literal", "context", "limit")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    GLOB_FIELD_NUMBER: _ClassVar[int]
    IGNORE_CASE_FIELD_NUMBER: _ClassVar[int]
    LITERAL_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    path: str
    glob: str
    ignore_case: bool
    literal: bool
    context: int
    limit: int
    def __init__(self, pattern: _Optional[str] = ..., path: _Optional[str] = ..., glob: _Optional[str] = ..., ignore_case: _Optional[bool] = ..., literal: _Optional[bool] = ..., context: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class PiGrepToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiGrepToolArgs
    result: PiGrepToolResult
    def __init__(self, args: _Optional[_Union[PiGrepToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiGrepToolResult, _Mapping]] = ...) -> None: ...

class PiGrepToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiGrepToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiGrepToolSuccess
    error: PiGrepToolError
    def __init__(self, success: _Optional[_Union[PiGrepToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiGrepToolError, _Mapping]] = ...) -> None: ...

class PiGrepToolSuccess(_message.Message):
    __slots__ = ("output", "truncation", "match_limit_reached", "lines_truncated")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
    LINES_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    match_limit_reached: int
    lines_truncated: bool
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., match_limit_reached: _Optional[int] = ..., lines_truncated: _Optional[bool] = ...) -> None: ...

class PiLsExecArgs(_message.Message):
    __slots__ = ("path", "limit")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    path: str
    limit: int
    def __init__(self, path: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class PiLsExecError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiLsExecResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiLsExecSuccess
    error: PiLsExecError
    def __init__(self, success: _Optional[_Union[PiLsExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiLsExecError, _Mapping]] = ...) -> None: ...

class PiLsExecSuccess(_message.Message):
    __slots__ = ("output", "truncation", "entry_limit_reached")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    entry_limit_reached: int
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., entry_limit_reached: _Optional[int] = ...) -> None: ...

class PiLsToolArgs(_message.Message):
    __slots__ = ("path", "limit")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    path: str
    limit: int
    def __init__(self, path: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class PiLsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiLsToolArgs
    result: PiLsToolResult
    def __init__(self, args: _Optional[_Union[PiLsToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiLsToolResult, _Mapping]] = ...) -> None: ...

class PiLsToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiLsToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiLsToolSuccess
    error: PiLsToolError
    def __init__(self, success: _Optional[_Union[PiLsToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiLsToolError, _Mapping]] = ...) -> None: ...

class PiLsToolSuccess(_message.Message):
    __slots__ = ("output", "truncation", "entry_limit_reached")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    entry_limit_reached: int
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ..., entry_limit_reached: _Optional[int] = ...) -> None: ...

class PiReadExecArgs(_message.Message):
    __slots__ = ("path", "offset", "limit")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    limit: int
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class PiReadExecError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiReadExecResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiReadExecSuccess
    error: PiReadExecError
    def __init__(self, success: _Optional[_Union[PiReadExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiReadExecError, _Mapping]] = ...) -> None: ...

class PiReadExecSuccess(_message.Message):
    __slots__ = ("output", "truncation")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ...) -> None: ...

class PiReadToolArgs(_message.Message):
    __slots__ = ("path", "offset", "limit")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    limit: int
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class PiReadToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiReadToolArgs
    result: PiReadToolResult
    def __init__(self, args: _Optional[_Union[PiReadToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiReadToolResult, _Mapping]] = ...) -> None: ...

class PiReadToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiReadToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: PiReadToolSuccess
    error: PiReadToolError
    def __init__(self, success: _Optional[_Union[PiReadToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiReadToolError, _Mapping]] = ...) -> None: ...

class PiReadToolSuccess(_message.Message):
    __slots__ = ("output", "truncation")
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATION_FIELD_NUMBER: _ClassVar[int]
    output: str
    truncation: PiTruncation
    def __init__(self, output: _Optional[str] = ..., truncation: _Optional[_Union[PiTruncation, _Mapping]] = ...) -> None: ...

class PiTruncation(_message.Message):
    __slots__ = ("truncated", "truncated_by", "total_lines", "output_lines", "output_bytes", "max_lines", "max_bytes", "first_line_exceeds_limit", "last_line_partial")
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_BY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LINES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LINES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_LINES_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    FIRST_LINE_EXCEEDS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LAST_LINE_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    truncated: bool
    truncated_by: str
    total_lines: int
    output_lines: int
    output_bytes: int
    max_lines: int
    max_bytes: int
    first_line_exceeds_limit: bool
    last_line_partial: bool
    def __init__(self, truncated: _Optional[bool] = ..., truncated_by: _Optional[str] = ..., total_lines: _Optional[int] = ..., output_lines: _Optional[int] = ..., output_bytes: _Optional[int] = ..., max_lines: _Optional[int] = ..., max_bytes: _Optional[int] = ..., first_line_exceeds_limit: _Optional[bool] = ..., last_line_partial: _Optional[bool] = ...) -> None: ...

class PiWriteExecArgs(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    def __init__(self, path: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class PiWriteExecError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiWriteExecRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class PiWriteExecResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: PiWriteExecSuccess
    error: PiWriteExecError
    rejected: PiWriteExecRejected
    def __init__(self, success: _Optional[_Union[PiWriteExecSuccess, _Mapping]] = ..., error: _Optional[_Union[PiWriteExecError, _Mapping]] = ..., rejected: _Optional[_Union[PiWriteExecRejected, _Mapping]] = ...) -> None: ...

class PiWriteExecSuccess(_message.Message):
    __slots__ = ("output",)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: str
    def __init__(self, output: _Optional[str] = ...) -> None: ...

class PiWriteToolArgs(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    def __init__(self, path: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class PiWriteToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PiWriteToolArgs
    result: PiWriteToolResult
    def __init__(self, args: _Optional[_Union[PiWriteToolArgs, _Mapping]] = ..., result: _Optional[_Union[PiWriteToolResult, _Mapping]] = ...) -> None: ...

class PiWriteToolError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PiWriteToolRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class PiWriteToolResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: PiWriteToolSuccess
    error: PiWriteToolError
    rejected: PiWriteToolRejected
    def __init__(self, success: _Optional[_Union[PiWriteToolSuccess, _Mapping]] = ..., error: _Optional[_Union[PiWriteToolError, _Mapping]] = ..., rejected: _Optional[_Union[PiWriteToolRejected, _Mapping]] = ...) -> None: ...

class PiWriteToolSuccess(_message.Message):
    __slots__ = ("output",)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: str
    def __init__(self, output: _Optional[str] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PlanRegistryEntry(_message.Message):
    __slots__ = ("id", "path")
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: str
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("line", "column")
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    line: int
    column: int
    def __init__(self, line: _Optional[int] = ..., column: _Optional[int] = ...) -> None: ...

class PostCommentAction(_message.Message):
    __slots__ = ("pr_url", "branch_name", "body", "repo_url", "in_reply_to", "path", "line", "start_line", "side", "reply_to_reference")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    IN_REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    branch_name: str
    body: str
    repo_url: str
    in_reply_to: int
    path: str
    line: int
    start_line: int
    side: str
    reply_to_reference: str
    def __init__(self, pr_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., body: _Optional[str] = ..., repo_url: _Optional[str] = ..., in_reply_to: _Optional[int] = ..., path: _Optional[str] = ..., line: _Optional[int] = ..., start_line: _Optional[int] = ..., side: _Optional[str] = ..., reply_to_reference: _Optional[str] = ...) -> None: ...

class PostRequestPromptUpdate(_message.Message):
    __slots__ = ("title", "message", "button_label", "button_url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    BUTTON_URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    message: str
    button_label: str
    button_url: str
    def __init__(self, title: _Optional[str] = ..., message: _Optional[str] = ..., button_label: _Optional[str] = ..., button_url: _Optional[str] = ...) -> None: ...

class PostToolUseFailureRequestQuery(_message.Message):
    __slots__ = ("tool_name", "tool_input", "error_message", "failure_type", "duration_ms", "tool_use_id", "is_interrupt", "conversation_id", "generation_id", "model", "model_id", "model_params")
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_INTERRUPT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    tool_input: _struct_pb2.Struct
    error_message: str
    failure_type: str
    duration_ms: int
    tool_use_id: str
    is_interrupt: bool
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, tool_name: _Optional[str] = ..., tool_input: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error_message: _Optional[str] = ..., failure_type: _Optional[str] = ..., duration_ms: _Optional[int] = ..., tool_use_id: _Optional[str] = ..., is_interrupt: _Optional[bool] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class PostToolUseFailureRequestResponse(_message.Message):
    __slots__ = ("additional_context",)
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    additional_context: str
    def __init__(self, additional_context: _Optional[str] = ...) -> None: ...

class PostToolUseRequestQuery(_message.Message):
    __slots__ = ("tool_name", "tool_input", "tool_output", "duration_ms", "tool_use_id", "cwd", "conversation_id", "generation_id", "model", "model_id", "model_params")
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    tool_input: _struct_pb2.Struct
    tool_output: str
    duration_ms: int
    tool_use_id: str
    cwd: str
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, tool_name: _Optional[str] = ..., tool_input: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tool_output: _Optional[str] = ..., duration_ms: _Optional[int] = ..., tool_use_id: _Optional[str] = ..., cwd: _Optional[str] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class PostToolUseRequestResponse(_message.Message):
    __slots__ = ("additional_context",)
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    additional_context: str
    def __init__(self, additional_context: _Optional[str] = ...) -> None: ...

class PrManagementArgs(_message.Message):
    __slots__ = ("tool_call_id", "create_pr", "update_pr", "post_comment", "resolve_comment", "get_ci_status", "set_pr_status")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_PR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PR_FIELD_NUMBER: _ClassVar[int]
    POST_COMMENT_FIELD_NUMBER: _ClassVar[int]
    RESOLVE_COMMENT_FIELD_NUMBER: _ClassVar[int]
    GET_CI_STATUS_FIELD_NUMBER: _ClassVar[int]
    SET_PR_STATUS_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    create_pr: CreatePrAction
    update_pr: UpdatePrAction
    post_comment: PostCommentAction
    resolve_comment: ResolveCommentAction
    get_ci_status: GetCiStatusAction
    set_pr_status: SetPrStatusAction
    def __init__(self, tool_call_id: _Optional[str] = ..., create_pr: _Optional[_Union[CreatePrAction, _Mapping]] = ..., update_pr: _Optional[_Union[UpdatePrAction, _Mapping]] = ..., post_comment: _Optional[_Union[PostCommentAction, _Mapping]] = ..., resolve_comment: _Optional[_Union[ResolveCommentAction, _Mapping]] = ..., get_ci_status: _Optional[_Union[GetCiStatusAction, _Mapping]] = ..., set_pr_status: _Optional[_Union[SetPrStatusAction, _Mapping]] = ...) -> None: ...

class PrManagementError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class PrManagementNeedsConfirmation(_message.Message):
    __slots__ = ("message", "discovered_pr_url", "discovered_pr_number", "discovered_pr_title", "branch_name")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_PR_URL_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_PR_TITLE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    message: str
    discovered_pr_url: str
    discovered_pr_number: int
    discovered_pr_title: str
    branch_name: str
    def __init__(self, message: _Optional[str] = ..., discovered_pr_url: _Optional[str] = ..., discovered_pr_number: _Optional[int] = ..., discovered_pr_title: _Optional[str] = ..., branch_name: _Optional[str] = ...) -> None: ...

class PrManagementRegistered(_message.Message):
    __slots__ = ("message", "title", "body", "base_branch", "draft", "branch_name")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    message: str
    title: str
    body: str
    base_branch: str
    draft: bool
    branch_name: str
    def __init__(self, message: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., base_branch: _Optional[str] = ..., draft: _Optional[bool] = ..., branch_name: _Optional[str] = ...) -> None: ...

class PrManagementRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class PrManagementRequestQuery(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: PrManagementArgs
    def __init__(self, args: _Optional[_Union[PrManagementArgs, _Mapping]] = ...) -> None: ...

class PrManagementResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "registered", "needs_confirmation")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_FIELD_NUMBER: _ClassVar[int]
    NEEDS_CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
    success: PrManagementSuccess
    error: PrManagementError
    rejected: PrManagementRejected
    registered: PrManagementRegistered
    needs_confirmation: PrManagementNeedsConfirmation
    def __init__(self, success: _Optional[_Union[PrManagementSuccess, _Mapping]] = ..., error: _Optional[_Union[PrManagementError, _Mapping]] = ..., rejected: _Optional[_Union[PrManagementRejected, _Mapping]] = ..., registered: _Optional[_Union[PrManagementRegistered, _Mapping]] = ..., needs_confirmation: _Optional[_Union[PrManagementNeedsConfirmation, _Mapping]] = ...) -> None: ...

class PrManagementSuccess(_message.Message):
    __slots__ = ("pr_url", "pr_number", "message")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    pr_number: int
    message: str
    def __init__(self, pr_url: _Optional[str] = ..., pr_number: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class PrManagementToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: PrManagementArgs
    result: PrManagementResult
    def __init__(self, args: _Optional[_Union[PrManagementArgs, _Mapping]] = ..., result: _Optional[_Union[PrManagementResult, _Mapping]] = ...) -> None: ...

class PreCompactRequestQuery(_message.Message):
    __slots__ = ("trigger", "context_usage_percent", "context_tokens", "context_window_size", "message_count", "messages_to_compact", "is_first_compaction", "conversation_id", "generation_id", "model", "model_id", "model_params")
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_TO_COMPACT_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_COMPACTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    trigger: str
    context_usage_percent: float
    context_tokens: int
    context_window_size: int
    message_count: int
    messages_to_compact: int
    is_first_compaction: bool
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, trigger: _Optional[str] = ..., context_usage_percent: _Optional[float] = ..., context_tokens: _Optional[int] = ..., context_window_size: _Optional[int] = ..., message_count: _Optional[int] = ..., messages_to_compact: _Optional[int] = ..., is_first_compaction: _Optional[bool] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class PreCompactRequestResponse(_message.Message):
    __slots__ = ("user_message",)
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user_message: str
    def __init__(self, user_message: _Optional[str] = ...) -> None: ...

class PreFetchedBlob(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    value: bytes
    def __init__(self, id: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class PreToolUseRequestQuery(_message.Message):
    __slots__ = ("tool_name", "tool_input", "tool_use_id", "cwd", "conversation_id", "generation_id", "model", "model_id", "model_params")
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_USE_ID_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    tool_input: _struct_pb2.Struct
    tool_use_id: str
    cwd: str
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, tool_name: _Optional[str] = ..., tool_input: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., tool_use_id: _Optional[str] = ..., cwd: _Optional[str] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class PreToolUseRequestResponse(_message.Message):
    __slots__ = ("permission", "user_message", "agent_message", "updated_input", "additional_context")
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AGENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_INPUT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    permission: str
    user_message: str
    agent_message: str
    updated_input: str
    additional_context: str
    def __init__(self, permission: _Optional[str] = ..., user_message: _Optional[str] = ..., agent_message: _Optional[str] = ..., updated_input: _Optional[str] = ..., additional_context: _Optional[str] = ...) -> None: ...

class PrecomputedHumanChange(_message.Message):
    __slots__ = ("path", "rendered_diffs", "is_new_file", "is_deleted_file")
    PATH_FIELD_NUMBER: _ClassVar[int]
    RENDERED_DIFFS_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FILE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FILE_FIELD_NUMBER: _ClassVar[int]
    path: str
    rendered_diffs: _containers.RepeatedCompositeFieldContainer[PrecomputedHumanChangeRenderedDiff]
    is_new_file: bool
    is_deleted_file: bool
    def __init__(self, path: _Optional[str] = ..., rendered_diffs: _Optional[_Iterable[_Union[PrecomputedHumanChangeRenderedDiff, _Mapping]]] = ..., is_new_file: _Optional[bool] = ..., is_deleted_file: _Optional[bool] = ...) -> None: ...

class PrecomputedHumanChangeRenderedDiff(_message.Message):
    __slots__ = ("start_line_number", "end_line_number_exclusive", "before_context_lines", "removed_lines", "added_lines", "after_context_lines")
    START_LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    END_LINE_NUMBER_EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_CONTEXT_LINES_FIELD_NUMBER: _ClassVar[int]
    REMOVED_LINES_FIELD_NUMBER: _ClassVar[int]
    ADDED_LINES_FIELD_NUMBER: _ClassVar[int]
    AFTER_CONTEXT_LINES_FIELD_NUMBER: _ClassVar[int]
    start_line_number: int
    end_line_number_exclusive: int
    before_context_lines: _containers.RepeatedScalarFieldContainer[str]
    removed_lines: _containers.RepeatedScalarFieldContainer[str]
    added_lines: _containers.RepeatedScalarFieldContainer[str]
    after_context_lines: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, start_line_number: _Optional[int] = ..., end_line_number_exclusive: _Optional[int] = ..., before_context_lines: _Optional[_Iterable[str]] = ..., removed_lines: _Optional[_Iterable[str]] = ..., added_lines: _Optional[_Iterable[str]] = ..., after_context_lines: _Optional[_Iterable[str]] = ...) -> None: ...

class PreparedTaskSubagent(_message.Message):
    __slots__ = ("subagent_id", "subagent_type_name", "subagent_type", "analytics_subagent_type", "resolved_model_id", "effective_readonly", "use_ask_mode_for_subagent", "conversation_state", "initial_action", "initial_turns_count", "subagent_request_id", "tool_call_id", "is_resume", "parent_request_id", "root_parent_request_id", "task_prompt", "task_description", "selected_context", "plugin", "marketplace", "parent_model_name", "raw_args", "subagent_credentials", "result_suffix", "enable_execute_hook_exec", "configured_steps", "readonly_shell_enabled", "tool_name", "prepared_timestamp_unix_ms", "plugin_id", "marketplace_id", "subagent_source", "cloud_subagent_bc_id", "provider_tool_name")
    SUBAGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_READONLY_FIELD_NUMBER: _ClassVar[int]
    USE_ASK_MODE_FOR_SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ACTION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_TURNS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RESUME_FIELD_NUMBER: _ClassVar[int]
    PARENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PARENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_PROMPT_FIELD_NUMBER: _ClassVar[int]
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SELECTED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
    PARENT_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    RAW_ARGS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    RESULT_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXECUTE_HOOK_EXEC_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_STEPS_FIELD_NUMBER: _ClassVar[int]
    READONLY_SHELL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    PREPARED_TIMESTAMP_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    MARKETPLACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SUBAGENT_BC_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    subagent_id: str
    subagent_type_name: str
    subagent_type: SubagentType
    analytics_subagent_type: str
    resolved_model_id: str
    effective_readonly: bool
    use_ask_mode_for_subagent: bool
    conversation_state: ConversationStateStructure
    initial_action: ConversationAction
    initial_turns_count: int
    subagent_request_id: str
    tool_call_id: str
    is_resume: bool
    parent_request_id: str
    root_parent_request_id: str
    task_prompt: str
    task_description: str
    selected_context: SelectedContext
    plugin: str
    marketplace: str
    parent_model_name: str
    raw_args: TaskToolCallArgsProto
    subagent_credentials: SubagentCredentials
    result_suffix: str
    enable_execute_hook_exec: bool
    configured_steps: _containers.RepeatedScalarFieldContainer[str]
    readonly_shell_enabled: bool
    tool_name: str
    prepared_timestamp_unix_ms: int
    plugin_id: str
    marketplace_id: str
    subagent_source: str
    cloud_subagent_bc_id: str
    provider_tool_name: str
    def __init__(self, subagent_id: _Optional[str] = ..., subagent_type_name: _Optional[str] = ..., subagent_type: _Optional[_Union[SubagentType, _Mapping]] = ..., analytics_subagent_type: _Optional[str] = ..., resolved_model_id: _Optional[str] = ..., effective_readonly: _Optional[bool] = ..., use_ask_mode_for_subagent: _Optional[bool] = ..., conversation_state: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., initial_action: _Optional[_Union[ConversationAction, _Mapping]] = ..., initial_turns_count: _Optional[int] = ..., subagent_request_id: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., is_resume: _Optional[bool] = ..., parent_request_id: _Optional[str] = ..., root_parent_request_id: _Optional[str] = ..., task_prompt: _Optional[str] = ..., task_description: _Optional[str] = ..., selected_context: _Optional[_Union[SelectedContext, _Mapping]] = ..., plugin: _Optional[str] = ..., marketplace: _Optional[str] = ..., parent_model_name: _Optional[str] = ..., raw_args: _Optional[_Union[TaskToolCallArgsProto, _Mapping]] = ..., subagent_credentials: _Optional[_Union[SubagentCredentials, _Mapping]] = ..., result_suffix: _Optional[str] = ..., enable_execute_hook_exec: _Optional[bool] = ..., configured_steps: _Optional[_Iterable[str]] = ..., readonly_shell_enabled: _Optional[bool] = ..., tool_name: _Optional[str] = ..., prepared_timestamp_unix_ms: _Optional[int] = ..., plugin_id: _Optional[str] = ..., marketplace_id: _Optional[str] = ..., subagent_source: _Optional[str] = ..., cloud_subagent_bc_id: _Optional[str] = ..., provider_tool_name: _Optional[str] = ...) -> None: ...

class PrewarmRequest(_message.Message):
    __slots__ = ("model_details", "requested_model", "conversation_id", "conversation_state", "mcp_tools", "mcp_file_system_options", "best_of_n_group_id", "try_use_best_of_n_promotion", "custom_system_prompt", "suggest_next_prompt", "subagent_type_name", "exclude_workspace_context", "harness", "selected_subagent_models", "selected_subagent_model_details", "conversation_group_id", "pre_fetched_blobs", "client_supports_inline_images", "subagent_model_overrides", "can_create_cloud_subagents", "suppress_subagent_progress_update_tool", "client_supports_send_to_user", "computer_use_coordinate_mode", "agent_session_id", "client_supports_prompt_context_usage_rpc")
    MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_MODEL_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    MCP_TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_FILE_SYSTEM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BEST_OF_N_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TRY_USE_BEST_OF_N_PROMOTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SYSTEM_PROMPT_FIELD_NUMBER: _ClassVar[int]
    SUGGEST_NEXT_PROMPT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_WORKSPACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    HARNESS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUBAGENT_MODELS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUBAGENT_MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_FETCHED_BLOBS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPORTS_INLINE_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_MODEL_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_CLOUD_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_SUBAGENT_PROGRESS_UPDATE_TOOL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPORTS_SEND_TO_USER_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_COORDINATE_MODE_FIELD_NUMBER: _ClassVar[int]
    AGENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPORTS_PROMPT_CONTEXT_USAGE_RPC_FIELD_NUMBER: _ClassVar[int]
    model_details: ModelDetails
    requested_model: RequestedModel
    conversation_id: str
    conversation_state: ConversationStateStructure
    mcp_tools: McpTools
    mcp_file_system_options: McpFileSystemOptions
    best_of_n_group_id: str
    try_use_best_of_n_promotion: bool
    custom_system_prompt: str
    suggest_next_prompt: bool
    subagent_type_name: str
    exclude_workspace_context: bool
    harness: str
    selected_subagent_models: _containers.RepeatedCompositeFieldContainer[RequestedModel]
    selected_subagent_model_details: _containers.RepeatedCompositeFieldContainer[ModelDetails]
    conversation_group_id: str
    pre_fetched_blobs: _containers.RepeatedCompositeFieldContainer[PreFetchedBlob]
    client_supports_inline_images: bool
    subagent_model_overrides: _containers.RepeatedCompositeFieldContainer[SubagentModelOverride]
    can_create_cloud_subagents: bool
    suppress_subagent_progress_update_tool: bool
    client_supports_send_to_user: bool
    computer_use_coordinate_mode: str
    agent_session_id: str
    client_supports_prompt_context_usage_rpc: bool
    def __init__(self, model_details: _Optional[_Union[ModelDetails, _Mapping]] = ..., requested_model: _Optional[_Union[RequestedModel, _Mapping]] = ..., conversation_id: _Optional[str] = ..., conversation_state: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., mcp_tools: _Optional[_Union[McpTools, _Mapping]] = ..., mcp_file_system_options: _Optional[_Union[McpFileSystemOptions, _Mapping]] = ..., best_of_n_group_id: _Optional[str] = ..., try_use_best_of_n_promotion: _Optional[bool] = ..., custom_system_prompt: _Optional[str] = ..., suggest_next_prompt: _Optional[bool] = ..., subagent_type_name: _Optional[str] = ..., exclude_workspace_context: _Optional[bool] = ..., harness: _Optional[str] = ..., selected_subagent_models: _Optional[_Iterable[_Union[RequestedModel, _Mapping]]] = ..., selected_subagent_model_details: _Optional[_Iterable[_Union[ModelDetails, _Mapping]]] = ..., conversation_group_id: _Optional[str] = ..., pre_fetched_blobs: _Optional[_Iterable[_Union[PreFetchedBlob, _Mapping]]] = ..., client_supports_inline_images: _Optional[bool] = ..., subagent_model_overrides: _Optional[_Iterable[_Union[SubagentModelOverride, _Mapping]]] = ..., can_create_cloud_subagents: _Optional[bool] = ..., suppress_subagent_progress_update_tool: _Optional[bool] = ..., client_supports_send_to_user: _Optional[bool] = ..., computer_use_coordinate_mode: _Optional[str] = ..., agent_session_id: _Optional[str] = ..., client_supports_prompt_context_usage_rpc: _Optional[bool] = ...) -> None: ...

class Process(_message.Message):
    __slots__ = ("shell", "args")
    SHELL_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    shell: str
    args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, shell: _Optional[str] = ..., args: _Optional[_Iterable[str]] = ...) -> None: ...

class ProjectDetails(_message.Message):
    __slots__ = ("name", "subagent", "side_chat")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    SIDE_CHAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    subagent: ProjectSubagentDetails
    side_chat: ProjectSideChatDetails
    def __init__(self, name: _Optional[str] = ..., subagent: _Optional[_Union[ProjectSubagentDetails, _Mapping]] = ..., side_chat: _Optional[_Union[ProjectSideChatDetails, _Mapping]] = ...) -> None: ...

class ProjectSideChatDetails(_message.Message):
    __slots__ = ("store_dir",)
    STORE_DIR_FIELD_NUMBER: _ClassVar[int]
    store_dir: str
    def __init__(self, store_dir: _Optional[str] = ...) -> None: ...

class ProjectSubagentDetails(_message.Message):
    __slots__ = ("store_dir",)
    STORE_DIR_FIELD_NUMBER: _ClassVar[int]
    store_dir: str
    def __init__(self, store_dir: _Optional[str] = ...) -> None: ...

class PromptContextNode(_message.Message):
    __slots__ = ("id", "parent_id", "kind", "label", "category_id", "estimated_tokens", "character_count", "content_available", "source", "inline_content")
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INLINE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    parent_id: str
    kind: str
    label: str
    category_id: str
    estimated_tokens: int
    character_count: int
    content_available: bool
    source: PromptContextSourceRef
    inline_content: str
    def __init__(self, id: _Optional[str] = ..., parent_id: _Optional[str] = ..., kind: _Optional[str] = ..., label: _Optional[str] = ..., category_id: _Optional[str] = ..., estimated_tokens: _Optional[int] = ..., character_count: _Optional[int] = ..., content_available: _Optional[bool] = ..., source: _Optional[_Union[PromptContextSourceRef, _Mapping]] = ..., inline_content: _Optional[str] = ...) -> None: ...

class PromptContextSourceRef(_message.Message):
    __slots__ = ("source_type", "message_index", "content_path", "start_offset", "end_offset")
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PATH_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    source_type: str
    message_index: int
    content_path: str
    start_offset: int
    end_offset: int
    def __init__(self, source_type: _Optional[str] = ..., message_index: _Optional[int] = ..., content_path: _Optional[str] = ..., start_offset: _Optional[int] = ..., end_offset: _Optional[int] = ...) -> None: ...

class PromptContextUsageSnapshot(_message.Message):
    __slots__ = ("prompt_context_usage_tree", "root_prompt_messages_json")
    PROMPT_CONTEXT_USAGE_TREE_FIELD_NUMBER: _ClassVar[int]
    ROOT_PROMPT_MESSAGES_JSON_FIELD_NUMBER: _ClassVar[int]
    prompt_context_usage_tree: PromptContextUsageTree
    root_prompt_messages_json: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, prompt_context_usage_tree: _Optional[_Union[PromptContextUsageTree, _Mapping]] = ..., root_prompt_messages_json: _Optional[_Iterable[bytes]] = ...) -> None: ...

class PromptContextUsageTree(_message.Message):
    __slots__ = ("schema_version", "nodes")
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    schema_version: int
    nodes: _containers.RepeatedCompositeFieldContainer[PromptContextNode]
    def __init__(self, schema_version: _Optional[int] = ..., nodes: _Optional[_Iterable[_Union[PromptContextNode, _Mapping]]] = ...) -> None: ...

class PromptSuggestionUpdate(_message.Message):
    __slots__ = ("suggestion",)
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    suggestion: str
    def __init__(self, suggestion: _Optional[str] = ...) -> None: ...

class PromptTokenBreakdownCategory(_message.Message):
    __slots__ = ("id", "label", "estimated_tokens", "character_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    estimated_tokens: int
    character_count: int
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., estimated_tokens: _Optional[int] = ..., character_count: _Optional[int] = ...) -> None: ...

class PromptTokenBreakdownSnapshot(_message.Message):
    __slots__ = ("total_used_tokens", "max_tokens", "categories")
    TOTAL_USED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    total_used_tokens: int
    max_tokens: int
    categories: _containers.RepeatedCompositeFieldContainer[PromptTokenBreakdownCategory]
    def __init__(self, total_used_tokens: _Optional[int] = ..., max_tokens: _Optional[int] = ..., categories: _Optional[_Iterable[_Union[PromptTokenBreakdownCategory, _Mapping]]] = ...) -> None: ...

class PromptUploadRef(_message.Message):
    __slots__ = ("upload_id",)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class PtyData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class PtyEvent(_message.Message):
    __slots__ = ("event_id", "pty_data", "pty_exited")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PTY_DATA_FIELD_NUMBER: _ClassVar[int]
    PTY_EXITED_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    pty_data: PtyData
    pty_exited: PtyExited
    def __init__(self, event_id: _Optional[str] = ..., pty_data: _Optional[_Union[PtyData, _Mapping]] = ..., pty_exited: _Optional[_Union[PtyExited, _Mapping]] = ...) -> None: ...

class PtyExited(_message.Message):
    __slots__ = ("exit_code", "signal")
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    exit_code: int
    signal: int
    def __init__(self, exit_code: _Optional[int] = ..., signal: _Optional[int] = ...) -> None: ...

class PtyInfo(_message.Message):
    __slots__ = ("pty_id", "shell", "cwd", "cols", "rows", "pid", "process_args")
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ARGS_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    shell: str
    cwd: str
    cols: int
    rows: int
    pid: int
    process_args: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, pty_id: _Optional[str] = ..., shell: _Optional[str] = ..., cwd: _Optional[str] = ..., cols: _Optional[int] = ..., rows: _Optional[int] = ..., pid: _Optional[int] = ..., process_args: _Optional[_Iterable[str]] = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: Position
    end: Position
    def __init__(self, start: _Optional[_Union[Position, _Mapping]] = ..., end: _Optional[_Union[Position, _Mapping]] = ...) -> None: ...

class ReadArgs(_message.Message):
    __slots__ = ("path", "tool_call_id", "offset", "limit", "encoding_hint")
    PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENCODING_HINT_FIELD_NUMBER: _ClassVar[int]
    path: str
    tool_call_id: str
    offset: int
    limit: int
    encoding_hint: str
    def __init__(self, path: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., encoding_hint: _Optional[str] = ...) -> None: ...

class ReadBinaryFileRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReadBinaryFileResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    def __init__(self, content: _Optional[bytes] = ...) -> None: ...

class ReadError(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class ReadFileNotFound(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReadInvalidFile(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ReadLintsToolArgs(_message.Message):
    __slots__ = ("paths",)
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, paths: _Optional[_Iterable[str]] = ...) -> None: ...

class ReadLintsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReadLintsToolArgs
    result: ReadLintsToolResult
    def __init__(self, args: _Optional[_Union[ReadLintsToolArgs, _Mapping]] = ..., result: _Optional[_Union[ReadLintsToolResult, _Mapping]] = ...) -> None: ...

class ReadLintsToolError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class ReadLintsToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ReadLintsToolSuccess
    error: ReadLintsToolError
    def __init__(self, success: _Optional[_Union[ReadLintsToolSuccess, _Mapping]] = ..., error: _Optional[_Union[ReadLintsToolError, _Mapping]] = ...) -> None: ...

class ReadLintsToolSuccess(_message.Message):
    __slots__ = ("file_diagnostics", "total_files", "total_diagnostics")
    FILE_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    file_diagnostics: _containers.RepeatedCompositeFieldContainer[FileDiagnostics]
    total_files: int
    total_diagnostics: int
    def __init__(self, file_diagnostics: _Optional[_Iterable[_Union[FileDiagnostics, _Mapping]]] = ..., total_files: _Optional[int] = ..., total_diagnostics: _Optional[int] = ...) -> None: ...

class ReadMcpResourceError(_message.Message):
    __slots__ = ("uri", "error")
    URI_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    uri: str
    error: str
    def __init__(self, uri: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class ReadMcpResourceExecArgs(_message.Message):
    __slots__ = ("server", "uri", "download_path", "tool_call_id", "smart_mode_approval")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    server: str
    uri: str
    download_path: str
    tool_call_id: str
    smart_mode_approval: SmartModeApproval
    def __init__(self, server: _Optional[str] = ..., uri: _Optional[str] = ..., download_path: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., smart_mode_approval: _Optional[_Union[SmartModeApproval, _Mapping]] = ...) -> None: ...

class ReadMcpResourceExecResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "not_found")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    success: ReadMcpResourceSuccess
    error: ReadMcpResourceError
    rejected: ReadMcpResourceRejected
    not_found: ReadMcpResourceNotFound
    def __init__(self, success: _Optional[_Union[ReadMcpResourceSuccess, _Mapping]] = ..., error: _Optional[_Union[ReadMcpResourceError, _Mapping]] = ..., rejected: _Optional[_Union[ReadMcpResourceRejected, _Mapping]] = ..., not_found: _Optional[_Union[ReadMcpResourceNotFound, _Mapping]] = ...) -> None: ...

class ReadMcpResourceNotFound(_message.Message):
    __slots__ = ("uri",)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str
    def __init__(self, uri: _Optional[str] = ...) -> None: ...

class ReadMcpResourceRejected(_message.Message):
    __slots__ = ("uri", "reason")
    URI_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    uri: str
    reason: str
    def __init__(self, uri: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ReadMcpResourceSuccess(_message.Message):
    __slots__ = ("uri", "name", "description", "mime_type", "annotations", "download_path", "output_location", "text", "blob")
    class AnnotationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    URI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BLOB_FIELD_NUMBER: _ClassVar[int]
    uri: str
    name: str
    description: str
    mime_type: str
    annotations: _containers.ScalarMap[str, str]
    download_path: str
    output_location: OutputLocation
    text: str
    blob: bytes
    def __init__(self, uri: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., mime_type: _Optional[str] = ..., annotations: _Optional[_Mapping[str, str]] = ..., download_path: _Optional[str] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ..., text: _Optional[str] = ..., blob: _Optional[bytes] = ...) -> None: ...

class ReadMcpResourceToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReadMcpResourceExecArgs
    result: ReadMcpResourceExecResult
    def __init__(self, args: _Optional[_Union[ReadMcpResourceExecArgs, _Mapping]] = ..., result: _Optional[_Union[ReadMcpResourceExecResult, _Mapping]] = ...) -> None: ...

class ReadPermissionDenied(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReadRange(_message.Message):
    __slots__ = ("start_line", "end_line")
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    END_LINE_FIELD_NUMBER: _ClassVar[int]
    start_line: int
    end_line: int
    def __init__(self, start_line: _Optional[int] = ..., end_line: _Optional[int] = ...) -> None: ...

class ReadRejected(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ReadResult(_message.Message):
    __slots__ = ("success", "error", "rejected", "file_not_found", "permission_denied", "invalid_file")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    FILE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    INVALID_FILE_FIELD_NUMBER: _ClassVar[int]
    success: ReadSuccess
    error: ReadError
    rejected: ReadRejected
    file_not_found: ReadFileNotFound
    permission_denied: ReadPermissionDenied
    invalid_file: ReadInvalidFile
    def __init__(self, success: _Optional[_Union[ReadSuccess, _Mapping]] = ..., error: _Optional[_Union[ReadError, _Mapping]] = ..., rejected: _Optional[_Union[ReadRejected, _Mapping]] = ..., file_not_found: _Optional[_Union[ReadFileNotFound, _Mapping]] = ..., permission_denied: _Optional[_Union[ReadPermissionDenied, _Mapping]] = ..., invalid_file: _Optional[_Union[ReadInvalidFile, _Mapping]] = ...) -> None: ...

class ReadSuccess(_message.Message):
    __slots__ = ("path", "total_lines", "file_size", "truncated", "output_blob_id", "range_applied", "content", "data")
    PATH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LINES_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    RANGE_APPLIED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    path: str
    total_lines: int
    file_size: int
    truncated: bool
    output_blob_id: bytes
    range_applied: bool
    content: str
    data: bytes
    def __init__(self, path: _Optional[str] = ..., total_lines: _Optional[int] = ..., file_size: _Optional[int] = ..., truncated: _Optional[bool] = ..., output_blob_id: _Optional[bytes] = ..., range_applied: _Optional[bool] = ..., content: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class ReadTextFileRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class ReadTextFileResponse(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class ReadTodosArgs(_message.Message):
    __slots__ = ("status_filter", "id_filter")
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    status_filter: _containers.RepeatedScalarFieldContainer[TodoStatus]
    id_filter: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status_filter: _Optional[_Iterable[_Union[TodoStatus, str]]] = ..., id_filter: _Optional[_Iterable[str]] = ...) -> None: ...

class ReadTodosError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ReadTodosResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ReadTodosSuccess
    error: ReadTodosError
    def __init__(self, success: _Optional[_Union[ReadTodosSuccess, _Mapping]] = ..., error: _Optional[_Union[ReadTodosError, _Mapping]] = ...) -> None: ...

class ReadTodosSuccess(_message.Message):
    __slots__ = ("todos", "total_count")
    TODOS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    total_count: int
    def __init__(self, todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class ReadTodosToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReadTodosArgs
    result: ReadTodosResult
    def __init__(self, args: _Optional[_Union[ReadTodosArgs, _Mapping]] = ..., result: _Optional[_Union[ReadTodosResult, _Mapping]] = ...) -> None: ...

class ReadToolArgs(_message.Message):
    __slots__ = ("path", "offset", "limit", "include_line_numbers")
    PATH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LINE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    path: str
    offset: int
    limit: int
    include_line_numbers: bool
    def __init__(self, path: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ..., include_line_numbers: _Optional[bool] = ...) -> None: ...

class ReadToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReadToolArgs
    result: ReadToolResult
    def __init__(self, args: _Optional[_Union[ReadToolArgs, _Mapping]] = ..., result: _Optional[_Union[ReadToolResult, _Mapping]] = ...) -> None: ...

class ReadToolError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class ReadToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ReadToolSuccess
    error: ReadToolError
    def __init__(self, success: _Optional[_Union[ReadToolSuccess, _Mapping]] = ..., error: _Optional[_Union[ReadToolError, _Mapping]] = ...) -> None: ...

class ReadToolSuccess(_message.Message):
    __slots__ = ("is_empty", "exceeded_limit", "total_lines", "file_size", "path", "read_range", "include_line_numbers", "related_cursor_rule_paths", "related_cursor_rules", "content", "data", "data_blob_id", "content_blob_id")
    IS_EMPTY_FIELD_NUMBER: _ClassVar[int]
    EXCEEDED_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LINES_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    READ_RANGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LINE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    RELATED_CURSOR_RULE_PATHS_FIELD_NUMBER: _ClassVar[int]
    RELATED_CURSOR_RULES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DATA_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    is_empty: bool
    exceeded_limit: bool
    total_lines: int
    file_size: int
    path: str
    read_range: ReadRange
    include_line_numbers: bool
    related_cursor_rule_paths: _containers.RepeatedScalarFieldContainer[str]
    related_cursor_rules: _containers.RepeatedCompositeFieldContainer[CursorRule]
    content: str
    data: bytes
    data_blob_id: bytes
    content_blob_id: bytes
    def __init__(self, is_empty: _Optional[bool] = ..., exceeded_limit: _Optional[bool] = ..., total_lines: _Optional[int] = ..., file_size: _Optional[int] = ..., path: _Optional[str] = ..., read_range: _Optional[_Union[ReadRange, _Mapping]] = ..., include_line_numbers: _Optional[bool] = ..., related_cursor_rule_paths: _Optional[_Iterable[str]] = ..., related_cursor_rules: _Optional[_Iterable[_Union[CursorRule, _Mapping]]] = ..., content: _Optional[str] = ..., data: _Optional[bytes] = ..., data_blob_id: _Optional[bytes] = ..., content_blob_id: _Optional[bytes] = ...) -> None: ...

class RecentAgent(_message.Message):
    __slots__ = ("name", "path", "overview")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    overview: str
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., overview: _Optional[str] = ...) -> None: ...

class RecentAgentsContext(_message.Message):
    __slots__ = ("recent_agents",)
    RECENT_AGENTS_FIELD_NUMBER: _ClassVar[int]
    recent_agents: _containers.RepeatedCompositeFieldContainer[RecentAgent]
    def __init__(self, recent_agents: _Optional[_Iterable[_Union[RecentAgent, _Mapping]]] = ...) -> None: ...

class RecentlyAddedPlugin(_message.Message):
    __slots__ = ("display_name", "description", "skills", "subagents", "hooks", "rules", "commands", "mcp_servers")
    class CapabilityDescriptor(_message.Message):
        __slots__ = ("name", "description")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    MCP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    description: str
    skills: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    subagents: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    hooks: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    rules: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    commands: _containers.RepeatedCompositeFieldContainer[RecentlyAddedPlugin.CapabilityDescriptor]
    mcp_servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, display_name: _Optional[str] = ..., description: _Optional[str] = ..., skills: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., subagents: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., commands: _Optional[_Iterable[_Union[RecentlyAddedPlugin.CapabilityDescriptor, _Mapping]]] = ..., mcp_servers: _Optional[_Iterable[str]] = ...) -> None: ...

class RecordCiInvestigationFinding(_message.Message):
    __slots__ = ("check_name", "details_url", "tldr", "root_cause", "failing_signal", "suggested_next_step", "diff_relation", "diff_relation_evidence", "flake_assessment", "flake_evidence", "rerun_available", "rerun_evidence", "recommended_action", "recommended_action_evidence", "confidence")
    CHECK_NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    TLDR_FIELD_NUMBER: _ClassVar[int]
    ROOT_CAUSE_FIELD_NUMBER: _ClassVar[int]
    FAILING_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_NEXT_STEP_FIELD_NUMBER: _ClassVar[int]
    DIFF_RELATION_FIELD_NUMBER: _ClassVar[int]
    DIFF_RELATION_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    FLAKE_ASSESSMENT_FIELD_NUMBER: _ClassVar[int]
    FLAKE_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    RERUN_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    RERUN_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTION_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    check_name: str
    details_url: str
    tldr: str
    root_cause: str
    failing_signal: str
    suggested_next_step: str
    diff_relation: str
    diff_relation_evidence: str
    flake_assessment: str
    flake_evidence: str
    rerun_available: bool
    rerun_evidence: str
    recommended_action: str
    recommended_action_evidence: str
    confidence: str
    def __init__(self, check_name: _Optional[str] = ..., details_url: _Optional[str] = ..., tldr: _Optional[str] = ..., root_cause: _Optional[str] = ..., failing_signal: _Optional[str] = ..., suggested_next_step: _Optional[str] = ..., diff_relation: _Optional[str] = ..., diff_relation_evidence: _Optional[str] = ..., flake_assessment: _Optional[str] = ..., flake_evidence: _Optional[str] = ..., rerun_available: _Optional[bool] = ..., rerun_evidence: _Optional[str] = ..., recommended_action: _Optional[str] = ..., recommended_action_evidence: _Optional[str] = ..., confidence: _Optional[str] = ...) -> None: ...

class RecordCiInvestigationFindingsArgs(_message.Message):
    __slots__ = ("findings", "overall", "tool_call_id")
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    OVERALL_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    findings: _containers.RepeatedCompositeFieldContainer[RecordCiInvestigationFinding]
    overall: RecordCiInvestigationOverall
    tool_call_id: str
    def __init__(self, findings: _Optional[_Iterable[_Union[RecordCiInvestigationFinding, _Mapping]]] = ..., overall: _Optional[_Union[RecordCiInvestigationOverall, _Mapping]] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class RecordCiInvestigationFindingsError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class RecordCiInvestigationFindingsResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: RecordCiInvestigationFindingsSuccess
    error: RecordCiInvestigationFindingsError
    def __init__(self, success: _Optional[_Union[RecordCiInvestigationFindingsSuccess, _Mapping]] = ..., error: _Optional[_Union[RecordCiInvestigationFindingsError, _Mapping]] = ...) -> None: ...

class RecordCiInvestigationFindingsSuccess(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RecordCiInvestigationFindingsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: RecordCiInvestigationFindingsArgs
    result: RecordCiInvestigationFindingsResult
    def __init__(self, args: _Optional[_Union[RecordCiInvestigationFindingsArgs, _Mapping]] = ..., result: _Optional[_Union[RecordCiInvestigationFindingsResult, _Mapping]] = ...) -> None: ...

class RecordCiInvestigationOverall(_message.Message):
    __slots__ = ("summary", "themes", "recommended_action", "recommended_action_evidence", "check_keys")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTION_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    CHECK_KEYS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    themes: _containers.RepeatedScalarFieldContainer[str]
    recommended_action: str
    recommended_action_evidence: str
    check_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, summary: _Optional[str] = ..., themes: _Optional[_Iterable[str]] = ..., recommended_action: _Optional[str] = ..., recommended_action_evidence: _Optional[str] = ..., check_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class RecordScreenArgs(_message.Message):
    __slots__ = ("mode", "tool_call_id", "save_as_filename")
    MODE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SAVE_AS_FILENAME_FIELD_NUMBER: _ClassVar[int]
    mode: RecordingMode
    tool_call_id: str
    save_as_filename: str
    def __init__(self, mode: _Optional[_Union[RecordingMode, str]] = ..., tool_call_id: _Optional[str] = ..., save_as_filename: _Optional[str] = ...) -> None: ...

class RecordScreenDiscardSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordScreenFailure(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class RecordScreenResult(_message.Message):
    __slots__ = ("start_success", "save_success", "discard_success", "failure")
    START_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SAVE_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DISCARD_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    start_success: RecordScreenStartSuccess
    save_success: RecordScreenSaveSuccess
    discard_success: RecordScreenDiscardSuccess
    failure: RecordScreenFailure
    def __init__(self, start_success: _Optional[_Union[RecordScreenStartSuccess, _Mapping]] = ..., save_success: _Optional[_Union[RecordScreenSaveSuccess, _Mapping]] = ..., discard_success: _Optional[_Union[RecordScreenDiscardSuccess, _Mapping]] = ..., failure: _Optional[_Union[RecordScreenFailure, _Mapping]] = ...) -> None: ...

class RecordScreenSaveSuccess(_message.Message):
    __slots__ = ("path", "recording_duration_ms", "requested_file_path_rejected_reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    RECORDING_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_FILE_PATH_REJECTED_REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    recording_duration_ms: int
    requested_file_path_rejected_reason: RequestedFilePathRejectedReason
    def __init__(self, path: _Optional[str] = ..., recording_duration_ms: _Optional[int] = ..., requested_file_path_rejected_reason: _Optional[_Union[RequestedFilePathRejectedReason, str]] = ...) -> None: ...

class RecordScreenStartSuccess(_message.Message):
    __slots__ = ("was_prior_recording_cancelled", "was_save_as_filename_ignored")
    WAS_PRIOR_RECORDING_CANCELLED_FIELD_NUMBER: _ClassVar[int]
    WAS_SAVE_AS_FILENAME_IGNORED_FIELD_NUMBER: _ClassVar[int]
    was_prior_recording_cancelled: bool
    was_save_as_filename_ignored: bool
    def __init__(self, was_prior_recording_cancelled: _Optional[bool] = ..., was_save_as_filename_ignored: _Optional[bool] = ...) -> None: ...

class RecordScreenToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: RecordScreenArgs
    result: RecordScreenResult
    def __init__(self, args: _Optional[_Union[RecordScreenArgs, _Mapping]] = ..., result: _Optional[_Union[RecordScreenResult, _Mapping]] = ...) -> None: ...

class RecordingDataPackage(_message.Message):
    __slots__ = ("raw_video_path", "duration_ms", "display_width", "display_height", "api_width", "api_height", "recording_start_epoch_ms", "input_events", "cursor_paths", "zoom_candidates", "idle_periods", "click_effects", "keystroke_events", "decision_input", "decision_output", "polished_video_path")
    RAW_VIDEO_PATH_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_WIDTH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    API_WIDTH_FIELD_NUMBER: _ClassVar[int]
    API_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    RECORDING_START_EPOCH_MS_FIELD_NUMBER: _ClassVar[int]
    INPUT_EVENTS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_PATHS_FIELD_NUMBER: _ClassVar[int]
    ZOOM_CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    IDLE_PERIODS_FIELD_NUMBER: _ClassVar[int]
    CLICK_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    KEYSTROKE_EVENTS_FIELD_NUMBER: _ClassVar[int]
    DECISION_INPUT_FIELD_NUMBER: _ClassVar[int]
    DECISION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    POLISHED_VIDEO_PATH_FIELD_NUMBER: _ClassVar[int]
    raw_video_path: str
    duration_ms: int
    display_width: int
    display_height: int
    api_width: int
    api_height: int
    recording_start_epoch_ms: int
    input_events: _containers.RepeatedCompositeFieldContainer[InputEvent]
    cursor_paths: _containers.RepeatedCompositeFieldContainer[CursorPath]
    zoom_candidates: _containers.RepeatedCompositeFieldContainer[ZoomCandidate]
    idle_periods: _containers.RepeatedCompositeFieldContainer[IdlePeriod]
    click_effects: _containers.RepeatedCompositeFieldContainer[ClickEffectKeyframe]
    keystroke_events: _containers.RepeatedCompositeFieldContainer[KeystrokeEvent]
    decision_input: DecisionInput
    decision_output: DecisionOutput
    polished_video_path: str
    def __init__(self, raw_video_path: _Optional[str] = ..., duration_ms: _Optional[int] = ..., display_width: _Optional[int] = ..., display_height: _Optional[int] = ..., api_width: _Optional[int] = ..., api_height: _Optional[int] = ..., recording_start_epoch_ms: _Optional[int] = ..., input_events: _Optional[_Iterable[_Union[InputEvent, _Mapping]]] = ..., cursor_paths: _Optional[_Iterable[_Union[CursorPath, _Mapping]]] = ..., zoom_candidates: _Optional[_Iterable[_Union[ZoomCandidate, _Mapping]]] = ..., idle_periods: _Optional[_Iterable[_Union[IdlePeriod, _Mapping]]] = ..., click_effects: _Optional[_Iterable[_Union[ClickEffectKeyframe, _Mapping]]] = ..., keystroke_events: _Optional[_Iterable[_Union[KeystrokeEvent, _Mapping]]] = ..., decision_input: _Optional[_Union[DecisionInput, _Mapping]] = ..., decision_output: _Optional[_Union[DecisionOutput, _Mapping]] = ..., polished_video_path: _Optional[str] = ...) -> None: ...

class ReflectArgs(_message.Message):
    __slots__ = ("unexpected_action_outcomes", "relevant_instructions", "scenario_analysis", "critical_synthesis", "next_steps", "tool_call_id")
    UNEXPECTED_ACTION_OUTCOMES_FIELD_NUMBER: _ClassVar[int]
    RELEVANT_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_SYNTHESIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_STEPS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    unexpected_action_outcomes: str
    relevant_instructions: str
    scenario_analysis: str
    critical_synthesis: str
    next_steps: str
    tool_call_id: str
    def __init__(self, unexpected_action_outcomes: _Optional[str] = ..., relevant_instructions: _Optional[str] = ..., scenario_analysis: _Optional[str] = ..., critical_synthesis: _Optional[str] = ..., next_steps: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class ReflectError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ReflectResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ReflectSuccess
    error: ReflectError
    def __init__(self, success: _Optional[_Union[ReflectSuccess, _Mapping]] = ..., error: _Optional[_Union[ReflectError, _Mapping]] = ...) -> None: ...

class ReflectSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReflectToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReflectArgs
    result: ReflectResult
    def __init__(self, args: _Optional[_Union[ReflectArgs, _Mapping]] = ..., result: _Optional[_Union[ReflectResult, _Mapping]] = ...) -> None: ...

class RefreshGithubAccessTokenRequest(_message.Message):
    __slots__ = ("github_access_token", "hostname", "repo_url", "clone_username")
    GITHUB_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    CLONE_USERNAME_FIELD_NUMBER: _ClassVar[int]
    github_access_token: str
    hostname: str
    repo_url: str
    clone_username: str
    def __init__(self, github_access_token: _Optional[str] = ..., hostname: _Optional[str] = ..., repo_url: _Optional[str] = ..., clone_username: _Optional[str] = ...) -> None: ...

class RefreshGithubAccessTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReleaseWorkerRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReloadAgentSkillsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReloadAgentSkillsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReloadPluginsRequest(_message.Message):
    __slots__ = ("reload_targets",)
    RELOAD_TARGETS_FIELD_NUMBER: _ClassVar[int]
    reload_targets: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, reload_targets: _Optional[_Iterable[str]] = ...) -> None: ...

class ReloadPluginsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReplaceEnvArgs(_message.Message):
    __slots__ = ("config", "mode", "checkout_ref_overrides")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_REF_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    config: ReplaceEnvConfig
    mode: ReplaceEnvMode
    checkout_ref_overrides: _containers.RepeatedCompositeFieldContainer[RepoCheckoutRefOverride]
    def __init__(self, config: _Optional[_Union[ReplaceEnvConfig, _Mapping]] = ..., mode: _Optional[_Union[ReplaceEnvMode, str]] = ..., checkout_ref_overrides: _Optional[_Iterable[_Union[RepoCheckoutRefOverride, _Mapping]]] = ...) -> None: ...

class ReplaceEnvConfig(_message.Message):
    __slots__ = ("install_script", "dockerfile_contents")
    INSTALL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    DOCKERFILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    install_script: str
    dockerfile_contents: str
    def __init__(self, install_script: _Optional[str] = ..., dockerfile_contents: _Optional[str] = ...) -> None: ...

class ReplaceEnvFailure(_message.Message):
    __slots__ = ("error_message", "setup_logs")
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SETUP_LOGS_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    setup_logs: str
    def __init__(self, error_message: _Optional[str] = ..., setup_logs: _Optional[str] = ...) -> None: ...

class ReplaceEnvResult(_message.Message):
    __slots__ = ("success", "failure")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ReplaceEnvSuccess
    failure: ReplaceEnvFailure
    def __init__(self, success: _Optional[_Union[ReplaceEnvSuccess, _Mapping]] = ..., failure: _Optional[_Union[ReplaceEnvFailure, _Mapping]] = ...) -> None: ...

class ReplaceEnvSuccess(_message.Message):
    __slots__ = ("setup_logs",)
    SETUP_LOGS_FIELD_NUMBER: _ClassVar[int]
    setup_logs: str
    def __init__(self, setup_logs: _Optional[str] = ...) -> None: ...

class ReplaceEnvToolCall(_message.Message):
    __slots__ = ("args", "result", "associated_pod_key")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_POD_KEY_FIELD_NUMBER: _ClassVar[int]
    args: ReplaceEnvArgs
    result: ReplaceEnvResult
    associated_pod_key: str
    def __init__(self, args: _Optional[_Union[ReplaceEnvArgs, _Mapping]] = ..., result: _Optional[_Union[ReplaceEnvResult, _Mapping]] = ..., associated_pod_key: _Optional[str] = ...) -> None: ...

class ReplaceEnvToolCallDelta(_message.Message):
    __slots__ = ("associated_pod_key",)
    ASSOCIATED_POD_KEY_FIELD_NUMBER: _ClassVar[int]
    associated_pod_key: str
    def __init__(self, associated_pod_key: _Optional[str] = ...) -> None: ...

class RepoCheckoutRefOverride(_message.Message):
    __slots__ = ("repo_url", "ref")
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    repo_url: str
    ref: str
    def __init__(self, repo_url: _Optional[str] = ..., ref: _Optional[str] = ...) -> None: ...

class ReportBugArgs(_message.Message):
    __slots__ = ("title", "file", "start_line", "end_line", "description", "severity", "category", "rationale")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    END_LINE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    title: str
    file: str
    start_line: int
    end_line: int
    description: str
    severity: str
    category: str
    rationale: str
    def __init__(self, title: _Optional[str] = ..., file: _Optional[str] = ..., start_line: _Optional[int] = ..., end_line: _Optional[int] = ..., description: _Optional[str] = ..., severity: _Optional[str] = ..., category: _Optional[str] = ..., rationale: _Optional[str] = ...) -> None: ...

class ReportBugError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class ReportBugResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ReportBugSuccess
    error: ReportBugError
    def __init__(self, success: _Optional[_Union[ReportBugSuccess, _Mapping]] = ..., error: _Optional[_Union[ReportBugError, _Mapping]] = ...) -> None: ...

class ReportBugSuccess(_message.Message):
    __slots__ = ("output",)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: str
    def __init__(self, output: _Optional[str] = ...) -> None: ...

class ReportBugToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReportBugArgs
    result: ReportBugResult
    def __init__(self, args: _Optional[_Union[ReportBugArgs, _Mapping]] = ..., result: _Optional[_Union[ReportBugResult, _Mapping]] = ...) -> None: ...

class ReportBugfixResultsArgs(_message.Message):
    __slots__ = ("summary", "results")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    results: _containers.RepeatedCompositeFieldContainer[BugfixResultItem]
    def __init__(self, summary: _Optional[str] = ..., results: _Optional[_Iterable[_Union[BugfixResultItem, _Mapping]]] = ...) -> None: ...

class ReportBugfixResultsError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class ReportBugfixResultsResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: ReportBugfixResultsSuccess
    error: ReportBugfixResultsError
    def __init__(self, success: _Optional[_Union[ReportBugfixResultsSuccess, _Mapping]] = ..., error: _Optional[_Union[ReportBugfixResultsError, _Mapping]] = ...) -> None: ...

class ReportBugfixResultsSuccess(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[BugfixResultItem]
    def __init__(self, results: _Optional[_Iterable[_Union[BugfixResultItem, _Mapping]]] = ...) -> None: ...

class ReportBugfixResultsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ReportBugfixResultsArgs
    result: ReportBugfixResultsResult
    def __init__(self, args: _Optional[_Union[ReportBugfixResultsArgs, _Mapping]] = ..., result: _Optional[_Union[ReportBugfixResultsResult, _Mapping]] = ...) -> None: ...

class RepositoryIndexingInfo(_message.Message):
    __slots__ = ("relative_workspace_path", "remote_urls", "remote_names", "repo_name", "repo_owner", "is_tracked", "is_local", "orthogonal_transform_seed", "workspace_uri", "path_encryption_key")
    RELATIVE_WORKSPACE_PATH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URLS_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAMES_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    REPO_OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_TRACKED_FIELD_NUMBER: _ClassVar[int]
    IS_LOCAL_FIELD_NUMBER: _ClassVar[int]
    ORTHOGONAL_TRANSFORM_SEED_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_URI_FIELD_NUMBER: _ClassVar[int]
    PATH_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    relative_workspace_path: str
    remote_urls: _containers.RepeatedScalarFieldContainer[str]
    remote_names: _containers.RepeatedScalarFieldContainer[str]
    repo_name: str
    repo_owner: str
    is_tracked: bool
    is_local: bool
    orthogonal_transform_seed: float
    workspace_uri: str
    path_encryption_key: str
    def __init__(self, relative_workspace_path: _Optional[str] = ..., remote_urls: _Optional[_Iterable[str]] = ..., remote_names: _Optional[_Iterable[str]] = ..., repo_name: _Optional[str] = ..., repo_owner: _Optional[str] = ..., is_tracked: _Optional[bool] = ..., is_local: _Optional[bool] = ..., orthogonal_transform_seed: _Optional[float] = ..., workspace_uri: _Optional[str] = ..., path_encryption_key: _Optional[str] = ...) -> None: ...

class RequestContext(_message.Message):
    __slots__ = ("rules", "env", "repository_info", "tools", "conversation_notes_listing", "shared_notes_listing", "git_repos", "project_layouts", "mcp_instructions", "debug_mode_config", "cloud_rule", "web_search_enabled", "skill_options", "repository_info_should_query_prod", "file_contents", "user_intent_summary", "custom_subagents", "mcp_file_system_options", "web_fetch_enabled", "hooks_additional_context", "commit_attribution_message", "pr_attribution_message", "hooks_config", "agent_skills", "precomputed_human_changes", "recently_added_plugin", "supports_mcp_auth", "git_repo_info_complete", "mcp_meta_tool_options", "read_lints_enabled", "mcp_info_complete", "non_file_rules", "matched_installed_plugin", "rules_info_complete", "env_info_complete", "repository_info_complete", "custom_subagents_info_complete", "agent_skills_info_complete", "mcp_file_system_info_complete", "git_status_info_complete", "user_permissions_auto_run", "project_permissions_auto_run", "admin_permissions_auto_run", "disabled_team_rules", "search_conversations_enabled", "send_message_enabled", "admin_command_denylist")
    class FileContentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RULES_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_INFO_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_NOTES_LISTING_FIELD_NUMBER: _ClassVar[int]
    SHARED_NOTES_LISTING_FIELD_NUMBER: _ClassVar[int]
    GIT_REPOS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
    MCP_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_MODE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RULE_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SKILL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_INFO_SHOULD_QUERY_PROD_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    USER_INTENT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    MCP_FILE_SYSTEM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WEB_FETCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOOKS_ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ATTRIBUTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PR_ATTRIBUTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HOOKS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    PRECOMPUTED_HUMAN_CHANGES_FIELD_NUMBER: _ClassVar[int]
    RECENTLY_ADDED_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_MCP_AUTH_FIELD_NUMBER: _ClassVar[int]
    GIT_REPO_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    MCP_META_TOOL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    READ_LINTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MCP_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    NON_FILE_RULES_FIELD_NUMBER: _ClassVar[int]
    MATCHED_INSTALLED_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    RULES_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    ENV_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_SUBAGENTS_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    MCP_FILE_SYSTEM_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    GIT_STATUS_INFO_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSIONS_AUTO_RUN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_PERMISSIONS_AUTO_RUN_FIELD_NUMBER: _ClassVar[int]
    ADMIN_PERMISSIONS_AUTO_RUN_FIELD_NUMBER: _ClassVar[int]
    DISABLED_TEAM_RULES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONVERSATIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ADMIN_COMMAND_DENYLIST_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[CursorRule]
    env: RequestContextEnv
    repository_info: _containers.RepeatedCompositeFieldContainer[RepositoryIndexingInfo]
    tools: _containers.RepeatedCompositeFieldContainer[McpToolDefinition]
    conversation_notes_listing: str
    shared_notes_listing: str
    git_repos: _containers.RepeatedCompositeFieldContainer[GitRepoInfo]
    project_layouts: _containers.RepeatedCompositeFieldContainer[LsDirectoryTreeNode]
    mcp_instructions: _containers.RepeatedCompositeFieldContainer[McpInstructions]
    debug_mode_config: DebugModeConfig
    cloud_rule: str
    web_search_enabled: bool
    skill_options: SkillOptions
    repository_info_should_query_prod: bool
    file_contents: _containers.ScalarMap[str, str]
    user_intent_summary: str
    custom_subagents: _containers.RepeatedCompositeFieldContainer[CustomSubagent]
    mcp_file_system_options: McpFileSystemOptions
    web_fetch_enabled: bool
    hooks_additional_context: str
    commit_attribution_message: str
    pr_attribution_message: str
    hooks_config: HooksConfigInfo
    agent_skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    precomputed_human_changes: _containers.RepeatedCompositeFieldContainer[PrecomputedHumanChange]
    recently_added_plugin: RecentlyAddedPlugin
    supports_mcp_auth: bool
    git_repo_info_complete: bool
    mcp_meta_tool_options: McpMetaToolOptions
    read_lints_enabled: bool
    mcp_info_complete: bool
    non_file_rules: _containers.RepeatedCompositeFieldContainer[CursorRule]
    matched_installed_plugin: MatchedInstalledPlugin
    rules_info_complete: bool
    env_info_complete: bool
    repository_info_complete: bool
    custom_subagents_info_complete: bool
    agent_skills_info_complete: bool
    mcp_file_system_info_complete: bool
    git_status_info_complete: bool
    user_permissions_auto_run: PermissionsAutoRunInstructions
    project_permissions_auto_run: PermissionsAutoRunInstructions
    admin_permissions_auto_run: PermissionsAutoRunInstructions
    disabled_team_rules: _containers.RepeatedScalarFieldContainer[str]
    search_conversations_enabled: bool
    send_message_enabled: bool
    admin_command_denylist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, rules: _Optional[_Iterable[_Union[CursorRule, _Mapping]]] = ..., env: _Optional[_Union[RequestContextEnv, _Mapping]] = ..., repository_info: _Optional[_Iterable[_Union[RepositoryIndexingInfo, _Mapping]]] = ..., tools: _Optional[_Iterable[_Union[McpToolDefinition, _Mapping]]] = ..., conversation_notes_listing: _Optional[str] = ..., shared_notes_listing: _Optional[str] = ..., git_repos: _Optional[_Iterable[_Union[GitRepoInfo, _Mapping]]] = ..., project_layouts: _Optional[_Iterable[_Union[LsDirectoryTreeNode, _Mapping]]] = ..., mcp_instructions: _Optional[_Iterable[_Union[McpInstructions, _Mapping]]] = ..., debug_mode_config: _Optional[_Union[DebugModeConfig, _Mapping]] = ..., cloud_rule: _Optional[str] = ..., web_search_enabled: _Optional[bool] = ..., skill_options: _Optional[_Union[SkillOptions, _Mapping]] = ..., repository_info_should_query_prod: _Optional[bool] = ..., file_contents: _Optional[_Mapping[str, str]] = ..., user_intent_summary: _Optional[str] = ..., custom_subagents: _Optional[_Iterable[_Union[CustomSubagent, _Mapping]]] = ..., mcp_file_system_options: _Optional[_Union[McpFileSystemOptions, _Mapping]] = ..., web_fetch_enabled: _Optional[bool] = ..., hooks_additional_context: _Optional[str] = ..., commit_attribution_message: _Optional[str] = ..., pr_attribution_message: _Optional[str] = ..., hooks_config: _Optional[_Union[HooksConfigInfo, _Mapping]] = ..., agent_skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ..., precomputed_human_changes: _Optional[_Iterable[_Union[PrecomputedHumanChange, _Mapping]]] = ..., recently_added_plugin: _Optional[_Union[RecentlyAddedPlugin, _Mapping]] = ..., supports_mcp_auth: _Optional[bool] = ..., git_repo_info_complete: _Optional[bool] = ..., mcp_meta_tool_options: _Optional[_Union[McpMetaToolOptions, _Mapping]] = ..., read_lints_enabled: _Optional[bool] = ..., mcp_info_complete: _Optional[bool] = ..., non_file_rules: _Optional[_Iterable[_Union[CursorRule, _Mapping]]] = ..., matched_installed_plugin: _Optional[_Union[MatchedInstalledPlugin, _Mapping]] = ..., rules_info_complete: _Optional[bool] = ..., env_info_complete: _Optional[bool] = ..., repository_info_complete: _Optional[bool] = ..., custom_subagents_info_complete: _Optional[bool] = ..., agent_skills_info_complete: _Optional[bool] = ..., mcp_file_system_info_complete: _Optional[bool] = ..., git_status_info_complete: _Optional[bool] = ..., user_permissions_auto_run: _Optional[_Union[PermissionsAutoRunInstructions, _Mapping]] = ..., project_permissions_auto_run: _Optional[_Union[PermissionsAutoRunInstructions, _Mapping]] = ..., admin_permissions_auto_run: _Optional[_Union[PermissionsAutoRunInstructions, _Mapping]] = ..., disabled_team_rules: _Optional[_Iterable[str]] = ..., search_conversations_enabled: _Optional[bool] = ..., send_message_enabled: _Optional[bool] = ..., admin_command_denylist: _Optional[_Iterable[str]] = ...) -> None: ...

class RequestContextArgs(_message.Message):
    __slots__ = ("notes_session_id", "workspace_id", "read_only_pinned_tree_sha", "read_only_plugin_cache_root", "use_cached")
    NOTES_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_PINNED_TREE_SHA_FIELD_NUMBER: _ClassVar[int]
    READ_ONLY_PLUGIN_CACHE_ROOT_FIELD_NUMBER: _ClassVar[int]
    USE_CACHED_FIELD_NUMBER: _ClassVar[int]
    notes_session_id: str
    workspace_id: str
    read_only_pinned_tree_sha: str
    read_only_plugin_cache_root: str
    use_cached: bool
    def __init__(self, notes_session_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., read_only_pinned_tree_sha: _Optional[str] = ..., read_only_plugin_cache_root: _Optional[str] = ..., use_cached: _Optional[bool] = ...) -> None: ...

class RequestContextEnv(_message.Message):
    __slots__ = ("os_version", "workspace_paths", "shell", "sandbox_enabled", "terminals_folder", "agent_shared_notes_folder", "agent_conversation_notes_folder", "time_zone", "project_folder", "agent_transcripts_folder", "artifacts_folder", "sandbox_supported", "sandbox_network_has_defaults", "sandbox_network_explicit_allowlist", "secret_redaction_enabled", "computer_use_supported", "is_working_dir_home_dir", "process_working_directory", "smart_mode_classifier_auto_mode_enabled", "dev_force_next_smart_mode_classifier_block_token", "dev_delay_next_smart_mode_classifier_token", "mounted_agent_stores")
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_PATHS_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TERMINALS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    AGENT_SHARED_NOTES_FOLDER_FIELD_NUMBER: _ClassVar[int]
    AGENT_CONVERSATION_NOTES_FOLDER_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FOLDER_FIELD_NUMBER: _ClassVar[int]
    AGENT_TRANSCRIPTS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NETWORK_HAS_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NETWORK_EXPLICIT_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    SECRET_REDACTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_WORKING_DIR_HOME_DIR_FIELD_NUMBER: _ClassVar[int]
    PROCESS_WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_CLASSIFIER_AUTO_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEV_FORCE_NEXT_SMART_MODE_CLASSIFIER_BLOCK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DEV_DELAY_NEXT_SMART_MODE_CLASSIFIER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MOUNTED_AGENT_STORES_FIELD_NUMBER: _ClassVar[int]
    os_version: str
    workspace_paths: _containers.RepeatedScalarFieldContainer[str]
    shell: str
    sandbox_enabled: bool
    terminals_folder: str
    agent_shared_notes_folder: str
    agent_conversation_notes_folder: str
    time_zone: str
    project_folder: str
    agent_transcripts_folder: str
    artifacts_folder: str
    sandbox_supported: bool
    sandbox_network_has_defaults: bool
    sandbox_network_explicit_allowlist: _containers.RepeatedScalarFieldContainer[str]
    secret_redaction_enabled: bool
    computer_use_supported: bool
    is_working_dir_home_dir: bool
    process_working_directory: str
    smart_mode_classifier_auto_mode_enabled: bool
    dev_force_next_smart_mode_classifier_block_token: str
    dev_delay_next_smart_mode_classifier_token: str
    mounted_agent_stores: _containers.RepeatedCompositeFieldContainer[MountedAgentStore]
    def __init__(self, os_version: _Optional[str] = ..., workspace_paths: _Optional[_Iterable[str]] = ..., shell: _Optional[str] = ..., sandbox_enabled: _Optional[bool] = ..., terminals_folder: _Optional[str] = ..., agent_shared_notes_folder: _Optional[str] = ..., agent_conversation_notes_folder: _Optional[str] = ..., time_zone: _Optional[str] = ..., project_folder: _Optional[str] = ..., agent_transcripts_folder: _Optional[str] = ..., artifacts_folder: _Optional[str] = ..., sandbox_supported: _Optional[bool] = ..., sandbox_network_has_defaults: _Optional[bool] = ..., sandbox_network_explicit_allowlist: _Optional[_Iterable[str]] = ..., secret_redaction_enabled: _Optional[bool] = ..., computer_use_supported: _Optional[bool] = ..., is_working_dir_home_dir: _Optional[bool] = ..., process_working_directory: _Optional[str] = ..., smart_mode_classifier_auto_mode_enabled: _Optional[bool] = ..., dev_force_next_smart_mode_classifier_block_token: _Optional[str] = ..., dev_delay_next_smart_mode_classifier_token: _Optional[str] = ..., mounted_agent_stores: _Optional[_Iterable[_Union[MountedAgentStore, _Mapping]]] = ...) -> None: ...

class RequestContextError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class RequestContextMcpsPart(_message.Message):
    __slots__ = ("tools", "mcp_instructions", "mcp_file_system_options", "mcp_meta_tool_options")
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    MCP_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    MCP_FILE_SYSTEM_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MCP_META_TOOL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    tools: _containers.RepeatedCompositeFieldContainer[McpToolDefinition]
    mcp_instructions: _containers.RepeatedCompositeFieldContainer[McpInstructions]
    mcp_file_system_options: McpFileSystemOptions
    mcp_meta_tool_options: McpMetaToolOptions
    def __init__(self, tools: _Optional[_Iterable[_Union[McpToolDefinition, _Mapping]]] = ..., mcp_instructions: _Optional[_Iterable[_Union[McpInstructions, _Mapping]]] = ..., mcp_file_system_options: _Optional[_Union[McpFileSystemOptions, _Mapping]] = ..., mcp_meta_tool_options: _Optional[_Union[McpMetaToolOptions, _Mapping]] = ...) -> None: ...

class RequestContextPartReferences(_message.Message):
    __slots__ = ("rules_blob_id", "rules_byte_length", "skills_blob_id", "skills_byte_length", "subagents_blob_id", "subagents_byte_length", "mcps_blob_id", "mcps_byte_length", "dynamic_context")
    RULES_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    RULES_BYTE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SKILLS_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_BYTE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SUBAGENTS_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENTS_BYTE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MCPS_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    MCPS_BYTE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    rules_blob_id: bytes
    rules_byte_length: int
    skills_blob_id: bytes
    skills_byte_length: int
    subagents_blob_id: bytes
    subagents_byte_length: int
    mcps_blob_id: bytes
    mcps_byte_length: int
    dynamic_context: RequestContext
    def __init__(self, rules_blob_id: _Optional[bytes] = ..., rules_byte_length: _Optional[int] = ..., skills_blob_id: _Optional[bytes] = ..., skills_byte_length: _Optional[int] = ..., subagents_blob_id: _Optional[bytes] = ..., subagents_byte_length: _Optional[int] = ..., mcps_blob_id: _Optional[bytes] = ..., mcps_byte_length: _Optional[int] = ..., dynamic_context: _Optional[_Union[RequestContext, _Mapping]] = ...) -> None: ...

class RequestContextRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class RequestContextResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: RequestContextSuccess
    error: RequestContextError
    rejected: RequestContextRejected
    def __init__(self, success: _Optional[_Union[RequestContextSuccess, _Mapping]] = ..., error: _Optional[_Union[RequestContextError, _Mapping]] = ..., rejected: _Optional[_Union[RequestContextRejected, _Mapping]] = ...) -> None: ...

class RequestContextRulesPart(_message.Message):
    __slots__ = ("rules", "non_file_rules", "cloud_rule")
    RULES_FIELD_NUMBER: _ClassVar[int]
    NON_FILE_RULES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RULE_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[CursorRule]
    non_file_rules: _containers.RepeatedCompositeFieldContainer[CursorRule]
    cloud_rule: str
    def __init__(self, rules: _Optional[_Iterable[_Union[CursorRule, _Mapping]]] = ..., non_file_rules: _Optional[_Iterable[_Union[CursorRule, _Mapping]]] = ..., cloud_rule: _Optional[str] = ...) -> None: ...

class RequestContextSkillsPart(_message.Message):
    __slots__ = ("agent_skills", "skill_options")
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    SKILL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    agent_skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    skill_options: SkillOptions
    def __init__(self, agent_skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ..., skill_options: _Optional[_Union[SkillOptions, _Mapping]] = ...) -> None: ...

class RequestContextSubagentsPart(_message.Message):
    __slots__ = ("custom_subagents",)
    CUSTOM_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    custom_subagents: _containers.RepeatedCompositeFieldContainer[CustomSubagent]
    def __init__(self, custom_subagents: _Optional[_Iterable[_Union[CustomSubagent, _Mapping]]] = ...) -> None: ...

class RequestContextSuccess(_message.Message):
    __slots__ = ("request_context", "served_from_disk_cache")
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SERVED_FROM_DISK_CACHE_FIELD_NUMBER: _ClassVar[int]
    request_context: RequestContext
    served_from_disk_cache: bool
    def __init__(self, request_context: _Optional[_Union[RequestContext, _Mapping]] = ..., served_from_disk_cache: _Optional[bool] = ...) -> None: ...

class RequestedModel(_message.Message):
    __slots__ = ("model_id", "max_mode", "parameters", "built_in_model", "is_variant_string_representation", "api_key_credentials", "azure_credentials", "bedrock_credentials")
    class ModelParameterValue(_message.Message):
        __slots__ = ("id", "value")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        id: str
        value: str
        def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_MODE_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    BUILT_IN_MODEL_FIELD_NUMBER: _ClassVar[int]
    IS_VARIANT_STRING_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    max_mode: bool
    parameters: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    built_in_model: bool
    is_variant_string_representation: bool
    api_key_credentials: ApiKeyCredentials
    azure_credentials: AzureCredentials
    bedrock_credentials: BedrockCredentials
    def __init__(self, model_id: _Optional[str] = ..., max_mode: _Optional[bool] = ..., parameters: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ..., built_in_model: _Optional[bool] = ..., is_variant_string_representation: _Optional[bool] = ..., api_key_credentials: _Optional[_Union[ApiKeyCredentials, _Mapping]] = ..., azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]] = ..., bedrock_credentials: _Optional[_Union[BedrockCredentials, _Mapping]] = ...) -> None: ...

class ResizePtyRequest(_message.Message):
    __slots__ = ("pty_id", "cols", "rows")
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    cols: int
    rows: int
    def __init__(self, pty_id: _Optional[str] = ..., cols: _Optional[int] = ..., rows: _Optional[int] = ...) -> None: ...

class ResizePtyResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class ResolveCommentAction(_message.Message):
    __slots__ = ("pr_url", "branch_name", "comment_id", "repo_url", "comment_reference")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    COMMENT_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    branch_name: str
    comment_id: int
    repo_url: str
    comment_reference: str
    def __init__(self, pr_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., comment_id: _Optional[int] = ..., repo_url: _Optional[str] = ..., comment_reference: _Optional[str] = ...) -> None: ...

class RespondToAgentHostInteractionRequest(_message.Message):
    __slots__ = ("session_id", "interaction_id", "response")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    interaction_id: str
    response: InteractionResponse
    def __init__(self, session_id: _Optional[str] = ..., interaction_id: _Optional[str] = ..., response: _Optional[_Union[InteractionResponse, _Mapping]] = ...) -> None: ...

class RespondToAgentHostInteractionResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: AgentHostInteractionResponseStatus
    def __init__(self, status: _Optional[_Union[AgentHostInteractionResponseStatus, str]] = ...) -> None: ...

class ResponseComparisonCompleted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResponseComparisonSkipped(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: ResponseComparisonSkipReason
    def __init__(self, reason: _Optional[_Union[ResponseComparisonSkipReason, str]] = ...) -> None: ...

class ResponseComparisonStarted(_message.Message):
    __slots__ = ("display_order", "parent_invocation_id", "alternate_invocation_id", "parent_response", "comparison_config_id", "alternate_model_id")
    DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
    PARENT_INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ALTERNATE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    display_order: ResponseComparisonDisplayOrder
    parent_invocation_id: str
    alternate_invocation_id: str
    parent_response: str
    comparison_config_id: str
    alternate_model_id: str
    def __init__(self, display_order: _Optional[_Union[ResponseComparisonDisplayOrder, str]] = ..., parent_invocation_id: _Optional[str] = ..., alternate_invocation_id: _Optional[str] = ..., parent_response: _Optional[str] = ..., comparison_config_id: _Optional[str] = ..., alternate_model_id: _Optional[str] = ...) -> None: ...

class ResponseComparisonTextDelta(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ResponseComparisonUpdate(_message.Message):
    __slots__ = ("comparison_id", "started", "text_delta", "completed", "skipped")
    COMPARISON_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    TEXT_DELTA_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    comparison_id: str
    started: ResponseComparisonStarted
    text_delta: ResponseComparisonTextDelta
    completed: ResponseComparisonCompleted
    skipped: ResponseComparisonSkipped
    def __init__(self, comparison_id: _Optional[str] = ..., started: _Optional[_Union[ResponseComparisonStarted, _Mapping]] = ..., text_delta: _Optional[_Union[ResponseComparisonTextDelta, _Mapping]] = ..., completed: _Optional[_Union[ResponseComparisonCompleted, _Mapping]] = ..., skipped: _Optional[_Union[ResponseComparisonSkipped, _Mapping]] = ...) -> None: ...

class RestoreArtifactInstruction(_message.Message):
    __slots__ = ("absolute_path", "download_url", "updated_at_unix_ms")
    ABSOLUTE_PATH_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    absolute_path: str
    download_url: str
    updated_at_unix_ms: int
    def __init__(self, absolute_path: _Optional[str] = ..., download_url: _Optional[str] = ..., updated_at_unix_ms: _Optional[int] = ...) -> None: ...

class RestoreArtifactResult(_message.Message):
    __slots__ = ("status", "error_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: ArtifactRestoreStatus
    error_message: str
    def __init__(self, status: _Optional[_Union[ArtifactRestoreStatus, str]] = ..., error_message: _Optional[str] = ...) -> None: ...

class RestoreArtifactsRequest(_message.Message):
    __slots__ = ("artifacts",)
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[RestoreArtifactInstruction]
    def __init__(self, artifacts: _Optional[_Iterable[_Union[RestoreArtifactInstruction, _Mapping]]] = ...) -> None: ...

class RestoreArtifactsResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[RestoreArtifactResult]
    def __init__(self, results: _Optional[_Iterable[_Union[RestoreArtifactResult, _Mapping]]] = ...) -> None: ...

class ResumeAction(_message.Message):
    __slots__ = ("request_context",)
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    request_context: RequestContext
    def __init__(self, request_context: _Optional[_Union[RequestContext, _Mapping]] = ...) -> None: ...

class RunScopedOverlay(_message.Message):
    __slots__ = ("run_id", "release", "holder")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    HOLDER_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    release: bool
    holder: str
    def __init__(self, run_id: _Optional[str] = ..., release: _Optional[bool] = ..., holder: _Optional[str] = ...) -> None: ...

class SameMachineTarget(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SandboxPolicy(_message.Message):
    __slots__ = ("type", "network_access", "additional_readwrite_paths", "additional_readonly_paths", "debug_output_dir", "disable_tmp_write", "allowlist_escalated", "enable_shared_build_cache", "network_policy", "network_policy_strict", "capture_denies", "skip_statsig_defaults", "read_boundary", "additional_read_paths")
    class ReadBoundaryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        READ_BOUNDARY_MODE_UNSPECIFIED: _ClassVar[SandboxPolicy.ReadBoundaryMode]
        READ_BOUNDARY_MODE_SYSTEM: _ClassVar[SandboxPolicy.ReadBoundaryMode]
        READ_BOUNDARY_MODE_WORKSPACE: _ClassVar[SandboxPolicy.ReadBoundaryMode]
        READ_BOUNDARY_MODE_CUSTOM: _ClassVar[SandboxPolicy.ReadBoundaryMode]
    READ_BOUNDARY_MODE_UNSPECIFIED: SandboxPolicy.ReadBoundaryMode
    READ_BOUNDARY_MODE_SYSTEM: SandboxPolicy.ReadBoundaryMode
    READ_BOUNDARY_MODE_WORKSPACE: SandboxPolicy.ReadBoundaryMode
    READ_BOUNDARY_MODE_CUSTOM: SandboxPolicy.ReadBoundaryMode
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[SandboxPolicy.Type]
        TYPE_INSECURE_NONE: _ClassVar[SandboxPolicy.Type]
        TYPE_WORKSPACE_READWRITE: _ClassVar[SandboxPolicy.Type]
        TYPE_WORKSPACE_READONLY: _ClassVar[SandboxPolicy.Type]
    TYPE_UNSPECIFIED: SandboxPolicy.Type
    TYPE_INSECURE_NONE: SandboxPolicy.Type
    TYPE_WORKSPACE_READWRITE: SandboxPolicy.Type
    TYPE_WORKSPACE_READONLY: SandboxPolicy.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ACCESS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_READWRITE_PATHS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_READONLY_PATHS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_OUTPUT_DIR_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TMP_WRITE_FIELD_NUMBER: _ClassVar[int]
    ALLOWLIST_ESCALATED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SHARED_BUILD_CACHE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_FIELD_NUMBER: _ClassVar[int]
    NETWORK_POLICY_STRICT_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_DENIES_FIELD_NUMBER: _ClassVar[int]
    SKIP_STATSIG_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    READ_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_READ_PATHS_FIELD_NUMBER: _ClassVar[int]
    type: SandboxPolicy.Type
    network_access: bool
    additional_readwrite_paths: _containers.RepeatedScalarFieldContainer[str]
    additional_readonly_paths: _containers.RepeatedScalarFieldContainer[str]
    debug_output_dir: str
    disable_tmp_write: bool
    allowlist_escalated: bool
    enable_shared_build_cache: bool
    network_policy: NetworkPolicy
    network_policy_strict: bool
    capture_denies: bool
    skip_statsig_defaults: bool
    read_boundary: SandboxPolicy.ReadBoundaryMode
    additional_read_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[_Union[SandboxPolicy.Type, str]] = ..., network_access: _Optional[bool] = ..., additional_readwrite_paths: _Optional[_Iterable[str]] = ..., additional_readonly_paths: _Optional[_Iterable[str]] = ..., debug_output_dir: _Optional[str] = ..., disable_tmp_write: _Optional[bool] = ..., allowlist_escalated: _Optional[bool] = ..., enable_shared_build_cache: _Optional[bool] = ..., network_policy: _Optional[_Union[NetworkPolicy, _Mapping]] = ..., network_policy_strict: _Optional[bool] = ..., capture_denies: _Optional[bool] = ..., skip_statsig_defaults: _Optional[bool] = ..., read_boundary: _Optional[_Union[SandboxPolicy.ReadBoundaryMode, str]] = ..., additional_read_paths: _Optional[_Iterable[str]] = ...) -> None: ...

class SandboxPolicyMergeSources(_message.Message):
    __slots__ = ("per_user", "per_repo", "team_admin")
    PER_USER_FIELD_NUMBER: _ClassVar[int]
    PER_REPO_FIELD_NUMBER: _ClassVar[int]
    TEAM_ADMIN_FIELD_NUMBER: _ClassVar[int]
    per_user: SandboxPolicy
    per_repo: SandboxPolicy
    team_admin: SandboxPolicy
    def __init__(self, per_user: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., per_repo: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., team_admin: _Optional[_Union[SandboxPolicy, _Mapping]] = ...) -> None: ...

class ScreenshotAction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScrollAction(_message.Message):
    __slots__ = ("coordinate", "direction", "amount", "modifier_keys")
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_KEYS_FIELD_NUMBER: _ClassVar[int]
    coordinate: Coordinate
    direction: ScrollDirection
    amount: int
    modifier_keys: str
    def __init__(self, coordinate: _Optional[_Union[Coordinate, _Mapping]] = ..., direction: _Optional[_Union[ScrollDirection, str]] = ..., amount: _Optional[int] = ..., modifier_keys: _Optional[str] = ...) -> None: ...

class SearchConversationsToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: ConversationSearchArgs
    result: ConversationSearchResult
    def __init__(self, args: _Optional[_Union[ConversationSearchArgs, _Mapping]] = ..., result: _Optional[_Union[ConversationSearchResult, _Mapping]] = ...) -> None: ...

class SelectedAgenticGitAction(_message.Message):
    __slots__ = ("branch_context", "path_to_template_file", "path_to_template_dir", "commit_params", "commit_and_push_params", "push_params", "create_pr_params", "create_pr_with_changes_params", "fix_merge_conflicts_params", "babysit_pr_in_cloud_params", "apply_locally_params", "checkout_branch_params", "create_branch_and_commit_params", "create_branch_commit_and_push_params", "update_branch_params", "create_branch_params")
    BRANCH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PATH_TO_TEMPLATE_FILE_FIELD_NUMBER: _ClassVar[int]
    PATH_TO_TEMPLATE_DIR_FIELD_NUMBER: _ClassVar[int]
    COMMIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_AND_PUSH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PUSH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_PR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_PR_WITH_CHANGES_PARAMS_FIELD_NUMBER: _ClassVar[int]
    FIX_MERGE_CONFLICTS_PARAMS_FIELD_NUMBER: _ClassVar[int]
    BABYSIT_PR_IN_CLOUD_PARAMS_FIELD_NUMBER: _ClassVar[int]
    APPLY_LOCALLY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_BRANCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_BRANCH_AND_COMMIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_BRANCH_COMMIT_AND_PUSH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_BRANCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_BRANCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    branch_context: SelectedGitBranchContext
    path_to_template_file: str
    path_to_template_dir: str
    commit_params: SelectedAgenticGitActionCommitParams
    commit_and_push_params: SelectedAgenticGitActionCommitParams
    push_params: SelectedAgenticGitActionPushParams
    create_pr_params: SelectedAgenticGitActionPushParams
    create_pr_with_changes_params: SelectedAgenticGitActionCommitParams
    fix_merge_conflicts_params: SelectedAgenticGitActionFixMergeConflictsParams
    babysit_pr_in_cloud_params: SelectedAgenticGitActionBabysitPrInCloudParams
    apply_locally_params: SelectedAgenticGitActionPullLocallyParams
    checkout_branch_params: SelectedAgenticGitActionPullLocallyParams
    create_branch_and_commit_params: SelectedAgenticGitActionCommitParams
    create_branch_commit_and_push_params: SelectedAgenticGitActionCommitParams
    update_branch_params: SelectedAgenticGitActionUpdateBranchParams
    create_branch_params: SelectedAgenticGitActionCreateBranchParams
    def __init__(self, branch_context: _Optional[_Union[SelectedGitBranchContext, _Mapping]] = ..., path_to_template_file: _Optional[str] = ..., path_to_template_dir: _Optional[str] = ..., commit_params: _Optional[_Union[SelectedAgenticGitActionCommitParams, _Mapping]] = ..., commit_and_push_params: _Optional[_Union[SelectedAgenticGitActionCommitParams, _Mapping]] = ..., push_params: _Optional[_Union[SelectedAgenticGitActionPushParams, _Mapping]] = ..., create_pr_params: _Optional[_Union[SelectedAgenticGitActionPushParams, _Mapping]] = ..., create_pr_with_changes_params: _Optional[_Union[SelectedAgenticGitActionCommitParams, _Mapping]] = ..., fix_merge_conflicts_params: _Optional[_Union[SelectedAgenticGitActionFixMergeConflictsParams, _Mapping]] = ..., babysit_pr_in_cloud_params: _Optional[_Union[SelectedAgenticGitActionBabysitPrInCloudParams, _Mapping]] = ..., apply_locally_params: _Optional[_Union[SelectedAgenticGitActionPullLocallyParams, _Mapping]] = ..., checkout_branch_params: _Optional[_Union[SelectedAgenticGitActionPullLocallyParams, _Mapping]] = ..., create_branch_and_commit_params: _Optional[_Union[SelectedAgenticGitActionCommitParams, _Mapping]] = ..., create_branch_commit_and_push_params: _Optional[_Union[SelectedAgenticGitActionCommitParams, _Mapping]] = ..., update_branch_params: _Optional[_Union[SelectedAgenticGitActionUpdateBranchParams, _Mapping]] = ..., create_branch_params: _Optional[_Union[SelectedAgenticGitActionCreateBranchParams, _Mapping]] = ...) -> None: ...

class SelectedAgenticGitActionBabysitPrInCloudParams(_message.Message):
    __slots__ = ("base_branch",)
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    base_branch: str
    def __init__(self, base_branch: _Optional[str] = ...) -> None: ...

class SelectedAgenticGitActionCommitParams(_message.Message):
    __slots__ = ("files_to_commit", "files_to_exclude_from_commit", "should_stage_all_changes", "create_pr_draft", "files_to_commit_with_status", "files_to_exclude_from_commit_with_status")
    FILES_TO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_EXCLUDE_FROM_COMMIT_FIELD_NUMBER: _ClassVar[int]
    SHOULD_STAGE_ALL_CHANGES_FIELD_NUMBER: _ClassVar[int]
    CREATE_PR_DRAFT_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_COMMIT_WITH_STATUS_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_EXCLUDE_FROM_COMMIT_WITH_STATUS_FIELD_NUMBER: _ClassVar[int]
    files_to_commit: _containers.RepeatedScalarFieldContainer[str]
    files_to_exclude_from_commit: _containers.RepeatedScalarFieldContainer[str]
    should_stage_all_changes: bool
    create_pr_draft: bool
    files_to_commit_with_status: _containers.RepeatedCompositeFieldContainer[SelectedAgenticGitFileWithStatus]
    files_to_exclude_from_commit_with_status: _containers.RepeatedCompositeFieldContainer[SelectedAgenticGitFileWithStatus]
    def __init__(self, files_to_commit: _Optional[_Iterable[str]] = ..., files_to_exclude_from_commit: _Optional[_Iterable[str]] = ..., should_stage_all_changes: _Optional[bool] = ..., create_pr_draft: _Optional[bool] = ..., files_to_commit_with_status: _Optional[_Iterable[_Union[SelectedAgenticGitFileWithStatus, _Mapping]]] = ..., files_to_exclude_from_commit_with_status: _Optional[_Iterable[_Union[SelectedAgenticGitFileWithStatus, _Mapping]]] = ...) -> None: ...

class SelectedAgenticGitActionCreateBranchParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SelectedAgenticGitActionFixMergeConflictsParams(_message.Message):
    __slots__ = ("base_branch", "pr_url")
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    base_branch: str
    pr_url: str
    def __init__(self, base_branch: _Optional[str] = ..., pr_url: _Optional[str] = ...) -> None: ...

class SelectedAgenticGitActionPullLocallyParams(_message.Message):
    __slots__ = ("remote_branch",)
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    remote_branch: str
    def __init__(self, remote_branch: _Optional[str] = ...) -> None: ...

class SelectedAgenticGitActionPushParams(_message.Message):
    __slots__ = ("files_to_push", "create_pr_draft")
    FILES_TO_PUSH_FIELD_NUMBER: _ClassVar[int]
    CREATE_PR_DRAFT_FIELD_NUMBER: _ClassVar[int]
    files_to_push: _containers.RepeatedScalarFieldContainer[str]
    create_pr_draft: bool
    def __init__(self, files_to_push: _Optional[_Iterable[str]] = ..., create_pr_draft: _Optional[bool] = ...) -> None: ...

class SelectedAgenticGitActionUpdateBranchParams(_message.Message):
    __slots__ = ("base_branch",)
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    base_branch: str
    def __init__(self, base_branch: _Optional[str] = ...) -> None: ...

class SelectedAgenticGitFileWithStatus(_message.Message):
    __slots__ = ("path", "status")
    PATH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    path: str
    status: str
    def __init__(self, path: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class SelectedBrowser(_message.Message):
    __slots__ = ("browser_id", "url", "page_title")
    BROWSER_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
    browser_id: str
    url: str
    page_title: str
    def __init__(self, browser_id: _Optional[str] = ..., url: _Optional[str] = ..., page_title: _Optional[str] = ...) -> None: ...

class SelectedCodeSelection(_message.Message):
    __slots__ = ("content", "path", "relative_path", "range")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    content: str
    path: str
    relative_path: str
    range: Range
    def __init__(self, content: _Optional[str] = ..., path: _Optional[str] = ..., relative_path: _Optional[str] = ..., range: _Optional[_Union[Range, _Mapping]] = ...) -> None: ...

class SelectedConsoleLog(_message.Message):
    __slots__ = ("message", "timestamp", "level", "client_name", "session_id", "stack_trace", "object_data_json")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_DATA_JSON_FIELD_NUMBER: _ClassVar[int]
    message: str
    timestamp: float
    level: str
    client_name: str
    session_id: str
    stack_trace: StackTrace
    object_data_json: str
    def __init__(self, message: _Optional[str] = ..., timestamp: _Optional[float] = ..., level: _Optional[str] = ..., client_name: _Optional[str] = ..., session_id: _Optional[str] = ..., stack_trace: _Optional[_Union[StackTrace, _Mapping]] = ..., object_data_json: _Optional[str] = ...) -> None: ...

class SelectedContext(_message.Message):
    __slots__ = ("selected_images", "invocation_context", "extra_context", "extra_context_entries", "files", "code_selections", "terminals", "terminal_selections", "folders", "external_links", "cursor_rules", "git_diff", "git_diff_from_branch_to_main", "cursor_commands", "documentations", "ui_elements", "console_logs", "git_commits", "past_chats", "git_pr_diff_selections", "selected_pull_requests", "selected_subagents", "selected_videos", "selected_browsers", "selected_documents", "selected_skills", "recent_agents_context", "selected_agentic_git_action")
    SELECTED_IMAGES_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONTEXT_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CODE_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    TERMINALS_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_LINKS_FIELD_NUMBER: _ClassVar[int]
    CURSOR_RULES_FIELD_NUMBER: _ClassVar[int]
    GIT_DIFF_FIELD_NUMBER: _ClassVar[int]
    GIT_DIFF_FROM_BRANCH_TO_MAIN_FIELD_NUMBER: _ClassVar[int]
    CURSOR_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATIONS_FIELD_NUMBER: _ClassVar[int]
    UI_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_LOGS_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMITS_FIELD_NUMBER: _ClassVar[int]
    PAST_CHATS_FIELD_NUMBER: _ClassVar[int]
    GIT_PR_DIFF_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_PULL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUBAGENTS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_BROWSERS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SKILLS_FIELD_NUMBER: _ClassVar[int]
    RECENT_AGENTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_AGENTIC_GIT_ACTION_FIELD_NUMBER: _ClassVar[int]
    selected_images: _containers.RepeatedCompositeFieldContainer[SelectedImage]
    invocation_context: InvocationContext
    extra_context: _containers.RepeatedScalarFieldContainer[str]
    extra_context_entries: _containers.RepeatedCompositeFieldContainer[ExtraContextEntry]
    files: _containers.RepeatedCompositeFieldContainer[SelectedFile]
    code_selections: _containers.RepeatedCompositeFieldContainer[SelectedCodeSelection]
    terminals: _containers.RepeatedCompositeFieldContainer[SelectedTerminal]
    terminal_selections: _containers.RepeatedCompositeFieldContainer[SelectedTerminalSelection]
    folders: _containers.RepeatedCompositeFieldContainer[SelectedFolder]
    external_links: _containers.RepeatedCompositeFieldContainer[SelectedExternalLink]
    cursor_rules: _containers.RepeatedCompositeFieldContainer[SelectedCursorRule]
    git_diff: SelectedGitDiff
    git_diff_from_branch_to_main: SelectedGitDiffFromBranchToMain
    cursor_commands: _containers.RepeatedCompositeFieldContainer[SelectedCursorCommand]
    documentations: _containers.RepeatedCompositeFieldContainer[SelectedDocumentation]
    ui_elements: _containers.RepeatedCompositeFieldContainer[SelectedUIElement]
    console_logs: _containers.RepeatedCompositeFieldContainer[SelectedConsoleLog]
    git_commits: _containers.RepeatedCompositeFieldContainer[SelectedGitCommit]
    past_chats: _containers.RepeatedCompositeFieldContainer[SelectedPastChat]
    git_pr_diff_selections: _containers.RepeatedCompositeFieldContainer[SelectedGitPRDiffSelection]
    selected_pull_requests: _containers.RepeatedCompositeFieldContainer[SelectedPullRequest]
    selected_subagents: _containers.RepeatedCompositeFieldContainer[SelectedSubagent]
    selected_videos: _containers.RepeatedCompositeFieldContainer[SelectedVideo]
    selected_browsers: _containers.RepeatedCompositeFieldContainer[SelectedBrowser]
    selected_documents: _containers.RepeatedCompositeFieldContainer[SelectedDocument]
    selected_skills: _containers.RepeatedCompositeFieldContainer[AgentSkill]
    recent_agents_context: RecentAgentsContext
    selected_agentic_git_action: SelectedAgenticGitAction
    def __init__(self, selected_images: _Optional[_Iterable[_Union[SelectedImage, _Mapping]]] = ..., invocation_context: _Optional[_Union[InvocationContext, _Mapping]] = ..., extra_context: _Optional[_Iterable[str]] = ..., extra_context_entries: _Optional[_Iterable[_Union[ExtraContextEntry, _Mapping]]] = ..., files: _Optional[_Iterable[_Union[SelectedFile, _Mapping]]] = ..., code_selections: _Optional[_Iterable[_Union[SelectedCodeSelection, _Mapping]]] = ..., terminals: _Optional[_Iterable[_Union[SelectedTerminal, _Mapping]]] = ..., terminal_selections: _Optional[_Iterable[_Union[SelectedTerminalSelection, _Mapping]]] = ..., folders: _Optional[_Iterable[_Union[SelectedFolder, _Mapping]]] = ..., external_links: _Optional[_Iterable[_Union[SelectedExternalLink, _Mapping]]] = ..., cursor_rules: _Optional[_Iterable[_Union[SelectedCursorRule, _Mapping]]] = ..., git_diff: _Optional[_Union[SelectedGitDiff, _Mapping]] = ..., git_diff_from_branch_to_main: _Optional[_Union[SelectedGitDiffFromBranchToMain, _Mapping]] = ..., cursor_commands: _Optional[_Iterable[_Union[SelectedCursorCommand, _Mapping]]] = ..., documentations: _Optional[_Iterable[_Union[SelectedDocumentation, _Mapping]]] = ..., ui_elements: _Optional[_Iterable[_Union[SelectedUIElement, _Mapping]]] = ..., console_logs: _Optional[_Iterable[_Union[SelectedConsoleLog, _Mapping]]] = ..., git_commits: _Optional[_Iterable[_Union[SelectedGitCommit, _Mapping]]] = ..., past_chats: _Optional[_Iterable[_Union[SelectedPastChat, _Mapping]]] = ..., git_pr_diff_selections: _Optional[_Iterable[_Union[SelectedGitPRDiffSelection, _Mapping]]] = ..., selected_pull_requests: _Optional[_Iterable[_Union[SelectedPullRequest, _Mapping]]] = ..., selected_subagents: _Optional[_Iterable[_Union[SelectedSubagent, _Mapping]]] = ..., selected_videos: _Optional[_Iterable[_Union[SelectedVideo, _Mapping]]] = ..., selected_browsers: _Optional[_Iterable[_Union[SelectedBrowser, _Mapping]]] = ..., selected_documents: _Optional[_Iterable[_Union[SelectedDocument, _Mapping]]] = ..., selected_skills: _Optional[_Iterable[_Union[AgentSkill, _Mapping]]] = ..., recent_agents_context: _Optional[_Union[RecentAgentsContext, _Mapping]] = ..., selected_agentic_git_action: _Optional[_Union[SelectedAgenticGitAction, _Mapping]] = ...) -> None: ...

class SelectedCursorCommand(_message.Message):
    __slots__ = ("name", "content", "plugin_capability", "full_path", "display_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    FULL_PATH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    content: str
    plugin_capability: SelectedPluginCapabilityRef
    full_path: str
    display_name: str
    def __init__(self, name: _Optional[str] = ..., content: _Optional[str] = ..., plugin_capability: _Optional[_Union[SelectedPluginCapabilityRef, _Mapping]] = ..., full_path: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...

class SelectedCursorRule(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: CursorRule
    def __init__(self, rule: _Optional[_Union[CursorRule, _Mapping]] = ...) -> None: ...

class SelectedDocument(_message.Message):
    __slots__ = ("uuid", "filename", "mime_type", "path", "blob_id", "data", "blob_id_with_data", "prompt_upload_ref")
    class BlobIdWithData(_message.Message):
        __slots__ = ("blob_id", "data")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        blob_id: bytes
        data: bytes
        def __init__(self, blob_id: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_WITH_DATA_FIELD_NUMBER: _ClassVar[int]
    PROMPT_UPLOAD_REF_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    filename: str
    mime_type: str
    path: str
    blob_id: bytes
    data: bytes
    blob_id_with_data: SelectedDocument.BlobIdWithData
    prompt_upload_ref: PromptUploadRef
    def __init__(self, uuid: _Optional[str] = ..., filename: _Optional[str] = ..., mime_type: _Optional[str] = ..., path: _Optional[str] = ..., blob_id: _Optional[bytes] = ..., data: _Optional[bytes] = ..., blob_id_with_data: _Optional[_Union[SelectedDocument.BlobIdWithData, _Mapping]] = ..., prompt_upload_ref: _Optional[_Union[PromptUploadRef, _Mapping]] = ...) -> None: ...

class SelectedDocumentation(_message.Message):
    __slots__ = ("doc_id", "name")
    DOC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    doc_id: str
    name: str
    def __init__(self, doc_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SelectedExternalLink(_message.Message):
    __slots__ = ("url", "uuid", "pdf_content", "is_pdf", "filename", "blob_id")
    URL_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    PDF_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_PDF_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    uuid: str
    pdf_content: str
    is_pdf: bool
    filename: str
    blob_id: bytes
    def __init__(self, url: _Optional[str] = ..., uuid: _Optional[str] = ..., pdf_content: _Optional[str] = ..., is_pdf: _Optional[bool] = ..., filename: _Optional[str] = ..., blob_id: _Optional[bytes] = ...) -> None: ...

class SelectedFile(_message.Message):
    __slots__ = ("content", "path", "relative_path")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    content: str
    path: str
    relative_path: str
    def __init__(self, content: _Optional[str] = ..., path: _Optional[str] = ..., relative_path: _Optional[str] = ...) -> None: ...

class SelectedFolder(_message.Message):
    __slots__ = ("path", "relative_path", "directory_tree")
    PATH_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_TREE_FIELD_NUMBER: _ClassVar[int]
    path: str
    relative_path: str
    directory_tree: LsDirectoryTreeNode
    def __init__(self, path: _Optional[str] = ..., relative_path: _Optional[str] = ..., directory_tree: _Optional[_Union[LsDirectoryTreeNode, _Mapping]] = ...) -> None: ...

class SelectedGitBranchContext(_message.Message):
    __slots__ = ("current_branch", "base_branch", "agent_branch_prefix")
    CURRENT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    AGENT_BRANCH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    current_branch: str
    base_branch: str
    agent_branch_prefix: str
    def __init__(self, current_branch: _Optional[str] = ..., base_branch: _Optional[str] = ..., agent_branch_prefix: _Optional[str] = ...) -> None: ...

class SelectedGitCommit(_message.Message):
    __slots__ = ("sha", "message", "description", "diff")
    SHA_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIFF_FIELD_NUMBER: _ClassVar[int]
    sha: str
    message: str
    description: str
    diff: str
    def __init__(self, sha: _Optional[str] = ..., message: _Optional[str] = ..., description: _Optional[str] = ..., diff: _Optional[str] = ...) -> None: ...

class SelectedGitDiff(_message.Message):
    __slots__ = ("content", "full_content_length_char_count")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FULL_CONTENT_LENGTH_CHAR_COUNT_FIELD_NUMBER: _ClassVar[int]
    content: str
    full_content_length_char_count: int
    def __init__(self, content: _Optional[str] = ..., full_content_length_char_count: _Optional[int] = ...) -> None: ...

class SelectedGitDiffFromBranchToMain(_message.Message):
    __slots__ = ("content", "full_content_length_char_count")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FULL_CONTENT_LENGTH_CHAR_COUNT_FIELD_NUMBER: _ClassVar[int]
    content: str
    full_content_length_char_count: int
    def __init__(self, content: _Optional[str] = ..., full_content_length_char_count: _Optional[int] = ...) -> None: ...

class SelectedGitPRDiffSelection(_message.Message):
    __slots__ = ("pr_url", "file_path", "start_line", "end_line", "diff_content", "blob_id")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    START_LINE_FIELD_NUMBER: _ClassVar[int]
    END_LINE_FIELD_NUMBER: _ClassVar[int]
    DIFF_CONTENT_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    file_path: str
    start_line: int
    end_line: int
    diff_content: str
    blob_id: bytes
    def __init__(self, pr_url: _Optional[str] = ..., file_path: _Optional[str] = ..., start_line: _Optional[int] = ..., end_line: _Optional[int] = ..., diff_content: _Optional[str] = ..., blob_id: _Optional[bytes] = ...) -> None: ...

class SelectedImage(_message.Message):
    __slots__ = ("uuid", "path", "dimension", "mime_type", "blob_id", "data", "blob_id_with_data")
    class BlobIdWithData(_message.Message):
        __slots__ = ("blob_id", "data")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        blob_id: bytes
        data: bytes
        def __init__(self, blob_id: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...
    class Dimension(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_WITH_DATA_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    path: str
    dimension: SelectedImage.Dimension
    mime_type: str
    blob_id: bytes
    data: bytes
    blob_id_with_data: SelectedImage.BlobIdWithData
    def __init__(self, uuid: _Optional[str] = ..., path: _Optional[str] = ..., dimension: _Optional[_Union[SelectedImage.Dimension, _Mapping]] = ..., mime_type: _Optional[str] = ..., blob_id: _Optional[bytes] = ..., data: _Optional[bytes] = ..., blob_id_with_data: _Optional[_Union[SelectedImage.BlobIdWithData, _Mapping]] = ...) -> None: ...

class SelectedPastChat(_message.Message):
    __slots__ = ("agent_id", "name")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SelectedPluginCapabilityRef(_message.Message):
    __slots__ = ("plugin_id", "capability_type", "source_path", "snapshot_token", "resolved_commit_sha")
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    CAPABILITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    plugin_id: str
    capability_type: SelectedPluginCapabilityType
    source_path: str
    snapshot_token: str
    resolved_commit_sha: str
    def __init__(self, plugin_id: _Optional[str] = ..., capability_type: _Optional[_Union[SelectedPluginCapabilityType, str]] = ..., source_path: _Optional[str] = ..., snapshot_token: _Optional[str] = ..., resolved_commit_sha: _Optional[str] = ...) -> None: ...

class SelectedPullRequest(_message.Message):
    __slots__ = ("number", "url", "title", "folder_path", "summary_json", "description", "blob_id")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_JSON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    number: int
    url: str
    title: str
    folder_path: str
    summary_json: str
    description: str
    blob_id: bytes
    def __init__(self, number: _Optional[int] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., folder_path: _Optional[str] = ..., summary_json: _Optional[str] = ..., description: _Optional[str] = ..., blob_id: _Optional[bytes] = ...) -> None: ...

class SelectedSubagent(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SelectedTerminal(_message.Message):
    __slots__ = ("content", "title", "path")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    content: str
    title: str
    path: str
    def __init__(self, content: _Optional[str] = ..., title: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class SelectedTerminalSelection(_message.Message):
    __slots__ = ("content", "title", "path", "range")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    content: str
    title: str
    path: str
    range: Range
    def __init__(self, content: _Optional[str] = ..., title: _Optional[str] = ..., path: _Optional[str] = ..., range: _Optional[_Union[Range, _Mapping]] = ...) -> None: ...

class SelectedUIElement(_message.Message):
    __slots__ = ("element", "xpath", "text_content", "extra", "component", "component_props_json")
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    XPATH_FIELD_NUMBER: _ClassVar[int]
    TEXT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_PROPS_JSON_FIELD_NUMBER: _ClassVar[int]
    element: str
    xpath: str
    text_content: str
    extra: str
    component: str
    component_props_json: str
    def __init__(self, element: _Optional[str] = ..., xpath: _Optional[str] = ..., text_content: _Optional[str] = ..., extra: _Optional[str] = ..., component: _Optional[str] = ..., component_props_json: _Optional[str] = ...) -> None: ...

class SelectedVideo(_message.Message):
    __slots__ = ("uuid", "path", "fps", "mime_type", "filename", "materialize_to_filesystem", "blob_id", "data", "blob_id_with_data", "signed_url")
    class BlobIdWithData(_message.Message):
        __slots__ = ("blob_id", "data")
        BLOB_ID_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        blob_id: bytes
        data: bytes
        def __init__(self, blob_id: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...
    class SignedUrl(_message.Message):
        __slots__ = ("url", "key", "expires_at_unix_ms", "refresh_after_unix_ms", "conversation_id")
        URL_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        EXPIRES_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_AFTER_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
        CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
        url: str
        key: str
        expires_at_unix_ms: int
        refresh_after_unix_ms: int
        conversation_id: str
        def __init__(self, url: _Optional[str] = ..., key: _Optional[str] = ..., expires_at_unix_ms: _Optional[int] = ..., refresh_after_unix_ms: _Optional[int] = ..., conversation_id: _Optional[str] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZE_TO_FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BLOB_ID_WITH_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNED_URL_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    path: str
    fps: float
    mime_type: str
    filename: str
    materialize_to_filesystem: bool
    blob_id: bytes
    data: bytes
    blob_id_with_data: SelectedVideo.BlobIdWithData
    signed_url: SelectedVideo.SignedUrl
    def __init__(self, uuid: _Optional[str] = ..., path: _Optional[str] = ..., fps: _Optional[float] = ..., mime_type: _Optional[str] = ..., filename: _Optional[str] = ..., materialize_to_filesystem: _Optional[bool] = ..., blob_id: _Optional[bytes] = ..., data: _Optional[bytes] = ..., blob_id_with_data: _Optional[_Union[SelectedVideo.BlobIdWithData, _Mapping]] = ..., signed_url: _Optional[_Union[SelectedVideo.SignedUrl, _Mapping]] = ...) -> None: ...

class SelfHostedPoolTarget(_message.Message):
    __slots__ = ("pool", "labels")
    POOL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    pool: str
    labels: _containers.RepeatedCompositeFieldContainer[SelfHostedWorkerLabel]
    def __init__(self, pool: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[SelfHostedWorkerLabel, _Mapping]]] = ...) -> None: ...

class SelfHostedWorkerLabel(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SelfHostedWorkerTarget(_message.Message):
    __slots__ = ("worker_id",)
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    worker_id: str
    def __init__(self, worker_id: _Optional[str] = ...) -> None: ...

class SemSearchToolArgs(_message.Message):
    __slots__ = ("query", "target_directories", "explanation")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TARGET_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    query: str
    target_directories: _containers.RepeatedScalarFieldContainer[str]
    explanation: str
    def __init__(self, query: _Optional[str] = ..., target_directories: _Optional[_Iterable[str]] = ..., explanation: _Optional[str] = ...) -> None: ...

class SemSearchToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SemSearchToolArgs
    result: SemSearchToolResult
    def __init__(self, args: _Optional[_Union[SemSearchToolArgs, _Mapping]] = ..., result: _Optional[_Union[SemSearchToolResult, _Mapping]] = ...) -> None: ...

class SemSearchToolError(_message.Message):
    __slots__ = ("error_message",)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    def __init__(self, error_message: _Optional[str] = ...) -> None: ...

class SemSearchToolResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SemSearchToolSuccess
    error: SemSearchToolError
    def __init__(self, success: _Optional[_Union[SemSearchToolSuccess, _Mapping]] = ..., error: _Optional[_Union[SemSearchToolError, _Mapping]] = ...) -> None: ...

class SemSearchToolSuccess(_message.Message):
    __slots__ = ("results", "code_results")
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    CODE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: str
    code_results: _containers.RepeatedCompositeFieldContainer[CodeResult]
    def __init__(self, results: _Optional[str] = ..., code_results: _Optional[_Iterable[_Union[CodeResult, _Mapping]]] = ...) -> None: ...

class SendAgentHostActionRequest(_message.Message):
    __slots__ = ("session_id", "action", "model_id", "model_details", "turn_options", "requested_model", "base_history")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TURN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_MODEL_FIELD_NUMBER: _ClassVar[int]
    BASE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    action: ConversationAction
    model_id: str
    model_details: ModelDetails
    turn_options: AgentHostTurnOptions
    requested_model: RequestedModel
    base_history: ConversationStateStructure
    def __init__(self, session_id: _Optional[str] = ..., action: _Optional[_Union[ConversationAction, _Mapping]] = ..., model_id: _Optional[str] = ..., model_details: _Optional[_Union[ModelDetails, _Mapping]] = ..., turn_options: _Optional[_Union[AgentHostTurnOptions, _Mapping]] = ..., requested_model: _Optional[_Union[RequestedModel, _Mapping]] = ..., base_history: _Optional[_Union[ConversationStateStructure, _Mapping]] = ...) -> None: ...

class SendAgentHostActionResponse(_message.Message):
    __slots__ = ("turn_id",)
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    def __init__(self, turn_id: _Optional[str] = ...) -> None: ...

class SendAgentHostMessageRequest(_message.Message):
    __slots__ = ("session_id", "text", "model_id", "model_details", "turn_options", "requested_model")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    TURN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_MODEL_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    text: str
    model_id: str
    model_details: ModelDetails
    turn_options: AgentHostTurnOptions
    requested_model: RequestedModel
    def __init__(self, session_id: _Optional[str] = ..., text: _Optional[str] = ..., model_id: _Optional[str] = ..., model_details: _Optional[_Union[ModelDetails, _Mapping]] = ..., turn_options: _Optional[_Union[AgentHostTurnOptions, _Mapping]] = ..., requested_model: _Optional[_Union[RequestedModel, _Mapping]] = ...) -> None: ...

class SendAgentHostMessageResponse(_message.Message):
    __slots__ = ("turn_id",)
    TURN_ID_FIELD_NUMBER: _ClassVar[int]
    turn_id: str
    def __init__(self, turn_id: _Optional[str] = ...) -> None: ...

class SendFinalSummaryArgs(_message.Message):
    __slots__ = ("final_summary",)
    FINAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    final_summary: str
    def __init__(self, final_summary: _Optional[str] = ...) -> None: ...

class SendFinalSummaryError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class SendFinalSummaryResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SendFinalSummarySuccess
    error: SendFinalSummaryError
    def __init__(self, success: _Optional[_Union[SendFinalSummarySuccess, _Mapping]] = ..., error: _Optional[_Union[SendFinalSummaryError, _Mapping]] = ...) -> None: ...

class SendFinalSummarySuccess(_message.Message):
    __slots__ = ("final_summary",)
    FINAL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    final_summary: str
    def __init__(self, final_summary: _Optional[str] = ...) -> None: ...

class SendFinalSummaryToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SendFinalSummaryArgs
    result: SendFinalSummaryResult
    def __init__(self, args: _Optional[_Union[SendFinalSummaryArgs, _Mapping]] = ..., result: _Optional[_Union[SendFinalSummaryResult, _Mapping]] = ...) -> None: ...

class SendInputRequest(_message.Message):
    __slots__ = ("pty_id", "data")
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    data: bytes
    def __init__(self, pty_id: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class SendInputResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class SendMessageArgs(_message.Message):
    __slots__ = ("text", "attachment")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    text: SendMessageText
    attachment: SendMessageAttachment
    def __init__(self, text: _Optional[_Union[SendMessageText, _Mapping]] = ..., attachment: _Optional[_Union[SendMessageAttachment, _Mapping]] = ...) -> None: ...

class SendMessageAttachment(_message.Message):
    __slots__ = ("url", "alt")
    URL_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    url: str
    alt: str
    def __init__(self, url: _Optional[str] = ..., alt: _Optional[str] = ...) -> None: ...

class SendMessageError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class SendMessageResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SendMessageSuccess
    error: SendMessageError
    def __init__(self, success: _Optional[_Union[SendMessageSuccess, _Mapping]] = ..., error: _Optional[_Union[SendMessageError, _Mapping]] = ...) -> None: ...

class SendMessageSuccess(_message.Message):
    __slots__ = ("timestamp", "message_id")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    message_id: str
    def __init__(self, timestamp: _Optional[int] = ..., message_id: _Optional[str] = ...) -> None: ...

class SendMessageText(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class SendMessageToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SendMessageArgs
    result: SendMessageResult
    def __init__(self, args: _Optional[_Union[SendMessageArgs, _Mapping]] = ..., result: _Optional[_Union[SendMessageResult, _Mapping]] = ...) -> None: ...

class SendToUserArgs(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SendToUserError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class SendToUserResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SendToUserSuccess
    error: SendToUserError
    def __init__(self, success: _Optional[_Union[SendToUserSuccess, _Mapping]] = ..., error: _Optional[_Union[SendToUserError, _Mapping]] = ...) -> None: ...

class SendToUserSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendToUserToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SendToUserArgs
    result: SendToUserResult
    def __init__(self, args: _Optional[_Union[SendToUserArgs, _Mapping]] = ..., result: _Optional[_Union[SendToUserResult, _Mapping]] = ...) -> None: ...

class SessionParent(_message.Message):
    __slots__ = ("parent_session_id", "parent_tool_call_id", "root_session_id")
    PARENT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    parent_session_id: str
    parent_tool_call_id: str
    root_session_id: str
    def __init__(self, parent_session_id: _Optional[str] = ..., parent_tool_call_id: _Optional[str] = ..., root_session_id: _Optional[str] = ...) -> None: ...

class SetActiveBranchArgs(_message.Message):
    __slots__ = ("path", "branch_name")
    PATH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    path: str
    branch_name: str
    def __init__(self, path: _Optional[str] = ..., branch_name: _Optional[str] = ...) -> None: ...

class SetActiveBranchError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class SetActiveBranchResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SetActiveBranchSuccess
    error: SetActiveBranchError
    def __init__(self, success: _Optional[_Union[SetActiveBranchSuccess, _Mapping]] = ..., error: _Optional[_Union[SetActiveBranchError, _Mapping]] = ...) -> None: ...

class SetActiveBranchSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetActiveBranchToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SetActiveBranchArgs
    result: SetActiveBranchResult
    def __init__(self, args: _Optional[_Union[SetActiveBranchArgs, _Mapping]] = ..., result: _Optional[_Union[SetActiveBranchResult, _Mapping]] = ...) -> None: ...

class SetBlobArgs(_message.Message):
    __slots__ = ("blob_id", "blob_data")
    BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_DATA_FIELD_NUMBER: _ClassVar[int]
    blob_id: bytes
    blob_data: bytes
    def __init__(self, blob_id: _Optional[bytes] = ..., blob_data: _Optional[bytes] = ...) -> None: ...

class SetBlobResult(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: Error
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class SetPrStatusAction(_message.Message):
    __slots__ = ("pr_url", "branch_name", "repo_url", "status")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    branch_name: str
    repo_url: str
    status: PullRequestStatus
    def __init__(self, pr_url: _Optional[str] = ..., branch_name: _Optional[str] = ..., repo_url: _Optional[str] = ..., status: _Optional[_Union[PullRequestStatus, str]] = ...) -> None: ...

class SetupVmEnvironmentArgs(_message.Message):
    __slots__ = ("install_command", "start_command", "dockerfile_contents")
    INSTALL_COMMAND_FIELD_NUMBER: _ClassVar[int]
    START_COMMAND_FIELD_NUMBER: _ClassVar[int]
    DOCKERFILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    install_command: str
    start_command: str
    dockerfile_contents: str
    def __init__(self, install_command: _Optional[str] = ..., start_command: _Optional[str] = ..., dockerfile_contents: _Optional[str] = ...) -> None: ...

class SetupVmEnvironmentResult(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: SetupVmEnvironmentSuccess
    def __init__(self, success: _Optional[_Union[SetupVmEnvironmentSuccess, _Mapping]] = ...) -> None: ...

class SetupVmEnvironmentSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetupVmEnvironmentToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SetupVmEnvironmentArgs
    result: SetupVmEnvironmentResult
    def __init__(self, args: _Optional[_Union[SetupVmEnvironmentArgs, _Mapping]] = ..., result: _Optional[_Union[SetupVmEnvironmentResult, _Mapping]] = ...) -> None: ...

class ShellAllowlistPrecheckArgs(_message.Message):
    __slots__ = ("command", "working_directory", "parsing_result", "classifier_result", "tool_call_id")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    PARSING_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIER_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    parsing_result: ShellCommandParsingResult
    classifier_result: CommandClassifierResult
    tool_call_id: str
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., parsing_result: _Optional[_Union[ShellCommandParsingResult, _Mapping]] = ..., classifier_result: _Optional[_Union[CommandClassifierResult, _Mapping]] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class ShellAllowlistPrecheckResult(_message.Message):
    __slots__ = ("allowlisted",)
    ALLOWLISTED_FIELD_NUMBER: _ClassVar[int]
    allowlisted: bool
    def __init__(self, allowlisted: _Optional[bool] = ...) -> None: ...

class ShellArgs(_message.Message):
    __slots__ = ("command", "working_directory", "timeout", "tool_call_id", "simple_commands", "has_input_redirect", "has_output_redirect", "parsing_result", "requested_sandbox_policy", "file_output_threshold_bytes", "is_background", "skip_approval", "timeout_behavior", "hard_timeout", "description", "classifier_result", "close_stdin", "output_notification", "smart_mode_approval", "hook_approval_requirement", "conversation_id", "admin_command_denylist")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    HAS_INPUT_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    HAS_OUTPUT_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    PARSING_RESULT_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_SANDBOX_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILE_OUTPUT_THRESHOLD_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    SKIP_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    HARD_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIER_RESULT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_STDIN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    HOOK_APPROVAL_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_COMMAND_DENYLIST_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    timeout: int
    tool_call_id: str
    simple_commands: _containers.RepeatedScalarFieldContainer[str]
    has_input_redirect: bool
    has_output_redirect: bool
    parsing_result: ShellCommandParsingResult
    requested_sandbox_policy: SandboxPolicy
    file_output_threshold_bytes: int
    is_background: bool
    skip_approval: bool
    timeout_behavior: TimeoutBehavior
    hard_timeout: int
    description: str
    classifier_result: CommandClassifierResult
    close_stdin: bool
    output_notification: ShellOutputNotificationConfig
    smart_mode_approval: SmartModeApproval
    hook_approval_requirement: ShellHookApprovalRequirement
    conversation_id: str
    admin_command_denylist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., timeout: _Optional[int] = ..., tool_call_id: _Optional[str] = ..., simple_commands: _Optional[_Iterable[str]] = ..., has_input_redirect: _Optional[bool] = ..., has_output_redirect: _Optional[bool] = ..., parsing_result: _Optional[_Union[ShellCommandParsingResult, _Mapping]] = ..., requested_sandbox_policy: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., file_output_threshold_bytes: _Optional[int] = ..., is_background: _Optional[bool] = ..., skip_approval: _Optional[bool] = ..., timeout_behavior: _Optional[_Union[TimeoutBehavior, str]] = ..., hard_timeout: _Optional[int] = ..., description: _Optional[str] = ..., classifier_result: _Optional[_Union[CommandClassifierResult, _Mapping]] = ..., close_stdin: _Optional[bool] = ..., output_notification: _Optional[_Union[ShellOutputNotificationConfig, _Mapping]] = ..., smart_mode_approval: _Optional[_Union[SmartModeApproval, _Mapping]] = ..., hook_approval_requirement: _Optional[_Union[ShellHookApprovalRequirement, _Mapping]] = ..., conversation_id: _Optional[str] = ..., admin_command_denylist: _Optional[_Iterable[str]] = ...) -> None: ...

class ShellCommand(_message.Message):
    __slots__ = ("command",)
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    command: str
    def __init__(self, command: _Optional[str] = ...) -> None: ...

class ShellCommandAction(_message.Message):
    __slots__ = ("shell_command", "exec_id")
    SHELL_COMMAND_FIELD_NUMBER: _ClassVar[int]
    EXEC_ID_FIELD_NUMBER: _ClassVar[int]
    shell_command: ShellCommand
    exec_id: str
    def __init__(self, shell_command: _Optional[_Union[ShellCommand, _Mapping]] = ..., exec_id: _Optional[str] = ...) -> None: ...

class ShellCommandParsingResult(_message.Message):
    __slots__ = ("parsing_failed", "executable_commands", "has_redirects", "has_command_substitution", "all_redirects_are_dev_null", "redirects")
    class ExecutableCommand(_message.Message):
        __slots__ = ("name", "args", "full_text")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        FULL_TEXT_FIELD_NUMBER: _ClassVar[int]
        name: str
        args: _containers.RepeatedCompositeFieldContainer[ShellCommandParsingResult.ExecutableCommandArg]
        full_text: str
        def __init__(self, name: _Optional[str] = ..., args: _Optional[_Iterable[_Union[ShellCommandParsingResult.ExecutableCommandArg, _Mapping]]] = ..., full_text: _Optional[str] = ...) -> None: ...
    class ExecutableCommandArg(_message.Message):
        __slots__ = ("type", "value")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        type: str
        value: str
        def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Redirect(_message.Message):
        __slots__ = ("operator", "destination_fds", "target_node_type", "target_text")
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_FDS_FIELD_NUMBER: _ClassVar[int]
        TARGET_NODE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TARGET_TEXT_FIELD_NUMBER: _ClassVar[int]
        operator: str
        destination_fds: _containers.RepeatedScalarFieldContainer[int]
        target_node_type: str
        target_text: str
        def __init__(self, operator: _Optional[str] = ..., destination_fds: _Optional[_Iterable[int]] = ..., target_node_type: _Optional[str] = ..., target_text: _Optional[str] = ...) -> None: ...
    PARSING_FAILED_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    HAS_REDIRECTS_FIELD_NUMBER: _ClassVar[int]
    HAS_COMMAND_SUBSTITUTION_FIELD_NUMBER: _ClassVar[int]
    ALL_REDIRECTS_ARE_DEV_NULL_FIELD_NUMBER: _ClassVar[int]
    REDIRECTS_FIELD_NUMBER: _ClassVar[int]
    parsing_failed: bool
    executable_commands: _containers.RepeatedCompositeFieldContainer[ShellCommandParsingResult.ExecutableCommand]
    has_redirects: bool
    has_command_substitution: bool
    all_redirects_are_dev_null: bool
    redirects: _containers.RepeatedCompositeFieldContainer[ShellCommandParsingResult.Redirect]
    def __init__(self, parsing_failed: _Optional[bool] = ..., executable_commands: _Optional[_Iterable[_Union[ShellCommandParsingResult.ExecutableCommand, _Mapping]]] = ..., has_redirects: _Optional[bool] = ..., has_command_substitution: _Optional[bool] = ..., all_redirects_are_dev_null: _Optional[bool] = ..., redirects: _Optional[_Iterable[_Union[ShellCommandParsingResult.Redirect, _Mapping]]] = ...) -> None: ...

class ShellConversationTurn(_message.Message):
    __slots__ = ("shell_command", "shell_output")
    SHELL_COMMAND_FIELD_NUMBER: _ClassVar[int]
    SHELL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    shell_command: ShellCommand
    shell_output: ShellOutput
    def __init__(self, shell_command: _Optional[_Union[ShellCommand, _Mapping]] = ..., shell_output: _Optional[_Union[ShellOutput, _Mapping]] = ...) -> None: ...

class ShellConversationTurnStructure(_message.Message):
    __slots__ = ("shell_command", "shell_output")
    SHELL_COMMAND_FIELD_NUMBER: _ClassVar[int]
    SHELL_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    shell_command: bytes
    shell_output: bytes
    def __init__(self, shell_command: _Optional[bytes] = ..., shell_output: _Optional[bytes] = ...) -> None: ...

class ShellFailure(_message.Message):
    __slots__ = ("command", "working_directory", "exit_code", "signal", "stdout", "stderr", "execution_time", "output_location", "interleaved_output", "abort_reason", "aborted", "local_execution_time_ms", "output_head", "output_tail", "elided_chars")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    INTERLEAVED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ABORT_REASON_FIELD_NUMBER: _ClassVar[int]
    ABORTED_FIELD_NUMBER: _ClassVar[int]
    LOCAL_EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEAD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TAIL_FIELD_NUMBER: _ClassVar[int]
    ELIDED_CHARS_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    exit_code: int
    signal: str
    stdout: str
    stderr: str
    execution_time: int
    output_location: OutputLocation
    interleaved_output: str
    abort_reason: ShellAbortReason
    aborted: bool
    local_execution_time_ms: int
    output_head: str
    output_tail: str
    elided_chars: int
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., exit_code: _Optional[int] = ..., signal: _Optional[str] = ..., stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., execution_time: _Optional[int] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ..., interleaved_output: _Optional[str] = ..., abort_reason: _Optional[_Union[ShellAbortReason, str]] = ..., aborted: _Optional[bool] = ..., local_execution_time_ms: _Optional[int] = ..., output_head: _Optional[str] = ..., output_tail: _Optional[str] = ..., elided_chars: _Optional[int] = ...) -> None: ...

class ShellHookApprovalRequirement(_message.Message):
    __slots__ = ("kind", "reason")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[ShellHookApprovalRequirement.Kind]
        KIND_FORCE_PROMPT: _ClassVar[ShellHookApprovalRequirement.Kind]
    KIND_UNSPECIFIED: ShellHookApprovalRequirement.Kind
    KIND_FORCE_PROMPT: ShellHookApprovalRequirement.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    kind: ShellHookApprovalRequirement.Kind
    reason: str
    def __init__(self, kind: _Optional[_Union[ShellHookApprovalRequirement.Kind, str]] = ..., reason: _Optional[str] = ...) -> None: ...

class ShellOutput(_message.Message):
    __slots__ = ("stdout", "stderr", "exit_code")
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    stdout: str
    stderr: str
    exit_code: int
    def __init__(self, stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., exit_code: _Optional[int] = ...) -> None: ...

class ShellOutputDeltaUpdate(_message.Message):
    __slots__ = ("stdout", "stderr", "exit", "start")
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    stdout: ShellStreamStdout
    stderr: ShellStreamStderr
    exit: ShellStreamExit
    start: ShellStreamStart
    def __init__(self, stdout: _Optional[_Union[ShellStreamStdout, _Mapping]] = ..., stderr: _Optional[_Union[ShellStreamStderr, _Mapping]] = ..., exit: _Optional[_Union[ShellStreamExit, _Mapping]] = ..., start: _Optional[_Union[ShellStreamStart, _Mapping]] = ...) -> None: ...

class ShellOutputNotificationConfig(_message.Message):
    __slots__ = ("pattern", "reason", "debounce", "notification_limit")
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DEBOUNCE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    reason: str
    debounce: float
    notification_limit: int
    def __init__(self, pattern: _Optional[str] = ..., reason: _Optional[str] = ..., debounce: _Optional[float] = ..., notification_limit: _Optional[int] = ...) -> None: ...

class ShellPartialResult(_message.Message):
    __slots__ = ("stdout_delta", "stderr_delta")
    STDOUT_DELTA_FIELD_NUMBER: _ClassVar[int]
    STDERR_DELTA_FIELD_NUMBER: _ClassVar[int]
    stdout_delta: str
    stderr_delta: str
    def __init__(self, stdout_delta: _Optional[str] = ..., stderr_delta: _Optional[str] = ...) -> None: ...

class ShellPermissionDenied(_message.Message):
    __slots__ = ("command", "working_directory", "error", "is_readonly")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    error: str
    is_readonly: bool
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., error: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class ShellRejected(_message.Message):
    __slots__ = ("command", "working_directory", "reason", "is_readonly")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    reason: str
    is_readonly: bool
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., reason: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class ShellResult(_message.Message):
    __slots__ = ("sandbox_policy", "is_background", "terminals_folder", "pid", "success", "failure", "timeout", "rejected", "spawn_error", "permission_denied")
    SANDBOX_POLICY_FIELD_NUMBER: _ClassVar[int]
    IS_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    TERMINALS_FOLDER_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    SPAWN_ERROR_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    sandbox_policy: SandboxPolicy
    is_background: bool
    terminals_folder: str
    pid: int
    success: ShellSuccess
    failure: ShellFailure
    timeout: ShellTimeout
    rejected: ShellRejected
    spawn_error: ShellSpawnError
    permission_denied: ShellPermissionDenied
    def __init__(self, sandbox_policy: _Optional[_Union[SandboxPolicy, _Mapping]] = ..., is_background: _Optional[bool] = ..., terminals_folder: _Optional[str] = ..., pid: _Optional[int] = ..., success: _Optional[_Union[ShellSuccess, _Mapping]] = ..., failure: _Optional[_Union[ShellFailure, _Mapping]] = ..., timeout: _Optional[_Union[ShellTimeout, _Mapping]] = ..., rejected: _Optional[_Union[ShellRejected, _Mapping]] = ..., spawn_error: _Optional[_Union[ShellSpawnError, _Mapping]] = ..., permission_denied: _Optional[_Union[ShellPermissionDenied, _Mapping]] = ...) -> None: ...

class ShellSandboxUnsupported(_message.Message):
    __slots__ = ("command", "working_directory", "sandbox_policy_type", "reason", "is_readonly")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_POLICY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    sandbox_policy_type: str
    reason: str
    is_readonly: bool
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., sandbox_policy_type: _Optional[str] = ..., reason: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class ShellSpawnError(_message.Message):
    __slots__ = ("command", "working_directory", "error")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    error: str
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class ShellStream(_message.Message):
    __slots__ = ("stdout", "stderr", "exit", "start", "rejected", "permission_denied", "backgrounded", "hook_context", "sandbox_unsupported")
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXIT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    BACKGROUNDED_FIELD_NUMBER: _ClassVar[int]
    HOOK_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_UNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    stdout: ShellStreamStdout
    stderr: ShellStreamStderr
    exit: ShellStreamExit
    start: ShellStreamStart
    rejected: ShellRejected
    permission_denied: ShellPermissionDenied
    backgrounded: ShellStreamBackgrounded
    hook_context: ShellStreamHookContext
    sandbox_unsupported: ShellSandboxUnsupported
    def __init__(self, stdout: _Optional[_Union[ShellStreamStdout, _Mapping]] = ..., stderr: _Optional[_Union[ShellStreamStderr, _Mapping]] = ..., exit: _Optional[_Union[ShellStreamExit, _Mapping]] = ..., start: _Optional[_Union[ShellStreamStart, _Mapping]] = ..., rejected: _Optional[_Union[ShellRejected, _Mapping]] = ..., permission_denied: _Optional[_Union[ShellPermissionDenied, _Mapping]] = ..., backgrounded: _Optional[_Union[ShellStreamBackgrounded, _Mapping]] = ..., hook_context: _Optional[_Union[ShellStreamHookContext, _Mapping]] = ..., sandbox_unsupported: _Optional[_Union[ShellSandboxUnsupported, _Mapping]] = ...) -> None: ...

class ShellStreamBackgrounded(_message.Message):
    __slots__ = ("shell_id", "command", "working_directory", "pid", "ms_to_wait", "reason")
    SHELL_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    MS_TO_WAIT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    shell_id: int
    command: str
    working_directory: str
    pid: int
    ms_to_wait: int
    reason: ShellBackgroundReason
    def __init__(self, shell_id: _Optional[int] = ..., command: _Optional[str] = ..., working_directory: _Optional[str] = ..., pid: _Optional[int] = ..., ms_to_wait: _Optional[int] = ..., reason: _Optional[_Union[ShellBackgroundReason, str]] = ...) -> None: ...

class ShellStreamExit(_message.Message):
    __slots__ = ("code", "cwd", "output_location", "aborted", "abort_reason", "local_execution_time_ms")
    CODE_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ABORTED_FIELD_NUMBER: _ClassVar[int]
    ABORT_REASON_FIELD_NUMBER: _ClassVar[int]
    LOCAL_EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    code: int
    cwd: str
    output_location: OutputLocation
    aborted: bool
    abort_reason: ShellAbortReason
    local_execution_time_ms: int
    def __init__(self, code: _Optional[int] = ..., cwd: _Optional[str] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ..., aborted: _Optional[bool] = ..., abort_reason: _Optional[_Union[ShellAbortReason, str]] = ..., local_execution_time_ms: _Optional[int] = ...) -> None: ...

class ShellStreamHookContext(_message.Message):
    __slots__ = ("hook_additional_contexts",)
    HOOK_ADDITIONAL_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    hook_additional_contexts: _containers.RepeatedCompositeFieldContainer[HookAdditionalContext]
    def __init__(self, hook_additional_contexts: _Optional[_Iterable[_Union[HookAdditionalContext, _Mapping]]] = ...) -> None: ...

class ShellStreamStart(_message.Message):
    __slots__ = ("sandbox_policy",)
    SANDBOX_POLICY_FIELD_NUMBER: _ClassVar[int]
    sandbox_policy: SandboxPolicy
    def __init__(self, sandbox_policy: _Optional[_Union[SandboxPolicy, _Mapping]] = ...) -> None: ...

class ShellStreamStderr(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class ShellStreamStdout(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class ShellSuccess(_message.Message):
    __slots__ = ("command", "working_directory", "exit_code", "signal", "stdout", "stderr", "execution_time", "output_location", "shell_id", "interleaved_output", "pid", "ms_to_wait", "local_execution_time_ms", "background_reason", "output_head", "output_tail", "elided_chars")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SHELL_ID_FIELD_NUMBER: _ClassVar[int]
    INTERLEAVED_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    MS_TO_WAIT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_EXECUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_REASON_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_HEAD_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TAIL_FIELD_NUMBER: _ClassVar[int]
    ELIDED_CHARS_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    exit_code: int
    signal: str
    stdout: str
    stderr: str
    execution_time: int
    output_location: OutputLocation
    shell_id: int
    interleaved_output: str
    pid: int
    ms_to_wait: int
    local_execution_time_ms: int
    background_reason: ShellBackgroundReason
    output_head: str
    output_tail: str
    elided_chars: int
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., exit_code: _Optional[int] = ..., signal: _Optional[str] = ..., stdout: _Optional[str] = ..., stderr: _Optional[str] = ..., execution_time: _Optional[int] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ..., shell_id: _Optional[int] = ..., interleaved_output: _Optional[str] = ..., pid: _Optional[int] = ..., ms_to_wait: _Optional[int] = ..., local_execution_time_ms: _Optional[int] = ..., background_reason: _Optional[_Union[ShellBackgroundReason, str]] = ..., output_head: _Optional[str] = ..., output_tail: _Optional[str] = ..., elided_chars: _Optional[int] = ...) -> None: ...

class ShellTimeout(_message.Message):
    __slots__ = ("command", "working_directory", "timeout_ms")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    command: str
    working_directory: str
    timeout_ms: int
    def __init__(self, command: _Optional[str] = ..., working_directory: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class ShellToolCall(_message.Message):
    __slots__ = ("args", "result", "description")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    args: ShellArgs
    result: ShellResult
    description: str
    def __init__(self, args: _Optional[_Union[ShellArgs, _Mapping]] = ..., result: _Optional[_Union[ShellResult, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class ShellToolCallDelta(_message.Message):
    __slots__ = ("stdout", "stderr")
    STDOUT_FIELD_NUMBER: _ClassVar[int]
    STDERR_FIELD_NUMBER: _ClassVar[int]
    stdout: ShellToolCallStdoutDelta
    stderr: ShellToolCallStderrDelta
    def __init__(self, stdout: _Optional[_Union[ShellToolCallStdoutDelta, _Mapping]] = ..., stderr: _Optional[_Union[ShellToolCallStderrDelta, _Mapping]] = ...) -> None: ...

class ShellToolCallStderrDelta(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class ShellToolCallStdoutDelta(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class SkillDescriptor(_message.Message):
    __slots__ = ("name", "description", "folder_path", "enabled", "parse_error", "readme_file_path", "package_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PARSE_ERROR_FIELD_NUMBER: _ClassVar[int]
    README_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    folder_path: str
    enabled: bool
    parse_error: str
    readme_file_path: str
    package_type: PackageType
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., folder_path: _Optional[str] = ..., enabled: _Optional[bool] = ..., parse_error: _Optional[str] = ..., readme_file_path: _Optional[str] = ..., package_type: _Optional[_Union[PackageType, str]] = ...) -> None: ...

class SkillOptions(_message.Message):
    __slots__ = ("skill_descriptors",)
    SKILL_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    skill_descriptors: _containers.RepeatedCompositeFieldContainer[SkillDescriptor]
    def __init__(self, skill_descriptors: _Optional[_Iterable[_Union[SkillDescriptor, _Mapping]]] = ...) -> None: ...

class SmartModeApproval(_message.Message):
    __slots__ = ("request_id", "reason")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    reason: str
    def __init__(self, request_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class SmartModeClassifierArgs(_message.Message):
    __slots__ = ("tool_call_id", "parent_conversation_id", "target", "conversation_context")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    parent_conversation_id: str
    target: SmartModeRiskTarget
    conversation_context: _containers.RepeatedCompositeFieldContainer[SmartModeClassifierConversationMessage]
    def __init__(self, tool_call_id: _Optional[str] = ..., parent_conversation_id: _Optional[str] = ..., target: _Optional[_Union[SmartModeRiskTarget, _Mapping]] = ..., conversation_context: _Optional[_Iterable[_Union[SmartModeClassifierConversationMessage, _Mapping]]] = ...) -> None: ...

class SmartModeClassifierConversationMessage(_message.Message):
    __slots__ = ("role", "content")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class SmartModeClassifierError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class SmartModeClassifierResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SmartModeClassifierSuccess
    error: SmartModeClassifierError
    def __init__(self, success: _Optional[_Union[SmartModeClassifierSuccess, _Mapping]] = ..., error: _Optional[_Union[SmartModeClassifierError, _Mapping]] = ...) -> None: ...

class SmartModeClassifierSuccess(_message.Message):
    __slots__ = ("decision", "block_reason")
    DECISION_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    decision: SmartModeClassifierDecision
    block_reason: str
    def __init__(self, decision: _Optional[_Union[SmartModeClassifierDecision, str]] = ..., block_reason: _Optional[str] = ...) -> None: ...

class SmartModeRiskTarget(_message.Message):
    __slots__ = ("action", "arguments")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    action: str
    arguments: _struct_pb2.Struct
    def __init__(self, action: _Optional[str] = ..., arguments: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class SpanContext(_message.Message):
    __slots__ = ("trace_id", "span_id", "trace_flags", "trace_state")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    TRACE_STATE_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    span_id: str
    trace_flags: int
    trace_state: str
    def __init__(self, trace_id: _Optional[str] = ..., span_id: _Optional[str] = ..., trace_flags: _Optional[int] = ..., trace_state: _Optional[str] = ...) -> None: ...

class SpawnPtyRequest(_message.Message):
    __slots__ = ("process", "cwd", "env", "cols", "rows")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROCESS_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    COLS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    process: Process
    cwd: str
    env: _containers.ScalarMap[str, str]
    cols: int
    rows: int
    def __init__(self, process: _Optional[_Union[Process, _Mapping]] = ..., cwd: _Optional[str] = ..., env: _Optional[_Mapping[str, str]] = ..., cols: _Optional[int] = ..., rows: _Optional[int] = ...) -> None: ...

class SpawnPtyResponse(_message.Message):
    __slots__ = ("pty_id",)
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    def __init__(self, pty_id: _Optional[str] = ...) -> None: ...

class SpeedupSelection(_message.Message):
    __slots__ = ("candidate_index", "speed_override")
    CANDIDATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    SPEED_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    candidate_index: int
    speed_override: float
    def __init__(self, candidate_index: _Optional[int] = ..., speed_override: _Optional[float] = ...) -> None: ...

class StackTrace(_message.Message):
    __slots__ = ("call_frames", "raw_stack_trace")
    CALL_FRAMES_FIELD_NUMBER: _ClassVar[int]
    RAW_STACK_TRACE_FIELD_NUMBER: _ClassVar[int]
    call_frames: _containers.RepeatedCompositeFieldContainer[CallFrame]
    raw_stack_trace: str
    def __init__(self, call_frames: _Optional[_Iterable[_Union[CallFrame, _Mapping]]] = ..., raw_stack_trace: _Optional[str] = ...) -> None: ...

class StartGrindExecutionArgs(_message.Message):
    __slots__ = ("explanation", "tool_call_id")
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    explanation: str
    tool_call_id: str
    def __init__(self, explanation: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class StartGrindExecutionError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class StartGrindExecutionResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: StartGrindExecutionSuccess
    error: StartGrindExecutionError
    def __init__(self, success: _Optional[_Union[StartGrindExecutionSuccess, _Mapping]] = ..., error: _Optional[_Union[StartGrindExecutionError, _Mapping]] = ...) -> None: ...

class StartGrindExecutionSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartGrindExecutionToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: StartGrindExecutionArgs
    result: StartGrindExecutionResult
    def __init__(self, args: _Optional[_Union[StartGrindExecutionArgs, _Mapping]] = ..., result: _Optional[_Union[StartGrindExecutionResult, _Mapping]] = ...) -> None: ...

class StartGrindPlanningArgs(_message.Message):
    __slots__ = ("explanation", "tool_call_id")
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    explanation: str
    tool_call_id: str
    def __init__(self, explanation: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class StartGrindPlanningError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class StartGrindPlanningResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: StartGrindPlanningSuccess
    error: StartGrindPlanningError
    def __init__(self, success: _Optional[_Union[StartGrindPlanningSuccess, _Mapping]] = ..., error: _Optional[_Union[StartGrindPlanningError, _Mapping]] = ...) -> None: ...

class StartGrindPlanningSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartGrindPlanningToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: StartGrindPlanningArgs
    result: StartGrindPlanningResult
    def __init__(self, args: _Optional[_Union[StartGrindPlanningArgs, _Mapping]] = ..., result: _Optional[_Union[StartGrindPlanningResult, _Mapping]] = ...) -> None: ...

class StartPlanAction(_message.Message):
    __slots__ = ("user_message", "request_context", "is_spec")
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_SPEC_FIELD_NUMBER: _ClassVar[int]
    user_message: UserMessage
    request_context: RequestContext
    is_spec: bool
    def __init__(self, user_message: _Optional[_Union[UserMessage, _Mapping]] = ..., request_context: _Optional[_Union[RequestContext, _Mapping]] = ..., is_spec: _Optional[bool] = ...) -> None: ...

class StderrEvent(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class StdoutEvent(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: str
    def __init__(self, data: _Optional[str] = ...) -> None: ...

class StepCompletedUpdate(_message.Message):
    __slots__ = ("step_id", "step_duration_ms")
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    STEP_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    step_id: int
    step_duration_ms: int
    def __init__(self, step_id: _Optional[int] = ..., step_duration_ms: _Optional[int] = ...) -> None: ...

class StepStartedUpdate(_message.Message):
    __slots__ = ("step_id",)
    STEP_ID_FIELD_NUMBER: _ClassVar[int]
    step_id: int
    def __init__(self, step_id: _Optional[int] = ...) -> None: ...

class StepTiming(_message.Message):
    __slots__ = ("duration_ms", "timestamp_ms")
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    duration_ms: int
    timestamp_ms: int
    def __init__(self, duration_ms: _Optional[int] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class StopRequestQuery(_message.Message):
    __slots__ = ("status", "loop_count", "conversation_id", "generation_id", "model", "model_id", "model_params", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOOP_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    status: str
    loop_count: int
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    def __init__(self, status: _Optional[str] = ..., loop_count: _Optional[int] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ...) -> None: ...

class StopRequestResponse(_message.Message):
    __slots__ = ("followup_message",)
    FOLLOWUP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    followup_message: str
    def __init__(self, followup_message: _Optional[str] = ...) -> None: ...

class SubagentArgs(_message.Message):
    __slots__ = ("tool_call_id", "subagent_type", "model_id", "prompt", "readonly", "resume_agent_id", "run_in_background", "continuation_config", "parent_conversation_id", "interrupt", "mode", "fork_agent_id", "root_parent_conversation_id", "selected_context", "direct_meta_parent_child_subagent", "environment", "cloud_base_branch", "api_key_credentials", "azure_credentials", "bedrock_credentials")
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    RESUME_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_IN_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    INTERRUPT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    FORK_AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PARENT_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DIRECT_META_PARENT_CHILD_SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    tool_call_id: str
    subagent_type: str
    model_id: str
    prompt: str
    readonly: bool
    resume_agent_id: str
    run_in_background: bool
    continuation_config: ClientContinuationConfig
    parent_conversation_id: str
    interrupt: bool
    mode: TaskMode
    fork_agent_id: str
    root_parent_conversation_id: str
    selected_context: SelectedContext
    direct_meta_parent_child_subagent: bool
    environment: SubagentExecutionEnvironment
    cloud_base_branch: str
    api_key_credentials: ApiKeyCredentials
    azure_credentials: AzureCredentials
    bedrock_credentials: BedrockCredentials
    def __init__(self, tool_call_id: _Optional[str] = ..., subagent_type: _Optional[str] = ..., model_id: _Optional[str] = ..., prompt: _Optional[str] = ..., readonly: _Optional[bool] = ..., resume_agent_id: _Optional[str] = ..., run_in_background: _Optional[bool] = ..., continuation_config: _Optional[_Union[ClientContinuationConfig, _Mapping]] = ..., parent_conversation_id: _Optional[str] = ..., interrupt: _Optional[bool] = ..., mode: _Optional[_Union[TaskMode, str]] = ..., fork_agent_id: _Optional[str] = ..., root_parent_conversation_id: _Optional[str] = ..., selected_context: _Optional[_Union[SelectedContext, _Mapping]] = ..., direct_meta_parent_child_subagent: _Optional[bool] = ..., environment: _Optional[_Union[SubagentExecutionEnvironment, str]] = ..., cloud_base_branch: _Optional[str] = ..., api_key_credentials: _Optional[_Union[ApiKeyCredentials, _Mapping]] = ..., azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]] = ..., bedrock_credentials: _Optional[_Union[BedrockCredentials, _Mapping]] = ...) -> None: ...

class SubagentAwaitArgs(_message.Message):
    __slots__ = ("agent_id", "timeout_ms")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    timeout_ms: int
    def __init__(self, agent_id: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class SubagentAwaitComplete(_message.Message):
    __slots__ = ("agent_id", "transcript_path", "tool_call_count", "final_message")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    transcript_path: str
    tool_call_count: int
    final_message: str
    def __init__(self, agent_id: _Optional[str] = ..., transcript_path: _Optional[str] = ..., tool_call_count: _Optional[int] = ..., final_message: _Optional[str] = ...) -> None: ...

class SubagentAwaitError(_message.Message):
    __slots__ = ("agent_id", "error")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    error: str
    def __init__(self, agent_id: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class SubagentAwaitNotFound(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class SubagentAwaitResult(_message.Message):
    __slots__ = ("complete", "still_running", "not_found", "error")
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    STILL_RUNNING_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    complete: SubagentAwaitComplete
    still_running: SubagentAwaitStillRunning
    not_found: SubagentAwaitNotFound
    error: SubagentAwaitError
    def __init__(self, complete: _Optional[_Union[SubagentAwaitComplete, _Mapping]] = ..., still_running: _Optional[_Union[SubagentAwaitStillRunning, _Mapping]] = ..., not_found: _Optional[_Union[SubagentAwaitNotFound, _Mapping]] = ..., error: _Optional[_Union[SubagentAwaitError, _Mapping]] = ...) -> None: ...

class SubagentAwaitStillRunning(_message.Message):
    __slots__ = ("agent_id", "transcript_path")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    transcript_path: str
    def __init__(self, agent_id: _Optional[str] = ..., transcript_path: _Optional[str] = ...) -> None: ...

class SubagentCredentials(_message.Message):
    __slots__ = ("api_key_credentials", "azure_credentials", "bedrock_credentials")
    API_KEY_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    AZURE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    BEDROCK_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    api_key_credentials: ApiKeyCredentials
    azure_credentials: AzureCredentials
    bedrock_credentials: BedrockCredentials
    def __init__(self, api_key_credentials: _Optional[_Union[ApiKeyCredentials, _Mapping]] = ..., azure_credentials: _Optional[_Union[AzureCredentials, _Mapping]] = ..., bedrock_credentials: _Optional[_Union[BedrockCredentials, _Mapping]] = ...) -> None: ...

class SubagentError(_message.Message):
    __slots__ = ("agent_id", "error")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    error: str
    def __init__(self, agent_id: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class SubagentModelOverride(_message.Message):
    __slots__ = ("subagent_type", "model", "inherit", "disabled")
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INHERIT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    subagent_type: str
    model: RequestedModel
    inherit: bool
    disabled: bool
    def __init__(self, subagent_type: _Optional[str] = ..., model: _Optional[_Union[RequestedModel, _Mapping]] = ..., inherit: _Optional[bool] = ..., disabled: _Optional[bool] = ...) -> None: ...

class SubagentPersistedState(_message.Message):
    __slots__ = ("conversation_state", "created_timestamp_ms", "last_used_timestamp_ms", "subagent_type", "model_id", "environment", "cloud_subagent", "first_class_bc_id", "cloud_requested_environment_build_id", "machine")
    CONVERSATION_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SUBAGENT_FIELD_NUMBER: _ClassVar[int]
    FIRST_CLASS_BC_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REQUESTED_ENVIRONMENT_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    conversation_state: ConversationStateStructure
    created_timestamp_ms: int
    last_used_timestamp_ms: int
    subagent_type: SubagentType
    model_id: str
    environment: SubagentExecutionEnvironment
    cloud_subagent: CloudSubagentReference
    first_class_bc_id: str
    cloud_requested_environment_build_id: str
    machine: TargetMachine
    def __init__(self, conversation_state: _Optional[_Union[ConversationStateStructure, _Mapping]] = ..., created_timestamp_ms: _Optional[int] = ..., last_used_timestamp_ms: _Optional[int] = ..., subagent_type: _Optional[_Union[SubagentType, _Mapping]] = ..., model_id: _Optional[str] = ..., environment: _Optional[_Union[SubagentExecutionEnvironment, str]] = ..., cloud_subagent: _Optional[_Union[CloudSubagentReference, _Mapping]] = ..., first_class_bc_id: _Optional[str] = ..., cloud_requested_environment_build_id: _Optional[str] = ..., machine: _Optional[_Union[TargetMachine, _Mapping]] = ...) -> None: ...

class SubagentResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: SubagentSuccess
    error: SubagentError
    def __init__(self, success: _Optional[_Union[SubagentSuccess, _Mapping]] = ..., error: _Optional[_Union[SubagentError, _Mapping]] = ...) -> None: ...

class SubagentRunState(_message.Message):
    __slots__ = ("parent_tool_call_id", "subagent_id", "environment", "status", "title", "detail", "transcript_path", "output_path", "completed_timestamp_ms", "completion_reason")
    PARENT_TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PATH_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_REASON_FIELD_NUMBER: _ClassVar[int]
    parent_tool_call_id: str
    subagent_id: str
    environment: SubagentExecutionEnvironment
    status: SubagentRunStatus
    title: str
    detail: str
    transcript_path: str
    output_path: str
    completed_timestamp_ms: int
    completion_reason: BackgroundTaskCompletionReason
    def __init__(self, parent_tool_call_id: _Optional[str] = ..., subagent_id: _Optional[str] = ..., environment: _Optional[_Union[SubagentExecutionEnvironment, str]] = ..., status: _Optional[_Union[SubagentRunStatus, str]] = ..., title: _Optional[str] = ..., detail: _Optional[str] = ..., transcript_path: _Optional[str] = ..., output_path: _Optional[str] = ..., completed_timestamp_ms: _Optional[int] = ..., completion_reason: _Optional[_Union[BackgroundTaskCompletionReason, str]] = ...) -> None: ...

class SubagentStartRequestQuery(_message.Message):
    __slots__ = ("subagent_id", "subagent_type", "task", "parent_conversation_id", "tool_call_id", "subagent_model", "is_parallel_worker", "git_branch", "conversation_id", "generation_id", "model", "model_id", "model_params")
    SUBAGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    IS_PARALLEL_WORKER_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    subagent_id: str
    subagent_type: str
    task: str
    parent_conversation_id: str
    tool_call_id: str
    subagent_model: str
    is_parallel_worker: bool
    git_branch: str
    conversation_id: str
    generation_id: str
    model: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, subagent_id: _Optional[str] = ..., subagent_type: _Optional[str] = ..., task: _Optional[str] = ..., parent_conversation_id: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., subagent_model: _Optional[str] = ..., is_parallel_worker: _Optional[bool] = ..., git_branch: _Optional[str] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class SubagentStartRequestResponse(_message.Message):
    __slots__ = ("permission", "user_message", "additional_context")
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    permission: str
    user_message: str
    additional_context: str
    def __init__(self, permission: _Optional[str] = ..., user_message: _Optional[str] = ..., additional_context: _Optional[str] = ...) -> None: ...

class SubagentStopRequestQuery(_message.Message):
    __slots__ = ("subagent_id", "subagent_type", "status", "duration_ms", "summary", "parent_conversation_id", "message_count", "tool_call_count", "error_message", "modified_files", "git_branch", "conversation_id", "generation_id", "model", "loop_count", "task", "description", "model_id", "model_params")
    SUBAGENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_FILES_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LOOP_COUNT_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    subagent_id: str
    subagent_type: str
    status: str
    duration_ms: int
    summary: str
    parent_conversation_id: str
    message_count: int
    tool_call_count: int
    error_message: str
    modified_files: _containers.RepeatedScalarFieldContainer[str]
    git_branch: str
    conversation_id: str
    generation_id: str
    model: str
    loop_count: int
    task: str
    description: str
    model_id: str
    model_params: _containers.RepeatedCompositeFieldContainer[RequestedModel.ModelParameterValue]
    def __init__(self, subagent_id: _Optional[str] = ..., subagent_type: _Optional[str] = ..., status: _Optional[str] = ..., duration_ms: _Optional[int] = ..., summary: _Optional[str] = ..., parent_conversation_id: _Optional[str] = ..., message_count: _Optional[int] = ..., tool_call_count: _Optional[int] = ..., error_message: _Optional[str] = ..., modified_files: _Optional[_Iterable[str]] = ..., git_branch: _Optional[str] = ..., conversation_id: _Optional[str] = ..., generation_id: _Optional[str] = ..., model: _Optional[str] = ..., loop_count: _Optional[int] = ..., task: _Optional[str] = ..., description: _Optional[str] = ..., model_id: _Optional[str] = ..., model_params: _Optional[_Iterable[_Union[RequestedModel.ModelParameterValue, _Mapping]]] = ...) -> None: ...

class SubagentStopRequestResponse(_message.Message):
    __slots__ = ("followup_message", "additional_context")
    FOLLOWUP_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    followup_message: str
    additional_context: str
    def __init__(self, followup_message: _Optional[str] = ..., additional_context: _Optional[str] = ...) -> None: ...

class SubagentSuccess(_message.Message):
    __slots__ = ("agent_id", "final_message", "tool_call_count", "background_reason", "transcript_path")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    FINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_REASON_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    final_message: str
    tool_call_count: int
    background_reason: SubagentBackgroundReason
    transcript_path: str
    def __init__(self, agent_id: _Optional[str] = ..., final_message: _Optional[str] = ..., tool_call_count: _Optional[int] = ..., background_reason: _Optional[_Union[SubagentBackgroundReason, str]] = ..., transcript_path: _Optional[str] = ...) -> None: ...

class SubagentType(_message.Message):
    __slots__ = ("unspecified", "computer_use", "custom", "explore", "media_review", "bash", "browser_use", "shell", "vm_setup_helper", "debug", "cursor_guide", "watch_video")
    UNSPECIFIED_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    EXPLORE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_REVIEW_FIELD_NUMBER: _ClassVar[int]
    BASH_FIELD_NUMBER: _ClassVar[int]
    BROWSER_USE_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    VM_SETUP_HELPER_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    CURSOR_GUIDE_FIELD_NUMBER: _ClassVar[int]
    WATCH_VIDEO_FIELD_NUMBER: _ClassVar[int]
    unspecified: SubagentTypeUnspecified
    computer_use: SubagentTypeComputerUse
    custom: SubagentTypeCustom
    explore: SubagentTypeExplore
    media_review: SubagentTypeMediaReview
    bash: SubagentTypeBash
    browser_use: SubagentTypeBrowserUse
    shell: SubagentTypeShell
    vm_setup_helper: SubagentTypeVmSetupHelper
    debug: SubagentTypeDebug
    cursor_guide: SubagentTypeCursorGuide
    watch_video: SubagentTypeWatchVideo
    def __init__(self, unspecified: _Optional[_Union[SubagentTypeUnspecified, _Mapping]] = ..., computer_use: _Optional[_Union[SubagentTypeComputerUse, _Mapping]] = ..., custom: _Optional[_Union[SubagentTypeCustom, _Mapping]] = ..., explore: _Optional[_Union[SubagentTypeExplore, _Mapping]] = ..., media_review: _Optional[_Union[SubagentTypeMediaReview, _Mapping]] = ..., bash: _Optional[_Union[SubagentTypeBash, _Mapping]] = ..., browser_use: _Optional[_Union[SubagentTypeBrowserUse, _Mapping]] = ..., shell: _Optional[_Union[SubagentTypeShell, _Mapping]] = ..., vm_setup_helper: _Optional[_Union[SubagentTypeVmSetupHelper, _Mapping]] = ..., debug: _Optional[_Union[SubagentTypeDebug, _Mapping]] = ..., cursor_guide: _Optional[_Union[SubagentTypeCursorGuide, _Mapping]] = ..., watch_video: _Optional[_Union[SubagentTypeWatchVideo, _Mapping]] = ...) -> None: ...

class SubagentTypeBash(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeBrowserUse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeComputerUse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeCursorGuide(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeCustom(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SubagentTypeDebug(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeExplore(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeMediaReview(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeShell(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeUnspecified(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeVmSetupHelper(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubagentTypeWatchVideo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubmittedCustomMode(_message.Message):
    __slots__ = ("id", "label", "source", "source_path", "source_hash", "managed_skill_id", "plugin_id", "plugin_snapshot_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HASH_FIELD_NUMBER: _ClassVar[int]
    MANAGED_SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_SNAPSHOT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    source: CustomModeSource
    source_path: str
    source_hash: str
    managed_skill_id: str
    plugin_id: str
    plugin_snapshot_token: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ..., source: _Optional[_Union[CustomModeSource, str]] = ..., source_path: _Optional[str] = ..., source_hash: _Optional[str] = ..., managed_skill_id: _Optional[str] = ..., plugin_id: _Optional[str] = ..., plugin_snapshot_token: _Optional[str] = ...) -> None: ...

class SubmittedExitedCustomMode(_message.Message):
    __slots__ = ("id", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class SubscriptionEventDisplay(_message.Message):
    __slots__ = ("display_label", "resource_url", "subscription_id")
    DISPLAY_LABEL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    display_label: str
    resource_url: str
    subscription_id: str
    def __init__(self, display_label: _Optional[str] = ..., resource_url: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class SubscriptionNotificationAction(_message.Message):
    __slots__ = ("notifications", "request_context", "send_to_interaction_listener")
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SEND_TO_INTERACTION_LISTENER_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[UserMessage]
    request_context: RequestContext
    send_to_interaction_listener: bool
    def __init__(self, notifications: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ..., request_context: _Optional[_Union[RequestContext, _Mapping]] = ..., send_to_interaction_listener: _Optional[bool] = ...) -> None: ...

class SummarizeAction(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SummaryCompletedUpdate(_message.Message):
    __slots__ = ("hook_message",)
    HOOK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    hook_message: str
    def __init__(self, hook_message: _Optional[str] = ...) -> None: ...

class SummaryStartedUpdate(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SummaryUpdate(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: str
    def __init__(self, summary: _Optional[str] = ...) -> None: ...

class SwitchModeArgs(_message.Message):
    __slots__ = ("target_mode_id", "explanation", "tool_call_id")
    TARGET_MODE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    target_mode_id: str
    explanation: str
    tool_call_id: str
    def __init__(self, target_mode_id: _Optional[str] = ..., explanation: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class SwitchModeError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class SwitchModeRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class SwitchModeRequestQuery(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: SwitchModeArgs
    def __init__(self, args: _Optional[_Union[SwitchModeArgs, _Mapping]] = ...) -> None: ...

class SwitchModeRequestResponse(_message.Message):
    __slots__ = ("approved", "rejected")
    class Approved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Rejected(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    approved: SwitchModeRequestResponse.Approved
    rejected: SwitchModeRequestResponse.Rejected
    def __init__(self, approved: _Optional[_Union[SwitchModeRequestResponse.Approved, _Mapping]] = ..., rejected: _Optional[_Union[SwitchModeRequestResponse.Rejected, _Mapping]] = ...) -> None: ...

class SwitchModeResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: SwitchModeSuccess
    error: SwitchModeError
    rejected: SwitchModeRejected
    def __init__(self, success: _Optional[_Union[SwitchModeSuccess, _Mapping]] = ..., error: _Optional[_Union[SwitchModeError, _Mapping]] = ..., rejected: _Optional[_Union[SwitchModeRejected, _Mapping]] = ...) -> None: ...

class SwitchModeSuccess(_message.Message):
    __slots__ = ("from_mode_id", "to_mode_id")
    FROM_MODE_ID_FIELD_NUMBER: _ClassVar[int]
    TO_MODE_ID_FIELD_NUMBER: _ClassVar[int]
    from_mode_id: str
    to_mode_id: str
    def __init__(self, from_mode_id: _Optional[str] = ..., to_mode_id: _Optional[str] = ...) -> None: ...

class SwitchModeToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: SwitchModeArgs
    result: SwitchModeResult
    def __init__(self, args: _Optional[_Union[SwitchModeArgs, _Mapping]] = ..., result: _Optional[_Union[SwitchModeResult, _Mapping]] = ...) -> None: ...

class SystemContextInjection(_message.Message):
    __slots__ = ("producer", "content")
    PRODUCER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    producer: str
    content: str
    def __init__(self, producer: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class TargetMachine(_message.Message):
    __slots__ = ("same_machine", "new_cloud_vm", "self_hosted_worker", "self_hosted_pool")
    SAME_MACHINE_FIELD_NUMBER: _ClassVar[int]
    NEW_CLOUD_VM_FIELD_NUMBER: _ClassVar[int]
    SELF_HOSTED_WORKER_FIELD_NUMBER: _ClassVar[int]
    SELF_HOSTED_POOL_FIELD_NUMBER: _ClassVar[int]
    same_machine: SameMachineTarget
    new_cloud_vm: NewCloudVmTarget
    self_hosted_worker: SelfHostedWorkerTarget
    self_hosted_pool: SelfHostedPoolTarget
    def __init__(self, same_machine: _Optional[_Union[SameMachineTarget, _Mapping]] = ..., new_cloud_vm: _Optional[_Union[NewCloudVmTarget, _Mapping]] = ..., self_hosted_worker: _Optional[_Union[SelfHostedWorkerTarget, _Mapping]] = ..., self_hosted_pool: _Optional[_Union[SelfHostedPoolTarget, _Mapping]] = ...) -> None: ...

class TaskArgs(_message.Message):
    __slots__ = ("description", "prompt", "subagent_type", "model", "resume", "agent_id", "attachments", "mode", "responding_to_message_ids", "environment", "machine")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RESPONDING_TO_MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    description: str
    prompt: str
    subagent_type: SubagentType
    model: str
    resume: str
    agent_id: str
    attachments: _containers.RepeatedScalarFieldContainer[str]
    mode: TaskMode
    responding_to_message_ids: _containers.RepeatedScalarFieldContainer[str]
    environment: SubagentExecutionEnvironment
    machine: TargetMachine
    def __init__(self, description: _Optional[str] = ..., prompt: _Optional[str] = ..., subagent_type: _Optional[_Union[SubagentType, _Mapping]] = ..., model: _Optional[str] = ..., resume: _Optional[str] = ..., agent_id: _Optional[str] = ..., attachments: _Optional[_Iterable[str]] = ..., mode: _Optional[_Union[TaskMode, str]] = ..., responding_to_message_ids: _Optional[_Iterable[str]] = ..., environment: _Optional[_Union[SubagentExecutionEnvironment, str]] = ..., machine: _Optional[_Union[TargetMachine, _Mapping]] = ...) -> None: ...

class TaskError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class TaskResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: TaskSuccess
    error: TaskError
    def __init__(self, success: _Optional[_Union[TaskSuccess, _Mapping]] = ..., error: _Optional[_Union[TaskError, _Mapping]] = ...) -> None: ...

class TaskSuccess(_message.Message):
    __slots__ = ("conversation_steps", "agent_id", "is_background", "duration_ms", "result_suffix", "background_reason", "transcript_path")
    CONVERSATION_STEPS_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    RESULT_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_REASON_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_PATH_FIELD_NUMBER: _ClassVar[int]
    conversation_steps: _containers.RepeatedCompositeFieldContainer[ConversationStep]
    agent_id: str
    is_background: bool
    duration_ms: int
    result_suffix: str
    background_reason: SubagentBackgroundReason
    transcript_path: str
    def __init__(self, conversation_steps: _Optional[_Iterable[_Union[ConversationStep, _Mapping]]] = ..., agent_id: _Optional[str] = ..., is_background: _Optional[bool] = ..., duration_ms: _Optional[int] = ..., result_suffix: _Optional[str] = ..., background_reason: _Optional[_Union[SubagentBackgroundReason, str]] = ..., transcript_path: _Optional[str] = ...) -> None: ...

class TaskToolCall(_message.Message):
    __slots__ = ("args", "result", "cloud_agent_bc_id")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_AGENT_BC_ID_FIELD_NUMBER: _ClassVar[int]
    args: TaskArgs
    result: TaskResult
    cloud_agent_bc_id: str
    def __init__(self, args: _Optional[_Union[TaskArgs, _Mapping]] = ..., result: _Optional[_Union[TaskResult, _Mapping]] = ..., cloud_agent_bc_id: _Optional[str] = ...) -> None: ...

class TaskToolCallArgsProto(_message.Message):
    __slots__ = ("description", "prompt", "model", "subagent_type", "resume", "readonly", "run_in_background", "attachments", "environment", "cloud_base_branch", "cloud_requested_environment_build_id", "machine")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESUME_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    RUN_IN_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REQUESTED_ENVIRONMENT_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    description: str
    prompt: str
    model: str
    subagent_type: str
    resume: str
    readonly: bool
    run_in_background: bool
    attachments: _containers.RepeatedScalarFieldContainer[str]
    environment: SubagentExecutionEnvironment
    cloud_base_branch: str
    cloud_requested_environment_build_id: str
    machine: TargetMachine
    def __init__(self, description: _Optional[str] = ..., prompt: _Optional[str] = ..., model: _Optional[str] = ..., subagent_type: _Optional[str] = ..., resume: _Optional[str] = ..., readonly: _Optional[bool] = ..., run_in_background: _Optional[bool] = ..., attachments: _Optional[_Iterable[str]] = ..., environment: _Optional[_Union[SubagentExecutionEnvironment, str]] = ..., cloud_base_branch: _Optional[str] = ..., cloud_requested_environment_build_id: _Optional[str] = ..., machine: _Optional[_Union[TargetMachine, _Mapping]] = ...) -> None: ...

class TaskToolCallDelta(_message.Message):
    __slots__ = ("interaction_update",)
    INTERACTION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    interaction_update: InteractionUpdate
    def __init__(self, interaction_update: _Optional[_Union[InteractionUpdate, _Mapping]] = ...) -> None: ...

class TerminalMetadata(_message.Message):
    __slots__ = ("cwd", "last_commands", "last_modified_ms", "current_command")
    class Command(_message.Message):
        __slots__ = ("command", "exit_code", "timestamp_ms", "duration_ms")
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        command: str
        exit_code: int
        timestamp_ms: int
        duration_ms: int
        def __init__(self, command: _Optional[str] = ..., exit_code: _Optional[int] = ..., timestamp_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...
    CWD_FIELD_NUMBER: _ClassVar[int]
    LAST_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_MS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COMMAND_FIELD_NUMBER: _ClassVar[int]
    cwd: str
    last_commands: _containers.RepeatedCompositeFieldContainer[TerminalMetadata.Command]
    last_modified_ms: int
    current_command: TerminalMetadata.Command
    def __init__(self, cwd: _Optional[str] = ..., last_commands: _Optional[_Iterable[_Union[TerminalMetadata.Command, _Mapping]]] = ..., last_modified_ms: _Optional[int] = ..., current_command: _Optional[_Union[TerminalMetadata.Command, _Mapping]] = ...) -> None: ...

class TerminatePtyRequest(_message.Message):
    __slots__ = ("pty_id",)
    PTY_ID_FIELD_NUMBER: _ClassVar[int]
    pty_id: str
    def __init__(self, pty_id: _Optional[str] = ...) -> None: ...

class TerminatePtyResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...

class TextDeltaUpdate(_message.Message):
    __slots__ = ("text", "is_server_notice")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IS_SERVER_NOTICE_FIELD_NUMBER: _ClassVar[int]
    text: str
    is_server_notice: bool
    def __init__(self, text: _Optional[str] = ..., is_server_notice: _Optional[bool] = ...) -> None: ...

class ThinkingCompletedUpdate(_message.Message):
    __slots__ = ("thinking_duration_ms",)
    THINKING_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    thinking_duration_ms: int
    def __init__(self, thinking_duration_ms: _Optional[int] = ...) -> None: ...

class ThinkingDeltaUpdate(_message.Message):
    __slots__ = ("text", "thinking_style")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    THINKING_STYLE_FIELD_NUMBER: _ClassVar[int]
    text: str
    thinking_style: ThinkingStyle
    def __init__(self, text: _Optional[str] = ..., thinking_style: _Optional[_Union[ThinkingStyle, str]] = ...) -> None: ...

class ThinkingDetails(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ThinkingMessage(_message.Message):
    __slots__ = ("text", "duration_ms")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    text: str
    duration_ms: int
    def __init__(self, text: _Optional[str] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class TmuxSession(_message.Message):
    __slots__ = ("session_id", "session_name", "display_name", "kind", "cwd", "shell", "process_args", "created_at_unix_ms", "attached_client_count")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    CWD_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    PROCESS_ARGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_CLIENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    session_name: str
    display_name: str
    kind: TmuxSessionKind
    cwd: str
    shell: str
    process_args: _containers.RepeatedScalarFieldContainer[str]
    created_at_unix_ms: int
    attached_client_count: int
    def __init__(self, session_id: _Optional[str] = ..., session_name: _Optional[str] = ..., display_name: _Optional[str] = ..., kind: _Optional[_Union[TmuxSessionKind, str]] = ..., cwd: _Optional[str] = ..., shell: _Optional[str] = ..., process_args: _Optional[_Iterable[str]] = ..., created_at_unix_ms: _Optional[int] = ..., attached_client_count: _Optional[int] = ...) -> None: ...

class TodoItem(_message.Message):
    __slots__ = ("id", "content", "status", "created_at", "updated_at", "dependencies")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    status: TodoStatus
    created_at: int
    updated_at: int
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[TodoStatus, str]] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ..., dependencies: _Optional[_Iterable[str]] = ...) -> None: ...

class TokenDeltaUpdate(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: int
    def __init__(self, tokens: _Optional[int] = ...) -> None: ...

class ToolCall(_message.Message):
    __slots__ = ("hook_additional_contexts", "tool_call_id", "started_at_ms", "completed_at_ms", "shell_tool_call", "delete_tool_call", "glob_tool_call", "grep_tool_call", "read_tool_call", "update_todos_tool_call", "read_todos_tool_call", "edit_tool_call", "ls_tool_call", "read_lints_tool_call", "mcp_tool_call", "sem_search_tool_call", "create_plan_tool_call", "web_search_tool_call", "task_tool_call", "list_mcp_resources_tool_call", "read_mcp_resource_tool_call", "apply_agent_diff_tool_call", "ask_question_tool_call", "fetch_tool_call", "switch_mode_tool_call", "generate_image_tool_call", "record_screen_tool_call", "computer_use_tool_call", "write_shell_stdin_tool_call", "reflect_tool_call", "setup_vm_environment_tool_call", "truncated_tool_call", "start_grind_execution_tool_call", "start_grind_planning_tool_call", "web_fetch_tool_call", "report_bugfix_results_tool_call", "ai_attribution_tool_call", "pr_management_tool_call", "mcp_auth_tool_call", "await_tool_call", "blame_by_file_path_tool_call", "get_mcp_tools_tool_call", "report_bug_tool_call", "set_active_branch_tool_call", "communicate_update_tool_call", "send_final_summary_tool_call", "update_pr_code_tour_tool_call", "replace_env_tool_call", "edit_pr_labels_tool_call", "record_ci_investigation_findings_tool_call", "send_message_tool_call", "fetch_cloud_agent_data_tool_call", "send_to_user_tool_call", "pi_read_tool_call", "pi_bash_tool_call", "pi_edit_tool_call", "pi_write_tool_call", "pi_grep_tool_call", "pi_find_tool_call", "pi_ls_tool_call", "connect_scm_tool_call", "search_conversations_tool_call", "create_goal_tool_call", "update_goal_tool_call")
    HOOK_ADDITIONAL_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    SHELL_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    DELETE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    GLOB_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    GREP_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    READ_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TODOS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    READ_TODOS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    EDIT_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    LS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    READ_LINTS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    MCP_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SEM_SEARCH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    CREATE_PLAN_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    TASK_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    LIST_MCP_RESOURCES_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    READ_MCP_RESOURCE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    APPLY_AGENT_DIFF_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    ASK_QUESTION_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    FETCH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SWITCH_MODE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    GENERATE_IMAGE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    RECORD_SCREEN_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    COMPUTER_USE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    WRITE_SHELL_STDIN_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    REFLECT_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SETUP_VM_ENVIRONMENT_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    START_GRIND_EXECUTION_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    START_GRIND_PLANNING_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    WEB_FETCH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    REPORT_BUGFIX_RESULTS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    AI_ATTRIBUTION_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PR_MANAGEMENT_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    MCP_AUTH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    AWAIT_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    BLAME_BY_FILE_PATH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    GET_MCP_TOOLS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    REPORT_BUG_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SET_ACTIVE_BRANCH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATE_UPDATE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SEND_FINAL_SUMMARY_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PR_CODE_TOUR_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ENV_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    EDIT_PR_LABELS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    RECORD_CI_INVESTIGATION_FINDINGS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    FETCH_CLOUD_AGENT_DATA_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SEND_TO_USER_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_READ_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_BASH_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_EDIT_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_WRITE_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_GREP_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_FIND_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    PI_LS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    CONNECT_SCM_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONVERSATIONS_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    CREATE_GOAL_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_GOAL_TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    hook_additional_contexts: _containers.RepeatedCompositeFieldContainer[HookAdditionalContext]
    tool_call_id: str
    started_at_ms: int
    completed_at_ms: int
    shell_tool_call: ShellToolCall
    delete_tool_call: DeleteToolCall
    glob_tool_call: GlobToolCall
    grep_tool_call: GrepToolCall
    read_tool_call: ReadToolCall
    update_todos_tool_call: UpdateTodosToolCall
    read_todos_tool_call: ReadTodosToolCall
    edit_tool_call: EditToolCall
    ls_tool_call: LsToolCall
    read_lints_tool_call: ReadLintsToolCall
    mcp_tool_call: McpToolCall
    sem_search_tool_call: SemSearchToolCall
    create_plan_tool_call: CreatePlanToolCall
    web_search_tool_call: WebSearchToolCall
    task_tool_call: TaskToolCall
    list_mcp_resources_tool_call: ListMcpResourcesToolCall
    read_mcp_resource_tool_call: ReadMcpResourceToolCall
    apply_agent_diff_tool_call: ApplyAgentDiffToolCall
    ask_question_tool_call: AskQuestionToolCall
    fetch_tool_call: FetchToolCall
    switch_mode_tool_call: SwitchModeToolCall
    generate_image_tool_call: GenerateImageToolCall
    record_screen_tool_call: RecordScreenToolCall
    computer_use_tool_call: ComputerUseToolCall
    write_shell_stdin_tool_call: WriteShellStdinToolCall
    reflect_tool_call: ReflectToolCall
    setup_vm_environment_tool_call: SetupVmEnvironmentToolCall
    truncated_tool_call: TruncatedToolCall
    start_grind_execution_tool_call: StartGrindExecutionToolCall
    start_grind_planning_tool_call: StartGrindPlanningToolCall
    web_fetch_tool_call: WebFetchToolCall
    report_bugfix_results_tool_call: ReportBugfixResultsToolCall
    ai_attribution_tool_call: AiAttributionToolCall
    pr_management_tool_call: PrManagementToolCall
    mcp_auth_tool_call: McpAuthToolCall
    await_tool_call: AwaitToolCall
    blame_by_file_path_tool_call: BlameByFilePathToolCall
    get_mcp_tools_tool_call: GetMcpToolsToolCall
    report_bug_tool_call: ReportBugToolCall
    set_active_branch_tool_call: SetActiveBranchToolCall
    communicate_update_tool_call: CommunicateUpdateToolCall
    send_final_summary_tool_call: SendFinalSummaryToolCall
    update_pr_code_tour_tool_call: UpdatePrCodeTourToolCall
    replace_env_tool_call: ReplaceEnvToolCall
    edit_pr_labels_tool_call: EditPrLabelsToolCall
    record_ci_investigation_findings_tool_call: RecordCiInvestigationFindingsToolCall
    send_message_tool_call: SendMessageToolCall
    fetch_cloud_agent_data_tool_call: FetchCloudAgentDataToolCall
    send_to_user_tool_call: SendToUserToolCall
    pi_read_tool_call: PiReadToolCall
    pi_bash_tool_call: PiBashToolCall
    pi_edit_tool_call: PiEditToolCall
    pi_write_tool_call: PiWriteToolCall
    pi_grep_tool_call: PiGrepToolCall
    pi_find_tool_call: PiFindToolCall
    pi_ls_tool_call: PiLsToolCall
    connect_scm_tool_call: ConnectScmToolCall
    search_conversations_tool_call: SearchConversationsToolCall
    create_goal_tool_call: CreateGoalToolCall
    update_goal_tool_call: UpdateGoalToolCall
    def __init__(self, hook_additional_contexts: _Optional[_Iterable[_Union[HookAdditionalContext, _Mapping]]] = ..., tool_call_id: _Optional[str] = ..., started_at_ms: _Optional[int] = ..., completed_at_ms: _Optional[int] = ..., shell_tool_call: _Optional[_Union[ShellToolCall, _Mapping]] = ..., delete_tool_call: _Optional[_Union[DeleteToolCall, _Mapping]] = ..., glob_tool_call: _Optional[_Union[GlobToolCall, _Mapping]] = ..., grep_tool_call: _Optional[_Union[GrepToolCall, _Mapping]] = ..., read_tool_call: _Optional[_Union[ReadToolCall, _Mapping]] = ..., update_todos_tool_call: _Optional[_Union[UpdateTodosToolCall, _Mapping]] = ..., read_todos_tool_call: _Optional[_Union[ReadTodosToolCall, _Mapping]] = ..., edit_tool_call: _Optional[_Union[EditToolCall, _Mapping]] = ..., ls_tool_call: _Optional[_Union[LsToolCall, _Mapping]] = ..., read_lints_tool_call: _Optional[_Union[ReadLintsToolCall, _Mapping]] = ..., mcp_tool_call: _Optional[_Union[McpToolCall, _Mapping]] = ..., sem_search_tool_call: _Optional[_Union[SemSearchToolCall, _Mapping]] = ..., create_plan_tool_call: _Optional[_Union[CreatePlanToolCall, _Mapping]] = ..., web_search_tool_call: _Optional[_Union[WebSearchToolCall, _Mapping]] = ..., task_tool_call: _Optional[_Union[TaskToolCall, _Mapping]] = ..., list_mcp_resources_tool_call: _Optional[_Union[ListMcpResourcesToolCall, _Mapping]] = ..., read_mcp_resource_tool_call: _Optional[_Union[ReadMcpResourceToolCall, _Mapping]] = ..., apply_agent_diff_tool_call: _Optional[_Union[ApplyAgentDiffToolCall, _Mapping]] = ..., ask_question_tool_call: _Optional[_Union[AskQuestionToolCall, _Mapping]] = ..., fetch_tool_call: _Optional[_Union[FetchToolCall, _Mapping]] = ..., switch_mode_tool_call: _Optional[_Union[SwitchModeToolCall, _Mapping]] = ..., generate_image_tool_call: _Optional[_Union[GenerateImageToolCall, _Mapping]] = ..., record_screen_tool_call: _Optional[_Union[RecordScreenToolCall, _Mapping]] = ..., computer_use_tool_call: _Optional[_Union[ComputerUseToolCall, _Mapping]] = ..., write_shell_stdin_tool_call: _Optional[_Union[WriteShellStdinToolCall, _Mapping]] = ..., reflect_tool_call: _Optional[_Union[ReflectToolCall, _Mapping]] = ..., setup_vm_environment_tool_call: _Optional[_Union[SetupVmEnvironmentToolCall, _Mapping]] = ..., truncated_tool_call: _Optional[_Union[TruncatedToolCall, _Mapping]] = ..., start_grind_execution_tool_call: _Optional[_Union[StartGrindExecutionToolCall, _Mapping]] = ..., start_grind_planning_tool_call: _Optional[_Union[StartGrindPlanningToolCall, _Mapping]] = ..., web_fetch_tool_call: _Optional[_Union[WebFetchToolCall, _Mapping]] = ..., report_bugfix_results_tool_call: _Optional[_Union[ReportBugfixResultsToolCall, _Mapping]] = ..., ai_attribution_tool_call: _Optional[_Union[AiAttributionToolCall, _Mapping]] = ..., pr_management_tool_call: _Optional[_Union[PrManagementToolCall, _Mapping]] = ..., mcp_auth_tool_call: _Optional[_Union[McpAuthToolCall, _Mapping]] = ..., await_tool_call: _Optional[_Union[AwaitToolCall, _Mapping]] = ..., blame_by_file_path_tool_call: _Optional[_Union[BlameByFilePathToolCall, _Mapping]] = ..., get_mcp_tools_tool_call: _Optional[_Union[GetMcpToolsToolCall, _Mapping]] = ..., report_bug_tool_call: _Optional[_Union[ReportBugToolCall, _Mapping]] = ..., set_active_branch_tool_call: _Optional[_Union[SetActiveBranchToolCall, _Mapping]] = ..., communicate_update_tool_call: _Optional[_Union[CommunicateUpdateToolCall, _Mapping]] = ..., send_final_summary_tool_call: _Optional[_Union[SendFinalSummaryToolCall, _Mapping]] = ..., update_pr_code_tour_tool_call: _Optional[_Union[UpdatePrCodeTourToolCall, _Mapping]] = ..., replace_env_tool_call: _Optional[_Union[ReplaceEnvToolCall, _Mapping]] = ..., edit_pr_labels_tool_call: _Optional[_Union[EditPrLabelsToolCall, _Mapping]] = ..., record_ci_investigation_findings_tool_call: _Optional[_Union[RecordCiInvestigationFindingsToolCall, _Mapping]] = ..., send_message_tool_call: _Optional[_Union[SendMessageToolCall, _Mapping]] = ..., fetch_cloud_agent_data_tool_call: _Optional[_Union[FetchCloudAgentDataToolCall, _Mapping]] = ..., send_to_user_tool_call: _Optional[_Union[SendToUserToolCall, _Mapping]] = ..., pi_read_tool_call: _Optional[_Union[PiReadToolCall, _Mapping]] = ..., pi_bash_tool_call: _Optional[_Union[PiBashToolCall, _Mapping]] = ..., pi_edit_tool_call: _Optional[_Union[PiEditToolCall, _Mapping]] = ..., pi_write_tool_call: _Optional[_Union[PiWriteToolCall, _Mapping]] = ..., pi_grep_tool_call: _Optional[_Union[PiGrepToolCall, _Mapping]] = ..., pi_find_tool_call: _Optional[_Union[PiFindToolCall, _Mapping]] = ..., pi_ls_tool_call: _Optional[_Union[PiLsToolCall, _Mapping]] = ..., connect_scm_tool_call: _Optional[_Union[ConnectScmToolCall, _Mapping]] = ..., search_conversations_tool_call: _Optional[_Union[SearchConversationsToolCall, _Mapping]] = ..., create_goal_tool_call: _Optional[_Union[CreateGoalToolCall, _Mapping]] = ..., update_goal_tool_call: _Optional[_Union[UpdateGoalToolCall, _Mapping]] = ...) -> None: ...

class ToolCallCompletedUpdate(_message.Message):
    __slots__ = ("call_id", "tool_call", "model_call_id")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    MODEL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    tool_call: ToolCall
    model_call_id: str
    def __init__(self, call_id: _Optional[str] = ..., tool_call: _Optional[_Union[ToolCall, _Mapping]] = ..., model_call_id: _Optional[str] = ...) -> None: ...

class ToolCallDelta(_message.Message):
    __slots__ = ("shell_tool_call_delta", "task_tool_call_delta", "edit_tool_call_delta", "replace_env_tool_call_delta")
    SHELL_TOOL_CALL_DELTA_FIELD_NUMBER: _ClassVar[int]
    TASK_TOOL_CALL_DELTA_FIELD_NUMBER: _ClassVar[int]
    EDIT_TOOL_CALL_DELTA_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ENV_TOOL_CALL_DELTA_FIELD_NUMBER: _ClassVar[int]
    shell_tool_call_delta: ShellToolCallDelta
    task_tool_call_delta: TaskToolCallDelta
    edit_tool_call_delta: EditToolCallDelta
    replace_env_tool_call_delta: ReplaceEnvToolCallDelta
    def __init__(self, shell_tool_call_delta: _Optional[_Union[ShellToolCallDelta, _Mapping]] = ..., task_tool_call_delta: _Optional[_Union[TaskToolCallDelta, _Mapping]] = ..., edit_tool_call_delta: _Optional[_Union[EditToolCallDelta, _Mapping]] = ..., replace_env_tool_call_delta: _Optional[_Union[ReplaceEnvToolCallDelta, _Mapping]] = ...) -> None: ...

class ToolCallDeltaUpdate(_message.Message):
    __slots__ = ("call_id", "tool_call_delta", "model_call_id")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_DELTA_FIELD_NUMBER: _ClassVar[int]
    MODEL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    tool_call_delta: ToolCallDelta
    model_call_id: str
    def __init__(self, call_id: _Optional[str] = ..., tool_call_delta: _Optional[_Union[ToolCallDelta, _Mapping]] = ..., model_call_id: _Optional[str] = ...) -> None: ...

class ToolCallStartedUpdate(_message.Message):
    __slots__ = ("call_id", "tool_call", "model_call_id")
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_FIELD_NUMBER: _ClassVar[int]
    MODEL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    call_id: str
    tool_call: ToolCall
    model_call_id: str
    def __init__(self, call_id: _Optional[str] = ..., tool_call: _Optional[_Union[ToolCall, _Mapping]] = ..., model_call_id: _Optional[str] = ...) -> None: ...

class TrackedGitRepo(_message.Message):
    __slots__ = ("repo_path", "branch_name")
    REPO_PATH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    repo_path: str
    branch_name: str
    def __init__(self, repo_path: _Optional[str] = ..., branch_name: _Optional[str] = ...) -> None: ...

class TriggeringUserInfo(_message.Message):
    __slots__ = ("auth_id", "user_id")
    AUTH_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    auth_id: str
    user_id: int
    def __init__(self, auth_id: _Optional[str] = ..., user_id: _Optional[int] = ...) -> None: ...

class TruncatedToolCall(_message.Message):
    __slots__ = ("original_step_blob_id", "args", "result")
    ORIGINAL_STEP_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    original_step_blob_id: bytes
    args: TruncatedToolCallArgs
    result: TruncatedToolCallResult
    def __init__(self, original_step_blob_id: _Optional[bytes] = ..., args: _Optional[_Union[TruncatedToolCallArgs, _Mapping]] = ..., result: _Optional[_Union[TruncatedToolCallResult, _Mapping]] = ...) -> None: ...

class TruncatedToolCallArgs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TruncatedToolCallError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class TruncatedToolCallResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: TruncatedToolCallSuccess
    error: TruncatedToolCallError
    def __init__(self, success: _Optional[_Union[TruncatedToolCallSuccess, _Mapping]] = ..., error: _Optional[_Union[TruncatedToolCallError, _Mapping]] = ...) -> None: ...

class TruncatedToolCallSuccess(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TtftBreakdown(_message.Message):
    __slots__ = ("server_first_token_ms", "pre_stream_setup_ms", "wait_for_first_event_ms", "provider_ttft_ms", "slow_pool_wait_ms")
    SERVER_FIRST_TOKEN_MS_FIELD_NUMBER: _ClassVar[int]
    PRE_STREAM_SETUP_MS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_FIRST_EVENT_MS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TTFT_MS_FIELD_NUMBER: _ClassVar[int]
    SLOW_POOL_WAIT_MS_FIELD_NUMBER: _ClassVar[int]
    server_first_token_ms: float
    pre_stream_setup_ms: float
    wait_for_first_event_ms: float
    provider_ttft_ms: float
    slow_pool_wait_ms: float
    def __init__(self, server_first_token_ms: _Optional[float] = ..., pre_stream_setup_ms: _Optional[float] = ..., wait_for_first_event_ms: _Optional[float] = ..., provider_ttft_ms: _Optional[float] = ..., slow_pool_wait_ms: _Optional[float] = ...) -> None: ...

class TurnEndedUpdate(_message.Message):
    __slots__ = ("input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens")
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    reasoning_tokens: int
    def __init__(self, input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ...) -> None: ...

class TypeAction(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class UpdateConversationMetadataRequest(_message.Message):
    __slots__ = ("conversation_id", "name", "only_set_name_if_empty", "workspace_paths")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONLY_SET_NAME_IF_EMPTY_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_PATHS_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    name: str
    only_set_name_if_empty: bool
    workspace_paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, conversation_id: _Optional[str] = ..., name: _Optional[str] = ..., only_set_name_if_empty: _Optional[bool] = ..., workspace_paths: _Optional[_Iterable[str]] = ...) -> None: ...

class UpdateConversationMetadataResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateEnvironmentVariablesRequest(_message.Message):
    __slots__ = ("env", "replace", "restore_previous_values", "run_scoped_overlay")
    class EnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENV_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PREVIOUS_VALUES_FIELD_NUMBER: _ClassVar[int]
    RUN_SCOPED_OVERLAY_FIELD_NUMBER: _ClassVar[int]
    env: _containers.ScalarMap[str, str]
    replace: bool
    restore_previous_values: bool
    run_scoped_overlay: RunScopedOverlay
    def __init__(self, env: _Optional[_Mapping[str, str]] = ..., replace: _Optional[bool] = ..., restore_previous_values: _Optional[bool] = ..., run_scoped_overlay: _Optional[_Union[RunScopedOverlay, _Mapping]] = ...) -> None: ...

class UpdateEnvironmentVariablesResponse(_message.Message):
    __slots__ = ("applied", "removed")
    APPLIED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    applied: int
    removed: int
    def __init__(self, applied: _Optional[int] = ..., removed: _Optional[int] = ...) -> None: ...

class UpdateGoalArgs(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: GoalStatus
    def __init__(self, status: _Optional[_Union[GoalStatus, str]] = ...) -> None: ...

class UpdateGoalResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UpdateGoalSuccess
    error: GoalError
    def __init__(self, success: _Optional[_Union[UpdateGoalSuccess, _Mapping]] = ..., error: _Optional[_Union[GoalError, _Mapping]] = ...) -> None: ...

class UpdateGoalSuccess(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: GoalStatus
    def __init__(self, status: _Optional[_Union[GoalStatus, str]] = ...) -> None: ...

class UpdateGoalToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: UpdateGoalArgs
    result: UpdateGoalResult
    def __init__(self, args: _Optional[_Union[UpdateGoalArgs, _Mapping]] = ..., result: _Optional[_Union[UpdateGoalResult, _Mapping]] = ...) -> None: ...

class UpdatePrAction(_message.Message):
    __slots__ = ("pr_url", "title", "body", "base_branch", "branch_name", "add_labels", "remove_labels", "repo_url", "stack_on_pr_number", "clear_stack", "draft")
    PR_URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    BASE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_LABELS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_LABELS_FIELD_NUMBER: _ClassVar[int]
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    STACK_ON_PR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CLEAR_STACK_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    pr_url: str
    title: str
    body: str
    base_branch: str
    branch_name: str
    add_labels: _containers.RepeatedScalarFieldContainer[str]
    remove_labels: _containers.RepeatedScalarFieldContainer[str]
    repo_url: str
    stack_on_pr_number: int
    clear_stack: bool
    draft: bool
    def __init__(self, pr_url: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., base_branch: _Optional[str] = ..., branch_name: _Optional[str] = ..., add_labels: _Optional[_Iterable[str]] = ..., remove_labels: _Optional[_Iterable[str]] = ..., repo_url: _Optional[str] = ..., stack_on_pr_number: _Optional[int] = ..., clear_stack: _Optional[bool] = ..., draft: _Optional[bool] = ...) -> None: ...

class UpdatePrCodeTourArgs(_message.Message):
    __slots__ = ("feedback", "tool_call_id")
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    feedback: str
    tool_call_id: str
    def __init__(self, feedback: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class UpdatePrCodeTourError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class UpdatePrCodeTourResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UpdatePrCodeTourSuccess
    error: UpdatePrCodeTourError
    def __init__(self, success: _Optional[_Union[UpdatePrCodeTourSuccess, _Mapping]] = ..., error: _Optional[_Union[UpdatePrCodeTourError, _Mapping]] = ...) -> None: ...

class UpdatePrCodeTourSuccess(_message.Message):
    __slots__ = ("revision_id", "message")
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    revision_id: str
    message: str
    def __init__(self, revision_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class UpdatePrCodeTourToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: UpdatePrCodeTourArgs
    result: UpdatePrCodeTourResult
    def __init__(self, args: _Optional[_Union[UpdatePrCodeTourArgs, _Mapping]] = ..., result: _Optional[_Union[UpdatePrCodeTourResult, _Mapping]] = ...) -> None: ...

class UpdateTodosArgs(_message.Message):
    __slots__ = ("todos", "merge")
    TODOS_FIELD_NUMBER: _ClassVar[int]
    MERGE_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    merge: bool
    def __init__(self, todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ..., merge: _Optional[bool] = ...) -> None: ...

class UpdateTodosError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class UpdateTodosResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: UpdateTodosSuccess
    error: UpdateTodosError
    def __init__(self, success: _Optional[_Union[UpdateTodosSuccess, _Mapping]] = ..., error: _Optional[_Union[UpdateTodosError, _Mapping]] = ...) -> None: ...

class UpdateTodosSuccess(_message.Message):
    __slots__ = ("todos", "total_count", "was_merge")
    TODOS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    WAS_MERGE_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[TodoItem]
    total_count: int
    was_merge: bool
    def __init__(self, todos: _Optional[_Iterable[_Union[TodoItem, _Mapping]]] = ..., total_count: _Optional[int] = ..., was_merge: _Optional[bool] = ...) -> None: ...

class UpdateTodosToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: UpdateTodosArgs
    result: UpdateTodosResult
    def __init__(self, args: _Optional[_Union[UpdateTodosArgs, _Mapping]] = ..., result: _Optional[_Union[UpdateTodosResult, _Mapping]] = ...) -> None: ...

class UploadArtifactsRequest(_message.Message):
    __slots__ = ("uploads", "wait_for_completion")
    UPLOADS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    uploads: _containers.RepeatedCompositeFieldContainer[ArtifactUploadInstruction]
    wait_for_completion: bool
    def __init__(self, uploads: _Optional[_Iterable[_Union[ArtifactUploadInstruction, _Mapping]]] = ..., wait_for_completion: _Optional[bool] = ...) -> None: ...

class UploadArtifactsResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ArtifactUploadDispatchResult]
    def __init__(self, results: _Optional[_Iterable[_Union[ArtifactUploadDispatchResult, _Mapping]]] = ...) -> None: ...

class UploadConversationBlobsRequest(_message.Message):
    __slots__ = ("conversation_id", "blobs", "chunk_index", "total_chunks")
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    BLOBS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_INDEX_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    blobs: _containers.RepeatedCompositeFieldContainer[BlobEntry]
    chunk_index: int
    total_chunks: int
    def __init__(self, conversation_id: _Optional[str] = ..., blobs: _Optional[_Iterable[_Union[BlobEntry, _Mapping]]] = ..., chunk_index: _Optional[int] = ..., total_chunks: _Optional[int] = ...) -> None: ...

class UploadConversationBlobsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadLocalAgentRunToPromptQualityRequest(_message.Message):
    __slots__ = ("schema_version", "generation_uuid", "conversation_id", "payload_digest", "invocations", "terminal_status", "created_at")
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_UUID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_DIGEST_FIELD_NUMBER: _ClassVar[int]
    INVOCATIONS_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    schema_version: int
    generation_uuid: str
    conversation_id: str
    payload_digest: str
    invocations: _containers.RepeatedCompositeFieldContainer[LocalPromptQualityInvocation]
    terminal_status: LocalPromptQualityInvocationStatus
    created_at: str
    def __init__(self, schema_version: _Optional[int] = ..., generation_uuid: _Optional[str] = ..., conversation_id: _Optional[str] = ..., payload_digest: _Optional[str] = ..., invocations: _Optional[_Iterable[_Union[LocalPromptQualityInvocation, _Mapping]]] = ..., terminal_status: _Optional[_Union[LocalPromptQualityInvocationStatus, str]] = ..., created_at: _Optional[str] = ...) -> None: ...

class UploadLocalAgentRunToPromptQualityResponse(_message.Message):
    __slots__ = ("request_id", "primary_invocation_id")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    primary_invocation_id: str
    def __init__(self, request_id: _Optional[str] = ..., primary_invocation_id: _Optional[str] = ...) -> None: ...

class UserContextInjection(_message.Message):
    __slots__ = ("user_message", "request_context")
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_message: UserMessage
    request_context: RequestContext
    def __init__(self, user_message: _Optional[_Union[UserMessage, _Mapping]] = ..., request_context: _Optional[_Union[RequestContext, _Mapping]] = ...) -> None: ...

class UserDisplayInfo(_message.Message):
    __slots__ = ("user_id", "display_name", "email", "profile_picture_url")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    display_name: str
    email: str
    profile_picture_url: str
    def __init__(self, user_id: _Optional[int] = ..., display_name: _Optional[str] = ..., email: _Optional[str] = ..., profile_picture_url: _Optional[str] = ...) -> None: ...

class UserGitContext(_message.Message):
    __slots__ = ("username", "email")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    username: str
    email: str
    def __init__(self, username: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class UserMessage(_message.Message):
    __slots__ = ("text", "message_id", "selected_context", "mode", "is_simulated_msg", "best_of_n_group_id", "try_use_best_of_n_promotion", "rich_text", "simulated_msg_reason", "conversation_state_blob_id", "subagent_system_reminder", "triggering_user_info", "execute_plan_info", "simulated_message_metadata", "prompt_reference_id", "thread_id", "text_blob_id", "rich_text_blob_id", "hook_additional_contexts", "custom_mode_intent", "project_details")
    class SimulatedMessageMetadata(_message.Message):
        __slots__ = ("title", "task_id", "fsd_finding_action", "url", "subscription_source", "subscription_event_display")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TASK_ID_FIELD_NUMBER: _ClassVar[int]
        FSD_FINDING_ACTION_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_SOURCE_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_EVENT_DISPLAY_FIELD_NUMBER: _ClassVar[int]
        title: str
        task_id: str
        fsd_finding_action: str
        url: str
        subscription_source: SubscriptionSource
        subscription_event_display: SubscriptionEventDisplay
        def __init__(self, title: _Optional[str] = ..., task_id: _Optional[str] = ..., fsd_finding_action: _Optional[str] = ..., url: _Optional[str] = ..., subscription_source: _Optional[_Union[SubscriptionSource, str]] = ..., subscription_event_display: _Optional[_Union[SubscriptionEventDisplay, _Mapping]] = ...) -> None: ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IS_SIMULATED_MSG_FIELD_NUMBER: _ClassVar[int]
    BEST_OF_N_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TRY_USE_BEST_OF_N_PROMOTION_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_MSG_REASON_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_STATE_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    SUBAGENT_SYSTEM_REMINDER_FIELD_NUMBER: _ClassVar[int]
    TRIGGERING_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_PLAN_INFO_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_MESSAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    PROMPT_REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    RICH_TEXT_BLOB_ID_FIELD_NUMBER: _ClassVar[int]
    HOOK_ADDITIONAL_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MODE_INTENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    text: str
    message_id: str
    selected_context: SelectedContext
    mode: AgentMode
    is_simulated_msg: bool
    best_of_n_group_id: str
    try_use_best_of_n_promotion: bool
    rich_text: str
    simulated_msg_reason: SimulatedMsgReason
    conversation_state_blob_id: bytes
    subagent_system_reminder: str
    triggering_user_info: TriggeringUserInfo
    execute_plan_info: ExecutePlanInfo
    simulated_message_metadata: UserMessage.SimulatedMessageMetadata
    prompt_reference_id: str
    thread_id: str
    text_blob_id: bytes
    rich_text_blob_id: bytes
    hook_additional_contexts: _containers.RepeatedCompositeFieldContainer[HookAdditionalContext]
    custom_mode_intent: CustomModeIntent
    project_details: ProjectDetails
    def __init__(self, text: _Optional[str] = ..., message_id: _Optional[str] = ..., selected_context: _Optional[_Union[SelectedContext, _Mapping]] = ..., mode: _Optional[_Union[AgentMode, str]] = ..., is_simulated_msg: _Optional[bool] = ..., best_of_n_group_id: _Optional[str] = ..., try_use_best_of_n_promotion: _Optional[bool] = ..., rich_text: _Optional[str] = ..., simulated_msg_reason: _Optional[_Union[SimulatedMsgReason, str]] = ..., conversation_state_blob_id: _Optional[bytes] = ..., subagent_system_reminder: _Optional[str] = ..., triggering_user_info: _Optional[_Union[TriggeringUserInfo, _Mapping]] = ..., execute_plan_info: _Optional[_Union[ExecutePlanInfo, _Mapping]] = ..., simulated_message_metadata: _Optional[_Union[UserMessage.SimulatedMessageMetadata, _Mapping]] = ..., prompt_reference_id: _Optional[str] = ..., thread_id: _Optional[str] = ..., text_blob_id: _Optional[bytes] = ..., rich_text_blob_id: _Optional[bytes] = ..., hook_additional_contexts: _Optional[_Iterable[_Union[HookAdditionalContext, _Mapping]]] = ..., custom_mode_intent: _Optional[_Union[CustomModeIntent, _Mapping]] = ..., project_details: _Optional[_Union[ProjectDetails, _Mapping]] = ...) -> None: ...

class UserMessageAction(_message.Message):
    __slots__ = ("user_message", "request_context", "send_to_interaction_listener", "prepend_user_messages", "interrupted_pending_tool_call_resolutions", "conversation_history")
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SEND_TO_INTERACTION_LISTENER_FIELD_NUMBER: _ClassVar[int]
    PREPEND_USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    INTERRUPTED_PENDING_TOOL_CALL_RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    user_message: UserMessage
    request_context: RequestContext
    send_to_interaction_listener: bool
    prepend_user_messages: _containers.RepeatedCompositeFieldContainer[UserMessage]
    interrupted_pending_tool_call_resolutions: InterruptedPendingToolCallResolutions
    conversation_history: ConversationHistory
    def __init__(self, user_message: _Optional[_Union[UserMessage, _Mapping]] = ..., request_context: _Optional[_Union[RequestContext, _Mapping]] = ..., send_to_interaction_listener: _Optional[bool] = ..., prepend_user_messages: _Optional[_Iterable[_Union[UserMessage, _Mapping]]] = ..., interrupted_pending_tool_call_resolutions: _Optional[_Union[InterruptedPendingToolCallResolutions, _Mapping]] = ..., conversation_history: _Optional[_Union[ConversationHistory, _Mapping]] = ...) -> None: ...

class UserMessageAppendedUpdate(_message.Message):
    __slots__ = ("user_message",)
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user_message: UserMessage
    def __init__(self, user_message: _Optional[_Union[UserMessage, _Mapping]] = ...) -> None: ...

class VideoCut(_message.Message):
    __slots__ = ("start_ms", "end_ms", "reason")
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    start_ms: int
    end_ms: int
    reason: str
    def __init__(self, start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class WaitAction(_message.Message):
    __slots__ = ("duration_ms",)
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    duration_ms: int
    def __init__(self, duration_ms: _Optional[int] = ...) -> None: ...

class WarmRemoteAccessServerRequest(_message.Message):
    __slots__ = ("commit", "port", "connection_token")
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    commit: str
    port: int
    connection_token: str
    def __init__(self, commit: _Optional[str] = ..., port: _Optional[int] = ..., connection_token: _Optional[str] = ...) -> None: ...

class WarmRemoteAccessServerResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchAgentHostSessionBackgroundWorkEvent(_message.Message):
    __slots__ = ("snapshot", "state")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    snapshot: AgentHostSessionBackgroundWorkSnapshot
    state: AgentHostSessionBackgroundWorkState
    def __init__(self, snapshot: _Optional[_Union[AgentHostSessionBackgroundWorkSnapshot, _Mapping]] = ..., state: _Optional[_Union[AgentHostSessionBackgroundWorkState, _Mapping]] = ...) -> None: ...

class WatchAgentHostSessionBackgroundWorkRequest(_message.Message):
    __slots__ = ("session_id", "kind", "state", "owner_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    kind: AgentHostBackgroundWorkKind
    state: AgentHostBackgroundWorkState
    owner_id: str
    def __init__(self, session_id: _Optional[str] = ..., kind: _Optional[_Union[AgentHostBackgroundWorkKind, str]] = ..., state: _Optional[_Union[AgentHostBackgroundWorkState, str]] = ..., owner_id: _Optional[str] = ...) -> None: ...

class WatchAgentHostSessionInteractionsEvent(_message.Message):
    __slots__ = ("snapshot", "state")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    snapshot: AgentHostSessionInteractionsSnapshot
    state: AgentHostSessionInteractionsState
    def __init__(self, snapshot: _Optional[_Union[AgentHostSessionInteractionsSnapshot, _Mapping]] = ..., state: _Optional[_Union[AgentHostSessionInteractionsState, _Mapping]] = ...) -> None: ...

class WatchAgentHostSessionInteractionsRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class WatchAgentHostSessionsEvent(_message.Message):
    __slots__ = ("snapshot", "added", "updated", "deleted")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    ADDED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    snapshot: AgentHostSessionsSnapshot
    added: AgentHostSessionAdded
    updated: AgentHostSessionUpdated
    deleted: AgentHostSessionDeleted
    def __init__(self, snapshot: _Optional[_Union[AgentHostSessionsSnapshot, _Mapping]] = ..., added: _Optional[_Union[AgentHostSessionAdded, _Mapping]] = ..., updated: _Optional[_Union[AgentHostSessionUpdated, _Mapping]] = ..., deleted: _Optional[_Union[AgentHostSessionDeleted, _Mapping]] = ...) -> None: ...

class WatchAgentHostSessionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchStatusResponse(_message.Message):
    __slots__ = ("worker_id", "status", "connected", "claimed")
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    CLAIMED_FIELD_NUMBER: _ClassVar[int]
    worker_id: str
    status: PrivateWorkerStatus
    connected: bool
    claimed: bool
    def __init__(self, worker_id: _Optional[str] = ..., status: _Optional[_Union[PrivateWorkerStatus, str]] = ..., connected: _Optional[bool] = ..., claimed: _Optional[bool] = ...) -> None: ...

class WebFetchAllowlistPrecheckArgs(_message.Message):
    __slots__ = ("url", "tool_call_id")
    URL_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    tool_call_id: str
    def __init__(self, url: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class WebFetchAllowlistPrecheckResult(_message.Message):
    __slots__ = ("allowlisted",)
    ALLOWLISTED_FIELD_NUMBER: _ClassVar[int]
    allowlisted: bool
    def __init__(self, allowlisted: _Optional[bool] = ...) -> None: ...

class WebFetchArgs(_message.Message):
    __slots__ = ("url", "tool_call_id")
    URL_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    tool_call_id: str
    def __init__(self, url: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class WebFetchError(_message.Message):
    __slots__ = ("url", "error")
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    url: str
    error: str
    def __init__(self, url: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class WebFetchRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class WebFetchRequestQuery(_message.Message):
    __slots__ = ("args", "skip_approval", "smart_mode_approval")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    SKIP_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    SMART_MODE_APPROVAL_FIELD_NUMBER: _ClassVar[int]
    args: WebFetchArgs
    skip_approval: bool
    smart_mode_approval: SmartModeApproval
    def __init__(self, args: _Optional[_Union[WebFetchArgs, _Mapping]] = ..., skip_approval: _Optional[bool] = ..., smart_mode_approval: _Optional[_Union[SmartModeApproval, _Mapping]] = ...) -> None: ...

class WebFetchRequestResponse(_message.Message):
    __slots__ = ("approved", "rejected")
    class Approved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Rejected(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    approved: WebFetchRequestResponse.Approved
    rejected: WebFetchRequestResponse.Rejected
    def __init__(self, approved: _Optional[_Union[WebFetchRequestResponse.Approved, _Mapping]] = ..., rejected: _Optional[_Union[WebFetchRequestResponse.Rejected, _Mapping]] = ...) -> None: ...

class WebFetchResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: WebFetchSuccess
    error: WebFetchError
    rejected: WebFetchRejected
    def __init__(self, success: _Optional[_Union[WebFetchSuccess, _Mapping]] = ..., error: _Optional[_Union[WebFetchError, _Mapping]] = ..., rejected: _Optional[_Union[WebFetchRejected, _Mapping]] = ...) -> None: ...

class WebFetchSuccess(_message.Message):
    __slots__ = ("url", "markdown", "output_location")
    URL_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    url: str
    markdown: str
    output_location: OutputLocation
    def __init__(self, url: _Optional[str] = ..., markdown: _Optional[str] = ..., output_location: _Optional[_Union[OutputLocation, _Mapping]] = ...) -> None: ...

class WebFetchToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: WebFetchArgs
    result: WebFetchResult
    def __init__(self, args: _Optional[_Union[WebFetchArgs, _Mapping]] = ..., result: _Optional[_Union[WebFetchResult, _Mapping]] = ...) -> None: ...

class WebSearchArgs(_message.Message):
    __slots__ = ("search_term", "tool_call_id")
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    tool_call_id: str
    def __init__(self, search_term: _Optional[str] = ..., tool_call_id: _Optional[str] = ...) -> None: ...

class WebSearchError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class WebSearchReference(_message.Message):
    __slots__ = ("title", "url", "chunk")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    title: str
    url: str
    chunk: str
    def __init__(self, title: _Optional[str] = ..., url: _Optional[str] = ..., chunk: _Optional[str] = ...) -> None: ...

class WebSearchRejected(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class WebSearchRequestQuery(_message.Message):
    __slots__ = ("args",)
    ARGS_FIELD_NUMBER: _ClassVar[int]
    args: WebSearchArgs
    def __init__(self, args: _Optional[_Union[WebSearchArgs, _Mapping]] = ...) -> None: ...

class WebSearchRequestResponse(_message.Message):
    __slots__ = ("approved", "rejected")
    class Approved(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Rejected(_message.Message):
        __slots__ = ("reason",)
        REASON_FIELD_NUMBER: _ClassVar[int]
        reason: str
        def __init__(self, reason: _Optional[str] = ...) -> None: ...
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    approved: WebSearchRequestResponse.Approved
    rejected: WebSearchRequestResponse.Rejected
    def __init__(self, approved: _Optional[_Union[WebSearchRequestResponse.Approved, _Mapping]] = ..., rejected: _Optional[_Union[WebSearchRequestResponse.Rejected, _Mapping]] = ...) -> None: ...

class WebSearchResult(_message.Message):
    __slots__ = ("success", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: WebSearchSuccess
    error: WebSearchError
    rejected: WebSearchRejected
    def __init__(self, success: _Optional[_Union[WebSearchSuccess, _Mapping]] = ..., error: _Optional[_Union[WebSearchError, _Mapping]] = ..., rejected: _Optional[_Union[WebSearchRejected, _Mapping]] = ...) -> None: ...

class WebSearchSuccess(_message.Message):
    __slots__ = ("references",)
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    references: _containers.RepeatedCompositeFieldContainer[WebSearchReference]
    def __init__(self, references: _Optional[_Iterable[_Union[WebSearchReference, _Mapping]]] = ...) -> None: ...

class WebSearchToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: WebSearchArgs
    result: WebSearchResult
    def __init__(self, args: _Optional[_Union[WebSearchArgs, _Mapping]] = ..., result: _Optional[_Union[WebSearchResult, _Mapping]] = ...) -> None: ...

class WriteArgs(_message.Message):
    __slots__ = ("path", "file_text", "tool_call_id", "return_file_content_after_write", "file_bytes", "encoding_hint")
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TEXT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    RETURN_FILE_CONTENT_AFTER_WRITE_FIELD_NUMBER: _ClassVar[int]
    FILE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENCODING_HINT_FIELD_NUMBER: _ClassVar[int]
    path: str
    file_text: str
    tool_call_id: str
    return_file_content_after_write: bool
    file_bytes: bytes
    encoding_hint: str
    def __init__(self, path: _Optional[str] = ..., file_text: _Optional[str] = ..., tool_call_id: _Optional[str] = ..., return_file_content_after_write: _Optional[bool] = ..., file_bytes: _Optional[bytes] = ..., encoding_hint: _Optional[str] = ...) -> None: ...

class WriteBinaryFileRequest(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: bytes
    def __init__(self, path: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class WriteBinaryFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WriteError(_message.Message):
    __slots__ = ("path", "error")
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    error: str
    def __init__(self, path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class WriteNoSpace(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class WritePermissionDenied(_message.Message):
    __slots__ = ("path", "directory", "operation", "error", "is_readonly")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    IS_READONLY_FIELD_NUMBER: _ClassVar[int]
    path: str
    directory: str
    operation: str
    error: str
    is_readonly: bool
    def __init__(self, path: _Optional[str] = ..., directory: _Optional[str] = ..., operation: _Optional[str] = ..., error: _Optional[str] = ..., is_readonly: _Optional[bool] = ...) -> None: ...

class WriteRejected(_message.Message):
    __slots__ = ("path", "reason")
    PATH_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    path: str
    reason: str
    def __init__(self, path: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class WriteResult(_message.Message):
    __slots__ = ("success", "permission_denied", "no_space", "error", "rejected")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
    NO_SPACE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    success: WriteSuccess
    permission_denied: WritePermissionDenied
    no_space: WriteNoSpace
    error: WriteError
    rejected: WriteRejected
    def __init__(self, success: _Optional[_Union[WriteSuccess, _Mapping]] = ..., permission_denied: _Optional[_Union[WritePermissionDenied, _Mapping]] = ..., no_space: _Optional[_Union[WriteNoSpace, _Mapping]] = ..., error: _Optional[_Union[WriteError, _Mapping]] = ..., rejected: _Optional[_Union[WriteRejected, _Mapping]] = ...) -> None: ...

class WriteShellStdinArgs(_message.Message):
    __slots__ = ("shell_id", "chars")
    SHELL_ID_FIELD_NUMBER: _ClassVar[int]
    CHARS_FIELD_NUMBER: _ClassVar[int]
    shell_id: int
    chars: str
    def __init__(self, shell_id: _Optional[int] = ..., chars: _Optional[str] = ...) -> None: ...

class WriteShellStdinError(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class WriteShellStdinResult(_message.Message):
    __slots__ = ("success", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: WriteShellStdinSuccess
    error: WriteShellStdinError
    def __init__(self, success: _Optional[_Union[WriteShellStdinSuccess, _Mapping]] = ..., error: _Optional[_Union[WriteShellStdinError, _Mapping]] = ...) -> None: ...

class WriteShellStdinSuccess(_message.Message):
    __slots__ = ("shell_id", "terminal_file_length_before_input_written")
    SHELL_ID_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_FILE_LENGTH_BEFORE_INPUT_WRITTEN_FIELD_NUMBER: _ClassVar[int]
    shell_id: int
    terminal_file_length_before_input_written: int
    def __init__(self, shell_id: _Optional[int] = ..., terminal_file_length_before_input_written: _Optional[int] = ...) -> None: ...

class WriteShellStdinToolCall(_message.Message):
    __slots__ = ("args", "result")
    ARGS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    args: WriteShellStdinArgs
    result: WriteShellStdinResult
    def __init__(self, args: _Optional[_Union[WriteShellStdinArgs, _Mapping]] = ..., result: _Optional[_Union[WriteShellStdinResult, _Mapping]] = ...) -> None: ...

class WriteSuccess(_message.Message):
    __slots__ = ("path", "lines_created", "file_size", "file_content_after_write")
    PATH_FIELD_NUMBER: _ClassVar[int]
    LINES_CREATED_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_CONTENT_AFTER_WRITE_FIELD_NUMBER: _ClassVar[int]
    path: str
    lines_created: int
    file_size: int
    file_content_after_write: str
    def __init__(self, path: _Optional[str] = ..., lines_created: _Optional[int] = ..., file_size: _Optional[int] = ..., file_content_after_write: _Optional[str] = ...) -> None: ...

class WriteTextFileRequest(_message.Message):
    __slots__ = ("path", "content")
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    def __init__(self, path: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class WriteTextFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ZoomCandidate(_message.Message):
    __slots__ = ("start_ms", "end_ms", "center_x", "center_y", "suggested_zoom", "action_type", "action_index", "importance_score", "context")
    START_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    CENTER_X_FIELD_NUMBER: _ClassVar[int]
    CENTER_Y_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_ZOOM_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    IMPORTANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    start_ms: int
    end_ms: int
    center_x: int
    center_y: int
    suggested_zoom: float
    action_type: str
    action_index: int
    importance_score: int
    context: str
    def __init__(self, start_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., center_x: _Optional[int] = ..., center_y: _Optional[int] = ..., suggested_zoom: _Optional[float] = ..., action_type: _Optional[str] = ..., action_index: _Optional[int] = ..., importance_score: _Optional[int] = ..., context: _Optional[str] = ...) -> None: ...

class ZoomSelection(_message.Message):
    __slots__ = ("candidate_index", "zoom_override", "start_ms_override", "end_ms_override")
    CANDIDATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ZOOM_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    START_MS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    END_MS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    candidate_index: int
    zoom_override: float
    start_ms_override: int
    end_ms_override: int
    def __init__(self, candidate_index: _Optional[int] = ..., zoom_override: _Optional[float] = ..., start_ms_override: _Optional[int] = ..., end_ms_override: _Optional[int] = ...) -> None: ...
