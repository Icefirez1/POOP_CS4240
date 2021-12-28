from sys import argv
def is_wanted_character(ch):
    return ch.isalnum() or ch == "'"
def sanitize_word(word):
    """prec word is a word
    postc:  lower case, get rid of unwanted characters.
    """
    out = ""
    word = word.lower()
    for letter in word:
        if is_wanted_character(letter):
            out += letter
    return out
def main():        
    input_file_name = argv[1]
    output_file_name = argv[1] + ".conc"
    items = {}
    with open(input_file_name, "r") as fp:
        for line in fp:
            words = line.split()
            for w in words:
                w = sanitize_word(w)
                if w in items:
                    items[w] += 1
                else:
                    items[w] = 1
    
    with open(output_file_name, "w") as fp:
        for k in sorted(items.keys()):
            fp.write(f"{k}\t\t {items[k]}\n")
    
if __name__ == "__main__":
    main()