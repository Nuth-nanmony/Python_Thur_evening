#Mini Project 1 — Student BACII Result Analyzer with function (V1)
#Input Viraible 
def info():
    ch = input("Choose Class Subject(Science or Social): ")
    if ch=="Science":
        print("+++ Enter Science SCore+++")
        kh=float(input("1. Khmer (0-75): "))
        math=float(input("2. Math (0-125): "))
        bio=float(input("3. Biology (0-75): "))
        his=float(input("4. History (0-50): "))
        chem=float(input("5. Chemistry (0-75): "))
        phy=float(input("6. Physic (0-75): "))
        eng=float(input("7. English (0-50): "))
        if eng>=25:
            eng=eng-25
        else: 
            eng=0
        total=kh+math+bio+his+chem+phy+eng
        return total
    elif ch=="Social":
        print("+++Enter Social Score")
        kh=float(input("1. Khmer (0-125): " ))
        math=float(input("2. Math (0-75): "))
        envir=float(input("3. Enviroment Sciecne (0-50): "))
        his=float(input("4. History (0-75): "))
        geo=float(input("5 Geography (0-75): "))
        moral=float(input("6. Moral Civics (0-75): "))
        eng=float(input("7. English (0-50):"))
        if eng>=25:
            eng=eng-25
        else: 
            eng=0
        total=kh+math+envir+his+geo+moral+eng
        return total
    else: print("Error input")
    return print("Try again!")
#processing  
def grade_cal (total):
    if total >= 237:
        return 'E'
    elif total >=285: 
        return 'D'
    elif total >=333: 
        return 'C'
    elif total >=380: 
        return 'B'
    elif total >=428: 
        return 'A'
    else: return'F'
#Main (output)
Total=info()
Grade=grade_cal(Total)
print (f"Total: {Total} \nGrade: {Grade} ")