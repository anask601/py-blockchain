blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    blockchain.append([last_transaction_value,transaction_amount])    

def get_user_amount():
    return float(input("enter transaction amount: "))
 
current_amount = get_user_amount()
add_value(current_amount)
current_amount = get_user_amount()
add_value(last_transaction_value = get_last_blockchain_value(),transaction_amount= current_amount)
current_amount = get_user_amount()
add_value(current_amount, get_last_blockchain_value())  

for block in blockchain: 
    print("op block")
    print(block)

print("done")    