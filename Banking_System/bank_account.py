from account_holder import AccountHolder
class BankAccount:
    def __init__(self,account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self,amount):
        amount = float(amount)
        if amount > 0:
            self.balance += amount
            print(f'Deposit Successfully!!!!!!! Your New_balance is: {self.balance:.2f}')
        else:
            print("Invalid Input")

    def withdraw(self,amount):
        amount = float(amount)
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Successfully Withdraw!!!! Your New_Balance is: {self.balance:.2f}')

    def get_account_details(self):
        print(f'Account_Number: {self.account_number}, Account_Holder: {self.account_holder.name}, '
              f' Date_of_Birth: {self.account_holder.date_of_birth}, '
              f' Address: {self.account_holder.address}, {self.balance:.2f}')

    def get_balance(self):
        print(f'Your Current Balance is : {self.balance:.2f}')




