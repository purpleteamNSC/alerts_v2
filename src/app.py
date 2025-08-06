import os
from dotenv import load_dotenv
load_dotenv()
from api import HelixFireeye as hf,HelixTrellix as ht

helix_id=os.getenv('HELIX_ID_F')
api_key=os.getenv('API_KEY_FIREEYE')

company = hf(helix_id,api_key)

r = company.get_alerts_v3()
print(r)