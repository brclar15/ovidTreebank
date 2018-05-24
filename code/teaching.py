# Teaching Tools with Treebanks
# Code by Brian Clark

# used for the file input
import os.path
from os import path


# import Element Tree XML Parser
import xml.etree.ElementTree as etree

# intial start up print statements 
print("Welcome to querying treebank data! \nYou can search for a grammtical freature using this program. \n")
print("When choosing a file, please enter the file name in a format that mirrors this: /Users/brian/Desktop/ovid13.xml \n")
print("HINT: This script needs to be in the same folder as your .xml file in order for it to work, and the file path just be typed correctly. \n")
fileName = input("Please enter a treebank XML file: ")



tree = etree.parse(fileName)
root = tree.getroot()



# gets every relation tag that occurs in this corupus
# retain only the unique elements, and sort them alphabetically
TBtagSet = set()
for element in root.getiterator('word'):
    TBtagSet.add(element.get('relation'))
TBtagList = list(TBtagSet)
TBtagList.sort()

# recombines the enclitics in a given sentence and returns the list
def combineEnclitics(L):
    k = 0
    while k < len(L):
        if L[k][0] == "-":
            L[k-1] = L[k-1] + L[k][1:]
            L.remove(L[k])
        k += 1
    return L





# retrieves the passage and line reference  using dictionaries
def getPassage(relation):
    bigList = list()             # ultimately a list of sentences where the desired tag is used
    sentenceList = list()        # a list to temporarily store each sentence 
    newList = list()             # a clear way to add the sentenceList to the bigList without worrying about clearing important data
    parentList = list()          # a list of the line references that correspond to each sentence
    i = 0      #counter
    k = 0      # different counter
    my_dict ={}                 # stores the line reference : sentence, eliminates duplicates
    for parent in tree.getiterator():
        for child in parent:
            if child.get('relation') == relation:               # find the desired tag
                parentSubDoc = parent.get('subdoc')
                parentList.append(parent.get('subdoc'))         
                if parent.get('subdoc') == parentSubDoc:        
                    for words in parent:
                        if words.get('artificial') != "elliptic":   # skips over words added to fillin ellipsis
                            sentenceList.append(words.get('form'))  
                    newList = list(sentenceList)
                    bigList.append(newList)                         # now a list of sentences as lists
                    sentenceList.clear()                                # clears as it re-enters the loop
    for item in parentList:
        my_dict[item] = bigList[i]                              # load the dictionary with line reference: sentence
        i += 1
    if len(my_dict) == 0:
        print("Sorry, there are no instances of this in your corpus. Please choose another selection.")
        exit()
    elif len(my_dict) > 15:
        print("You are about to print more than 15 sentences. Are you sure you want to do this?")
        userInput = input("Please type yes or no: ")
        if userInput == "yes":
            print("\n Okay, if you're sure.... \n")
            for key, value in my_dict.items():                  # prints the line reference, then the readable sentence with recombined enclitcs 
                print("\n", key)
                combineEnclitics(value)
                print(' '.join(value), "\n")
        if userInput == "no":
            print("Good call. Try a less common feature, as that will yield fewer results")
            exit() 
        if userInput != "yes" and userIntput != "no":
            print("ERROR: invalid entry. please rerun the program and try again.")
    else:
        for key, value in my_dict.items():                  # prints the line reference, then the readable sentence with recombined enclitcs 
            print("\n", key)
            combineEnclitics(value)
            print(' '.join(value), "\n")




def findChoices(userChoice):                        
    for item in TBtagList:                          # loops through a list of unique tags within this corpus 
        if userChoice[-6:] == "clause":             # if the user is looking for a clause (done to distinguish 'ADV' from 'ADV clause')
            if userChoice[:3] + "-" == item[:4]:
                print(item)                         # print options for that type of clause
        elif userChoice + "-" == item[:(len(userChoice)+1)]:            # OR prints out options that aren't clauses
            print(item)
    print("\n")


#### User interface starts here  #####

validChoices = ["A", "AB", "ADJ clause", "ADV clause", "ADV",           # list of valid user initial inputs
            "ATR", "AuxP", "D", "G", "INF", "N", "NOM clause", "PRED", "V"]
singleOptionChoices = ["ADV", "ATR", "L", "AuxP"]                          # list of choices that do not require another input (example: no types of ATRs, just ATRs)
manyOptionChoices = ["A", "AB", "ADJ clause", "ADV clause", "D", "G", "INF", "N", "NOM clause", "PRED", "V"]        # list of choices that require another input 


if fileName[-3:] != "xml":          # Needs to be a treebank XML file, but the parser won't event accept anything else from the getgo
    print("ERROR: You need to enter a treebank XML file. please try again.")
if path.exists(fileName):
    print("Please choose an option to retrieve")
    while True:
        topLevelChoice = input("Enter case, clause, or other:  ")      # user enters category, and gets their options
        if topLevelChoice == "case":
            print("N: nominatives")
            print("G: genitives")
            print("D: datives")
            print("A: accusatives")
            print("AB: ablatives")
            print("L: locatives")
            print("V: vocatives")
        elif topLevelChoice == "clause":
            print("ADJ clause: adjectival clauses")
            print("ADV clause: adverbial clauses")
            print("NOM clause: nominal clauses")
        elif topLevelChoice == "other":
            print("ADV: adverbs")
            print("ATR: adjectives")
            print("INF: infinitives")
            print("AuxP: prepositions")
        else:
            print("ERROR: Please choose from those three categories only.")       # Error message
            break
        secondChoice = input("Enter the abbreviated code that corresponds to your choice:  ")
        if secondChoice == "L":
            getPassage("L-LOCAT")
        elif secondChoice in singleOptionChoices:       # if true, no need for more input
            getPassage(secondChoice)                  # prints out sentences with their relation tag
        elif secondChoice in manyOptionChoices:       # if true, gives the user options within their subcategory 
            findChoices(secondChoice)
            thirdChoice = input("Please choose a specific tag from the list above: ")
            getPassage(thirdChoice)            # has them choose one, and prints out sentences with that relation tag
        else:
            print("ERROR: Please choose from the list above.")          # error message
            break
else:
    print("file does not exist")    # error message

