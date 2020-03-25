import requests
from requests.auth import AuthBase

# {'result': 'ok', 'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhdXRoX2xldmVsIjozLCJzY29wZXMiOlsiYnVpbGRpbmdzOnJlYWQiLCJhdXRoIiwiYWRtaW4iLCJnZW5lcmFsIiwiaW5nZXN0IiwidWkiXSwibG9nZ2VkX2luIjp0cnVlLCJzdWIiOjExMiwiaWF0IjoxNTg1MDk0MjI5LCJleHAiOjE1ODUyMzgyMjl9.lnHyCT2Xi9V1qsmQlsQjH-IoPpRgoKEGsak93OxW2Knhopu2YfEZVQMCCxueRibvWXjdqmuVwb9NajllZRhLIw', 'token_type': 'bearer', 'userInfo': {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhdXRoX2xldmVsIjozLCJzY29wZXMiOlsiYnVpbGRpbmdzOnJlYWQiLCJhdXRoIiwiYWRtaW4iLCJnZW5lcmFsIiwiaW5nZXN0IiwidWkiXSwibG9nZ2VkX2luIjp0cnVlLCJzdWIiOjExMiwiaWF0IjoxNTg1MDk0MjI5LCJleHAiOjE1ODUyMzgyMjl9.lnHyCT2Xi9V1qsmQlsQjH-IoPpRgoKEGsak93OxW2Knhopu2YfEZVQMCCxueRibvWXjdqmuVwb9NajllZRhLIw', 'scopes': ['buildings:read', 'auth', 'admin', 'general', 'ingest', 'ui']}}

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


url = 'https://api.onboarddata.io/login/api-key'
toke = "ob-p-VJqnaGrdsEX4LS9LOxdG2a-4sHnVAlVC976lnOnr9Lq8eLbIMff66HCa6IgT0XdSC-s"
r = requests.post(url, {"key": toke})


burl = 'https://api.onboarddata.io/buildings'
r2 = requests.get(burl, {"key": toke})


