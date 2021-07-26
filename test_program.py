def get_info(file):
    characters = 0
    lines = 0
    chapter = 0
    FILE = open(file, "r+", encoding="utf8")
    res = open("test_results.txt", "a", encoding="utf8")

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

