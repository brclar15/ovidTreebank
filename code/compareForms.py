# import Element Tree XML Parser
import xml.etree.ElementTree as etree


# intial start up print statements
print("This program allows you to find the different words used in a corpus for certain relations.")
print("When choosing a file, please enter the file name in a format that mirrors this: /Users/brian/Desktop/ovid13.xml \n")
print("HINT: This script needs to be in the same folder as your .xml file in order for it to work, and the file path must be typed correctly. \n")
fileName = input("Please enter a treebank XML file: ")


tree = etree.parse(fileName)
root = tree.getroot()


def authorInfo(fileName):
    author = fileName.split('/')                # Gets the author//book in a readable format
    author = author[-1][:-4]                    # to print later
    print("Currently analyzing :", author, "\n")
    
    


# Compare two trees for a specific tag, gives back form 
def findTag(relation):
    tagList = list()
    tagDict = {}
    for element in root.getiterator('word'):
        if element.get('relation') == relation:
            if element.get('artificial') != "elliptic": 
                tagList.append(element.get('lemma'))
    tagList.sort()
    total = len(tagList)

    for item in tagList:
        tagDict[item] = tagList.count(item)
    print("Here are the raw numbers" )
    print("Total number of relations for ", relation, ":", total, "\n")

    for key, value in tagDict.items():
        print(key, ",", value, sep="")
    print("\n")
    


# Gets all of the possible different relation tags and adds them to a list
TBtagSet = set()
for element in root.getiterator('word'):
    TBtagSet.add(element.get('relation'))
TBtagSet2 = set()

# Make the set a list, and sort it
TBtagList = list(TBtagSet)
TBtagList.sort()


############# User interface starts here

def startUp():
    allowedList = ["COORD","AuxP","AuxC"]
    while True:    
        print("\n Please enter COORD for coordinators, AuxP for preopostions, or AuxC for subordinating conjunctions. \n")               
        userChoice = input("Which of these three choices are you interested in? : ")
        if userChoice not in allowedList:
            print("ERROR: you must choose from the options above.")
            break
        else:
            authorInfo(fileName)
            findTag(userChoice)
            break

startUp()

while True:
    print("would you like to run the program again on a different relation? \n")
    newInput = input("Enter yes or no: ")
    if newInput != "yes" and newInput != "no":
        print("ERROR: you must choose 'yes' or 'no'. Please rerun the program.")
        break
    elif newInput == "yes":
        startUp()
    elif newInput == "no":
        print("Alright, goodbye!")
        break 
    
    


    

