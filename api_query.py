import requests
import ast
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


url = 'https://api.onboarddata.io/login/api-key'
key = "ob-p-VJqnaGrdsEX4LS9LOxdG2a-4sHnVAlVC976lnOnr9Lq8eLbIMff66HCa6IgT0XdSC-s"
r = requests.post(url, {"key": key})
# r_dict = ast.literal_eval(r.text)
# access_toke = r_dict['access_token']

headers = {
    'accept': 'application/json',
    'X-OB-Api': key
}

burl = 'https://api.onboarddata.io/buildings'
r2 = requests.get(burl, headers=headers)



