blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_value=[1]):
    blockchain.append([last_transaction_value,transaction_amount])    

def get_transaction_value():
    return float(input("enter transaction amount: "))

def get_user_choices():
    user_input = input("Your Choice: ")
    return user_input

def print_blockchain_element():
    for block in blockchain: 
            print("output block")
            print(block)
 
current_amount = get_transaction_value()
add_value(current_amount)

while True: 
    print("Please Choice")
    print("1: Add a new transaction amount")
    print("2: Output the blockchain element")
    user_choice = get_user_choices()
    if user_choice == '1':
        current_amount = get_transaction_value()
        add_value(current_amount, get_last_blockchain_value())  
    else:
        print_blockchain_element()


print("Done")    