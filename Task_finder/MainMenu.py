from Task import Task
from User import User
from Task_Finder import Task_Management

class MainMenu:
    def __init__(self):
        self.tasks = Task_Management()

    def run(self):
        while True:
            print("\n***** Welcome To Dashboard ******\n")
            print("Press 1 to Add Task")
            print("Press 2 to See all Tasks")
            print("Press 3 to Update Task")
            print("Press 4 to Delete Task")
            print("Press 5 to Add User")
            print("Press 6 to See History")
            print("Press 7 to Exits")
            choice = input('Enter your choice: ')
            if choice == '1':
                task_name = input('Enter your Task_name: ')
                task_status = 'incomplete'
                task_date = input('Enter task_date: ')
                t1 = Task(task_name,task_status,task_date)
                t1.add_task()
                self.tasks.task = t1.task
            elif choice == '2':
                self.tasks.display_all_task()
            elif choice == '3':
                self.tasks.update_task()
            elif choice == '4':
                self.tasks.delete_task()
            elif choice == '5':
                name = input('Enter your name: ')
                phone_number = input('Enter your phone_number: ')
                address = input('Enter your address: ')
                u1 = User(name,phone_number,address)
                u1.add_user()
                self.tasks.user = u1.user
            elif choice == '6':
                self.tasks.display_history()
            elif choice == '7':
                print("\n Thanks for using Task Finder \n")
                break
            else:
                print('Invalid Input...Choose Between 1 to 6')


if __name__ == '__main__':
    menu = MainMenu()
    menu.run()

