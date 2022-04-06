from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

json = ''


def calculate(json):
    jsn_out = {
        'SumResult': 0,
        'MulResult': 1,
        'SortedInputs': []
    }
    k = json['K']
    sum = 0
    for el in json['Sums']:
        sum += el
        jsn_out['SortedInputs'].append(el)

    jsn_out['SumResult'] = round(sum * k, 2)

    for el in json['Muls']:
        jsn_out['MulResult'] *= el
        jsn_out['SortedInputs'].append(el)

    jsn_out['SortedInputs'].sort()
    return jsn_out


@app.route('/')
def index():
    return ''


@app.route('/Ping')
def ping():
    res = requests.get('http://127.0.0.1:5000/')
    if res.status_code == 200:
        return jsonify(res.status_code)
    else:
        return 'server X_x'


@app.route('/PostInputData', methods=['POST'])
def post_input_data():

    json = request.get_json()

    return jsonify(json)


@app.route('/GetAnswer')
def get_answer():
    return jsonify(calculate(json))


if __name__ == '__main__':
    app.run(debug=True)
