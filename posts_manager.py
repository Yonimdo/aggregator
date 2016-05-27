'''posts_manager 1.0

Usage:
  posts_manager name <name> [--limit=100]
  posts_manager -h | --help
  posts_manager --version
  posts_manager --reset

Options:

    add_or_update_all_post is a mongo db class that updates posts from the  wanted page
    please hold a mongod service open, and insert name

  --version     version 1.0
  name      the name of the page (without spaces).

'''
from face_api import get_facebook_o
from docopt import docopt
from pprint import pprint
import secret
import facebook
import pymongo

URL = "{}/posts?limit={}"
URL_IDs = "{}?/?fields=id,name"


def insert_update_posts(input, o_creator_id, url="", check=False):
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    # pages = db.drop_collection('pages')
    posts = db.get_collection(secret.POSTS)
    posts.create_index('id', unique=True)

    modified, add = 0, 0
    for o in input['data']:
        update_rst = posts.update({'id': o['id']},
                                  {'id': o['id'],
                                   'message': o.get('message', ""),
                                   'created_time': o['created_time'],
                                   'creator_id': o_creator_id
                                   },
                                  upsert=True)

        if (check):
            for page in posts.find({'id': o['id']}):
                if update_rst['updatedExisting']:
                    modified += 1
                else:
                    add += 1
    return add, modified


def update_post_by_id(id, limit=100):
    add, modified = 0, 0
    url = URL.format(id, limit)
    o = get_facebook_o(url)
    o_creator = get_facebook_o(URL_IDs.format(arguments['<name>']))
    if o:
        add, modified = insert_update_posts(o, o_creator['id'], url, check=True)
    return add, modified


def reset_db():
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    db.drop_collection(secret.POSTS)


if __name__ == '__main__':
    arguments = docopt(__doc__, version='add_page 1.0')
    if arguments['--reset']:
        reset_db()
    if arguments['name']:
        limit = arguments['--limit'] if arguments['--limit'] else 100
        add, modified = update_post_by_id(arguments['<name>'], limit)
        o_creator = get_facebook_o(URL_IDs.format(arguments['<name>']))
        print("""Updating page "{}"
            Inserted {} posts, update {} posts.""".format(o_creator['name'], add, modified))
