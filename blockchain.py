#Initialzing empty blockchain lists
MINING_REWARD = 10
genesis_block = {
        'previous_hash': '',
        'index':0,
        'transactions':[]
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'John Doe' #dummy value (real will be in hash dkfkjsoij3oij4iosjd3)  
participants = {'John Doe'}       #Initializing a set



def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balances(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx)>0:
            amount_sent +=tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx)>0:
            amount_recieved +=tx[0]
    return amount_recieved-amount_sent



def get_last_blockchain_value():
    """Returns the value of last element of blockchain"""
    if len(blockchain) < 1:
        return None
    else:
        return blockchain[-1]


def add_transaction(recipient,sender=owner, amount = 1.0):
    """Appends the last value and new value to the open_transaction blockchain
    
    Add sender and recipient to the list of participants

    Arguments:
    sender : Sender of the coins by defualt owner
    recipient: Receiver of the coins
    amount: Amount you want to transact 1.0 by default"""
    transaction = {
        'sender':sender, 
        'recipient':recipient, 
        'amount':amount
    }
    open_transactions.append(transaction)
    participants.add(sender)                                #Adding it to list of participants
    participants.add(recipient)                             #Adding it to list of participants


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    reward_transaction = {
        'sender' : 'MINING',
        'recepient' : owner,
        'amount' : MINING_REWARD
    }
    open_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block,
        'index':len(blockchain),
        'transactions':open_transactions
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


def get_user_input():
    return input()


def verify_chain(blockchain):
    """Loops through the chain to check it's verification"""
    for (index,block) in enumerate(blockchain):
        if index==0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return "Problem in the hashing"
    return "No problem verfied chain"

loop_input = True

while loop_input:
    "Choices"
    print('1. Input into blockchain')
    print('2. Mine a new block')
    print('3. Print the blocks of blockchain')
    print('4. Output Participants')
    print('h. Hack the blockchain')
    print('q. To exit')
    
    user_input = get_user_input()
    
    "Logic"
    
    if user_input == '1':
        tx_data = get_transaction_value()
        recipient,amount = tx_data
        add_transaction(recipient,amount=amount)
        print(open_transactions)
    
    elif user_input == '2':
        if mine_block():
            open_transactions = []

    
    elif user_input == '3':
        for block in blockchain:
            print(block)
    
    elif user_input == '4':
        print(participants)
    
    elif user_input == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
        'previous_hash': '',
        'index': 0,
        'transactions':[{'sender': 'Jane', 'recipient': 'Doe', 'amount': '12.456'}]
    }
    
    elif user_input == 'q':
        loop_input = False
    
    else:
        print('Wrong choice man')

print(get_balances('John Doe'))
print(verify_chain(blockchain))


