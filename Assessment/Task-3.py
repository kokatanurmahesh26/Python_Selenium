class bank() : 
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"Balance amount is  : {self.balance}")

    def deposit(self,deposit_amount)  :
        self.deposit_amount = deposit_amount
        print(f"{self.deposit_amount} deposited to account successful")
        self.balance = self.balance + self.deposit_amount
        print(f"Balance amount is  : {self.balance}")

    def withdraw(self, withdraw_amount) :
        self.withdraw_amount = withdraw_amount
        print(f"{self.withdraw_amount} requested to withdraw")
        if int(withdraw_amount) < 0 :
            print("Negative withdrawal")
        else :
            self.balance = self.balance - self.withdraw_amount 
            print(f"Balance amount is  : {self.balance}")
b1  = bank("mahesh", 1000)
b1.deposit(1000)
b1.withdraw(1000)
b1.withdraw(-1000)
