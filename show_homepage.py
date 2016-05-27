from pprint import pprint

import show_pages
import show_posts
from bottle import route, run, template
import agg_server

pages = show_pages.get_Pages(True)


@route('/')
def index():
    html = ""
    for page_id in pages:
        posts = show_posts.get_posts(page_id, 3, True)
        html += '''<div class="row">'''
        html += str(show_pages.pages[page_id])
        for post in posts:
            html += '''<h2>test paragraph test text checking UI.</h2>'''
        html += '''</div>'''

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
