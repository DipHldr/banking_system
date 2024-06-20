from random import randint
import json
from datetime import datetime
class details:
    def __init__(self,accNo,name,addr,phone,pin,dob,balance,transaction_history):
        self.accNo=accNo
        self.name=name
        self.address=addr
        self.phone=phone
        self.pin=pin
        self.dob=dob
        self.balance=balance
        self.transaction_history=transaction_history

def createAccount():
    dict={}
    name=input("Enter Your name ")
    dict["name"]=name
    address=input("Enter Your address ")
    dict["address"]=address
    phone=input("Enter your phone number ")
    dict["phone"]=phone
    dob=input("Enter your date of birth ")
    dict["dob"]=dob
    accountNumber=random_N_digits(8)
    dict["account_Number"]=accountNumber
    pin=random_N_digits(4)
    dict["pin"]=pin
    balance=0
    dict["balance"]=balance
    # record=0
    transaction_hist=[]
    dict["records"]=[]
    info=details(accountNumber,name,address,phone,pin,phone,balance,transaction_hist)
    filename=accountNumber
    with open(f"./{filename}.json","w") as jsonFile:
        json.dump(dict,jsonFile)

def random_N_digits(n):
    start=10**(n-1)
    end=(10**n)-1
    return randint(start,end)

def depositMoney():
    acn=input("Please Enter Your Account Number: ")
    amount=int(input("Please Enter The amount you want to deposit: "))
    with open(f"./{acn}.json",'r') as jsonfile:
        data=json.load(jsonfile)
        jsonfile.close()

        temp=data["balance"]
        data["balance"]+=amount
        # x=datetime.now()
        data["records"].append(f"amount {amount} deposited at {str(datetime.now())}")

    with open(f'./{acn}.json','w') as jsonfile:
        json.dump(data,jsonfile)  

def withdrawMoney():
    acn=input("Please Enter Your Account Number: ")
    amount=int(input("Please Enter The amount you want to withdraw: "))
    with open(f"./{acn}.json",'r') as jsonfile:
        data=json.load(jsonfile)
        jsonfile.close()

        temp=data["balance"]
        if temp<amount:
            print("You dont have sufficient balance")
            data["records"].append(f"failed operation {datetime.now()}")
        else:
            data["balance"]-=amount
            # x=datetime.now()
            data["records"].append(f"amount {amount} withdrawn at {str(datetime.now())}")

    with open(f'./{acn}.json','w') as jsonfile:
        json.dump(data,jsonfile) 

def checkBalance():
    acn=input("Please Enter your account number: ")
    with open(f"./{acn}.json",'r') as jsonfile:
        data=json.load(jsonfile)
        jsonfile.close()
    temp=data["balance"]
    print(f"your current balance is: {temp}")

def checkTransactionHistory():
    acn=input("Please Enter your account number: ")
    with open(f"./{acn}.json",'r') as jsonfile:
        data=json.load(jsonfile)
        jsonfile.close()

    for i in data["records"]:
        print(f"{i}\n")


def changeInformation():
    acn=input("Please Enter your account number: ")
    print("Which information do you want to change:\n")
    with open(f"./{acn}.json") as jsonfile:
        data=json.load(jsonfile)
    cnt=0
    for attr,val in data.items():
        if attr!="account_Number" and  attr!="balance" and attr!="records": 
            cnt+=1
            print(f"{cnt}){attr} => {val}")
    cf=int(input("input the field you want to change"))
    with open(f"./{acn}.json",'r') as jsonfile:
        data=json.load(jsonfile)
        jsonfile.close() 
    if cf==1:
        inp=input("Enter new name: ")
        data["name"]=inp
    elif cf==2:
        inp=input("Enter New Address: ")
        data["address"]=inp
    elif cf==3:
        inp=input("Enter your new phone number: ")
        data["phone"]=inp
    elif cf==4:
         inp=input("Enter your new data of birth: ")
         data["dob"]=inp
    else:
        inp=int(input("Enter new pin: "))
        data["pin"]=inp
    with open(f"./{acn}.json",'w') as jsonfile:
        json.dump(data,jsonfile)
        jsonfile.close()

if __name__=="__main__":
    session=True
    while session == True:
         print("Enter the action you want to perform")
         action=["create account","deposit money","withdraw money","check balance","check transaction history","change information"]
         for i in range(len(action)):
             print(f"{i+1}) {action[i]}")
         inp=int(input())
         if inp==1:
             # print("Hello")
             createAccount()
         elif inp==2:
             depositMoney()
         elif inp==3:
             withdrawMoney()
         elif inp==4:
             checkBalance()
         elif inp==5:
             checkTransactionHistory()
         else:
             changeInformation()
        
        #continuation
         print("if you want to continue press 1 else 0")
         conti=int(input())
         if conti==0:
             session=False
             
