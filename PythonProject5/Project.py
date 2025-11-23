"""
Author: Bracha Glazer
Professor: Professor Spiegel-Cohen
Homework: Module 9- HW Class 9 File I/O Part 1
Project: Create a file and write a poem into it. Read the file and write the backwards poem into another file. Read the
    backwards file and append to the second file why this poem is a favorite and the author's name.
Thank you!
"""


import os


def create():
    """Create a new text file, poem.txt, within the docs folder."""
    with open(path1, "w") as f:  # file doesn't exist so this will create the file.
        f.write("Hope by Emily Dickinson: \n"
                "HOPE is the thing with feathers \n"
                "That perches in the soul, \n"
                "And sings the tune without the words, \n"
                "And never stops at all, \n"
                "And sweetest in the gale is heard; \n"
                "And sore must be the storm \n"
                "That could abash the little bird \n"
                "That kept so many warm. \n"
                "I've heard it in the chillest land, \n"
                "And on the strangest sea; \n"
                "Yet, never, in extremity, \n"
                "It asked a crumb of me. \n")


def read(file):
    """Create a list and append each line, from the file provided, to the list. Read the list."""
    with open(file, "r") as f:
        for line in f:
            line = line.strip()  # strip white spaces
            poem.append(line)  # append each line of the text file to the list
            print(line)
        print()


def write():
    """Create a new text file, poem2.txt, within the docs folder. Write in each list entry backwards."""
    with open(path2, "w") as f:
        for stanza in reversed(poem):  # for each entry in the list from last to first
            f.write(f"{stanza} \n")  # write poem backwards into the file


def app():
    """Append text to the poem2.txt file."""
    with open("docs/poem2.txt", "a") as f:
        f.write("My name is Bracha Glazer.\n")
        f.write("I like this poem because it brings back memories of high school, when I first heard this poem.")


if __name__ == "__main__":
    path1 = os.path.join("docs","poem.txt")  # make it usable on any general computer
    path2 = os.path.join("docs","poem2.txt")
    poem = []
    create()
    read(path1)
    write()
    read(path2)
    app()