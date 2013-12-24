import api_keys
from requests_oauthlib import OAuth1Session
import json
import sys

def stream(hashtag):
    twitter = OAuth1Session(api_keys.KEY, client_secret=api_keys.SECRET,
                            resource_owner_key=api_keys.TOKEN,
                            resource_owner_secret=api_keys.TOKEN_SECRET)

    r = twitter.post(
        'https://stream.twitter.com/1.1/statuses/filter.json',
        data={
            'track': hashtag
            },
        stream=True
    )

    for line in r.iter_lines():
        if line:
            print line

if __name__ == '__main__':
    hashtag = 'twitter'
    if len(sys.argv) >= 2:
        hashtag = sys.argv[1]
    stream(hashtag)
