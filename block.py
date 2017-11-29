import hashlib
import config


class Block:
    def __init__(self, index, timestamp, data, prev_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.prev_hash = prev_hash
        self.mine()

    def hash_block(self):
        sha = hashlib.sha256()
        block_data = (str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.nonce) +
                   str(self.prev_hash))
        sha.update(block_data.encode('utf-8'))
        return sha.hexdigest()

    def is_valid(self, hashstring):
        for rule in config.VALIDATION_RULES:
            if not rule(hashstring):
                return False

        return True

    def mine(self):
        self.hash = self.hash_block()
        while not self.is_valid(self.hash):
            self.nonce += 1
            self.hash = self.hash_block()
