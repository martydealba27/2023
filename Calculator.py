#Calculator 


#variables will normally be a string
#we will need to immediately convert the variable to a numerical data type 
num1 = float(input("Enter First Number: " ))

#we are getting a user input value for an operator (+ ,- , *, /, ^ )
op = input("Enter Operator Number: " )

#we will need to convert the second numerical variable to a numerical data type 
num2 = float(input("Enter First Number: " ))

#if the user enters a '+', we will add the two numbers. 
if op == "+":
    print(num1 + num2)
#if the user enters a '-', we will subtract the numbers. 
elif op == "-":
    print(num1 - num2)
#if the user enters a '*', we will multiuply the numbers.
elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)
else: 
    print("Invalid Operator")