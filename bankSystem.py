from abc import ABC, abstractmethod
#basic info which will bank have
class bank:
    
    def __init__(self,name):
        self.name=name
        self.totalBalance = 0
        self.accounts=[]
        self.totalLoan=0
        self.loanFacility=True
    
    #creating an account func which will come fom account class
    def createAccount(self,name,email,address,type):
        acc=account(name,email,address,type)
        self.accounts.append(acc)
    
    #delete account which will be given from admin
    def deleteAccount(self):
        for account in self.accounts:
            if account.accountId==accounts.accountsID:
                self.accounts.remove(account)
                del account
                return
            else:
                print("Can't find the account!")
        
    #All user showing
    def allUser(self):
        for account in self.accounts:
            print(f"Account name: {account.name}\t ID: {account.accountId}")
    
    #total loan
    def TotalLoanShow(self):
        print(f"The total loan is: {self.totalLoan}")
        
    #total balance in the bank
    def TotalBalance(self):
            print(f"The total balance is: {self.totalBalance}")
    
    #loan off feature        
    def loanOffFeature(self):
        if self.loanFacility==True:
            self.loanFacility=False
        else:
            print("He/She facility is off !")

    #loan on feature
    def loanOnFeature(self):
        if self.loanFacility==False:
            self.loanFacility=True
            print("His/her loan feature is off now!")
        else:
            print("He/She already has this facility!")
    
class account(ABC):
    createAccountId=0
    
    def __init__(self,name,email,address,type):
        self.name=name
        self.email=email
        self.address=address
        account.createAccountId+=1
        self.accountId=account.createAccountId
        self.type=type
        self.loanCount=0
        self.loanAmount=0
        self.balance=0
        self.transactions=[]
        self.transactionId=self.accountId*10
    
    #he/she can check balance:
    def checkBalance(self):
           print(f"Name: {self.name}\t AccId: {self.accountId}\t Balance: {self.balance}")

    #transfer balance
    def transfer(self,bank,accId,amount):
        for account in bank.accounts:
            if accId==account.accountId:
                other=account
                if self.balance>=amount:
                    self.balance-=amount
                    other.balance+=amount
                    print(f"Transferred {amount} from {self.name} to {other.name}")
                    
                    transaction={}
                    self.transactionId+=1
                    transaction['id']=self.transactionId
                    transaction['type']="transfer"
                    transaction['from']=self.name
                    transaction['to']=other.name
                    transaction['amount']=amount
                    self.transactions.append(transaction)
                else:
                    print(f"not enough Amount !")
                
                return
        
        print("Not enough Account to Transfer !")
    
    
    #deposit money
    def deposit(self, amount):
        if amount >= 0:
            bank.totalBalance+=amount
            self.balance += amount
            print(f"Deposited {amount}. New balance: ${self.balance}")
            
            transaction={}
            self.transactionId+=1
            transaction['id']=self.transactionId
            transaction['type']="deposit"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
        else:
            print("Invalid deposit amount")
    
    #withdraw money 
    def withdraw(self, amount):
        if amount >= 0 and bank.totalBalance>=amount and amount <= self.balance:
            self.takeBalance-=amount
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
            transaction={}
            self.transactionId+=1
            transaction['id']=self.transactionId
            transaction['type']="withdraw"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
            if bank.totalBalance==0:
                print("Alert: Bank is bankrupt!!!")
        else:
            print("Invalid withdrawal amount")

    #take loan
    def takeLoans(self,bank,amount):
         if bank.loanFacility==True and amount>=0 and bank.totalBalance>=amount and self.loanCount<2:
            self.loanAmount+=amount
            self.loanCount+=1
            bank.totalLoan+=amount
            print(f"Loan took ${self.loanAmount}.")
            
            transaction={}
            self.transactionId+=1
            transaction['id']=self.transactionId
            transaction['type']="Loan"
            transaction['amount']=amount
            
            self.transactions.append(transaction)
    #transaction history
    def transactionsHistory(self):
        print(f"Transaction History :{self.name}:")
        
        for transaction in self.transactions:
            if 'to' in transaction:
                print(f"{transaction['id']}: {transaction['type']} Dollar {transaction['amount']} to {transaction['to']}")
            
            elif 'id' in transaction:
                print(f"{transaction['id']}: {transaction['type']} Dollar {transaction['amount']}")


#giving Values    
bank=bank("Sonaly Bank Ltd.")
admin=bank.createAccount("admin","admin@gmail.com","agargaw","admin")

#admin user set
currentUser=admin
changeOfUser=True

# main kaj
while True:
    if currentUser==None:
        print(" No user logged in !")
        option=input("Register/Login (R/L) : ")
        #register
        if option == "R":
            name=input("Enter Name:")
            email=input("Enter E-mail:")
            addr=input("Enter Address:")
            type=input("Account Type (Savings/Current):")
            
            user=bank.createAccount(name,email,addr,type)
            
            currentUser=user
            changeOfUser=True
        #login korbe
        elif option =="L":
            id=int(input("Enter Account Number:"))
    
            match=False
            for user in bank.accounts:
                if user.accountId==id:
                    currentUser=user
                    changeOfUser=True
                    match=True
                    break
            if match==False:
                print("No user Found !\n")
    else:
        if changeOfUser:
            print(f"user: {currentUser.name}")
            changeOfUser=False
        else:
            print("\n\t<---------------------------->")
        
            if currentUser.name=="admin":
                print("Options:\n")
                print("1: Create Account")
                print("2: Delete Account")
                print("3: Show Users")
                print("4: Show Total Balance")
                print("5: Show Total Loan")
                print("6: On Loan facility")
                print("7: Off Loan facility")
                print("8: Log Out")
                    
                 #input choice
                option=int(input("choice:"))
                if option==1:
                    name=input("Enter Name:")
                    email=input("Enter E-mail:")
                    addr=input("Enter Address:")
                    type=input("Account Type (Savings/Current):")
                    bank.createAccount(name,email,addr,type)
                       
                elif option==2:
                    accId=int(input("\tEnter Account ID:"))
                    bank.deleteAccount(accId)  
                elif option==3:
                    bank.allUser()
                elif option==4:
                    bank.TotalBalance()
                elif option==5:
                    bank. TotalLoanShow()
                elif option==6:
                    bank.loanOnFeature()
                elif option==7:
                    bank.loanOffFeature()
                elif option==8:
                    currentUser=None
                else:
                    print(f"Invalid number")
                    
            #if admin na hoi er mane user
            else:
                print("Options:\n")
                print("1: Deposit")
                print("2: Withdraw")
                print("3: Show Balance")
                print("4: Show Transactions History")
                print("5: Take Loan")
                print("6: Transfer")
                print("7: Logout")   
                    
                choice=int(input("choice:"))
                    
                if choice==1:
                    amount=int(input("Enter Amount:"))
                    currentUser.deposit(amount)
                    
                elif choice==2:
                    amount=int(input("Enter Amount:"))
                    currentUser.withdraw(amount)
                    
                elif choice==3:
                    currentUser.checkBalance()
                    
                elif choice==4:
                    currentUser.transactionsHistory()
                
                elif choice==5:
                   amount=int(input("Enter Amount:"))
                   currentUser.takeLoans(bank,amount)
                   
                elif choice==6:
                   accId=int(input("Enter account number:"))
                   amount=int(input("Enter Amount:"))
                   currentUser.transfer(bank,accId,amount)
                
                elif choice==7:
                    currentUser=None
                    
                else:
                    print("Invalid number")