import constant
import oauth2
import urllib.parse as urlparse

consumer = oauth2.Consumer(constant.CONSUMER_KEY, constant.CONSUMER_SECRET)
client = oauth2.Client(consumer)

response, content = client.request(constant.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('An error happen! `request token from Twitter`')

request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

