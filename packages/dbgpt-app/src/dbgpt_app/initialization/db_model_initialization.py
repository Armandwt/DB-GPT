"""Import all models to make sure they are registered with SQLAlchemy."""

from dbgpt.model.cluster.registry_impl.db_storage import ModelInstanceEntity
from dbgpt.storage.chat_history.chat_history_db import (
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
)
from dbgpt_app.openapi.api_v1.feedback.feed_back_db import ChatFeedBackEntity
from dbgpt_serve.agent.app.recommend_question.recommend_question import (
    RecommendQuestionEntity,
)
from dbgpt_serve.agent.hub.db.my_plugin_db import MyPluginEntity
from dbgpt_serve.agent.hub.db.plugin_hub_db import PluginHubEntity
from dbgpt_serve.datasource.manages.connect_config_db import ConnectConfigEntity
from dbgpt_serve.file.models.models import ServeEntity as FileServeEntity
from dbgpt_serve.flow.models.models import ServeEntity as FlowServeEntity
from dbgpt_serve.flow.models.models import VariablesEntity as FlowVariableEntity
from dbgpt_serve.prompt.models.models import ServeEntity as PromptManageEntity
from dbgpt_serve.rag.models.chunk_db import DocumentChunkEntity
from dbgpt_serve.rag.models.document_db import KnowledgeDocumentEntity
from dbgpt_serve.rag.models.models import KnowledgeSpaceEntity

_MODELS = [
    PluginHubEntity,
    FileServeEntity,
    MyPluginEntity,
    PromptManageEntity,
    KnowledgeSpaceEntity,
    KnowledgeDocumentEntity,
    DocumentChunkEntity,
    ChatFeedBackEntity,
    ConnectConfigEntity,
    ChatHistoryEntity,
    ChatHistoryMessageEntity,
    ModelInstanceEntity,
    FlowServeEntity,
    RecommendQuestionEntity,
    FlowVariableEntity,
]
