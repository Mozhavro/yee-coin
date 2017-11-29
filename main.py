from datetime import datetime

from block import Block


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def main():
    # Create the blockchain and add the genesis block
    genesis = Block(0, datetime.now(), "Genesis Block", "0")
    blockchain = [genesis]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain
    # after the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}".format(block_to_add.hash) )
        print("Nonce: {}\n".format(block_to_add.nonce))


if __name__ == '__main__':
    main()