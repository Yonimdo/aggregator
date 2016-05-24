'''add_page 1.0

Usage:
  add_page name <name>
  add_page -h | --help
  add_page --version
  add_page --reset

Options:

    add_page is a mongo db class that hold information on wanted pages
    please hold a mongod service open, and insert url,name

  --version     version 1.0
  name      the name of the page (without spaces).

'''

from docopt import docopt
from pprint import pprint
import secret
import facebook
import pymongo

URL = "{}?/posts?fields=id,name,limit=100"


def get_facebook_o(url):
    try:
        graph = facebook.GraphAPI(access_token=secret.APP_TOKEN, version='2.5')
        o = graph.get_object(
            url)
    except facebook.GraphAPIError:
        o = False
    return o


def insert_update_posts(posts, url="", check=False):
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    # pages = db.drop_collection('pages')
    posts = db.get_collection(secret.POSTS)
    posts.create_index('id', unique=True)
    modified, add = 0, 0
    for o in posts['data']:
        update_rst = posts.update({'id': o['id']},
                                  {'message': o['message'],
                                   'created_time': o['created_time'],
                                   'creator_id': o['id']
                                   },
                                  upsert=True)

        if (check):
            for page in posts.find({'id': o['id']}):
                if update_rst['updatedExisting']:
                    modified += 1
                else:
                    add += 1

    print("""Updating page "{}"
Inserted {} posts, update {} posts.""".format(o['name'], add, modified))


# if __name__ == "__main__":

if __name__ == '__main__':
    arguments = docopt(__doc__, version='add_page 1.0')
    if arguments['--reset']:
        client = pymongo.MongoClient()
        db = client.get_database(secret.DB)
        db.drop_collection(secret.PAGES)
    if arguments['name']:
        url = URL.format(arguments['<name>'])
        o = get_facebook_o(url)
        if o:
            insert_update_posts(o, url, check=True)
