def format_text_file(file):
    FILE = open(file, "r+", encoding="utf8")
    text = FILE.read()
    text = text[text.find("CHAPTER I.\nDown the Rabbit-Hole"):]
    text = text[:text.find("*** END OF THE PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***")]
    FILE.close()

    FILE = open(file, "w", encoding="utf8")
    FILE.write(text)
    FILE.close()

def add_to_res_file(num_of_lines, num_of_chars):
    FILE = open("results.txt", "w")
    
    FILE.write("Number of lines: ")
    FILE.write(str(num_of_lines))
    FILE.write("\n")
    FILE.write("Number of characters: ")
    FILE.write(str(num_of_chars))
    FILE.write("\n")

    FILE.close()

def find_num_of_lines(file):
    num_of_lines = 0

    FILE = open(file, "r", encoding="utf8")
    for line in FILE:
        num_of_lines +=1
    FILE.close()

    print("Number of lines: ", num_of_lines)
    return num_of_lines

def find_num_of_chars(file):
    num_of_chars = 0

    FILE = open(file, "r", encoding="utf8")
    text = FILE.read()
    num_of_chars = len(text)
    FILE.close()

    print("Number of chars: ", num_of_chars)
    return num_of_chars

def get_info(file):
    characters = 0
    lines = 0
    chapter = 0
    FILE = open(file, "r+", encoding="utf8")
    res = open("results.txt", "a", encoding="utf8")

    for line in FILE:
        #liniq po liniq
        if line.find("CHAPTER") == 1:
            #ako e nova glava resetira line i broi glavite
            chapter += 1
            lines = 1
        characters = len(line) #broi znacite
        lines+=1 #broi redovete

        #printira v terminala
        print("Chapter " + str(chapter) + " - line " + str(lines) + " - symbols " + str(characters) + "\n")
        #slaga v results.txt
        res.write("Chapter " + str(chapter) + " - line " + str(lines) + " - symbols " + str(characters) + "\n")

    FILE.close()
    res.close()
            
#format_text_file("text copy.txt")
#num_of_lines = find_num_of_lines("text copy.txt")
#num_of_chars = find_num_of_chars("text copy.txt")
#add_to_res_file(num_of_lines, num_of_chars)
#get_info("text.txt")