import hashlib
import json
from time import time

class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#creates the genesis block
		self.new_block(proof=100, previous_hash=1)
	
	def new_block(self, proof, previous_hash=None):
		#Creates a new block and adds it to the chain
		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}

		#reset the current list of transactions
		self.current_transactions = []

		self.chain.append(block)

		return block
	
	def new_transaction(self, sender, recipient, amount):
		#Adds a new transaction to the list of transactions
		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount,
		})
		
		return self.last_block['index'] + 1
	
	@staticmethod
	def hash(block):
		#Creates a SHA-256 hash of a block
		#We must ensure that the dictionary is ordered, or we'll have inconsistent hashes
		block_string = json.dumps(block, sort_keys=True).encode()

		return hashlib.sha256(block_string).hexdigest()
	
	@property
	def last_block(self):
		#Returns the last block in the chain
		return self.chain[-1]
