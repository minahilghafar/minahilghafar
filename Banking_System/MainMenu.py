from account_holder import AccountHolder
from bank_account import BankAccount

class MainMenu():
    def __init__(self,bank_acc):
        self.bank_acc = bank_acc
    def run(self):
        print("\n------------------------")
        print("Welcome to Banking_System")
        print("-------------------------\n")
        while True:
            print("Press 1 to Deposit Amount")
            print("Press 2 to Withdraw")
            print("Press 3 to See Account_Holder Info")
            print("Press 4 to Get Balance")
            print("Press 5 to Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                amount = input('Enter your amount to deposit: ')
                self.bank_acc.deposit(amount)
            elif choice == '2':
                amount = input('Enter your amount to withdraw: ')
                self.bank_acc.withdraw(amount)
            elif choice == '3':
                self.bank_acc.get_account_details()
            elif choice == '4':
                self.bank_acc.get_balance()
            elif choice == '5':
                print("\n******** Thanks For Coming **********\n")
            else:
                print("******* Invalid Input.... Choose Between 1 to 5 ********")

if __name__ == '__main__':
    obj = AccountHolder('Minahil','24-06-2024', 'DHA(Raya)')
    bank_acc = BankAccount('XXXXXX',obj,'100')
    menu = MainMenu(bank_acc)
    menu.run()
