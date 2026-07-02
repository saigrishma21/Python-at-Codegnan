# first define the table structure

# users={
#     account1:{
#         'name':Username,
#         'email':Email,
#         'password':Password,
#         'balance':Balance
#     },
#     account2:{
#         'name':Username,
#         'email':Email,
#         'password':Password,
#         'balance':Balance
#     }
# }

users={
    1234:{
        'name':'Greeshma',
        'email':'greeshmareddy2218@gmail.com',
        'password':'1234',
        'balance':10000
    },
    1235:{
        'name':'bunny',
        'email':'bhargavipriya11@gmail.com',
        'password':'1235',
        'balance':5000
    }
}

##require services
#register function
def register(username:str,email:str,password:str,initial_deposit:int=0)->str:
    return "Registration page under development process"
    
def login(account:int,password:str)->bool:
    if account in users:
        if password==users[account].get('password'):
            return True
        else:
            return False
    return False

#balance function
def balance(account:int)->str:
    curr_amount=users[account].get('balance',-1)
    return curr_amount

#withdraw function
def withdraw(account:int,withdraw_amount:int)->str:
    curr_amount=users[account].get('balance',-1)
    if curr_amount>=withdraw_amount:
        users[account]['balance']-=withdraw_amount
        return f"withdraw successful and current balance{users[account]['balance']}"
    else:
        return "Insufficient balance"
    
#deposit function
def deposit(account:int,deposit_amount:int)->str:
    users[account]['balance']+=deposit_amount
    return f"{deposit_amount} deposit succesfull and current balance is {users[account]['balance']}"

#Transfer function
def transfer(from_account:int,to_account:int,transfer_amount:int)->str:
    if to_account in users:
        curr_amount=users[from_account].get('balance',-1)
        if curr_amount>=transfer_amount:
            users[from_account]['balance']-=transfer_amount
            users[to_account]['balance'] +=transfer_amount
            return f"{transfer_amount} amount transferred successfuly and current amount is { users[from_account]['balance']}"
        else:
            return "Insuffiecient balance"
    else:
        return "Check your receiver account number"     

#ministmt function
def ministatement(account:int)->str:
    return "ministatement page under development process...."

#logout function
def logout():
    return "Byee bye see you later"
 

#main
if __name__=="__main__":
    print("Welcome to the small scale bank")
    print("1.Register \n 2.Login")
    choice=int(input("Select your choice:"))
    if choice == 1:
        print("your are selected 1.Register")
        name=input("enter username:")
        email=input("enter email:")
        password=input("enter password:")
        deposit=int(input("enter deposit amount:"))
        #call register function
        account=register(username=name,
                         email=email,
                         password=password,
                         initial_deposit=deposit)
        print("your account number is:",account)
    elif choice==2:
        print("your selected 2.Login operation")
        account_number=int(input("enter your account number:"))
        password=input("enter your password:")
        #login function
        login_val=login(account=account_number,password=password)
        while login_val:
            print("1.Balance \n 2.Withdraw \n 3.deposit \n 4.transfer \n 5.mini statement \n 6.logout")
            choice=int(input("enter your choice:"))
            if choice==1:
                result=balance(account=account_number)
                print(result)
            elif choice==2:
                amount=int(input("enter withdraw amount:"))
                result=withdraw(account=account_number,withdraw_amount=amount)
                print(result)
            elif choice==3:
                deposit_am=int(input("enter the deposit amount:"))
                result=deposit(account=account_number,deposit_amount=deposit_am)
                print(result)
            elif choice==4:
                transfer_am=int(input("enter your transfer amount:"))
                receiver_acc=int(input("enter account number:"))
                result=transfer(from_account=account_number,
                                to_account=receiver_acc,
                                transfer_amount=transfer_am)
                print(result)
            elif choice==5:
                result=ministatement(account=account_number)
                print(result)
            elif choice==6:
                print(logout())
                exit()
            else:
                print("invalid choice,select choice btw 1 to 6")

