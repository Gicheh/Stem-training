def outputname(x):
    print("Hi",x)
outputname("tito")

#function to replace characters in a string
def replace_in (phrase):
    word=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            word= word+"g"
        elif letter.upper() in "aeiou":
            word= word +"G"
        else:
            word = word + letter
    return word
print(replace_in(input("Enter a phrase: ")))