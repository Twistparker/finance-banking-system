import json
from datetime import datetime
import os




if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        users = json.load(file)
else:
    users = {}
    
def register_user():
    print("To register Enter a username and a valid password: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "" or password == "":
        print("Enter username or password.Cant be left empty")
    elif username in users:
        print("Username already exists. Please choose a different username.")
    else:
        print("You have successfully registered")
        users[username] = {
            'password': password,
            'balance': 0,
            'transactions': []
        }
        
        with open('users.json', 'w')as file:
            json.dump(users,file,indent=4)
 
def login_user():
    login_username = input("Enter your username: ")
    login_password = input("Enter your password: ")

    if login_username in users:
        print("username found")
        if login_password == users[login_username]['password']:
            print("login successfull")
            banking_dashboard(login_username)
        else:
            print("Incorrect passoword")
    else:
        print("Username not found")

def deposite_money(login_username):
    try:
        deposite = int(input("How much do you want to deposite in your account: "))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return
    
    if deposite <= 0:
            print("invalid amount")
    else:
            deposited_amount = deposite + users[login_username]['balance']
            users[login_username]['transactions'].append({'type': 'deposit', 'amount': deposite, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            users[login_username]['balance'] = deposited_amount
            with open('users.json', 'w')as file:
                json.dump(users,file,indent=4)


def withdraw_money(login_username):
    try:
        withdraw_amount = int(input("How much do you want to withdraw from your account: " ))
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return

    if withdraw_amount <= 0:
            print("Invalid amount. Please enter a positive value.")
    elif withdraw_amount <= users[login_username]['balance']:
        withdrawal = users[login_username]['balance'] - withdraw_amount
        users[login_username]['balance'] = withdrawal
        users[login_username]['transactions'].append({'type': 'withdrawal', 'amount': withdraw_amount, 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        with open("users.json",'w')as file:
            json.dump(users,file,indent=4)
       
        print("Withdrawal successful!")
    else:
        print("Insufficient funds in your account")

   
def check_balance(login_username):
    print("Your account balance is ", users[login_username]['balance'])

    
def transaction_history(login_username):
    transactions = users[login_username]['transactions']
    if not transactions:
            print("No transactions found.")
        
    for transaction in transactions:
        print(f"Type: {transaction['type']}, Amount: {transaction['amount']}, Date: {transaction['date']}")



def change_password(login_username):
    current_pwd = input("Enter your current password: ")
    if current_pwd == users[login_username]['password']:
        new_pwd = input('Enter your new password:')
        users[login_username]['password'] =new_pwd
        with open("users.json",'w')as file:
            json.dump(users,file,indent=4)
        print("password changed successfully")

        
    else:
        print("Invalid password")


def account_statement(login_username):
    print(f'Your username: {login_username}\nYour current balance is: {users[login_username]["balance"]}')
    print("Transaction History: " )
    transaction_history(login_username)
    



def  banking_dashboard(login_username):
    while True:
        print("=========== BANKING DASHBOARD ===========   ")
        print(" 1.check balance \n 2.Deposit \n 3.Withdraw \n 4.Transaction \n 5.change password \n 6.Account Statement \n 7.Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            check_balance(login_username)
        elif choice == '2':
            deposite_money(login_username)  
        elif choice == '3':
            withdraw_money(login_username)  
        elif choice == '4':
            transaction_history(login_username)
        elif choice == '5':
            change_password(login_username)
        elif choice == '6':
            account_statement(login_username)
        elif choice == '7':
            print("Logging out...")
            break

while True:
    print("=========FINANCE MANAGEMENT SYSTEM==========")
    print(" 1.Register \n 2.Login \n 3.Exit ")
    Activity = input("Choose and option: ")

    if Activity == '1':
        register_user()
    elif Activity == "2":
        login_user()
    elif Activity == "3":
        print("Goodbye see you soon ")
        break
    else:
        print("Enter a valid input??")

