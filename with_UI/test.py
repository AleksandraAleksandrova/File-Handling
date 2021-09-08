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

    new_chapter = 0
    element = 0

    for line in text.splitlines():
        if line.find("CHAPTER") !=-1:
            #not working
            #overwrites 1 with 2 then with 3 in all positions
            chapters[element].number = element + 1
            print(chapters[element].number)
            element = element + 1
            new_chapter = 1
            continue
        if new_chapter==1:
            chapters[element-1].name = line
            print(chapters[element-1].name)
            new_chapter = 0
            continue
        else:
            chapters[element-1].text = chapters[element-1].text + line


chapters = [Chapter for _ in range (3)]
get_info("test_text.txt", chapters)