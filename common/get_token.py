import requests
import json
from config import host

def get_token():
    data = {"loginName": "admin", "password": "123456", "type": "01"}
    r = requests.post(host + "/provider/user/bsUser/login", data)
    respon = r.text
    token = json.loads(respon)["data"]["token"]
    return token

if __name__ == "__main__":
    get_token()