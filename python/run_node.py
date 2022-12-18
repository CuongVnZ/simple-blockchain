from node import Node
import json
from flask import Flask, jsonify, request


# Create a list to store the nodes in the network.
node_sets = []

# Create nodes and add them to the network.
node = Node("localhost:5000", node_sets)

app = Flask(__name__)

@app.route('/mine', methods=['GET'])
def mine():
    # Get the miner's address from the request body.
    miner_address = request.args.get('miner_address')
    if not node.is_valid_address(miner_address):
        return jsonify({'error': 'Invalid miner address'}), 400
    
    
    transaction = {
        "sender": "0",  # The mining reward is sent by the "0" address.
        "receiver": "0",
        "data": "Genesis block",
        "amount": 1
    }
    # Mine a new block.
    block = node.blockchain.mine(miner_address, transaction)

    # Return the response.
    response = {
        "message": "Block added to the blockchain.",
        "block": json.dumps(block, default=lambda o: o.__dict__, sort_keys=True, indent=4),
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def chain():
    blockchain = node.blockchain
    
    response = {
        'chain': json.dumps(blockchain.chain, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False),
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


app.run(host='0.0.0.0', port=5000)