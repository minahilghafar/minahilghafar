from grading_System import Grading_System
from STD_Class.student import Student

class StudentPortal(Grading_System, Student):
    def __init__(self):
        Student.__init__(self,'', 0,0)

        self.std_is_logged = False
        self.active_std = None

    def login_into_std_portal(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        if username in self.Students:
            if (self.Students[username]['personal_info']['username'] == username and
                self.Students[username]['personal_info']['password'] == password):
                print('\n***** SUCCESSFULLY LOGGED IN ******\n')
                self.active_std = self.Students[username]
                self.std_is_logged = True
            else:
                print('***** Wrong Email and Password ******')
                self.std_is_logged = False
        else:
            print('**** First register yourself ****')
            self.std_is_logged = False

    def access_std_portal(self):
        if self.std_is_logged:
            print(f'\n******* {self.active_std['welcome_message']} ******\n')
            print('Press 1 to calculate grade')
            print('Press 2 to customized your welcome message')
            print('Press 3 to edit your personal info')

            dashboard_choice = input('Enter your choice: ')
            if dashboard_choice == '1':
                self.update_grade()
            elif dashboard_choice == '2':
                self.customized_message()
            elif dashboard_choice == '3':
                self.change_password()
                self.change_username()


    def update_grade(self):
        marks = self.active_std['marks']
        self.grade = Grading_System(marks).calculate_grade()
        self.active_std['grade'] = self.grade
        print(f'\n Your updated Grade is: {self.grade}\n')

    def customized_message(self):
        new_message = input('Enter your new_message: ')
        list_message = self.active_std['welcome_message'].split()
        list_message.insert(1,new_message)
        self.active_std['welcome_message'] = ' '.join(list_message)
        print('\n Your name is added successfully\n')

    def change_password(self):
        print(f'Name: {self.active_std["name"]}, Age: {self.active_std["age"]}, Marks: {self.active_std["marks"]}, '
              f'Grade: {self.active_std["grade"]}, Email: {self.active_std["personal_info"]["email"]},'
              f' Username: {self.active_std["personal_info"]["username"]} ')
        edit_info_choice1 = input('Do you want change your password (Y/N): ')
        if edit_info_choice1 == 'Y':
            new_password = input('Enter your new password: ')
            self.active_std['personal_info']['password'] = new_password
            print('\n Your password is changed Successfully \n')
        elif edit_info_choice1 == 'N':
            print('Your password has not been changed')
        else:
            print('Invalid input....Enter Y or N')

    def change_username(self):
        print(f'Name: {self.active_std["name"]}, Age: {self.active_std["age"]}, Marks: {self.active_std["marks"]}, '
              f'Grade: {self.active_std["grade"]}, Email: {self.active_std["personal_info"]["email"]},'
              f' Username: {self.active_std["personal_info"]["username"]} ')
        edit_info_choice2 = input('Do you want change your username (Y/N): ')
        if edit_info_choice2 == 'Y':
            new_username = input('Enter your new username: ')
            self.active_std['personal_info']['username'] = new_username
            print('\n Your username is changed Successfully \n')
        elif edit_info_choice2 == 'N':
            print('Your username has not been changed')
        else:
            print('Invalid input....Enter Y or N')

    def logout_your_account(self):
        print('******** Logout *******')
        self.std_is_logged = False
        self.active_std = None







