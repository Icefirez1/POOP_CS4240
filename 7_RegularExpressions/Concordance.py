#__________Functions___________

#Sophia Dai 
#Al Pagar

# opening file 
# make a dictionary for words for each line 
# iterate thorugh each line and 
#first line we add each word to dictionary plus one 
# for the rest of the lines we iterate through the and check if each string in the dictionary
#   is in that line and if it isnt we add it to the dictionary plus 1
#   if the string is in the line we just plus one for that certain word 




from sys import argv
import re 


def sanitize(w): #This will remove every punctuation except ' 
    w = w.lower()
    return re.sub("[^\w\d'\s]+",'',w)

    return w.lower()
def outer(file, items):
    #__________This code gets the items and outputs them into and output file_____
    with open(file, "w") as fp:
        for k in sorted(items.keys()):
            fp.write(f"{k:30} {items[k]}\n")

def main():
    print("hello world")
    #____These iterate thorugh file and each word on line
    input_file_name = argv[1]
    output_file_name = argv[1] + ".conc"
    items = {} #concordance output
    with open(input_file_name, "r") as fp:
        for line in fp:
            words = line.split()
            for w in words:
                w = sanitize(w)
                if w in items:
                    items[w] += 1
                else:
                    items[w] =1 #this will add it to the dictionary


    #__________This code gets the items and outputs them into and output file_____
    outer(output_file_name, items)



#__________Main____________
if __name__ == "__main__":
    main()


