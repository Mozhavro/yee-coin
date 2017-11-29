from datetime import datetime
import json
from flask import Flask, request, make_response
from block_chain import BlockChain


# def next_block(last_block):
#     this_index = last_block.index + 1
#     this_timestamp = datetime.now()
#     this_data = "Hey! I'm block " + str(this_index)
#     this_hash = last_block.hash
#     return Block(this_index, this_timestamp, this_data, this_hash)

# def main():
#     # Create the blockchain and add the genesis block
#     genesis = Block(0, datetime.now(), "Genesis Block", "0")
#     blockchain = [genesis]
#     previous_block = blockchain[0]

#     # How many blocks should we add to the chain
#     # after the genesis block
#     num_of_blocks_to_add = 20

#     # Add blocks to the chain
#     for i in range(0, num_of_blocks_to_add):
#         block_to_add = next_block(previous_block)
#         blockchain.append(block_to_add)
#         previous_block = block_to_add
#         # Tell everyone about it!
#         print("Block #{} has been added to the blockchain!".format(block_to_add.index))
#         print("Hash: {}".format(block_to_add.hash) )
#         print("Nonce: {}\n".format(block_to_add.nonce))

app = Flask(__name__)
blockchain = BlockChain()


def pp(data):
    html = "<pre>{}</pre>".format(data)
    return make_response(html)

@app.route('/', methods=['GET'])
def index():
    return pp(blockchain.to_json())


@app.route('/mine', methods=['GET'])
def mine():
    blockchain.mine_new_block()
    return pp(blockchain.to_json())

@app.route('/add-transaction', methods=['POST'])
def add_transaction():
    donor = request.form.get("donor")
    recipient = request.form.get("recipient")
    amount = request.form.get("amount")
    blockchain.add_transaction(donor, recipient, amount)
    return pp(blockchain.to_json())

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()