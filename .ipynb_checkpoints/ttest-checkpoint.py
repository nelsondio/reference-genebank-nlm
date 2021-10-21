import hashlib

myFile = 'test.txt'
f = open(myFile)
lines = f.readlines()
build = ""
buildFasta = ""
symbolArr = []

for i, l in enumerate(lines):
    if l[0] == '>':
        symbolArr.append(i)

for i, l in enumerate(lines):
#    print(countLines)
    if i == 0:
        printLabel = '"' +   l.strip() + '",'   
        printLabelmd5 = (hashlib.md5(l.encode()).hexdigest() + ',')
        build += '"' + l.strip() + '",' +  hashlib.md5(l.encode()).hexdigest() + ','
        print("".format())
    elif i <  symbolArr[1] :
        buildFasta += l
        
    elif i == symbolArr[1]:
        printFasta = (buildFasta)
        printFastamd5= ( hashlib.md5(buildFasta.encode()).hexdigest() + '\n')
        print("{}{}{}".format(printLabel, printLabelmd5, printFastamd5))
        build += hashlib.md5(buildFasta.encode()).hexdigest() + '\n'
        buildFasta = ""

    elif l[0] == '>':
        #print("##############")
        build +=  '"' + l.strip() + '",' + hashlib.md5(l.encode()).hexdigest()  + ','
        build += (hashlib.md5(buildFasta.encode()).hexdigest() ) + '\n'
        printLabel = '"' + (l.strip()) + '",'
        printLabelmd5 = hashlib.md5(l.encode()).hexdigest() + ',' 
        printFastamd5 =  hashlib.md5(buildFasta.encode()).hexdigest()  + '\n'
        print("{}{}{}".format(printLabel, printLabelmd5, printFastamd5))
        buildFasta = ""
    else:
        buildFasta += l
print('==================')
fo = open("test-fasta-9-records.txt.out.txt", "w")
fo.write(build)
fo.close()
#print(build)
print(symbolArr)

'''
for i, l in enumerate(lines):
    print("Line {}: {}".format(i, l.strip()))

'''
f.close()

