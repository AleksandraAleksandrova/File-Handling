"""
- по един обект за всяка глава, но не различни
- в обект за глава да са : номера на главaта, името на главата и текста на главата 
- първия прозорец да е за избиране на пътя към файла - QFileDialog.getOpenFileName
- след зареждане на файла да има бутон процес или нещо такова 
- после да има втори прозорец който да представлява tree view с root-ове главите и да излиза текста при плюса
"""


class Chapter:
    def __init__(self, chapter):
        self.chapter = chapter
        self.name = None
        self.text = []

    def append_chapter_text(self, text):
        self.text.append(text)

    def set_name(self, name):
        self.name = name


def read_file(chapters):
    start_read = False
    read_chapter_name = False

    with open("text.txt", 'r', encoding="utf8") as inp:
        for index, line in enumerate(inp):
            if line.startswith('CHAPTER'):
                if start_read:
                    chapters.append(chapter_object)
                start_read = True
                read_chapter_name = True
                chapter_object = Chapter(line)
            elif line.startswith('THE END'):
                start_read = False
            elif read_chapter_name:
                chapter_object.set_name(line)
                read_chapter_name = False
            elif start_read:
                chapter_object.append_chapter_text(line)


if __name__ == '__main__':
    chapters = []
    read_file(chapters)

    for elem in chapters:
        print(elem.chapter)
        print(elem.name)
        print(elem.text)
