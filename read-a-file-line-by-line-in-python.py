 # https://stackabuse.com/read-a-file-line-by-line-in-python
import hashlib 
import sys
import os

def main():
   filepath = sys.argv[1]
   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   with open(filepath) as fp:
       build = ""
       for i, line in enumerate(fp):
            if isFirst(i, line):
                print(line.strip())
                print(getHash(i,line))
            elif not isAngle(i,line):
               build += line.strip()
               print("{} ::: {}".format(i, len(build)))
            elif isAngle(i, line):
                print(getHash(i,build))
                build = ""
                print(line.strip())
                print(getHash(i, line))
            else:
                print(i)



#           print(line.strip()) if isFirst(i, line)  else print(i)  TERNARY IF no questionMark
            
   bag_of_words = {}
   with open(filepath1) as fp:
       for line in fp:
           record_word_cnt(line.strip().split(' '), bag_of_words)
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   print("Most frequent 10 words {}".format(sorted_words[:10]))
  
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
        return "true"

def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1

if __name__ == '__main__':
    main()
