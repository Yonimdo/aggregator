import pymongo
import secret
from templates import get_html_templtate
from pprint import pprint

client = pymongo.MongoClient()
db = client.get_database(secret.DB)

pages = {}

get_html_templtate(
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


def get_Pages(as_html=True):
    pages = {}
    for index, page in enumerate(db.get_collection(secret.PAGES).find()):
        raw = get_html_templtate(**page, template_parameter="page") if as_html else page
        pages[page['id']] = raw
    return pages


pages = get_Pages()

if __name__ == "__main__":
    pprint(pages)
