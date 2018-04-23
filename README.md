# ovidTreebank

a very rudimentary site to host work done analyzing treebank `.xml` data

## Current Contents

- `compareTrees.py` : prints out a `.csv` file with the percentages of each tag for two authors
- `compareForms.py` : prints out the percent of certain forms used for a given tag
  - useful for AuxC, COORD, and AuxP
- `complex.py` : contains a function that analyzes what tags modify a given tag, as well as a function that analyzes what a given tag modifies
- `superCompare.py` : the same as `compareTrees.py` but for five different trees
- `teaching.py` : allows the user to search for grammatical constructions within a treebank file


## Data Files

- `ovidAll.xml`
  - Ov. Met 1, 13
- `vergil.xml`
  - Ver. An. AP Syllabus and all of book 1
- `caesar1.xml`
  - Book 1 of *De Bello Gallico*
- `juvenal6.xml`
  - Satire 6 of Juvenal
 - `ovid1.xml`
  - Book 1 of Ovid's *Metamorphoses*
- `ovid13.xml`
  - Book 13 of Ovid's *Metamorphoses*
