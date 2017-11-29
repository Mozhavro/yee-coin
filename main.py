from datetime import datetime
import json
from flask import Flask, request, make_response
from block_chain import BlockChain


app = Flask(__name__)
blockchain = BlockChain()
transactions = []


def pp(data):
    html = "<pre>{}</pre>".format(data)
    return make_response(html)

@app.route('/', methods=['GET'])
def index():
    return pp(blockchain.to_json())


@app.route('/mine', methods=['GET'])
def mine():
    blockchain.mine_new_block(transactions[:])
    transactions.clear()
    return pp(blockchain.to_json())

@app.route('/add-transaction', methods=['POST'])
def add_transaction():
    transaction = {
        "donor": request.form.get("donor"),
        "recipient": request.form.get("recipient"),
        "amount": request.form.get("amount"),
        "timestamp": datetime.now()
    }
    transactions.append(transaction)
    return pp(json.dumps(transaction, indent=4, default=str))

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()