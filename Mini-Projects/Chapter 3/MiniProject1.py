#Mini Project 1 — Student BACII Result Analyzer
#Processing
print("---Welcome BACII Grade Analyzer---")
print("")

while True:
    ch=input("Choose Class subject: ");
    if ch=="Science":
        print("+++ Enter Science Score +++")
        kh=float(input("1. Khmer (0-75): "))
        math=float(input("2. Math (0-125): "))
        bio=float(input("3. Biology (0-75): "))
        his=float(input("4. History (0-50): "))
        chem=float(input("5. Chemistry (0-75): "))
        Phy=float(input("6. Physic (0-75): "))
        Eng=float(input("7. English (0-50):"))
        if Eng>=25: Eng=Eng-25
        else: Eng=0
        total=kh+math+bio+his+chem+Phy+Eng
        if total>237: grade='E'
        elif total>=285: grade='D'
        elif total>=333: grade='C'
        elif total>=380: grade='B'
        elif total>=428: grade='A'
        else: grade='F'
        print(f"Total: {total} \nGrade: {grade}")
    elif ch=="Social Science":
        print("+++Enter Social Score")
        kh=float(input("1. Khmer (0-125):" ))
        math=float(input("2. Math (0-75): "))
        envir=float(input("3. Enviroment Sciecne (0-50): "))
        his=float(input("4. History (0-75): "))
        geo=float(input("5 Geography (0-75): "))
        moral=float(input("6. Moral Civics (0-75): "))
        Eng=float(input("7. English (0-50):"))
        if Eng>=25: Eng=Eng-25
        else: Eng=0
        total=kh+math+envir+his+geo+moral+Eng
        if total>237: grade='E'
        elif total>=285: grade='D'
        elif total>=332.5: grade='C'
        elif total>=380: grade='B'
        elif total>=428: grade='A'
        else: grade='F'
        print(f"Total: {total} \nGrade: {grade}")
    else: print("Wrong choice, try again!")
    test=input("type exit to leave: ")
    if test=='exit' : break 