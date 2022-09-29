"""
The project is aimed at taking a phrase from the user and sorting the words in the phrase alphabetically
    while returning the sorted phrase, including capital letters
"""


def revver(phrase):

    split = phrase.split()
    split.sort(key=str.lower)

    revved = ''
    for i in split:
        if i not in revved:

            revved += i+' '

    return revved


q = input('Enter a phrase of your desired length and we will sort it for you: ')
print(revver(q))
