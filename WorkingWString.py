#strings are basically plain text
# \n will move the following text of a string to the next line
# \ is an escape character. This will tell python that I would like the following characters to be a part of the string

MLB = "Major League of Baseball"
print("Free code academy - lets learn!")
print("free \n smoke") 
print("Major League of\"Baseball\"")
print(MLB)

NFL = "National Football League"
print(NFL)
print(NFL + " and " + MLB + " are cool.") 

#function is a block of code that will perform a series of actions for us.
#we can use functions to modify our strings and get more information about string

print(NFL.lower())
print(NFL.upper())

#MLS - variable
#print(MLS.isupper()) is asking if the variables are upper or lower case
# variable.lower/variable.upper converts the variable string to lower/upper case
# variable.islower/upper is asking if the variable is lower or upper case.

MLS = "MAJOR LEAGUE OF SOCCER"
print(MLS.isupper())
print(MLS.islower())

print(MLS.lower().isupper())

#len function will tell you how many characters are in the string
print(len(MLS))

#here I have indexed the string.  String Indexing begins with 0.
print(MLS[9])
print(MLS[0])

print(MLS.index("LEAGUE"))
print(MLS.replace("SOCCER","Baseball"))
print(MLS.replace("MAJOR", "Below Average"))
print(MLS)

