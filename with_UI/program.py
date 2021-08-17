"""
- по един обект за всяка глава, но не различни
- в обект за глава да са : номера на главaта, името на главата и текста на главата 
- първия прозорец да е за избиране на пътя към файла - QFileDialog.getOpenFileName
- след зареждане на файла да има бутон процес или нещо такова 
- после да има втори прозорец който да представлява tree view с root-ове главите и да излиза текста при плюса
"""
class Chapter:
    number = 0
    name = ""
    text = ""


def get_info(file):
    FILE = open(file, "r", encoding="utf8")
    text = FILE.read()
    text = text[text.find("CHAPTER I.\nDown the Rabbit-Hole"):]
    text = text[:text.find("*** END OF THE PROJECT GUTENBERG EBOOK ALICE’S ADVENTURES IN WONDERLAND ***")]
    FILE.close()

    for line in text:
        if line.find("CHAPTER") !=-1:
            


get_info("text.txt")