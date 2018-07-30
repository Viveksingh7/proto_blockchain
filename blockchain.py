import functools 
import hashlib 
import json

"""Own imports"""
from utility.hash_util import hash_block
from utility.verification import Verification
from block import Block
from transaction import Transaction

#Initialzing empty blockchain lists
MINING_REWARD = 10

print(__name__)

class Blockchain:
    def __init__(self, hosting_node_id):
        # Our starting block for the blockchain
        genesis_block = Block(0,'',[], 100, 0)
        #Initializing our empty blockchain list
        self.__chain = [genesis_block]
        #Unhandled Transaction
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def get_chain(self):
        return self.__chain[:]

    def get_open_transactions(self):
        return self.__open_transactions[:]   

    def load_data(self):
        try:
            with open('blockchain.txt', mode='r') as f:
                file_content = f.readlines()
                blockchain = json.loads(file_content[0][:-1])
                # We need to convert  the loaded data because Transactions should use OrderedDict
                updated_blockchain = []
                for block in blockchain:
                    converted_tx = [Transaction(tx['sender'],tx['recipient'],tx['amount']) for tx in block['transactions']]
                
                    updated_block = Block(block['index'],block['previous_hash'], converted_tx, block['proof'], block['timestamp'])
                    updated_blockchain.append(updated_block)

                self.__chain = updated_blockchain
                open_transactions = json.loads(file_content[1])
                # We need to convert  the loaded data because Transactions should use OrderedDict
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(tx['sender'],tx['recipient'],tx['amount'])

                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions
        except (IOError,IndexError):
            pass
        finally:
            print('Cleanup!')

    
    def save_data(self):
        try:
            with open('blockchain.txt',mode='w') as f:
                saveable_chain = [block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]]
                f.write(json.dumps(saveable_chain))
                f.write('\n')
                saveable_tx = [tx.__dict__ for tx in self.__open_transactions]
                f.write(json.dumps(saveable_tx))
        except IOError:
            print('Saving failed!')


    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof


    def get_balance(self):

        participant = self.hosting_node

        """Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)"""
        """This fetches sent amounts of transactions that were already included in blocks of the blockchain"""
        tx_sender = [[tx.amount for tx in block.transactions 
                            if tx.sender == participant] for block in self.__chain]

        """Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)"""
        """This fetches sent amounts of open transactions (to avoid double spending)"""

        open_tx_sender = [tx.amount for tx in self.__open_transactions if tx.sender == participant] 
        tx_sender.append(open_tx_sender)
        amount_sent = functools.reduce(lambda tx_sum,tx_amt : tx_sum +sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_sender,0) 
        
        tx_recipient = [[tx.amount for tx in block.transactions
                            if tx.recipient == participant] for block in self.__chain]
        amount_recieved = functools.reduce(lambda tx_sum,tx_amt : tx_sum +sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_recipient,0) 
        return amount_recieved - amount_sent

    def get_last_blockchain_value(self):
        """Returns the value of last element of blockchain"""
        if len(self.__chain) < 1:
            return None
        return self.__chain[-1]

    def add_transaction(self,recipient,sender, amount = 1.0):
        """Appends the last value and new value to the open_transaction blockchain
        
        Add sender and recipient to the list of participants

        Arguments:
        sender : Sender of the coins by defualt owner
        recipient: Receiver of the coins
        amount: Amount you want to transact 1.0 by default"""

        transaction = Transaction(sender,recipient,amount)

        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()                           #Adding it to list of participants
            return True
        return False

    def mine_block(self):
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()

        reward_transaction = Transaction('MINING', self.hosting_node, MINING_REWARD)
        

        # Copy transaction instead of manipulating the original open_transactions list
        # This ensures that if for some reason the mining should fail, we don't have the reward transaction stored in the open transactions
        
        copied_transactions = self.__open_transactions[:]
        copied_transactions.append(reward_transaction)

        block = Block(len(self.__chain),hashed_block,copied_transactions,proof,)
    
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        
        return True





