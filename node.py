from uuid import uuid4
from blockchain import Blockchain
from utility.verification import Verification
from wallet import Wallet


class Node:
    def __init__(self):
        #self.wallet.public_key = str(uuid4())
        self.wallet = Wallet()
        self.blockchain = None

    def get_transaction_value(self):
        """Takes input of a new transaction and returns recipient and amount"""
        tx_recipient = input('Enter the recipient of the transaction:')
        tx_amount =float(input('Enter the transaction amount:'))
        return tx_recipient,tx_amount

    def get_user_input(self):
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        """Output all the blocks of the blockchain"""
        for block in self.blockchain.get_chain():
            print('Outputting Block!')
            print(block)
        else:
            print('-' * 20)

    def listen_to_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print('1. Add a new transaction')
            print('2. Mine a new block')
            print('3. Output the blocks of blockchain')
            print('4. Verify the transactions')
            print('5. Create Wallet')
            print('6. Load Wallet')
            print('q. To exit')
            
            user_input = self.get_user_input()
            
            "Logic"
            
            if user_input == '1':
                tx_data = self.get_transaction_value()
                recipient,amount = tx_data
                #Adding the transaction amount to blockchain
                if self.blockchain.add_transaction(recipient, self.wallet.public_key, amount=amount):
                    print('Added transaction!')
                else :
                    print('Transaction Failed!')
                print(self.blockchain.get_open_transactions())

            elif user_input == '2':
                if not self.blockchain.mine_block():
                    print('Block Mining Failed, Got no Wallet?')
                    
            elif user_input == '3':
                self.print_blockchain_elements()

            elif user_input == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            
            elif user_input == '5':
                self.wallet.create_keys()
                self.blockchain = Blockchain(self.wallet.public_key) 
            elif user_input == '6': 
                pass
            elif user_input == 'q':
                waiting_for_input = False
            
            else:
                print('Invalid was invalid,please pick a given option')

            if not Verification.verify_chain(self.blockchain.get_chain()):
                self.print_blockchain_elements()
                print('Invalid Blockchain!')
                #Break out of loop
                break
            print('Balance of {} is {:6.8f}'.format(self.wallet.public_key, self.blockchain.get_balance()))
        else:
            print('User left!')

        print('Done!')

if __name__ == '__main__':
    node = Node()
    node.listen_to_input()