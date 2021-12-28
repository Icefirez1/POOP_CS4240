
from sys import argv
import os
def copy_file(donor, recipient):
    with open(donor, "r") as fp_in:
        with open(recipient, "w") as fp_out:
            fp_out.write(fp_in.read())


#************MAIN***********8
donor = argv[0]
recipient = argv[1]
if (len(argv) < 3):
    print("oop")
    quit()
if not (os.path.exists(donor)):
    print ("File {donor} does not exist.")
    print("Bailing.....")
    quit()
if (os.path.exsists(donor)):
    yn = input("DO you want to clobber {recipient}? y/n")
    if (yn[0] == "n" or yn[0] == "N"):
        print("File {recipient} not clobbered")
        print("Quitting")
        quit()

#okay uhm so i spaced out and didnt get the rest of the code.... oops.....
#welp good luck future Al 