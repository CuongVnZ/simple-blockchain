import hashlib
import time
import json
from flask import Flask, jsonify

# Define the difficulty for the proof-of-work algorithm
DIFFICULTY = 4

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Computes the hash of the block using SHA-256.
        """
        data = str(self.index) + str(self.data) + str(self.timestamp) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def proof_of_work(self, difficulty):
        """
        Simple proof-of-work algorithm.
        """
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.calc_hash()

        return self

class Blockchain:
    def __init__(self):
        self.difficulty = DIFFICULTY
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Generates the first block in the blockchain.
        """
        return Block(0, "Genesis Block", "0")

    def get_last_block(self):
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain.
        """
        last_block = self.get_last_block()
        new_block = Block(last_block.index + 1, data, last_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        """
        Check if the blockchain is valid.
        """
        for i in range(1, len(self.chain)):
            prev_block = self.chain[i-1]
            curr_block = self.chain[i]
            if curr_block.hash != curr_block.calc_hash():
                return False
            if curr_block.previous_hash != prev_block.hash:
                return False
        return True

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    # get the data we need to create a block
    last_block = blockchain.get_last_block()
    block = last_block.proof_of_work(blockchain.difficulty)

    if block:
        response = {
            'message': 'Block mined!',
            'index': block.index,
            'timestamp': block.timestamp,
            'nonce': block.nonce,
            'hash': block.hash,
            'previous_hash': block.previous_hash
        }
        blockchain.add_block("Next block")
        return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': json.dumps(blockchain.chain, default=lambda o: o.__dict__, sort_keys=True, indent=4),
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)