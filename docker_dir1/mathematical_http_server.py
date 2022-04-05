import flask
from create_db import processing_to_query

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return """<html>
    <head></head>
    <body>
        <form method="post" enctype="multipart/form-data">
            <input type="text" name="data" />
        </form>
    </body>
    </html>"""


@app.route('/', methods=['POST'])
def index_post():
    data = flask.request.form.get('data')
    return processing_to_query(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
