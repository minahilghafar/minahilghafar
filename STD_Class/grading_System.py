class Grading_System:
    def __init__(self,marks):
        self.marks = marks

    def calculate_grade(self):
        print('***** Welcome to Grading System ******')
        marks = self.marks
        grade = ''

        if 100 >= marks >= 90:
            grade = 'A'
        elif 90 > marks >= 80:
            grade = 'B'
        elif 80 > marks >= 70:
            grade = 'C'
        elif 70 > marks >= 0:
            grade = 'D'
            print('\nYour Grade is ', grade, '\n')
        else:
            print('Invalid Input')

        return grade