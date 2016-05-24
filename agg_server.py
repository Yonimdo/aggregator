from bottle import route, run, template
import show_pages


@route('/')
def index():
    print("index")
    html = ""
    for page_id in show_pages.pages:
        html += str(show_pages.pages[page_id])
    return template('<html><head></head><body>{{!body}}</body></html>!', body=html)


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)
