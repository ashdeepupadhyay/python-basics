#translator single line comments
'''
multiple line comments
'''
def tranlate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(tranlate(input("Enter a phrase")))