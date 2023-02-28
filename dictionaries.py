#keys = dictionary word
#keys need to be unique
#values = dictionary definition

#in this scenario, the key is the 3 letter month abbreviation. 
#in this scenario, the value is the full month
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May", 
    "Jun": "June",
    "Jul": "July",
    "Aug": "August", 
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December", 
}

print(monthConversion["Dec"])
print(monthConversion.get("Jul"))