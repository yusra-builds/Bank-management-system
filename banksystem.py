class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
        
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        
        
        if amount > self.balance:
            print("Insufficient balance, you can't withdraw this amount!")
        else:
            self.balance -= amount
            print("Withdrawal successful!")
        
    def checkBalance(self):
        print("\nAccount holder:", self.name)
        print("Current balance:", self.balance)
        

name = input("Enter your name:")
balance = int(input("\nEnter starting balance:"))
account1 = Bank(name, balance)
    


print("\n-----MENU-----")
print("1. Deposit")
print("2. Withdraw")
print("3. Check balance")
print("4. Exit")



while True:
    
    userInput = int(input("\nChoose a number from menu:"))
    
    if userInput == 1:
        amount = int(input("\nHow many amount would you deposit?"))
        if amount <= 0:
            print("Please enter a valid amount to deposit!")
        else:
            
            account1.deposit(amount)
            print(amount, "deposited successfully!")
            account1.checkBalance()
            
    
    elif userInput == 2:
        amount2 = int(input("\nHow many amount would you like to withdraw?"))
        
        account1.withdraw(amount2)
        
        
        account1.checkBalance()
    
    elif userInput == 3:
        account1.checkBalance()
    
    else:
        print("\nThanks for banking!")
        break