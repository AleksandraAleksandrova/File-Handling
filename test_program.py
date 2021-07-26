def get_info(file):
    characters = 0
    lines = 0
    chapter = 0
    FILE = open(file, "r+", encoding="utf8")
    res = open("test_results.txt", "a", encoding="utf8")

    for line in FILE:
        if line.find("CHAPTER") == 1:
            #ne vliza tuk nikoga
            chapter += 1
            lines = 1
        characters = len(line) 
        lines+=1 

        print("Chapter " + str(chapter) + " - line " + str(lines) + " - symbols " + str(characters) + "\n")
        res.write("Chapter " + str(chapter) + " - line " + str(lines) + " - symbols " + str(characters) + "\n")

    FILE.close()
    res.close()

get_info("short_text.txt")