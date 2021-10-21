import hashlib 
import sys
import os
def main():
#       myPath = './from-ftp-ensemble/'
   myPath = '../'
   myFile =  'sequence-homo-38-chr22-coding-nucleotides.txt'
   myFile = 'Homo_sapiens.GRCh38.cdna.all.fa'
   filepath = myPath + myFile
    #sys.argv[1]
   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
   numberOfLines = countLines(filepath)
   with open(filepath) as fp:
       build = ""
       buildFasta = ""
       for i, line in enumerate(fp):
            if isFirst(i, line):
                build += '"' + line.strip() + '",'
                build += getHash(i,line) + ', '
            elif not isAngle(i,line):
               buildFasta += line
               #buildFasta += line.strip()
               if i == numberOfLines-1:
                   build += getHash(i, buildFasta)
            elif isAngle(i, line):
                build += getHash(i, buildFasta) + '\n'
                buildFasta = ""
                build += '"' + line.strip() + '",'
                build += getHash(i,line) + ', '
            else:
                print('######')
       print(build)
       fo = open(filepath + ".out", 'w')
       fo.write(build)
       fo.close()
#       saveFile(build)
    #print(line.strip()) if isFirst(i, line)  else print(i)  TERNARY IF no questionMark\n",
def saveFile(build):
    fo = open('test-fasta-9-records.txt.out', 'w')
    fo.write("this is a test")
    fo.close()
def countLines(filepath):
    fo = open(filepath, 'r').readlines()
    return len(fo)
def isLast(i, line):
    return True
def getHash(i, labelOrFasta):
    print(i)
    return hashlib.md5(labelOrFasta.encode()).hexdigest()
def isAngle(i, line):
    if line[0] == ">":
        return True
    else:
        return False
def isFirst( i, line):
    if i == 0:
       return True
if __name__ == '__main__':
    main()

'''
print(build)
print(symbolArr)
'''


