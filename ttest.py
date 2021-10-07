import hashlib

myFile = 'test.txt'
f = open(myFile)
lines = f.readlines()
#print(len(lines))
count = 0 # total number of lines
countLines = 0 # number of lines in fasta sections
build = ""
buildFasta = ""
symbolArr = []

for i, l in enumerate(lines):
    if l[0] == '>':
        symbolArr.append(i)

for i, l in enumerate(lines):
#    print(countLines)
    if i == 0:
#        print(i )
#        print(l)
        print(l + hashlib.md5(l.encode()).hexdigest() )
#        build += l 
        build += hashlib.md5(l.encode()).hexdigest() 
        count += 1
    elif i <  symbolArr[1] :
        buildFasta += l
        
    elif i == symbolArr[1]:
#        print(i)
#        print(buildFasta)
        print( hashlib.md5(buildFasta.encode()).hexdigest() )
#        print(len(buildFasta))
#        build += buildFasta
        build += " " + hashlib.md5(buildFasta.encode()).hexdigest() + '\n'
#        build = str(len(buildFasta)) + '\n'
        buildFasta = ""

    elif l[0] == '>':
#        print("##############")
#        build += l 
        build += (hashlib.md5(l.encode()).hexdigest() ) 
        build += " " + (hashlib.md5(buildFasta.encode()).hexdigest() ) + '\n'
#        build += str(len(buildFasta)) + '\n'
        print(l + hashlib.md5(l.encode()).hexdigest() )
#        print(hashlib.md5(l.encode()).hexdigest() )
#        print(len(build))
#        print(buildFasta)
        print(hashlib.md5(buildFasta.encode()).hexdigest() )
#        print(len(buildFasta))
        buildFasta = ""
        count += 1
        countLines = 0
    else:
        buildFasta += l
        countLines += 1
        count += 1

onesequence = '''ATGGAGACAGTGTTTGAAGAGATGGATGAAGAAAGCACAGGAGGAGTTTCATCTTCGAAAGAAGAAATAG
TCCTTGGCCAGAGACTCCATCTAAGCTTTCCTTTTAGCATTATCTTCTCAACTGTTCTCTACTGTGGTGA
GGTTGCCTTTGGTTTATACATGTTTGAAATTTATCGAAAAGCTAATGACACATTCTGGATGTCATTTACC
ATCAGCTTTATTATTGTGGGGGCAATTTTGGATCAAATTATCCTGATGTTTTTCAACAAAGACTTGAGGA
GAAATAAGGCTGCATTACTTTTTTGGCACATTCTTCTTTTAGGACCTATTGTGAGGTGTTTGCACACCAT
TAGAAATTACCACAAATGGTTGAAAAATCTTAAACAGGAGAAGGAAGAGACTCAAGTTAGCATCACAAAG
AGAAACACGATGCTGGAAAGGGAGATTGCATTCTCAATCCGGGATAATTTCATGCAGCAGAAGGCTTTCA
AGTACATGTCAGTGATTCAGGCTTTTCTCGGTTCTGTTCCACAATTAATTTTGCAGATGTATATCAGTCT
CACTATACGAGAATGGCCTTTGAATAGAGCATTGCTGATGACATTTTCCCTGTTATCAGTTACTTATGGG
GCCATTCGCTGCAATATACTGGCCATCCAGATCAGCAATGATGATACTACCATTAAGCTACCGCCGATAG
AATTCTTCTGTGTCGTGATGTGGCGTTTTTTGGAGGTTATCTCACGTGTAGTGACTCTGGCATTTTTCAT
TGCATCTCTGAAACTGAAGAGCCTACCCGTTTTGTTAATCATATATTTTGTATCATTGTTGGCACCGTGG
CTGGAGTTTTGGAAAAGTGGAGCTCATCTTCCTGGCAACAAAGAAAATAATTCCAATATGGTGGGTACAG
TACTGATGCTTTTCTTGATCACACTGCTATATGCTGCCATCAACTTCTCCTGCTGGTCAGCAGTGAAACT
GCAGTTGTCAGATGACAAAATAATTGACGGGAGACAGAGGTGGGGCCATAGAATCCTACACTACAGCTTT
CAGTTTTTAGAAAATGTGATAATGATATTGGTATTTAGGTTCTTTGGAGGGAAAACTTTGCTGAATTGTT
GTGACTCATTAATTGCCGTGCAGCTCATCATAAGCTACCTATTGGCCACTGGCTTTATGCTCCTCTTCTA
TCAGTATTTGTACCCATGGCAGTCAGGCAAAGTGTTGCCAGGACGTACTGAAAATCAGCCAGAAGCACCG
TACTATTATGTAAACATCGAGAAAACTGAAAAGAATAAAAATAAGCAGCTGAGGAATTACTGTCACTCCT
GCAATAGGGTTGGATATTTTTCAATCAGAAAAAGTATGACATGTTCATAA
'''
twosequence = '''ATGGCAGAAGACAAAACCAAACCGAGTGAGTTGGACCAAGGGAAGTATGATGCTGATGACAACGTGAAGA
TCATCTGCCTGGGAGACAGCGCAGTGGGCAAATCCAAACTCATGGAGAGATTTCTCATGGATGGCTTTCA
GCCACAGCAGCTGTCCACGTACGCCCTGACCCTGTACAAGCACACAGCCACGGTAGATGGAAGGACCATC
CTTGTGGACTTTTGGGACACGGCAGGCCAGGAGCGGTTCCAGAGCATGCATGCCTCCTACTACCACAAGG
CCCACGCCTGCATCATGGCCCTGCTTCAATGCCACCACCTCCGTGCAGCCTCCTCTGATGTTTGTCATTA
G
'''
print("=======================")
print(build)
#print(symbolArr)

print(hashlib.md5(onesequence.encode()).hexdigest())
print(hashlib.md5(twosequence.encode()).hexdigest())
'''
for i, l in enumerate(lines):
    print("Line {}: {}".format(i, l.strip()))

'''
f.close()

