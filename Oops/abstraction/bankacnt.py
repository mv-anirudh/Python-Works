class Bank:
    def __init__(self,account_num,accnt_type):
        self.bank_name="SBI"
        self.account_num=account_num
        self.accnt_type=accnt_type
        self.__balance=2000  #__ makes the variable private
        
    def deposit(self,amount):
        self.__balance+=amount
        print(f"your {self.bank_name} account of {self.account_num} is credited with Rs {amount} ")
        
    def withdraw(self,amount):
        if self.__balance > amount:
            self.__balance-=amount
            print(f"your {self.bank_name} account of {self.account_num} is debited with  Rs {amount}")
        else:
            print(f"!!!Transaction failed, insufficient balance!!! ")
            
    def get_balance(self):
        print(f"your Available baance is Rs {self.__balance}") 

bank=Bank(1234,"savings")
        

bank.deposit(2000)
bank.get_balance()
bank.withdraw(6000)
bank.get_balance()