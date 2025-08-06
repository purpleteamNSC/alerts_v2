import requests


class HelixTrellix:
    def __init__(
        self, helix_id: str, client_id: str, secret: str, scope: str, apikey: str = ""
    ):
        self.helix_id = helix_id
        self.client_id = client_id
        self.secret = secret
        self.scope = scope
        self.apikey = apikey
        self.base_url = f"https://apps.fireeye.com/helix/id/{self.helix_id}/api"
        self.header = {"accept": "application/json", "x-fireeye-api-key": self.apikey}

    def get_token(self):
        url = "https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token"

        auth = (self.client_id, self.secret)

        headers = {}

        data = {"grant_type": "client_credentials", "scope": self.scope}

    def get_alerts_v1(self):
        pass

    def get_alerts_v3(self):
        pass


class HelixFireeye:
    def __init__(self, helix_id: str, api_key: str):
        self.helix_id = helix_id
        self.api_key = api_key
        self.headers = {"x-fireeye-api-key": self.api_key}

    def get_alerts_v3(self):
        url = f"https://apps.fireeye.com/helix/id/{self.helix_id}/api/v3/alerts"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Lança exceção para códigos 4xx ou 5xx
            return response.json()  # Retorna o JSON com os alertas
        except requests.exceptions.HTTPError as errh:
            print(f"Erro HTTP: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Erro de conexão: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Erro inesperado: {err}")

        return None
