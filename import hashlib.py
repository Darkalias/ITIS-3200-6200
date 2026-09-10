import os
import hashlib
import json
 

def hashFile(filePath):
    with open(filePath, "rb") as file:
        data = file.read()
        fileHash = hashlib.sha256(data).hexdigest()
        return fileHash

directory = input("Enter directory path: ")

files = os.listdir(directory)
fileHashes = {}


for x in files:
    if os.path.isfile(os.path.join(directory, x)):
        fileHashes[x] = hashFile(os.path.join(directory, x))  
with open("fileHashes.json", "w", indent=3) as file:
    json.dump(fileHashes, file)


