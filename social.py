'''social 1.0

Usage:
  social add <link>
  social list
  social serve [--port=8000] [--interface=127.0.0.1]
  social update page_id <page_id> [--limit=100]
  social update
  social remove <page_id>
  social -h | --help
  social --version
  social --reset

Options:
    add <link>:  add <link> page to the database
    list <link>:  add <link> page to the database
    serve :  run the agg_serve with --port and --interface if given if not runs on 127.0.0.1:8080
    update <page_id>:  updating or adding the <page_id> page and update page post with --limit if not given of 100
    remove <page_id>:  remove <page_id> page from the database


'''
from pprint import pprint

from docopt import docopt

import page_manager
import posts_manager
import show_pages
from service import agg_server
from testing import demo_urls

if __name__ == "__main__":
    arguments = docopt(__doc__, version='agg_server 1.0')
    if arguments['serve']:
        host = arguments['--interface'] if arguments['--interface'] else "localhost"
        port = int(arguments['--port']) if arguments['--port'] else 8080
        agg_server.run_server(host=host, port=port)
    if arguments['update']:
        if arguments['page_id']:
            page_manager.update_page_by_name(arguments['<page_id>'])
            limit = arguments['--limit'] if arguments['--limit'] else 100
            posts_manager.update_post_by_id(arguments['<page_id>'], limit)
        else:
            ids = [id for id, page in show_pages.get_Pages(False).items()]
            page_manager.update_multi_ids(ids)
            ids = [id for id, page in page_manager.get_Pages(False).items()]
            demo_urls.update_multi_ids(ids)
    if arguments['add']:
        page_manager.update_page_by_name(arguments['<link>'])
    if arguments['remove']:
        page_manager.remove_page_by_id(arguments['<page_id>'])
    if arguments['list']:
        pprint(page_manager.get_Pages(False))
    if arguments['--reset']:
        page_manager.reset_db()
        posts_manager.reset_db()
        pprint(page_manager.get_Pages(False))
