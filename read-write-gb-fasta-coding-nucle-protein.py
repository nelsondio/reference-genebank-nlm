import hashlib  
import sys      
import os 
from collections import Counter
import matplotlib.pylab as plt

def main():     
    myPath = '../'
    hardLink = 'SEQUENCE_HOMO38/'
    myFile =  'sequence-homo-38-chr2-coding-nucleotides.txt'
    myFile =  'sequence-homo-38-chr1-coding-nucleotides.txt'
    myFile =  'sequence-homo-38-chr1-coding-protein.txt'
    myFile =  'sequence-homo-38-chr5-coding-protein.txt'
    myFile =  'sequence-homo-38-chr5-coding-nucleotides.txt'
    myFile =  'sequence-homo-38-chr4-coding-protein.txt'
    myFile =  'sequence-homo-38-chr4-coding-nucleotides.txt'
    myFile =  'sequence-homo-38-chr3-coding-protein.txt'
    myFile =  'sequence-homo-38-chr3-coding-nucleotides.txt'
    outpath = myPath + hardLink + 'OUPUT/' + myFile 
    filepath = myPath + hardLink + myFile
    #sys.argv[1]
    chromosome = {}
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    numberOfLines = countLines(filepath)
    with open(filepath) as fp:
        dictObj = {}
        buildFasta = ""
        buildLabel = ""
        buildLabelMd5 = ""
        buildFastaMd5 = ""
        for i, line in enumerate(fp):
            dictObj = {}
            if isFirst(i, line):
                buildLabel = '"' + line.strip() + '"'
                buildLabelMd5 = getHash(i,line)
            elif not isAngle(i,line):
                buildFasta += line
               #buildFasta += line.strip()
                if i == numberOfLines-1:
                    buildFastaMd5 = getHash(i, buildFasta)
                    dictObj = {'label':buildLabel,'labelMd5':buildLabelMd5,'fastaMd5':buildFastaMd5 }
                    tmp =  buildLabelMd5
                    chromosome.update({tmp:dictObj})
            elif isAngle(i, line):
                buildFastaMd5 = getHash(i, buildFasta)
                dictObj = {'label':buildLabel,'labelMd5':buildLabelMd5,'fastaMd5':buildFastaMd5 }
                tmp =  buildLabelMd5
                chromosome.update({tmp:dictObj})
                buildFasta = ""
                buildFastaMd5 = ""
                buildLabel = ""
                buildLabelMd5 = ""
                buildLabel = '"' + line.strip() + '"'
                buildLabelMd5 = getHash(i,line)
            else:
                print('######')
 
        fo = open(myFile + ".dict.out", 'w')
        fo.write(displayDictDataItems(chromosome))
        fo.close()
        countDups = countDuplicates(chromosome)
        displayBar(countDups, outpath)

def displayBar(data, filepath):
    names = list(data.keys())
    shortName = shortenName(names)
    values = list(data.values())
    fig, ax = plt.subplots(figsize=(20,10))
    plt.xlabel('Key fastaMd5')
    plt.ylabel('Value duplicates')
    plt.title(filepath)
    plt.bar(range(len(data)),values,tick_label=shortName)
    plt.savefig(filepath + '.png')
    plt.show()
    
def shortenName(list):
    shortNameList = []
    for n in list:
        tmp = n[:6]
        shortNameList.append(tmp)
    return shortNameList
        
def countDuplicates(d):
    out = []
    #cnt = Counter()
    for h in d.values():
        out.append(h['fastaMd5'])
    print(type(out))
    dictOfElems = dict(Counter(out))
    return dictOfElems

def displayDictDataItems(d):
    out = ""
    for i,j in d.items():
        out += str(j['labelMd5']) + '\t' + str(j['fastaMd5']) + '\n'
    return out

def countLines(filepath):
    fo = open(filepath, 'r').readlines()
    return len(fo)
def isLast(i, line):
    return True
def getHash(i, labelOrFasta):
#    print(i)
    return hashlib.md5(labelOrFasta.encode()).hexdigest()
def isAngle(i, line):
    if line[0] == ">":
        return True
    else:
        return False
def isFirst( i, line):
    if i == 0:
       return True

def displayFastaMd5(d):
    fastaMd5List = []
    for i in d.values():
        fastaMd5List.append((i['fastaMd5']))
    return fastaMd5List

if __name__ == '__main__':
    main()

# LAST EDITED: 11.18.2021
