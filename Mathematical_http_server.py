from flask import Flask, request
from mathematical_logic import Logic

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
    return Logic.multi_func(data)


if __name__ == "__main__":
    app.run(debug=True)
