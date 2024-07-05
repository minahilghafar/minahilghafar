from datetime import datetime


class AccountHolder:
    def __init__(self,name,date_of_birth,address):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth,"%d-%m-%Y")
        self.address = address

    def get_info(self):
        print(f'Name: {self.name},Date_of_birth: {self.date_of_birth}, Address: {self.address}')
