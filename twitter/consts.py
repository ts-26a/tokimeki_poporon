from requests_oauthlib import OAuth1Session
from json import load
import os

# URL:
url_update = "https://api.twitter.com/1.1/statuses/update.json"
url_follow = "https://api.twitter.com/1.1/followers/list.json"
url_icon = "https://api.twitter.com/1.1/account/update_profile_image.json"
url_search_std = "https://api.twitter.com/1.1/search/tweets.json"

# common variables:
id_list = []
tweet_list = []

with open(os.path.dirname(os.path.abspath(__file__)) + "/env.json", "r") as f:
    data = load(f)
userID = data["userID"]
CK = data["CK"]
CS = data["CS"]
AT = data["AT"]
AS = data["AS"]

twitter = OAuth1Session(CK, CS, AT, AS)
