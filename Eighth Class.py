#May 4, 2022
#if comparatives

#Variable Initialization
first_number = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
second_number = int(input("Enter the second number: "))

#Loop
if operator == "+":
    print(str(first_number) + " " + operator + " " + str(second_number) + " = " + str(first_number + second_number))
elif operator == "-":
    print(str(first_number) + " " + operator + " " + str(second_number) + " = " + str(first_number - second_number))
elif operator == "/" and second_number != 0:
    print(str(first_number) + " " + operator + " " + str(second_number) + " = " + str(first_number / second_number))
elif operator == "*":
    print(str(first_number) + " " + operator + " " + str(second_number) + " = " + str(first_number * second_number))
else:
    print("Not valid operation")