import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, data):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'data': data,
        })

    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

# Example usage
blockchain = Blockchain()
blockchain.new_transaction("Hospital", "Credentialing Authority", {"credential": "MD", "name": "Dr. Jane Doe"})
blockchain.new_block(proof=12345)

with open('blockchain/credentials_chain.json', 'w') as file:
    json.dump(blockchain.chain, file)
