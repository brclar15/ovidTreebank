# import Element Tree XML Parser
import xml.etree.ElementTree as etree


tree1 = etree.parse('/Users/brian/Desktop/ovidAll.xml')
root1 = tree1.getroot()

tree2 = etree.parse('/Users/brian/Desktop/vergil.xml')
root2 = tree2.getroot()





# Trying to compare two trees
def compareRelations(root1, root2, relation):
    count1 = 0
    count2 = 0
    for element in root1.getiterator('word'):
        if element.get('relation') == relation:
            count1 += 1
        elif element.get('relation') == relation + "_CO":
            count1 += 1
        elif element.get('relation') == relation + "_AP":
            count1 += 1
        elif element.get('relation') == relation + "_SUBJ-CO":
            count1 += 1
        elif element.get('relation') == relation + "_SUBJ-AP":
            count1 += 1            
        elif element.get('relation') == relation + "_PRED-CO":
            count1 += 1
        elif element.get('relation') == relation + "_PRED-AP":
            count1 += 1
        elif element.get('relation') == relation + "_OBJ-CO":
            count1 += 1
        elif element.get('relation') == relation + "_OBJ-AP":
            count1 += 1
        elif element.get('relation') == relation + "_OBJ":
            count1 += 1
        elif element.get('relation') == relation + "_SUBJ":
            count1 += 1
        elif element.get('relation') == relation + "_PRED":
            count1 += 1
            
    for element in root2.getiterator('word'):
        if element.get('relation') == relation:
            count2 += 1
        elif element.get('relation') == relation + "_CO":
            count2 += 1
        elif element.get('relation') == relation + "_AP":
            count2 += 1
        elif element.get('relation') == relation + "_SUBJ-CO":
            count2 += 1
        elif element.get('relation') == relation + "_SUBJ-AP":
            count2 += 1            
        elif element.get('relation') == relation + "_PRED-CO":
            count2 += 1
        elif element.get('relation') == relation + "_PRED-AP":
            count2 += 1
        elif element.get('relation') == relation + "_OBJ-CO":
            count2 += 1
        elif element.get('relation') == relation + "_OBJ-AP":
            count2 += 1
        elif element.get('relation') == relation + "_OBJ":
            count2 += 1
        elif element.get('relation') == relation + "_SUBJ":
            count2 += 1
        elif element.get('relation') == relation + "_PRED":
            count2 += 1
          
    percent1 =  (count1/12950)*100
    percent2 =  (count2/3372)*100
    print(relation, ",", percent1, ",", percent2, sep="" )


# Gets all of the possible different relation tags and adds them to a list
TBtagSet = set()
for element in root1.getiterator('word'):
    TBtagSet.add(element.get('relation'))

# Make the set a list, and sort it
TBtagSet = list(TBtagSet)
TBtagSet.sort()

# Print out the count for all relations in order
for item in TBtagSet:
    compareRelations(root1, root2, item)





# Print out the count for all relations in order
for item in TBtagSet:
    compareRelations(root1, root2, 'relation')

    
##    # Gives any of them grater than a given number
##    if percent >= 1.5:
##        percent = str(percent)
##        percent = percent[:6]
##        # Readable print
##        #print(relation, "=", count, "  out of total words:", percent, "%")
##        
##        # short form print
##        print(relation, "=", percent, "%")
