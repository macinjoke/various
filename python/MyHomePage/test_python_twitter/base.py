import twitter

CK = 'tz2EzaqMRoZHnzyy4ZDDu1bTZ'                             # Consumer Key
CS = '9Euua9A6wS7dt6MxIyRAHsNSUHnQeegTENdVsWAkoBXaBXRgch'         # Consumer Secret
AT = '2385251989-A7gIU2lwFsbbFIVWRjQVclW2vYcDDm1ZNshMrvu' # Access Token
AS = 'f0Nlpe8UP19ipNpUTXCh28SJ5AgqLh77m71pxpCaj81qJ'         # Accesss Token Secert

api = twitter.Api(consumer_key=CK, consumer_secret=CS,
                  access_token_key=AT, access_token_secret=AS)

