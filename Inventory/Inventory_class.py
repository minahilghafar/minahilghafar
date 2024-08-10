from Items import Items
from Customer import Customer
class Inventory(Items, Customer):
    def __init__(self):
        Items.__init__(self, '', 0, 0)
        Customer.__init__(self, '', '', '')
        self.sale_history = {}

    def display_all_items(self):
        if not self.inventory:

            print('Inventory is empty')
        else:
            print('Current Inventory..')
            for key in self.inventory.keys():
                print(f'Item_Name: {self.inventory[key]["item_name"]}, Item_Price: {self.inventory[key]["item_price"]}, '
                      f' Quantity: {self.inventory[key]["quantity"]}')

    def sell_items(self):
        if not self.inventory:
            print('Inventory is Empty..!')
        else:
            item_name_to_sell = input('Enter Item Name to Buy: ')

            if item_name_to_sell in self.inventory:

                quantity_to_sell = int(input('Enter Item Quantity to Buy: '))

                if quantity_to_sell <= self.inventory[item_name_to_sell]['quantity']:
                        self.inventory[item_name_to_sell]['quantity'] -= quantity_to_sell
                        print(f'{item_name_to_sell} with Quantity {quantity_to_sell} is Sold')
                        total_price = self.inventory[item_name_to_sell]['item_price'] * quantity_to_sell
                        self.sale_history = {'name': item_name_to_sell, 'quantity': quantity_to_sell, 'total_price': total_price}
                else:
                    print(f'{item_name_to_sell} is out Stock..{self.inventory[item_name_to_sell]["quantity"]} is available!..')
            else:
                print(f'{item_name_to_sell} is not in the Inventory')

    def delete_item(self):
        if not self.inventory:
            print("Inventory is empty")
        else:
            item_name_to_delete = input("Enter your item name to delete: ")
            if item_name_to_delete in self.inventory:

                self.inventory.pop(item_name_to_delete)

                print(f"{item_name_to_delete} is deleted successfully")
            else:
                print(f"{item_name_to_delete} is not in inventory")

    def create_bill(self, name):
        print('*********** Customer Info ***********')
        print(f'Customer Name: {self.Customers[name]["name"]}, Phone Number: {self.Customers[name]["phone_number"]}')
        print('*********** Sale Bill ************')
        print(f'Item name: {self.sale_history["name"]}, Quantity Sold: {self.sale_history["quantity"]}, '
              f'Total Price: {self.sale_history["total_price"]}')


