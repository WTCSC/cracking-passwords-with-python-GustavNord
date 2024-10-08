# Imports argparse and hashlib
import argparse
import hashlib
# Defines parser to go through the file and scans each line.
parser = argparse.ArgumentParser()
# Scans through pswfile and dict and adds arguments to them.
parser.add_argument('pswfile')
parser.add_argument('dict')
# Defines args as scanning through the two files.
args = parser.parse_args()
# Opens both files in read mode and will scan the txts.
passwords = open(args.pswfile, "r")
word_list = open(args.dict, "r")
# Reads each line in each file.
password_split = passwords.readlines()
word_split = word_list.readlines()
# Creates a for loop with hash in the file that has split the passwords from each username by splitting it via the ':'.
for hash in password_split:
    hash = hash.split(":")
    # Creates another for loop for password in the word_split.
    for password in word_split:
        # Creates an if statment that if it can be hashed by sha256, then deletes all white lines, encode all passwords into sha256, turns it into a string, and compares the now hashed words with the passwords.
        if hashlib.sha256(password.strip().encode()).hexdigest() == hash[1].strip():
            # Prints the solved passwords.
            print(f'{hash[0]}:{password.strip()}')
