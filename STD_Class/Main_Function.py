from Stu_portal_Class import StudentPortal
from STD_Class.student import Student

class MainMenu:
    def __init__(self):
        self.portal = StudentPortal()

    def run(self):
        while True:
            print("Press 1 to Register Yourself")
            print("Press 2 to login")
            print("Press 3 to Access Student Portal")
            print("Press 4 to Logout")
            print("Press 5 to Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                marks = int(input("Enter your marks: "))
                student = Student(name, age, marks)
                student.register_yourself()
                self.portal.Students = student.Students
            elif choice == '2':
                self.portal.login_into_std_portal()
            elif choice == '3':
                self.portal.access_std_portal()
            elif choice == '4':
                self.portal.logout_your_account()
            elif choice == '5':
                print("Thanks For using Student Portal")
                break
            else:
                print("Invalid Input")


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()