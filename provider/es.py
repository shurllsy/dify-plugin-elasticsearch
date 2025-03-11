from typing import Any
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from tools.query import ElasticsearchQueryTool


class ElasticsearchProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            tools = ElasticsearchQueryTool.from_credentials(credentials=credentials)
            for response in tools.invoke(tool_parameters={"index": None}):
                pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
