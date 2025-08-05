import requests
from typing import Optional

class HelixF:
    def __init__(self, helix_id:str, apikey: str ):
        self.helix_id = helix_id
        self.apikey = apikey
        self.base_url = f'https://apps.fireeye.com/helix/id/{self.helix_id}/api'
        self.header = {
            'accept': 'application/json',
            'x-fireeye-api-key': self.apikey
        }
        
    