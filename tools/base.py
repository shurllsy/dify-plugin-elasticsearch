from elasticsearch import Elasticsearch


class ElasticsearchBaseTool:
    def auth(self, credentials: dict):
        client = self.from_credential(credentials=credentials)
        return client.info()

    def from_credential(self, credentials: dict) -> Elasticsearch:
        endpoint = credentials.get("endpoint", "")
        auth_method = credentials.get("auth_method")
        if auth_method == "no_auth":
            return Elasticsearch(endpoint)
        elif auth_method == "basic":
            username = credentials.get("username")
            password = credentials.get("password")
            return Elasticsearch(endpoint, basic_auth=(username, password))
        elif auth_method == "api_key":
            api_key = credentials.get("api_key")
            return Elasticsearch(endpoint, api_key=api_key)
        else:
            raise ValueError("Invalid auth_method")
