class Items:
    def __init__(self,item_name,item_price,item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.inventory = {}

    def items_info(self):
        print(f'Name: {self.item_name}, Price: {self.item_price}, Quantity: {self.item_quantity}')

    def add_item(self):
        if self.item_name in self.inventory:
            print(f'{self.item_name} is already in the Inventory.')
        else:
            self.inventory[self.item_name] = {'item_name': self.item_name, 'item_price': self.item_price,
                                              'quantity': self.item_quantity}
            print(f'{self.item_name} is added to the Inventory')