from flask import Flask, request
from create_db import fill_db, output

app = Flask(__name__)


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
    data = request.form.get('data')
    if data.split()[0] == 'get':
        offset, limit = data.split()[1:]
        query = output(int(offset), int(limit))
        return '\n'.join(map(str, query))
    else:
        return fill_db(data)


if __name__ == "__main__":
    app.run(debug=True)
