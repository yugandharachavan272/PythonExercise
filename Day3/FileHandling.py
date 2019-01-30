# Wap to accept a file name and directory name from user and create a backup of this file in same directory
import glob, os, shutil
# print os.getcwd()
# os.makedirs("test")
# path = os.getcwd()
# print os.listdir(path)

def word_count(str):
    counts = dict()
    wordslis = str.split()

    for word in wordslis:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

curDir = os.curdir
# print curDir
bkpDir = os.path.join(os.curdir, "Archiv")
# print "bkpDir ", bkpDir
if not os.path.exists(bkpDir):
    os.makedirs(bkpDir)

fileName = raw_input("Enter file name : ")
dirName = raw_input("Enter directory name: ")

files = glob.iglob(os.path.join(dirName, fileName))
if files:
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, bkpDir)
            # Wap to find out total no of lines total no of words total no of characters in file
            with open(file) as infile:
                lines = 0
                words = 0
                characters = 0
                for line in infile:
                    wordslist = line.split()
                    lines = lines + 1
                    words = words + len(wordslist)
                    characters += sum(len(word) for word in wordslist)
            print("lines : ", lines)
            print("words : ", words)
            print("characters : ", characters)

            # Wap to convert each n every word in upper case in file
            with open(file, 'r') as f:
                text = f.read()
                f.seek(0)
                with open(file, 'a') as fw:
                    fw.write(text.upper())
                    fw.truncate()

            # Wap to convert the content of files in reverse order.

            with open(file) as f:
                print f.readlines()[::-1]
                with open(file, 'a') as frv:
                    frv.writelines(" REVERSE TEXT OF FILE IS :\n")
                    frv.writelines(reversed(f.readlines()))
                    # frv.writelines(f.readlines()[::-1])
            # Find count of each and every word in file
            with open(file) as f:
                filetext = f.readlines()
                print type(filetext)
                print(word_count(str(filetext)))

        else:
            print "Their is no such file exist in entered directory."
    else:
        print "For else"
else:
    print "Their is no such file exist in entered directory."

# Wap to find out count of all the python files in any specific directory and subdirectory

files = glob.iglob(os.path.join(dirName,  "*.py"))
count= 0
if files:
    for file in files:
        if os.path.isfile(file):
            count += 1
    else:
        print " COUNT ", count




