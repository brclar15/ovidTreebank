# import Element Tree XML Parser
import xml.etree.ElementTree as etree

fileName1 = '/Users/brian/Desktop/vergil.xml'
fileName2 = '/Users/brian/Desktop/caesar1.xml'

tree1 = etree.parse(fileName1)
root1 = tree1.getroot()

tree2 = etree.parse(fileName2)
root2 = tree2.getroot()

author1 = fileName1.split('/')                # Gets the author//book in a readable format
author1 = author1[-1][:-4]                    # to print later

author2 = fileName2.split('/')     
author2 = author2[-1][:-4]  

def countWords(root):
    count = 0
    for element in root.getiterator('word'):
        if element.get('lemma') != "punc1":
            if element.get('artificial') != "elliptic":   # skips over words added to fillin ellipsis
                count += 1
    return count



# Compare two trees for a specific tag, gives back form 
def findTag(relation, root1, root2):
    tagList1 = list()
    tagList2 = list()
    tagDict1 = {}
    tagDict2 = {}
    for element in root1.getiterator('word'):
        if element.get('relation') == relation:
            if element.get('artificial') != "elliptic": 
                tagList1.append(element.get('lemma'))
    for element in root2.getiterator('word'):
        if element.get('relation') == relation:
            if element.get('artificial') != "elliptic": 
                tagList2.append(element.get('lemma'))
    tagList1.sort()
    tagList2.sort()
    total1 = len(tagList1)
    total2 = len(tagList2)

    for item in tagList1:
        tagDict1[item] = tagList1.count(item)
    for item in tagList2:
        tagDict2[item] = tagList2.count(item)
        
    print(author1, "has", total1, relation, "\n")
    print(tagDict1)
    print("\n", author2, "has", total2, relation, "\n")
    print(tagDict2)
    
               


findTag("COORD", root1, root2)



# Gets all of the possible different relation tags and adds them to a list
TBtagSet = set()
for element in root1.getiterator('word'):
    TBtagSet.add(element.get('relation'))
TBtagSet2 = set()
for element in root2.getiterator('word'):
    TBtagSet2.add(element.get('relation'))
newSet = TBtagSet2 - TBtagSet
for item in newSet:
    TBtagSet.add(item)

# Make the set a list, and sort it
TBtagList = list(TBtagSet)
TBtagList.sort()



    

