def format_text_file(file):
    FILE = open(file, "r+", encoding="utf8")
    text = FILE.read()
    text = text[text.find("CHAPTER I.\nDown the Rabbit-Hole"):]
    FILE.close()

    return(text)

text = format_text_file("short_text.txt")
print(text)