#Giraffe Language will translate all vowels to the letter G

#dog -> dgg
#cat -> cgt
#flag -> flgg

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

#this is a for loop with an if loops built inside of it 
