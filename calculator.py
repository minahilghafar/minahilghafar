num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))
choice = int(input("Do you want to add,sub,div,mul (1/2/3/4):"))
if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
else:
    result = 0
    print("Choose between 1 to 4")

print("Result",result)






