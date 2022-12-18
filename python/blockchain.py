import hashlib
import time
from flask import Flask, jsonify, request
from block import Block

# Define the difficulty for the proof-of-work algorithm
DIFFICULTY = 4

class Blockchain:
    def __init__(self):
        self.difficulty = DIFFICULTY
        self.chain = [self.create_genesis_block()]
        self.balances = {}

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
            "0",
            time.time(),
            "0",
            0,
            [transaction],
        )

    def update_balances(self):
        """
        Update the balances dictionary with the transactions in the last block.
        """
        last_block = self.get_last_block()

        # Loop through the transactions in the last block.
        for transaction in last_block.transactions:
            # Update the sender's balance.
            if transaction["sender"] in self.balances:
                self.balances[transaction["sender"]] -= transaction["amount"]
            else:
                self.balances[transaction["sender"]] = -transaction["amount"]

            # Update the receiver's balance.
            if transaction["receiver"] in self.balances:
                self.balances[transaction["receiver"]] += transaction["amount"]
            else:
                self.balances[transaction["receiver"]] = transaction["amount"]

    def proof_of_work(self, block):
        """
        Find a valid proof for the block.
        """
        while True:
            # Calculate the hash of the block.
            block_hash = block.get_hash()
            # Check if the hash starts with the required number of zeros.
            if block_hash.startswith('0' * self.difficulty):
                # If it does, return the nonce as the valid proof.
                return block_hash
            # If the hash does not start with the required number of zeros,
            # try the next nonce value.
            block.nonce += 1


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
        self.update_balances()

    
    def mine(self, miner_address, transaction):
        """
        Mines a new block and adds it to the blockchain.
        """
        last_block = self.get_last_block()
        
        # Create a new block using the transaction and the hash of the last block.
        new_block = Block(
            last_block.index + 1,
            last_block.get_hash(),
            time.time(),
            0,
            miner_address,
            [transaction],
        )

        # Find a valid proof for the new block.
        proof = self.proof_of_work(new_block)
        if(proof):
            # Add the new block to the chain.
            self.add_block(new_block)
            return new_block