def format_text_file(file):
    FILE = open(file, "r+", encoding="utf8")
    text = FILE.read()
    text = text[text.find("CHAPTER I.\nDown the Rabbit-Hole"):]
    text = text[:text.find("*** END OF THE PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***")]
    FILE.close()

    return(text)

def add_to_res_file(num_of_lines, num_of_chars):
    file = open("results.txt", "w")
    
    file.write("Number of lines: ")
    file.write(str(num_of_lines))

    file.write("Number of characters: ")
    file.write(str(num_of_chars))

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
    FILE = open(data, "r")
    #във for цикъл да се броят всички линии и знаци
    text = FILE.read()
    for char in text:
        if char != "\n":
            characters +=1
        lines +=1

text = format_text_file("short_text.txt")
print(text)
#num_of_lines = find_num_of_lines("text.txt")
#num_of_chars = find_num_of_chars("text.txt")
#add_to_res_file(num_of_lines, num_of_chars)


#I SHOULD SEE THIS 
"""
CHAPTER I.
Down the Rabbit-Hole


Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do: once or twice she had peeped into
the book her sister was reading, but it had no pictures or
conversations in it, “and what is the use of a book,” thought Alice
“without pictures or conversations?”

Lastly, she pictured to herself how this same little sister of hers
would, in the after-time, be herself a grown woman; and how she would
keep, through all her riper years, the simple and loving heart of her
childhood: and how she would gather about her other little children,
and make _their_ eyes bright and eager with many a strange tale,
perhaps even with the dream of Wonderland of long ago: and how she
would feel with all their simple sorrows, and find a pleasure in all
their simple joys, remembering her own child-life, and the happy summer
days.

THE END 
"""