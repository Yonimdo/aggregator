import requests
import facebook
import secret

URL = "https://graph.facebook.com/oauth/access_token"

r = requests.get(URL, {
    'client_id': secret.APP_ID,
    'client_secret': secret.APP_SECRET,
    'grant_type': 'client_credentials',
})


def get_facebook_o(url):
    try:
        graph = facebook.GraphAPI(access_token=secret.APP_TOKEN, version='2.5')
        o = graph.get_object(
            url)
    except facebook.GraphAPIError:
        o = False
    return o

r.raise_for_status()

key, value = r.text.split("=")
assert key == "access_token"

with open("TOKEN.txt", "w") as f:
    f.write(value)

print("OK")