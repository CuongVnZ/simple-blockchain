import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, nonce, miner_address, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = nonce
        self.miner_address = miner_address
        self.transactions = transactions

    def get_header(self):
        """
        Get the block header as a bytes object.
        """
        block_string = f"{self.index}:{self.previous_hash}:{self.timestamp}:{self.nonce}"
        return block_string.encode()

    def get_hash(self):
        """
        Calculate the hash of the block.
        """
        header = self.get_header()
        return hashlib.sha256(header).hexdigest()
            
    def add_transaction(self, transaction):
        self.transactions.append(transaction)