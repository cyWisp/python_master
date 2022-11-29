#!/usr/bin/env python
from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return 'OK', 204

@app.route('/total', methods=['GET'])
def get_total():
    total = sum([x['amount'] for x in incomes])
    return str(total), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)