import twitter
import json
from local_setting import twitter_api

CK = twitter_api.CK  # Consumer Key
CS = twitter_api.CS  # Consumer Secret
AT = twitter_api.AT  # Access Token
AS = twitter_api.AS  # Access Token Secert

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

api = twitter.Api(consumer_key=CK, consumer_secret=CS,
                  access_token_key=AT, access_token_secret=AS)


class JsonManager:
    @staticmethod
    def get_data(*files):
        data = []
        for file in files:
            r = open(file)
            lines = r.readlines()
            result = ''
            for (i, line) in enumerate(lines):
                # ignore first line
                if i == 0:
                    continue
                result += line
            data.append(json.loads(result))
        return data




