# import Element Tree XML Parser
import xml.etree.ElementTree as etree


tree1 = etree.parse('/Users/brian/Desktop/ovid1.xml')
root1 = tree1.getroot()

tree2 = etree.parse('/Users/brian/Desktop/ovid13.xml')
root2 = tree2.getroot()

tree3 = etree.parse('/Users/brian/Desktop/vergil.xml')
root3 = tree3.getroot()

tree4 = etree.parse('/Users/brian/Desktop/juvenal6.xml')
root4 = tree4.getroot()

tree5 = etree.parse('/Users/brian/Desktop/caesar1.xml')
root5 = tree5.getroot()





def countWords(root):
    count = 0
    for element in root.getiterator('word'):
        if element.get('lemma') != "punc1":
            if element.get('artificial') != "elliptic":   # skips over words added to fillin ellipsis
                count += 1
    return count



# Compare two trees
def compareRelations(root1, root2, relation):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for element in root1.getiterator('word'):
        if element.get('relation') == relation:
            count1 += 1

            
    for element in root2.getiterator('word'):
        if element.get('relation') == relation:
            count2 += 1

    for element in root3.getiterator('word'):
        if element.get('relation') == relation:
            count3 += 1

    for element in root4.getiterator('word'):
        if element.get('relation') == relation:
            count4 += 1

    for element in root5.getiterator('word'):
        if element.get('relation') == relation:
            count5 += 1


    percent1 =  (count1/countWords(root1))*100
    percent2 =  (count2/countWords(root2))*100
    percent3 =  (count3/countWords(root3))*100
    percent4 =  (count4/countWords(root4))*100
    percent5 =  (count5/countWords(root5))*100
    diff = percent1 - percent2
    percent1 = str(percent1)
    percent2 = str(percent2)
    percent3 = str(percent3)
    percent4 = str(percent4)
    percent5 = str(percent5)
    percent1 = percent1[:6]
    percent2 = percent2[:6]
    percent3 = percent3[:6]
    percent4 = percent4[:6]
    percent5 = percent5[:6]
    print(relation, ",", percent1, ",", percent2, ",", percent3, ",", percent4, ",", percent5, sep="")
    #print(relation, ",", count1, ",", count2,sep="")




    # DO THIS TO PRINT IT FOR MARKDOWN 
##    print("|  ", relation, "  |  ", percent1, "  |  ", percent2, "  |  ", sep="", end="")
##    if diff < 0.2  and diff > -0.2 :
##        diff = str(diff)
##        diff = diff[:6]
##        print("**", diff, "**  |", sep="")
##    else:
##        diff = str(diff)
##        diff = diff[:6]
##        print(diff, "   |")



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

# Print out the count for all relations in order
for item in TBtagList:
    compareRelations(root1, root2, item)




    

