def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3: 
        return num2
    else: 
        return num3 

print(max_num(123, 45, 39)) 

# == means if the two values are equal 
# != means is not equal to
# <= is less than or equal to
# >= is greater than or equal to