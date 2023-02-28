#if statements are specifying conditions for your code to run and execute

is_male = True
is_tall = True

if is_male or is_tall: 
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and not(is_tall):
    print("you not a male but are tall")
else: 
    print("You are not a male or not tall")

