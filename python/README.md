
# Simple proof-of-work blockchain in Python

This is a simple implementation of a blockchain in Python using Flask. The code defines a `Block` class to represent a block in the chain, and a `Blockchain` class to represent the entire chain. The `Blockchain` class contains several methods to manage the chain, including methods to add new blocks and to validate the proof-of-work for each block.

## Running the code

To run the code, you need to install Flask and start the Flask development server:

```sh
$ pip install Flask
$ python run_node.py
```


## Using the blockchain API

You can access the blockchain API using HTTP requests. To mine a new block, you can use the `/mine` endpoint, which accepts a `miner_address` parameter that specifies the address to which the mining reward should be sent. For example:

```sh
$ curl http://localhost:5000/mine?miner_address=0x12345
```


This will mine a new block and add it to the blockchain. You can view the current state of the chain by accessing the `/chain` endpoint:

```sh
$ curl http://localhost:5000/chain
```


This will return a JSON object that contains the entire blockchain, as well as the current length of the chain.


## To-do list (Network implementation):

- Implement the `find_longest_chain` method, which should return the longest blockchain among the nodes in `node_sets`.
- Add error handling for the case where the block being added is not valid or does not extend the local copy of the blockchain.
- Consider adding a method for sending a request for the latest block or for the entire blockchain to other nodes, to be used in the `synchronize` method.
- Add documentation for each method, including a brief description of what it does and the parameters it takes (if any).
- Add unit tests for each method to ensure that they are working as intended.
- Consider adding a method for starting the node and connecting to the network, if the node is not already connected. This could involve setting up a server to listen for incoming connections and sending out requests to join the network to other nodes.
- Think about how to handle cases where multiple nodes broadcast conflicting transactions or blocks. This may involve adding a method for resolving conflicts and ensuring that the local copy of the blockchain is consistent with the network.
- Consider adding methods for other functionality that may be needed for a full implementation of a Bitcoin node, such as retrieving the balance of an address or generating new addresses.