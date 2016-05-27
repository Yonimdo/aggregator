'''page_manager 1.0

Usage:
  add_page name <name>
  add_page -h | --help
  add_page --update-all
  add_page --version
  add_page --reset
  add page print
Options:

    add_page is a mongo db class that hold information on wanted pages
    please hold a mongod service open, and insert url,name

  --version     version 1.0
  name      the name of the page (without spaces).

'''

from docopt import docopt
from pprint import pprint
import secret
from dal import mdb_connect, fb_connect
from concurrent import futures
import pymongo
import sys
import re
import core
import templates

templates.get_html_templtate(
    template_parameter="page",
    template='''
 <div class="col-sm-6 col-md-3">
        <div class="thumbnail">
            <img src="{picture}" alt="{name}">
            <div class="caption">
                <h3>{name}</h3>
                <h6>{category}</h6>
                <p>{about}</p>
            </div>
        </div>
    </div>
''')
URL = "{}?fields=about,picture,hometown,fan_count,bio,insights.limit(1),category,name"


def insert_update_page(o, url="", check=False):
    update_rst = mdb_connect.insert_update(secret.PAGES, o['id'], data={'id': o['id'],
                                                                        'likes': o['fan_count'],
                                                                        'category': o['category'],
                                                                        'about': o['about'],
                                                                        'name': o['name'],
                                                                        'picture': o['picture']['data']['url'],
                                                                        'url': url,
                                                                        })
    # fast assertion area (when prod should cp to Unit test?)
    if (check):
        if update_rst['updatedExisting']:
            pprint(
                "OK, modified id #{} named {} with {} fans. url: {}".format(page['id'], page['name'], page['likes'],
                                                                            page['url']))
        else:
            pprint("OK, added id #{} named {} with {} fans. ".format(page['id'], page['name'], page['likes']))


def update_page_by_name(name):
    url = URL.format(name)
    o = fb_connect.get_facebook_o(url)
    if o:
        insert_update_page(o, url, check=True)
        return True
    return False


def remove_page_by_id(page_id):
    mdb_connect.remove_page(secret.PAGES, page_id)


def update_multi_ids(ids):
    jobs = [(update_page_by_name, id) for id in ids]
    core.do_jobs(jobs)


def reset_db():
    mdb_connect.reset_db(secret.PAGES)


def get_Pages(as_html=True):
    pages = {}
    for index, page in enumerate(mdb_connect.get_collection(secret.PAGES)):
        raw = templates.get_html_templtate(**page, template_parameter="page") if as_html else page
        pages[page['id']] = raw
    return pages


if __name__ == '__main__':
    arguments = docopt(__doc__, version='add_page 1.0')
    if arguments['--reset']:
        reset_db()
    if arguments['--update-all']:
        client = pymongo.MongoClient()
        db = client.get_database(secret.DB)
        for page in db.get_collection(secret.PAGES).find():
            update_page_by_name(page['id'])
    if arguments["print"]:
        pprint(get_Pages())
    if arguments['name']:
        if update_page_by_name(arguments['<name>']) == False:
            print("Not a page")
