print('**** Welcome to Grading System****')
marks = int(input('Enter your academic marks : '))
grade = ''
feedback = ''
if marks <= 100 and marks >= 90:
    grade = 'A'
elif marks < 90 and marks >= 80:
    grade = 'B'
elif marks < 80 and marks >= 70:
    grade = 'C'
elif marks < 70 and marks >= 0:
    grade = 'F'
else:
    print('Invalid Input!...')
if grade == 'A':
    feedback = 'Excellent Work'
elif grade == 'B':
    feedback = 'Good'
elif grade == 'C':
    feedback = 'Fair'
elif grade == 'F':
     feedback = 'Keep it up'
print('Your Grade is: ', grade, '', feedback)
