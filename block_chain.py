import json
import pprint
from datetime import datetime
from block import Block


class BlockChain:
    def __init__(self, chain=None):
        self._chain = chain or [Block(0, datetime.now(), "0")]

    def add_transaction(self, donor, recipient, amount):
        self._chain[-1].add_transaction(donor, recipient, amount)

    def mine_new_block(self):
        last_block = self._chain[-1]
        this_index = last_block.index + 1
        this_timestamp = datetime.now()
        this_data = []
        this_hash = last_block.hash
        new_block = Block(this_index, this_timestamp, this_hash, this_data)
        self._chain.append(new_block)

    def to_json(self):
        serialized_chain = [block.__dict__ for block in self._chain]
        pprint.pprint(serialized_chain)
        return json.dumps(serialized_chain, indent=4, default=str)
