'''show_posts 1.0

Usage:
  show_posts id <id>
  show_posts id <id> limit <limit>
  show_posts -h | --help
  show_posts --version
  show_posts --reset

Options:

    show_posts is a mongo db class that gets the posts for the name given
  --version     version 1.0
  id      the name of the posts creator (without spaces).

'''
from docopt import docopt
import pymongo
import secret
from templates import get_html_templtate
from pprint import pprint

client = pymongo.MongoClient()
db = client.get_database(secret.DB)

get_html_templtate(
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


def get_posts(creator_id, limit=100, as_html=True):
    posts = {}
    limit = int(limit)
    for index, post in enumerate(db.get_collection(secret.POSTS).find()):
        if index == limit:
            break
        raw = get_html_templtate(**post, template_parameter="post") if as_html else post
        posts[post['id']] = raw
    return posts


# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(str(pages))




if __name__ == '__main__':
    arguments = docopt(__doc__, version='show_posts 1.0')
    if arguments['--reset']:
        client = pymongo.MongoClient()
        db = client.get_database(secret.DB)
        db.drop_collection(secret.POSTS)
    if arguments['id']:
        posts = get_posts(arguments['id'], limit=arguments['<limit>']) if arguments['limit'] else get_posts(
            arguments['id'])
        pprint(posts)
