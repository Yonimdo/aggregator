'''add_page 1.0

Usage:
  add_page name <name>
  add_page -h | --help
  add_page --update-all
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
import sys
import re

URL = "{}?fields=about,picture,hometown,fan_count,bio,insights.limit(1),category,name"


def get_facebook_o(url):
    try:
        graph = facebook.GraphAPI(access_token=secret.APP_TOKEN, version='2.5')
        o = graph.get_object(
            url)
    except facebook.GraphAPIError:
        o = False
    return o


def insert_update_page(o, url="", check=False):
    client = pymongo.MongoClient()
    db = client.get_database(secret.DB)
    # pages = db.drop_collection('pages')
    pages = db.get_collection(secret.PAGES)
    pages.create_index('id', unique=True)
    update_rst = pages.update({'id': o['id']},
                              {'id': o['id'],
                               'likes': o['fan_count'],
                               'category': o['category'],
                               'about': o['about'],
                               'name': o['name'],
                               'picture': o['picture']['data']['url'],
                               'url': url,

                               },
                              upsert=True)

    if (check):
        count = 0
        for page in pages.find({'id': o['id']}):
            if update_rst['updatedExisting']:
                pprint(
                    "OK, modified id #{} named {} with {} fans. url: {}".format(page['id'], page['name'], page['likes'],
                                                                                page['url']))
            else:
                pprint("OK, added id #{} named {} with {} fans. ".format(page['id'], page['name'], page['likes']))
            assert count >= 0
            count -= 1


def update_page_by_name(name):
    url = URL.format(name)
    o = get_facebook_o(url)
    if o:
        insert_update_page(o, url, check=True)
        return True
    return False


if __name__ == '__main__':
    arguments = docopt(__doc__, version='add_page 1.0')
    if arguments['--reset']:
        client = pymongo.MongoClient()
        db = client.get_database(secret.DB)
        db.drop_collection(secret.PAGES)
    if arguments['--update-all']:
        client = pymongo.MongoClient()
        db = client.get_database(secret.DB)
        for page in db.get_collection(secret.PAGES).find():
            update_page_by_name(page['id'])

    if arguments['name']:
        if update_page_by_name(arguments['<name>']) == False:
            print("Not a page")
