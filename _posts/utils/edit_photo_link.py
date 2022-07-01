from os import listdir
import sys
#run with command line arg of filename (including extention) ex python3 edit_photo_link.py filename.md
# get list of all files in dir -> filter for .md files
# read file -> find line starting with ![] -> replace path with /assets/<filename>/<imagename>.img

def handleCommandLineArgs():
    # total arguments
    print(len(sys.argv))
    if(len(sys.argv)<=1):
        print("no command line arguments were found!")
        return False
    else:
        filename = sys.argv[1]
        print('Got filename from command line argument: ', filename)
        return filename



def isImageLink(line:str)-> bool:
    return line[:3] == "![]"

def correctLink(filename:str, line:str)->str:
    try:
        indexOfImageName = line.index("img/") + 4
    except ValueError as ve:
        print("could not find 'img/', returning same link")
        return line
    correctImageLink = f"![](/assets/{filename}/{line[indexOfImageName::]}"
    return correctImageLink

def processFile(filename:str):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for lineNumber,line in enumerate(lines):
        if(isImageLink(line)):
            print("old: " + line)
            print("new: " + correctLink(filename, line))
            lines[lineNumber] = correctLink(filename, line)
    
    with open(filename, 'w') as outputFile:
        outputFile.writelines(lines)

# processFile('2022-03-17-Feature-matching-using-BRISK-test.md')
def isMd(file:str)->bool:
    try:
        result = file.index(".md") or file.index(".markdown")
        return True
    except ValueError:
        print(f"{file} is not markdown file!")
        return False


filename = handleCommandLineArgs()
if(filename != False and isMd(filename)):
    processFile(filename)
# activate the following lines for batch processing all .md files in current directory
# filesInDir = listdir()
# markdownFiles = []
# for file in filesInDir:
#     if(isMd(file)):
#         markdownFiles.append(file)
# for file in markdownFiles:
#     processFile(file)