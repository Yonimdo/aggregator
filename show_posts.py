import pymongo
import secret
from templates import get_html_templtate
from pprint import pprint

client = pymongo.MongoClient()
db = client.get_database(secret.DB)

posts = {}

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


def get_post(creator_id, limit=100):
    for index, post in enumerate(db.get_collection(secret.POSTS).find({{'creator_id': creator_id}})):
        if index == limit:
            break
        raw = get_html_templtate(**post, template_parameter="post")
        posts[post['id']] = raw


# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(str(pages))
pprint(posts)
