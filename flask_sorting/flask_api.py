from flask import Flask, jsonify, request
import math_logic
app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_input_data():
    f_json = request.get_json()
    print(f_json)
    return jsonify(f_json)


if __name__ == '__main__':
    app.run(debug=True)
