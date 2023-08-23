import pyzipper
import sys
from tqdm import tqdm
from time import sleep


file = input(str("Enter Your ZIP File: "))
wordlist = input(str("Enter Your Wordlist TXT: "))

if ".txt" in wordlist and ".zip" in file:
    print("Wait for an Minute")
    sleep(2)
    fileobject = pyzipper.AESZipFile(file)
    count = len(list(open(wordlist, "rb")))

    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=count, unit="word"):
            try:
                fileobject.pwd = word.strip()
                fileobject.extractall()
            except:
                print("Trying Password: ", word.decode().strip())
                continue
            else:
                print("PASSWORD FOUND: ".center(20, ' '))
                print("\n", word.decode().strip())
                break
    print("No password Found.")
else:
    print("Wrong Entry!")
    print("Exiting...")
    sys.exit(0)
