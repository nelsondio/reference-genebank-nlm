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
        print(  l   )
        print(hashlib.md5(l.encode()).hexdigest() + ' ')
        build += '"' + l.strip() + '",' +  hashlib.md5(l.encode()).hexdigest() + ','
    elif i <  symbolArr[1] :
        buildFasta += l
        
    elif i == symbolArr[1]:
        print(buildFasta)
        print( hashlib.md5(buildFasta.encode()).hexdigest() + '\n')
        print(len(buildFasta))
        build += hashlib.md5(buildFasta.encode()).hexdigest() + '\n'
        buildFasta = ""

    elif l[0] == '>':
        print("##############")
        build +=  '"' + l.strip() + '",' + hashlib.md5(l.encode()).hexdigest()  + ','
        build += (hashlib.md5(buildFasta.encode()).hexdigest() ) + '\n'
        print(l)
        print(hashlib.md5(l.encode()).hexdigest() + ' ' + hashlib.md5(buildFasta.encode()).hexdigest() )
        buildFasta = ""
    else:
        buildFasta += l
print('==================')
fo = open("short.out.txt", "w")
fo.write(build)
fo.close()
print(build)
print(symbolArr)

'''
for i, l in enumerate(lines):
    print("Line {}: {}".format(i, l.strip()))

'''
f.close()

