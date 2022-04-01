import flask
import requests


app = flask.Flask(__name__)


def get_answer_from_serv(url: str, inter_dict: dict):
    try:
        answer = requests.head(url)
        if answer.status_code == 200:
            inter_dict[url] = 'ok'
        else:
            answer = requests.get(url)
            if answer.status_code == 200:
                inter_dict[url] = 'ok'
    except requests.exceptions.ConnectionError:
        inter_dict[url] = 'no'


@app.route('/', methods=['POST', 'GET'])
def form_example():
    # handle the POST request
    if flask.request.method == 'POST':
        urls = flask.request.form.get('url')
        print(urls.split(', '))
        inter_dict = dict()
        for i in urls.split(', '):
            get_answer_from_serv(i, inter_dict)
        print(inter_dict)
        return flask.jsonify(inter_dict)

    return '''
                  <html>
      <head>
        <title>Title of the document</title>
        <style>
          label {
            display: block;
            width: 130px;
          }
        </style>
      </head>
      <body>
        <form method="POST">
           <label for="url">Enter URLs:</label>
          <input id="url" name="url" type="text" />
        </form>
      </body>
    </html>'''


if __name__ == "__main__":
    app.run(debug=True)
