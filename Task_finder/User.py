class User:
    def __init__(self,name,phone_number,address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.user = {}
    def user_info(self):
        print(f'name: {self.name}, phone_number: {self.phone_number}, address: {self.address}')


    def add_user(self):
        if self.name in self.user:
            print(f'{self.name} is already added')
        else:
            self.user[self.name] = {'name': self.name, 'phone_number': self.phone_number,
                                    'address': self.address}
            print(f'{self.name} is added successfully')




