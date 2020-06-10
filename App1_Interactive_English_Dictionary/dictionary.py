import json
from difflib import get_close_matches

data=json.load(open("App1/data.json"))

def translate(words):
    w=words.lower()

    if w in data:
        return data[w]

    elif w.title() in data:               #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]

    elif w.upper() in data:               #in case user enters words like USA or NATO
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        correct = input("Did you mean %s instead? \nEnter Y/y if yes, or N/n if no: " % get_close_matches(w, data.keys())[0])
        if correct == "Y" or correct == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif correct == "N" or correct == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."

word=input("Enter the word: ")
output=translate(word)

if isinstance(output,list):
    for items in output:
        print(items)
else:
    print(output)