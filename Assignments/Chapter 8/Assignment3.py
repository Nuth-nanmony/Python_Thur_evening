#Chapter 8, Assignment 3
"""Run Assignment2 first"""

file_path="students.txt"

def loganalyze(file_path):
    with open(file_path,"r") as log:
        text=log.read()
    
    lines=text.splitlines()
    word=text.split()
    char=len(text)

    print(f"Log Results\n=================\nTotal Lines: {len(lines)}\nTotal words: {len(word)}\nTotal Characters: {char}")

loganalyze(file_path)
