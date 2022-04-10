import flask
import requests
import multiprocessing


app = flask.Flask(__name__)


def get_answer_from_serv(url: str) -> str:
    try:
        answer = requests.head(url)
        if answer.status_code != 405:
            return 'ok'
        else:
            answer = requests.get(url)
            if answer.status_code != 405:
                return 'ok'
            else:
                return 'no connection'
    except requests.exceptions.ConnectionError:
        return 'no connection'


def processing_url(urls: list):
    with multiprocessing.Pool() as pool:
        res = pool.map(get_answer_from_serv, urls)
    return dict(zip(urls, res))


@app.route('/', methods=['POST', 'GET'])
def form_example():
    # handle the POST request
    if flask.request.method == 'POST':
        # URLs are entered with ", "
        url = flask.request.form.get('url')

        answers = processing_url(url.split(', '))
        return flask.jsonify(answers)

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
