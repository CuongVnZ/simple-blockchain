import hashlib
import time
import json
from flask import Flask, jsonify, request

# Define the difficulty for the proof-of-work algorithm
DIFFICULTY = 4

class Block:
    def __init__(self, index, timestamp, transaction, proof, nonce, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.proof = proof
        self.nonce = nonce
        self.previous_hash = previous_hash

    def hash(self):
        """
        Calculate the hash of this block.
        """
        # Convert the block into a string representation.
        block_string = f"{self.index}:{self.timestamp}:{self.transaction}:{self.proof}:{self.nonce}:{self.previous_hash}"
        # Calculate the hash of the string representation.
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.difficulty = DIFFICULTY
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Generates the first block in the blockchain.
        """
        # Create a new transaction.
        transaction = {
            "sender": "0",  # The mining reward is sent by the "0" address.
            "receiver": "0",
            "data": "Genesis block",
            "amount": 1
        }
        return Block(
            0,
            time.time(),
            [transaction],
            None,
            None,
            "0",
        )

    def proof_of_work(self, block):
        nonce = 0
        while not self.valid_proof(block, nonce):
            nonce += 1
        return nonce

    def get_last_block(self):
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain.
        """
        self.chain.append(new_block)

    def valid_proof(self, block, nonce):
        """
        Check if the block is valid.
        """
        # Calculate the hash of the block and the nonce.
        guess = f"{block}:{nonce}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # The proof is valid if the hash starts with two zeroes.
        return guess_hash.startswith('0' * self.difficulty)

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # Get the data we need to create a block
    last_block = blockchain.get_last_block()

    nonce = blockchain.proof_of_work(last_block)
    previous_hash = str(last_block.hash())

    # Generate the proof using the nonce and the last block's proof
    proof = hashlib.sha256(f"{last_block}:{nonce}".encode()).hexdigest()

    # Create a new transaction.
    transaction = {
        "sender": "0",  # The mining reward is sent by the "0" address.
        "receiver": request.args.get("miner_address"),
        "data": "New generated block",
        "amount": 1,
    }

    # Create a new block and add it to the blockchain.
    block = Block(
        last_block.index + 1,
        time.time(),
        [transaction],
        proof,
        nonce,
        previous_hash,
    )
    blockchain.add_block(block)

    # Return the response.
    response = {
        "message": "Block added to the blockchain.",
        "block": json.dumps(block, default=lambda o: o.__dict__, sort_keys=True, indent=4),
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def chain():
    response = {
        'chain': json.dumps(blockchain.chain, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False),
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)