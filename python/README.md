
# Simple proof-of-work blockchain in Python

This code defines a simple blockchain and a proof-of-work algorithm, and exposes two HTTP endpoints for mining blocks and getting the current state of the blockchain.

The `Block` class represents a single block in the blockchain, and has the following attributes:

index: the position of the block in the blockchain.
- `timestamp` : the time at which the block was created.
- `data` : the data contained in the block.
- `previous_hash` : the hash of the previous block in the blockchain.
- `nonce` : a value that is incremented and included in the block's hash until the block's hash meets certain criteria (in this case, it must start with a certain number of zeros).
- `hash` : the block's hash.

The `Blockchain` class represents a blockchain, and has the following attributes:

- `difficulty`: the number of zeros that the block's hash must start with in order for the proof-of-work to be considered valid.
- `chain`: a list of Block objects representing the blocks in the blockchain.

The mine_block function mines a new block by calling the proof_of_work function on the last block in the blockchain, and then appending the newly mined block to the chain. The get_chain function returns the current state of the blockchain in JSON format.