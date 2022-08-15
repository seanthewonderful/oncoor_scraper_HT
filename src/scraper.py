import requests
import json
import os
import datetime
import argparse
from mako.template import Template


endpoint = "https://api.twitter.com/2/tweets/search/recent?query="
bearer_token = os.environ.get("BEARER_TOKEN")
twitter_api_key = os.environ.get("TWITTER_API_KEY")
twitter_api_key_secret = os.environ.get("TWITTER_API_KEY_SECRET")
# oauth
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


headers = {
    "access_token": "PbCpzCP5aVq39GembNWSAo89V",
    "token_secret": "aKOYl7fP4lQauA9yKDaBrC67Kl8d2SYiVtXnY4O3luC5FvurX1",
    "bearer_token": "Bearer AAAAAAAAAAAAAAAAAAAAAGefcQEAAAAAWtdc9ZAkIjTgWx%2FP7l7h4KXV%2BX8%3DsEfZdl5ZeZtEaf8om1JPhy51PAJYaEpyuGf1TkAHybiPNAPmGG"
}
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# params = {
#     'id': "2620199928"
# }

hashtag_params = "sponsored"

url = endpoint + hashtag_params

response = requests.get(url=endpoint, params=params, headers=headers)
print(response.json())