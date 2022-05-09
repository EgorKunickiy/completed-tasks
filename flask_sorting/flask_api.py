from flask import Flask, jsonify, request
from math_logic import get_sort
from parser import parse

app = Flask(__name__)


@app.route('/SelectionSort', methods=['POST'])
def proc_selection_sort():
    f_json = request.get_json()
    print(type(f_json))
    data = parse(f_json)
    result = get_sort(data, "selection sort")
    return jsonify(result)


@app.route('/InsertionSort', methods=['POST'])
def proc_insertion_sort():
    f_json = request.get_json()
    data = parse(f_json)
    result = get_sort(data, "insertion sort")
    return jsonify(result)


@app.route('/HeapSort', methods=['POST'])
def proc_heap_sort():
    f_json = request.get_json()
    data = parse(f_json)
    result = get_sort(data, "heap sort")
    return jsonify(result)


@app.route('/FastSort', methods=['POST'])
def proc_fast_sort():
    f_json = request.get_json()
    data = parse(f_json)
    result = get_sort(data, "fast sort")
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
