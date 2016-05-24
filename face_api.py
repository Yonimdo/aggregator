import facebook
import secret


def get_facebook_o(url):
    try:
        graph = facebook.GraphAPI(access_token=secret.APP_TOKEN, version='2.5')
        o = graph.get_object(
            url)
    except facebook.GraphAPIError:
        o = False
    return o
