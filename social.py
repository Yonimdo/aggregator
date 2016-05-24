'''social 1.0

Usage:
  social add <link>
  social list
  social serve [--port=8000] [--interface=127.0.0.1]
  social update page_id <page_id> [--limit=100]
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
from bottle import route, run, template
import show_pages
import add_page
import agg_server
import get_or_update_all_posts

if __name__ == "__main__":
    arguments = docopt(__doc__, version='agg_server 1.0')
    if arguments['serve']:
        host = arguments['--interface'] if arguments['--interface'] else "localhost"
        port = int(arguments['--port']) if arguments['--port'] else 8080
        agg_server.run_server(host=host, port=port)
    if arguments['update']:
        add_page.update_page_by_name(arguments['<page_id>'])
        limit = arguments['--limit'] if arguments['--limit'] else 100
        get_or_update_all_posts.update_post_by_id(arguments['<page_id>'], limit)
    if arguments['add']:
        add_page.update_page_by_name(arguments['<link>'])
    if arguments['remove']:
        add_page.remove_page_by_id(arguments['<page_id>'])
    if arguments['list']:
        pprint(show_pages.get_Pages(False))
    if arguments['--reset']:
        add_page.reset_db()
        get_or_update_all_posts.reset_db()
        pprint(show_pages.get_Pages(False))
