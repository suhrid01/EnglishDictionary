import json,difflib
from difflib import get_close_matches

data=json.load(open("Your folder address/data.json"))

def meaning(word):
    word=word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        yn= input("Did you mean %s instead?? Enter y or n:" % get_close_matches(word,data.keys(),cutoff=0.8)[0])
        if "y" in yn:
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif "n" in yn:
            return "The word doesnot exist, Please re enter"
        else:
            return "Wrong input"
    else:
        return "The word %s doesn't exist" % word

word=input("Enter a word: ")
output=meaning(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
