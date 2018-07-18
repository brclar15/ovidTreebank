# ovidTreebank

a very rudimentary site to host work done analyzing treebank `.xml` data


## Focus: Teaching Tool

- `teaching.py` : allows the user to search for grammatical constructions within a treebank file


  The program gives a brief description of its function, and then prompts the user for a treebank XML file. The user is prompted to choose a case, clause, or other category to look at more closely. If the user enters “case”, the program prints out the abbreviated codes for each case, and the corresponding case name. The user selects the case that they want to look at by entering the abbreviated code. Each case in Latin has a variety of uses, so the program prints out the specific uses that are found in this corpus. This mirrors the step above, where the user is given the abbreviated code and the corresponding description of the code. Due to the nature of treebanks, a high level of specificity is allowed here. The user can choose to look at accusative direct objects (A-DO), accusative direct objects in coordination (A-DO_CO), or accusative direct objects in apposition (A-DO_AP). This level of precision allows a teacher to pinpoint exactly what examples they want to give their students. The user then chooses one of these specific uses, again by entering its abbreviated code. The program then finds every instance of that case function, and prints out every line reference and the accompanying sentence. 
  
  If the user enters “clause”, the program prints out the broad categories for the different clauses that are used in Latin. Each of these types of clauses has their own subcategories and ways that the clause can function. For example, relative clauses are adjectival clause, temporal clauses are adverbial clauses, and direct statements are nominal clauses. The user chooses one of these categories, which are again printed out with their abbreviated code and corresponding name. Then the program prints out the various clauses in that category and their specific uses. As with the specific case use, the user chooses a specific clause use to look at, such as concessive clauses in coordination, indirect questions in apposition, or any others by using the abbreviated code. Then the program prints out the line references and sentences where that specific clause use occurs. 
  
The last of the three main categories is an “other” category, which has adverbs, attributes (adjectives), infinitives, and prepositions. As with the other two categories, the program will prompt the user for a selection within this broader category, and then let them choose from the possible uses that occur within this corpus. Then, the program will return the line references and sentences where this selection occurs. Some of the features in this other category do not have subcategories. There is only one use of attributes (ATR), prepositions (AuxP), and adverbs (ADV), so the program does not prompt the user to enter a more specific usage. 

As mentioned above, some features are very common. If the program is about to print out more than fifteen sentences, the user is asked to agree to this. Common features are numerous, including N-SUBJ, A-DO, ATR, ADJ-RC, and the majority of other tags. More rare usages include D-AGENT, AB-DEGDIF, ADV-CONCESS, INF-COMP_CO, or most things with an _AP or an _OBJ-AP behind it.



## Current Contents

- `compareTrees.py` : prints out a `.csv` file with the percentages of each tag for two authors
- `compareForms.py` : prints out the percent of certain forms used for a given tag
  - useful for AuxC, COORD, and AuxP
- `complex.py` : contains a function that analyzes what tags modify a given tag, as well as a function that analyzes what a given tag modifies
- `superCompare.py` : the same as `compareTrees.py` but for five different trees


## Data Files

- `ovidAll.xml`
  - Ov. Met 1, 13
- `vergil.xml`
  - *Aeneid* AP Syllabus and all of book 1
- `caesar1.xml`
  - Book 1 of *De Bello Gallico*
- `juvenal6.xml`
  - Satire 6 of Juvenal
 - `ovid1.xml`
  - Book 1 of Ovid's *Metamorphoses*
- `ovid13.xml`
  - Book 13 of Ovid's *Metamorphoses*
