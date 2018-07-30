from time import time

from utility.printable import Printable

class Block(Printable):
    def __init__(self, index, previous_hash, transactions, proof,time = time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof
    
    def __repr__(self):
        return 'Index: {}, Previous Hash: {}, Proof: {}, Transactions: {}'.format(self.index, self.previous_hash,self.proof, self.transactions)

