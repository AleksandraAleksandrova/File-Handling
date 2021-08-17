class Chapter:
    number = 0
    name = ""
    text = ""


def get_info(file, chapters):
    FILE = open(file, "r", encoding="utf8")
    text = FILE.read()
    text = text[text.find("CHAPTER I.\nDown the Rabbit-Hole"):]
    text = text[:text.find("*** END OF THE PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***")]
    FILE.close()

    element = 0
    new_chapter = 0

    for line in text:
        if line.find("CHAPTER") !=-1:
            print("here\n")
            chapters[element].number = element + 1
            element +=1
            new_chapter = 1
        if new_chapter==1:
            chapters[element-1].name = text.readline()
            new_chapter = 0
        else:
            chapters[element].text = text.readline()

    
    print(chapters[0].name) 
    #Down the Rabbit-Hole
    print(chapters[1].number)
    #2
    print(chapters[1].name)
    #The Pool of Tears

chapters = [Chapter for _ in range (3)]
get_info("test_text.txt", chapters)