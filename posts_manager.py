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
from pprint import pprint
from docopt import docopt

import core
import secret
from dal import mdb_connect, fb_connect
import templates

templates.get_html_templtate(
    template_parameter="post",
    template='''
 <div class="col-sm-6 col-md-3">
        <div class="thumbnail">
            <div class="caption">
                <h6>{created_time}</h6>
                <p>{message}</p>
            </div>
        </div>
    </div>
''')
URL = "{}/posts?limit={}"
URL_IDs = "{}?/?fields=id,name"


def insert_update_posts(input, o_creator_id, url="", check=False):
    modified, add = 0, 0
    jobs = [(mdb_connect.insert_update, secret.POSTS, o['id'], {'id': o['id'],
                                                                'message': o.get('message', ""),
                                                                'created_time': o['created_time'],
                                                                'creator_id': o_creator_id
                                                                }) for o in input['data']]
    core.do_jobs(jobs)
    if (check):  # to do check jobs
        pass
    return add, modified


def update_post_by_id(id, limit=100):
    add, modified = 0, 0
    url = URL.format(id, limit)
    o = fb_connect.get_facebook_o(url)
    o_creator = fb_connect.get_facebook_o(URL_IDs.format(arguments['<name>']))
    if o:
        add, modified = insert_update_posts(o, o_creator['id'], url, check=True)
    return add, modified


def remove_post_by_id(post_id):
    mdb_connect.remove_page(secret.POSTS, post_id)


def reset_db():
    mdb_connect.reset_db(secret.PAGES)


def get_posts(creator_id, limit=100, as_html=True):
    posts = {}
    limit = int(limit)
    for index, post in enumerate(mdb_connect.get_collection(secret.POSTS, {"creator_id": creator_id})):
        if index == limit:
            break
        raw = templates.get_html_templtate(**post, template_parameter="post") if as_html else post
        posts[post['id']] = raw
    return posts


if __name__ == '__main__':
    arguments = docopt(__doc__, version='add_page 1.0')
    if arguments['--reset']:
        reset_db()
    if arguments['name']:
        limit = arguments['--limit'] if arguments['--limit'] else 100
        add, modified = update_post_by_id(arguments['<name>'], limit)
        o_creator = fb_connect.get_facebook_o(URL_IDs.format(arguments['<name>']))
        print("""Updating page "{}"
            Inserted {} posts, update {} posts.""".format(o_creator['name'], add, modified))
    arguments = docopt(__doc__, version='show_posts 1.0')
    if arguments['print']:
        posts = get_posts(arguments['id'], limit=arguments['<limit>']) if arguments['limit'] else get_posts(
            arguments['id'])
        pprint(posts)
