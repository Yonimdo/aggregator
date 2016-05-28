from pprint import pprint

import page_manager
import posts_manager

from bottle import route, run, template
from service import agg_server

pages = page_manager.get_Pages(True)


@route('/')
def index():
    html = ""
    for page_id in pages:
        print("page id: {}".format(page_id))
        posts = posts_manager.get_posts(page_id, 3, True)
        html += '''<div class="row">'''
        html += str(pages[page_id])
        pprint("posts length = {}".format(len(posts)))
        for post in posts:
            html += posts[post] # posts is EMPTY!?
        for i in range(3): # dummy line to show text where a post should be
            html += '''<div><h3>This is where a post should be. However, no posts are retrieved by page_id. (??????)</h3></div>'''
        html += '''<div class="clearfix visible-xs"></div></div>'''

    return template('''<html>
                        <head>
                            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
                            <meta name="viewport" content="width=device-width, initial-scale=1">
                            <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        </head>
                        <body>
                            <div class="container">{{!body}}<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
                                <!-- Include all compiled plugins (below), or include individual files as needed -->
                                <script src="js/bootstrap.min.js"></script>
                            </div>
                        </body>
                    </html>!''', body=html)


@route('/css/our_css')
def css():
    with open("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css") as f:
        return f.read()
    # with open("css/temp.css") as f:
    #     return f.read()



if __name__ == "__main__":
    index()
    agg_server.run_server('localhost', 8080)
