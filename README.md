# Code name: ALDEBARAN

## CONTENT
1) read-gb-fasta-nucle.py
2) README
3) ttest.py

## 10.07.2021
4) git init
5) master
======== I had issues with md5 values with slightly different versions of the initial script
======== I am testing the fasta length (len()), how the new line char are treated, consiering the possibility to delete the new line char or to process fasta as it is, which is 60 char lenght. Still unsure how the last line is processed. 
======== Also, I started the git project to keep track of changes. Before today I just saved separate files.
======== run tail -250 sequence-homo-38-chr22-coding-nucl.txt and then added a few lines missing from the last record. It output 18 records, made a copy on the server to be able to watch on a web page. 

6) ===== current version of ttest.py has print as well as build statements. The first record is a problem. Print statements are correct, but build output is missing the first record to no avail. I will commit and pipe the output to a file. build output is commented out


## 10.21.2021
7) =====
===== Last commit before using matplotlib
===== 
===== diff-genebank-ensemble.txt = genebank vs ensemble different number of chars per line
===== 

## 11.18.2021
### Using most recent assemby from genebank:
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/
### STEPS
8) Manual download of cDNA sequences as well as protein sequences per each chromosome at such URL:
https://www.ncbi.nlm.nih.gov/nuccore/NC_000006.12 for human chromosome 6
9) download default name sequence.txt, I named sequence-homo-38-chrNN-coding-nucleotides/protein.txt
10) PLAN: save data in separate folder, main code in a folder with git
README.md
11) read-write-gb-fasta-coding-nucletide-protein.py: 
  a) import libraries: hashlib, sys, os, collections, matplotlib 
  b) define path to read file c) file is in FASTA format: first line with open angle bracket, label, second line with sequence. d) read label, hash. Read sequence line-by-line, keeping new line in between, hash e) create a dictionary object with fields: label, lableMd5, fastaMd5 f) add dictionary object to chromosome object: an object of objects g) Once chromosome object is built, save with same name plus extension "dict.out". h) Save into a file two columns: labelMd5 and fasta Md5 (hashes) i) count duplicates of chromosome object (no need to sort based on fastaMd5, in order to keep order within chromosome) j) Display duplicates as bars in a png format.
12) for loop in enumerate(file) needed to read line-by-line
### In summary: 
#### input a fasta file, output file with label hash and fasta hash, and a png few png files with bar representing the number of duplicate sequences within chromosome.

## PENDING
13) DONE: extracted hashes of chr22, drawn png figures on 56 mega bases
14) Add legends to x axis with label on most numerous duplicates.
15) Split the number of bases per chromosome in gropus of about 56-60 mega bases per page
17) Automatize the analysis: create a function to process each chromosome with input as a list/array
18) Create an html file with all the generated png images.

