blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    blockchain.append([last_transaction_value,transaction_amount])    

add_value(2)
add_value(last_transaction_value = get_last_blockchain_value(),transaction_amount= 0.9)    
add_value(10.88, get_last_blockchain_value())    
print(blockchain)
# add_value(get_last_blockchain_value(),0.9)