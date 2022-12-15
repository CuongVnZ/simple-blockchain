
# Simple proof-of-work blockchain in Python

This is a simple implementation of a blockchain in Python using Flask. The code defines a Block class to represent a block in the chain, and a Blockchain class to represent the entire chain. The Blockchain class contains several methods to manage the chain, including methods to add new blocks and to validate the proof-of-work for each block.

To run the code, you need to install Flask and start the Flask development server:

$ pip install Flask
$ python app.py

You can then access the blockchain API using HTTP requests. To mine a new block, you can use the /mine endpoint, which accepts a miner_address parameter that specifies the address to which the mining reward should be sent. For example:

$ curl http://localhost:5000/mine?miner_address=0x12345

This will mine a new block and add it to the blockchain. You can view the current state of the chain by accessing the /chain endpoint:

$ curl http://localhost:5000/chain

This will return a JSON object that contains the entire blockchain, as well as the current length of the chain.