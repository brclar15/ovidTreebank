# Desperate attempt to parse Treebank XML
# spits out all of the tags and proportions with percentages for ONE tree

# import Element Tree XML Parser
import xml.etree.ElementTree as etree


tree = etree.parse('/Users/brian/Desktop/vergil.xml')
root = tree.getroot()


# Grab all of the sentences 
sentences = root.findall('sentence')

# grabs one word
word = root.find('sentence')


# prints unhelpful element word at series of letters//numbers
#print(sentences[0])

#prints out the attributes for the first word of the sentence
#print(word[0].attrib)


#prints out attributes of the sentence
#print(sentences[0].attrib)

#attributes = word.attrib
#print(attributes.attrib)


# prints out the elements of each word for the first sentence 
count = 0
for thing in word:
    #print(word[count].attrib)
    count += 1

# gets at the elements of a sentence
#print(word.get("subdoc"))

# prints out all of the elements for every subelement
#children = root.getchildren()
#for element in children:
#    appt_children = element.getchildren()
#    for appt_child in appt_children:
#        print("%s=%s" % (appt_child.tag, appt_child.attrib))            

# Counts all of the non-punctuation words
## NOT SURE IF THIS WORKS RIGHT
def countWords():
    count = 0
    for element in root.getiterator('word'):
        if element.get('lemma') != "punc1":
            count += 1
    return count

#print(countWords())

# A function to count all of a given relation
# Gives percent to  4 decimal places
# Last if gives them above a certain %
def getRelationTag(relation):
    count = 0
    for element in root.getiterator('word'):
        if element.get('relation') == relation:
            count += 1
        elif element.get('relation') == relation + "_CO":
            count += 1
        elif element.get('relation') == relation + "_AP":
            count += 1
        elif element.get('relation') == relation + "_SUBJ-CO":
            count += 1
        elif element.get('relation') == relation + "_SUBJ-AP":
            count += 1            
        elif element.get('relation') == relation + "_PRED-CO":
            count += 1
        elif element.get('relation') == relation + "_PRED-AP":
            count += 1
        elif element.get('relation') == relation + "_OBJ-CO":
            count += 1
        elif element.get('relation') == relation + "_OBJ-AP":
            count += 1
        elif element.get('relation') == relation + "_OBJ":
            count += 1
        elif element.get('relation') == relation + "_SUBJ":
            count += 1
        elif element.get('relation') == relation + "_PRED":
            count += 1
    percent =  (count/countWords())*100
    # Gives any of them grater than a given number
    if percent >= 0:
        percent = str(percent)
        percent = percent[:6]
        # Readable print
#        print(relation, "=", count, "  out of total words:", percent, "%")

        print(relation, ",", count, ",", percent, "%",sep="")
        
        # short form print
        #print(relation, " = ", percent, "%", sep="")



# Gets all of the possible different relation tags and adds them to a list
TBtagSet = set()
for element in root.getiterator('word'):
    TBtagSet.add(element.get('relation'))

# Make the set a list, and sort it
TBtagSet = list(TBtagSet)
TBtagSet.sort()

# Print out the count for all relations in order
for item in TBtagSet:
    getRelationTag(item)




##for element in root.getiterator('word'):
##    setAuxC = set()
##    if element.get('relation') == "AuxC":
##        setAuxC.add(element.get('form'))
##        print(setAuxC)
    
