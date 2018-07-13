import functools 
"""for reduce"""
import hashlib as hl
"""for hashing"""
import json
"""for string conversion"""
from collections import OrderedDict
"""for ordering of Dictionaries"""

#Initialzing empty blockchain lists
MINING_REWARD = 10

genesis_block = {
        'previous_hash': '',
        'index':0,
        'transactions':[],
        'proof':100
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'John Doe' #dummy value (real will be in hash dkfkjsoij3oij4iosjd3)  
participants = {'John Doe'}       #Initializing a set




def hash_block(block):
    return hl.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

 
def valid_proof(transactions,last_hash,proof):
    guess = (str(transactions)+str(last_hash)+str(proof)).encode()
    guess_hash = hl.sha256(guess).hexdigest()
    print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof+=1
    return proof


def get_balance(participant):
      # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of transactions that were already included in blocks of the blockchain
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    # Fetch a list of all sent coin amounts for the given person (empty lists are returned if the person was NOT the sender)
    # This fetches sent amounts of open transactions (to avoid double spending)
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)

    amount_sent = functools.reduce(lambda tx_sum,tx_amt : tx_sum +sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_sender,0) 
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = functools.reduce(lambda tx_sum,tx_amt : tx_sum +sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_recipient,0) 
    
    return amount_recieved - amount_sent



def get_last_blockchain_value():
    """Returns the value of last element of blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(recipient,sender=owner, amount = 1.0):
    """Appends the last value and new value to the open_transaction blockchain
    
    Add sender and recipient to the list of participants

    Arguments:
    sender : Sender of the coins by defualt owner
    recipient: Receiver of the coins
    amount: Amount you want to transact 1.0 by default"""
    
    
    #transaction = {
     #   'sender':sender, 
      #  'recipient':recipient, 
       # 'amount':amount
    #}
    transaction = OrderedDict([('sender',sender),('recipient',recipient),('amount',amount)])


    open_transactions.append(transaction)
    participants.add(sender)                                #Adding it to list of participants
    participants.add(recipient)                             #Adding it to list of participants


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()


    #reward_transaction = {
    #    'sender' : 'MINING',
    #    'recipient' : owner,
    #    'amount' : MINING_REWARD
    #}

    reward_transaction = OrderedDict([('sender','MINING',),('recipient',owner),('amount',MINING_REWARD)])

    open_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions':open_transactions,
        'proof' : proof
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """Takes input of a new transaction and returns recipient and amount"""
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount =float(input('Enter the transaction amount:'))
    return tx_recipient,tx_amount

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def get_user_input():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    """Output all the blocks of the blockchain"""
    for block in blockchain:
        print('Outputting Block!')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    """Loops through the chain to check it's verification"""
    for (index,block) in enumerate(blockchain):
        if index==0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1],block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True

def verify_transactions():
    """Verifies all open transactions."""
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

while waiting_for_input:
    print('1. Add a new transaction')
    print('2. Mine a new block')
    print('3. Output the blocks of blockchain')
    print('4. Output Participants')
    print('5. Verify the transactions')
    print('h. Hack the blockchain')
    print('q. To exit')
    
    user_input = get_user_input()
    
    "Logic"
    
    if user_input == '1':
        tx_data = get_transaction_value()
        recipient,amount = tx_data
        #Adding the transaction amount to blockchain
        if add_transaction(recipient,amount=amount):
            print('Added transaction!')
        else :
            print('Transaction Failed!')

    elif user_input == '2':
        if mine_block():
            open_transactions = []

    elif user_input == '3':
        print_blockchain_elements()

    elif user_input == '4':
        print(participants)

    elif user_input == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    
    elif user_input == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
        'previous_hash': '',
        'index': 0,
        'transactions':[{'sender': 'Jane', 'recipient': 'Doe', 'amount': '12.456'}]
    }
    
    elif user_input == 'q':
        waiting_for_input = False
    
    else:
        print('Invalid was invalid,please pick a given option')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain!')
        #Break out of loop
        break
    print('Balance of {} is {:6.8f}'.format('John Doe',get_balance('John Doe')))
else:
    print('User left!')

print('Done!')


