import { FormEvent, useEffect, useState } from "react";
import {
  createModel,
  deleteModel,
  emptyModelInput,
  listModels,
  testModel,
  updateModel,
  type ConnectivityResult,
  type Model,
  type ModelInput,
} from "../api/client";
import { Button } from "../shared/ui/Button";
import controls from "../shared/ui/Controls.module.scss";
import { Field } from "../shared/ui/Field";
import fieldStyles from "../shared/ui/Field.module.scss";
import { TitledCard } from "../shared/ui/TitledCard";
import { PageContent, pageStyles } from "../shell/layout/PageContent";

const controlUrl =
  (import.meta.env.VITE_CONTROL_URL as string | undefined) ?? "http://127.0.0.1:8787";

function toInput(model: Model): ModelInput {
  return {
    display_name: model.display_name,
    provider_type: model.provider_type,
    base_url: model.base_url,
    api_key: model.api_key,
    model_name: model.model_name,
    notes: model.notes,
    context_tokens: model.context_tokens,
    max_output_tokens: model.max_output_tokens,
    enabled: model.enabled,
    sort_order: model.sort_order,
    extra: model.extra,
    headers: model.headers,
  };
}

export function ModelsPage() {
  const [models, setModels] = useState<Model[]>([]);
  const [draft, setDraft] = useState<ModelInput>(emptyModelInput());
  const [editingId, setEditingId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [testingId, setTestingId] = useState<string | null>(null);
  const [results, setResults] = useState<Record<string, ConnectivityResult>>({});

  const reload = async () => {
    setModels(await listModels(controlUrl));
  };

  useEffect(() => {
    void reload().catch((cause: unknown) => {
      setError(cause instanceof Error ? cause.message : String(cause));
    });
  }, []);

  const resetForm = () => {
    setEditingId(null);
    setDraft(emptyModelInput());
  };

  const onEdit = (model: Model) => {
    setEditingId(model.id);
    setDraft(toInput(model));
    setError(null);
  };

  const onSubmit = async (event: FormEvent) => {
    event.preventDefault();
    setBusy(true);
    setError(null);
    try {
      if (editingId) {
        await updateModel(controlUrl, editingId, draft);
      } else {
        await createModel(controlUrl, { ...draft, sort_order: models.length + 1 });
      }
      resetForm();
      await reload();
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  const onDelete = async (id: string) => {
    setBusy(true);
    setError(null);
    try {
      await deleteModel(controlUrl, id);
      if (editingId === id) resetForm();
      await reload();
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setBusy(false);
    }
  };

  const onTest = async (id: string) => {
    setBusy(true);
    setTestingId(id);
    setError(null);
    try {
      const result = await testModel(controlUrl, id);
      setResults((current) => ({ ...current, [id]: result }));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : String(cause));
    } finally {
      setTestingId(null);
      setBusy(false);
    }
  };

  return (
    <PageContent title="Cursor">
      {error ? <p className={pageStyles.err}>{error}</p> : null}
      <TitledCard title="模型列表">
        <ul className={pageStyles.list}>
          {models.map((model) => {
            const result = results[model.id];
            const active = editingId === model.id;
            return (
              <li key={model.id} className={pageStyles.listItem}>
                <div>
                  <strong>
                    {model.display_name}
                    {active ? " · 编辑中" : null}
                    {!model.enabled ? " · 已停用" : null}
                  </strong>
                  <div className={pageStyles.muted}>
                    {model.provider_type} · {model.model_name}
                  </div>
                  {testingId === model.id ? (
                    <div className={pageStyles.muted}>测试中…</div>
                  ) : result ? (
                    <div className={result.ok ? pageStyles.ok : pageStyles.err}>
                      {result.ok
                        ? `连通 · 首字 ${result.first_token_ms ?? "-"}ms · 总 ${result.total_ms}ms`
                        : `失败 · ${result.error ?? "无响应"}`}
                    </div>
                  ) : null}
                </div>
                <div className={pageStyles.actions} data-no-drag>
                  <Button size="small" disabled={busy} onClick={() => onEdit(model)}>
                    更改
                  </Button>
                  <Button size="small" disabled={busy} onClick={() => void onTest(model.id)}>
                    {testingId === model.id ? "测试中…" : "测试"}
                  </Button>
                  <Button
                    size="small"
                    className={controls.danger}
                    disabled={busy}
                    onClick={() => void onDelete(model.id)}
                  >
                    删除
                  </Button>
                </div>
              </li>
            );
          })}
          {models.length === 0 ? <li className={pageStyles.muted}>还没有模型，先添加一个。</li> : null}
        </ul>
      </TitledCard>
      <TitledCard title={editingId ? "更改模型" : "添加模型"}>
        <form className={pageStyles.form} onSubmit={(event) => void onSubmit(event)} data-no-drag>
          <Field label="显示名称">
            <input
              value={draft.display_name}
              onChange={(event) => setDraft({ ...draft, display_name: event.target.value })}
              required
            />
          </Field>
          <Field label="协议">
            <select
              value={draft.provider_type}
              onChange={(event) =>
                setDraft({
                  ...draft,
                  provider_type: event.target.value as ModelInput["provider_type"],
                })
              }
            >
              <option value="openai_responses">OpenAI Responses</option>
              <option value="openai_chat">OpenAI Chat</option>
              <option value="anthropic">Anthropic</option>
            </select>
          </Field>
          <Field label="服务地址">
            <input
              value={draft.base_url}
              onChange={(event) => setDraft({ ...draft, base_url: event.target.value })}
              required
            />
          </Field>
          <Field label="模型名称">
            <input
              value={draft.model_name}
              onChange={(event) => setDraft({ ...draft, model_name: event.target.value })}
              required
            />
          </Field>
          <Field label="API Key">
            <input
              type="password"
              value={draft.api_key}
              onChange={(event) => setDraft({ ...draft, api_key: event.target.value })}
            />
          </Field>
          <Field label="备注">
            <input
              value={draft.notes}
              onChange={(event) => setDraft({ ...draft, notes: event.target.value })}
            />
          </Field>
          <Field label="上下文窗口">
            <input
              type="number"
              value={draft.context_tokens}
              onChange={(event) =>
                setDraft({ ...draft, context_tokens: Number(event.target.value) || 0 })
              }
            />
          </Field>
          <Field label="最大输出">
            <input
              type="number"
              value={draft.max_output_tokens}
              onChange={(event) =>
                setDraft({ ...draft, max_output_tokens: Number(event.target.value) || 0 })
              }
            />
          </Field>
          <label className={`${fieldStyles.root} ${fieldStyles.check}`}>
            <input
              type="checkbox"
              checked={draft.enabled}
              onChange={(event) => setDraft({ ...draft, enabled: event.target.checked })}
            />
            启用
          </label>
          <div className={pageStyles.actions}>
            <Button type="submit" variant="primary" disabled={busy}>
              {editingId ? "保存更改" : "添加模型"}
            </Button>
            {editingId ? (
              <Button type="button" disabled={busy} onClick={resetForm}>
                取消
              </Button>
            ) : null}
          </div>
        </form>
      </TitledCard>
    </PageContent>
  );
}
