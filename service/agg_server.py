from bottle import route, run, template
import page_manager


@route('/')
def index():
    print("index")
    html = ""
    for id, page in page_manager.get_Pages().items():
        html += str(page)
    return template('<html><head></head><body>{{!body}}</body></html>!', body=html)


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


def run_server(host='localhost', port=8080):
    run(host=host, port=port)
