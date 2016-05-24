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

for index, page in enumerate(db.get_collection(secret.PAGES).find()):
    raw = get_html_templtate(**page, template_parameter="page")
    pages[page['id']] = raw

with open("index.html", "w", encoding="utf-8") as f:
    f.write(str(pages))
pprint(pages)



'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <title>SuperBootcamp Small Gallery!!</title>
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet"/>
    <link href="gallery.css" rel="stylesheet"/>
</head>
<body>
<div class="container-fluid">

    <h1>
        SuperBootcamp Small Gallery!!
    </h1>

    <div class="row">

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Pooh!</h3>
                    <p>The best teddy bear ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Winnie The Pooh"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

    </div>

    <div class="row">

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

    </div>

    <div class="row">

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

    </div>

    <div class="row">

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/ym.png" alt="Moody">
                <div class="caption">
                    <h3>Moody</h3>
                    <p>Just my text no wiki for me :(
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

    </div>

    <div class="row">

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

        <div class="col-sm-6 col-md-3">
            <div class="thumbnail">
                <img src="images/snoopy.jpg" alt="Snoopy">
                <div class="caption">
                    <h3>Snoopy!</h3>
                    <p>The best character ever.</p>
                    <p><a href="https://en.wikipedia.org/wiki/Snoopy"
                          class="btn btn-primary"
                          role="button">Wikipedia</a>
                    </p>
                </div>
            </div>
        </div>

    </div>

</div>


</body>
</html>


'''
