import os
import hashlib
import json

def hashFile(filePath):
    with open(filePath, "rb") as file:
        data = file.read()
        fileHash = hashlib.sha256(data).hexdigest()
        return fileHash

def hashMaking():

    directory = input("Enter directory path: ")

    files = os.listdir(directory)
    fileHashes = {}


    for x in files:
        if os.path.isfile(os.path.join(directory, x)):
            fileHashes[os.path.join(directory, x)] = hashFile(os.path.join(directory, x))  
    
    with open("fileHashes.json", "w") as file:
        json.dump(fileHashes, file, indent=3)

    print("Hash table generated")

def validateHash():
    directory = input("Enter directory path: ")

    modCount = 0
    newCount = 0
    newFiles = []    
    delCount = 0
    delFiles = []

    with open("fileHashes.json", "r") as file:
        savedHashes = json.load(file)
    
    files = os.listdir(directory)

    

    for x in files:
        filePath = os.path.join(directory, x)

        if os.path.isfile(os.path.join(directory, x)) and x != "fileHashes.json":
            currentHash = hashFile(filePath)

            
            if filePath in savedHashes:
            
                if currentHash == savedHashes[filePath]:
                    print(f"{filePath} hash is valid \n")
                else:
                    print(f"{filePath} hash is invalid \n")
                    modCount += 1
            else:
                
                newCount += 1
                newFiles.append(filePath)


    for x in savedHashes:
            if not os.path.isfile(x):
                
                delCount += 1
                delFiles.append(x) 

    for newFile in newFiles:
        for delFile in delFiles:
            if delFile in savedHashes:  
                if hashFile(newFile) == savedHashes[delFile]:
                    newCount -= 1
                    delCount -= 1
                    savedHashes[newFile] = savedHashes[delFile]
                    savedHashes.pop(delFile)
                    print(f"{newFile} has been replaced with {delFile} \n")
                    break
            
    for newFile in newFiles:
        if newFile not in savedHashes:
            print(f"{newFile} is New \n")

    for delFile in delFiles:
        if delFile in savedHashes:
            print(f"{delFile} has been deleted \n")

    with open("fileHashes.json", "w") as file:
                    json.dump(savedHashes, file, indent=3)


    if modCount == 0 and newCount == 0 and delCount == 0:
        print("No problems found")
    else:
        if modCount == 1:
            print("Found 1 modified file \n")
        elif modCount > 1:
            print(f"Found {modCount} modified files \n")
            
        if newCount == 1:
            print("Found 1 new file \n")
        elif newCount > 1:
            print(f"Found {newCount} new files \n")
        
        if delCount == 1:
            print("Found 1 deleted file")
        elif delCount > 1:
            print(f"Found {delCount} deleted files")
        

def choice():
    num = input("Please choose 1 if you wish to make a hash table or 2 if you wish to verify your table: ")
    while num != "1" and num != "2":
        print("Please try again")
        num = input("Please choose 1 or 2: ")

    return num 

def main():    

    chosen = choice()

    if chosen == "1":
        hashMaking()
    elif chosen == "2":
        validateHash()

main()



