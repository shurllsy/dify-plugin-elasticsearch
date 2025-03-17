from elasticsearch import Elasticsearch


class ElasticsearchBaseTool:
    @staticmethod
    def auth(credentials: dict):
        endpoint = credentials.get("endpoint", "")
        api_key = credentials.get("api_key", None)
        client = Elasticsearch(endpoint, api_key=api_key)
        return client.info()

    def from_credential(self, credentials: dict) -> Elasticsearch:
        endpoint = credentials.get("endpoint", "")
        api_key = credentials.get("api_key", None)
        return Elasticsearch(endpoint, api_key=api_key)
