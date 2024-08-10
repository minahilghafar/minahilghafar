class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.email = ''
        self.username = ''
        self.password = ''
        self.Students = {}
        self.std_id = ''
        self.garde = ''
        self.welcome_message = 'Welcome to Dashboard'

    def register_yourself(self):
        self.email = input('Enter your email_address: ')
        self.password = input('Enter your password: ')
        self.username = self.email.split('@')[0]
        self.std_id = self.username

        single_std = {
            'id': self.std_id,
            'name': self.name,
            'age': self.age,
            'marks': self.marks,
            'grade': self.garde,
            'welcome_message': self.welcome_message,
            'personal_info':{
                'email': self.email,
                'username': self.username,
                'password': self.password
            }
        }
        self.Students[self.std_id] = single_std
        self.password_strength()
        print('\n Your Username is: ', self.username, '\n')


    def password_strength(self):
        strength = 0
        for char in self.password:
            if char.isdigit():
                strength += 1
                break

        for char in self.password:
            if char.isupper():
                strength += 1
                break

        for char in self.password:
            special_char = '!@#$%^&*'
            if special_char.__contains__(char):
                strength += 1
                break

        if strength == 1:
            print('Password is weak')
        elif strength == 2:
            print('Password is medium')
        else:
            print('Password is strong')






