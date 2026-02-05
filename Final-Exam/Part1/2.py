#Write a program that count

fp="Final-Exam/Part1/students.txt"

with open(fp,"r") as name:
    student=name.read()
    total_words = len(student.split())

print(f"""
    Program Count line
    1. Total line: {len(student)}
    2. Total words: {total_words}
    """
)
