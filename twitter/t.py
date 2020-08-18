from tweet_post import (
    initialize,
    fetch_offset,
    tweet_destroy,
    tweet_post,
    tweet_edit,
    tweet_icon,
    id_to_unix,
    time_check,
)
from consts import CK, CS, AT, AS, id_list, tweet_list
from subprocess import run
import os
from sys import __stderr__

twitter = initialize(CK, CS, AT, AS)
offset = fetch_offset()

while True:
    print("Input: ", end="")
    tweet = input()
    if tweet == "cls":
        try:
            if os.name == "nt":
                run("cls")
            else:
                run("clear")
            id_list = []
            tweet_list = []
        except Exception as e:
            print(e, file=__stderr__)
    elif tweet[0:6] == "delete":
        id_list, tweet_list = tweet_destroy(id_list, tweet_list, tweet, twitter)
    elif tweet[0:4] == "edit":
        id_list, tweet_list = tweet_edit(id_list, tweet_list, tweet, twitter)
    elif tweet[0:4] == "icon":
        tweet_icon(tweet, twitter)
    elif tweet[0:6] == "offset":
        offset = fetch_offset()
    elif tweet[0:5] == "check":
        time_check(tweet, twitter)
    elif (tweet.isdigit()) and (len(tweet) == 19):
        print(id_to_unix(int(tweet)).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    else:
        id_list, tweet_list = tweet_post(id_list, tweet_list, tweet, offset, twitter)
