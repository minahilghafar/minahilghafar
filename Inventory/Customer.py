class Customer:
    def __init__(self,name,phone_number,address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.Customers = {}



    def add_customer(self):
        if self.name in self.Customers:
            print(f'Customer_Name: {self.name} is already added')
        else:
            self.Customers[self.name] = {'name': self.name, 'phone_number': self.phone_number,
                                         'address': self.address}
            print(f'{self.name} is added to customers')

    def customer_info(self):
        print(f'Name: {self.name}, Phone_number:{self.phone_number},'
              f'Address: {self.address}')