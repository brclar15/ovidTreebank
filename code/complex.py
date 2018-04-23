# Complicated Attempt


# import Element Tree XML Parser
import xml.etree.ElementTree as etree

fileName = '/Users/brian/Desktop/caesar1.xml'
tree = etree.parse(fileName)
root = tree.getroot()

author = fileName.split('/')                # Gets the author//book in a readable format
author = author[-1][:-4]                    # to print later


# Get all of the tags in the tree
TBtagSet = set()
for element in root.getiterator('word'):
    TBtagSet.add(element.get('relation'))
TBtagList = list(TBtagSet)
TBtagList.sort()




#############



def countRelation(relation):
    possibleTags = [relation, relation + "_CO", relation + "_AP", relation + "_SBJ",        # adds the _CO or others to the desired tag
                    relation + "_SUBJ-CO", relation + "_SUBJ-AP", relation + "_PRED",
                    relation + "_PRED-CO", relation + "_PRED-AP", relation + "_OBJ",
                    relation + "_OBJ-CO", relation + "_OBJ-AP"]
    count = 0
    for element in root.getiterator('word'):
        if element.get('relation') in possibleTags:
            count += 1
    return count





            

# ARCHIVE COPY finds the things that modify a given relation tag
def modified(relation):
    typeList = list()
    tagCount = list()           # used to get the total count of that tag
    my_dict = {}
    ignoredTags = ["AuxX", "AuxK", "AuxG"]          # dont care about punctuation
    possibleTags = [relation, relation + "_CO", relation + "_AP", relation + "_SBJ",        # adds the _CO or others to the desired tag
                    relation + "_SUBJ-CO", relation + "_SUBJ-AP", relation + "_PRED",
                    relation + "_PRED-CO", relation + "_PRED-AP", relation + "_OBJ",
                    relation + "_OBJ-CO", relation + "_OBJ-AP"]
    for parent in tree.getiterator():
        for child in parent:
            if child.get('relation') in possibleTags:
                parentSubDoc = parent.get('subdoc')
                wordID = child.get('id')
                if parent.get('subdoc') == parentSubDoc:
                    for word in parent:
                        if word.get('relation') not in ignoredTags:
                            if word.get('head') == wordID:
                                typeList.append(word.get('relation'))     # adds the relation that modifies the target tag to a list
                            

    typeList.sort()
    for item in typeList:
        my_dict[item] = typeList.count(item)     # loads a dictionary with the tag modifying as the key, and its count as the value
    if relation == "AB-ABSOL":
        numberOfDesiredTag = my_dict[relation]           # to get total of the tag used ONLY FOR AB-ABSOL
    else:
        numberOfDesiredTag = countRelation(relation)
    print("Data for:", author, "\n")

    print("Number of ", relation, ": ", numberOfDesiredTag)
    if relation == "AB-ABSOL":
        del my_dict[relation]                         # ONLY FOR AB-ABSOL
    total = 0 
    for key, value in sorted(my_dict.items()):       # used to figure out how many bare items to add
        total = total + value
    my_dict["bare"] = numberOfDesiredTag - total    # when it is unmodified 
    print("This author uses", len(my_dict), "different tags to modify", relation)

    for key, value in my_dict.items():
        print(key, ",", value, sep="")
                                  
                    
#modified("NOM-INDSTAT")





############





# STILL WORKING, NOT sure its accurate
# finds the things that modify a given relation tag
def modifies(relation):
    typeList = list()
    bigList = list()
    my_dict = {}
    count = 0
    newWordID = ""     # need to initialize this for some reason...
    possibleTags = [relation, relation + "_CO", relation + "_AP", relation + "_SBJ",        # adds the _CO or others to the desired tag
                    relation + "_SUBJ-CO", relation + "_SUBJ-AP", relation + "_PRED",
                    relation + "_PRED-CO", relation + "_PRED-AP", relation + "_OBJ",
                    relation + "_OBJ-CO", relation + "_OBJ-AP"]
    for parent in tree.getiterator():
        for child in parent:
            if child.get('relation') in possibleTags:
                parentSubDoc = parent.get('subdoc')
                parentID = parent.get('id')
                wordHead = child.get('head')
                if parent.get('subdoc') == parentSubDoc:
                    for word in parent:
                        if word.get('id') == wordHead:
                            typeList.append(word.get('relation'))
                            if word.get('relation') == "APOS":
                                print(parentSubDoc)

    typeList.sort()
    for item in typeList:
        my_dict[item] = typeList.count(item)     # loads a dictionary with the tag modifying as the key, and its count as the value

    if relation == "AB-ABSOL":          # don't need the pair of them
        del my_dict[relation] 
    numberOfDesiredTag = countRelation(relation)      # how many overall
    print("Data for:", author, "\n")
    if relation == "AB-ABSOL":
        numberOfDesiredTag = numberOfDesiredTag/2
    print("Number of ", relation, ": ", numberOfDesiredTag)
    total = 0 
    for key, value in sorted(my_dict.items()):       # used to figure out how many bare items to add
        total = total + value
    if relation != "AB-ABSOL":
        my_dict["bare"] = numberOfDesiredTag - total    # when it is unmodified
    print("This author uses", relation, " to modify", len(my_dict), "different tags \n")

    for key, value in my_dict.items():
        print(key, ",", value, sep="")

                    
modifies("AB-ABSOL")



##############


def polysyndeton():
    count = 0                       # count of coords labeled with ADV
    total = 10                       # total coords by morphology



    for parent in tree.getiterator():
        for child in parent:
            posTag = child.get('postag')
            if child.get('relation') == "ADV":
                if child.get('postag')[0] == "c":
                    count += 1

    
    percent = count / total
    return count


#print(polysyndeton())



    
