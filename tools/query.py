import json
from collections.abc import Generator
from typing import Any
from elasticsearch import Elasticsearch
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ElasticsearchQueryTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        endpoint = self.runtime.credentials.get("endpoint", "")
        api_key = self.runtime.credentials.get("api_key", None)
        client = Elasticsearch(endpoint, api_key=api_key)
        index = tool_parameters.get("index", None)
        query = tool_parameters.get("query")
        from_ = tool_parameters.get("from", 0)
        size = tool_parameters.get("size", 10)
        if index is None:
            client.info()
            return None

        resp = client.search(
            index=index, query=json.loads(query), from_=from_, size=size
        )
        result = []
        for hit in resp['hits']['hits']:
            result.append(hit['_source'])
        yield self.create_text_message(json.dumps(result))
        yield self.create_json_message({
            "result": result
        })
