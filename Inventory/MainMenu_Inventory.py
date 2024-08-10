from Inventory_class import Inventory
from Customer import Customer
from Items import Items


class MainMenu:
    def __init__(self):
        self.invent = Inventory()

    def run(self):
        while True:
            print("\n***** Welcome to Dashboard ******\n")
            print("Press 1 to Add Items")
            print("Press 2 to See All Items")
            print("Press 3 to Sell Items")
            print("Press 4 to Delete Items")
            print("Press 5 to Generate Bill")
            print("Press 6 to Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                inventory_name = input('Enter grocery item_name: ')
                inventory_price = int(input('Enter price of item: '))
                quantity = int(input('Enter quantity of item: '))
                i1 = Items(inventory_name,inventory_price,quantity)
                i1.add_item()
                self.invent.inventory = i1.inventory
            elif choice == '2':
                self.invent.display_all_items()
            elif choice == '3':
                self.invent.sell_items()
            elif choice == '4':
                self.invent.delete_item()
            elif choice == '5':
                name = input('Enter customer_name: ')
                phone_number = input('Enter customer phone_number: ')
                address = input('Enter customer address: ')
                u1 = Customer(name,phone_number,address)
                u1.add_customer()
                self.invent.Customers = u1.Customers
                self.invent.create_bill(name)
            elif choice == '6':
                print("\n*****Thanks For Using Inventory******\n")
                break
            else:
                print("Invalid Input....Choose Between 1 to 5")


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()