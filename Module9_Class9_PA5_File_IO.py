"""
import os
import sys


def create() to create a new file to hold the poem
    try:
        use with open to write in the poem
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
    except FileNotFoundError as err just in case
        print an error message
        exit


def read() to read the poem to the screen and create a list with the lines
    try:
        use with open in read mode
            for every line in the file:
                .strip() the line of all whitespaces
                append(line) append each line of the text file to the list
                print each line
            print()
    except FileNotFoundError as err just in case
        print an error message
        exit


def write() to create a new file that will change and reverse the poem
    try:
        use with open for the second file in w mode
            poem_edit = a new empty list
            for each line in the old list
                update each line = line.replace("And", "&")
                poem_edit.append(line) - append the updated lines to the new list
            for each entry in the new list reverse the list - reversed(poem_edit)
                f.write(stanza) -  write the poem backwards into the file
            print the updated poem to the screen
    except FileNotFoundError as err just in case
        print an error message
        exit


def read2() to read the second text file
    try:
        use with open in read mode
            for each line in the file
                read the line
    except FileNotFoundError as err just in case
        print an error message
        exit


def app() to append text to the poem_remix.txt file
    try:
        use with open in a mode
            append "Remixed by: Bracha Glazer.\n" to the second file
            append "I changed the word 'and' to '&' and reversed the lines."
    except FileNotFoundError as err just in case
        print an error message
        exit


if __name__ == "__main__" to call all functions and run the program.
    path1 = os.path.join("docs","poem_original.txt")  # make it usable on any general computer
    path2 = os.path.join("docs","poem_remix.txt")
    poem = []
    create()
    read()
    write()
    read2()
    app()
"""


import os
import sys


def create():
    """Create a new text file, poem_original.txt, within the docs folder."""
    try:
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
    except FileNotFoundError as err:
        print("File not found", err)
        sys.exit(1)


def read():
    """Create a list and append each line, from the file provided, to the list. Print each line."""
    try:
        with open(path1, "r") as f:
            for line in f:
                line = line.strip()  # strip white spaces
                poem.append(line)  # append each line of the text file to the list
                print(line)
            print()
    except FileNotFoundError as err:
        print("File not found", err)
        sys.exit(1)

def write():
    """Create a new text file, poem_remixed.txt, within the docs folder. Change all 'and' and write in each list entry backwards."""
    try:
        with open(path2, "w") as f:
            poem_edit = []
            for line in poem:
                line = line.replace("And", "&")  # replace if 'and' exists in the line
                poem_edit.append(line)  # append the updated lines to a new list
            for stanza in reversed(poem_edit):  # for each entry in the list from last to first
                f.write(f"{stanza} \n")  # write poem backwards into the file
            print(reversed(poem_edit))
    except FileNotFoundError as err:
        print("File not found", err)
        sys.exit(1)

def read2():
    """Read each line of the text file."""
    try:
        with open(path2, "r") as f:
            for line in f:
                f.read(line)
    except FileNotFoundError as err:
        print("File not found", err)
        sys.exit(1)

def app():
    """Append text to the poem_remix.txt file."""
    try:
        with open(path2, "a") as f:
            f.write("Remixed by: Bracha Glazer.\n")
            f.write("I changed the word 'and' to '&' and reversed the lines.")
    except FileNotFoundError as err:
        print("File not found", err)
        sys.exit(1)


if __name__ == "__main__":
    path1 = os.path.join("docs","poem_original.txt")  # make it usable on any general computer
    path2 = os.path.join("docs","poem_remix.txt")
    poem = []
    create()
    read()
    write()
    read2()
    app()