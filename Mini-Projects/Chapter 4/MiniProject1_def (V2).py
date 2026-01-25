#Mini Project 1 — Student BACII Result Analyzer with function (V2)
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
        if eng>=25: eng=eng-25
        else: eng=0
        Total=kh+math+bio+his+chem+phy+eng
        return kh,math,bio,his,chem,phy,eng,Total
    elif ch=="Social":
        print("+++Enter Social Score")
        kh=float(input("1. Khmer (0-125): " ))
        math=float(input("2. Math (0-75): "))
        envir=float(input("3. Enviroment Sciecne (0-50): "))
        his=float(input("4. History (0-75): "))
        geo=float(input("5 Geography (0-75): "))
        moral=float(input("6. Moral Civics (0-75): "))
        eng=float(input("7. English (0-50):"))
        if eng>=25: eng=eng-25
        else: eng=0
        Total=kh+math+envir+his+geo+moral+eng
        return kh,math,envir,his,geo,moral,eng,Total
    else: print("Error input")
    return print("Try again!")
#processing
def grade_cal (Grade):
    if Grade >=428: return 'A'
    elif Grade >=380: return 'B'
    elif Grade >=333: return 'C'
    elif Grade >=285: return 'D'
    elif Grade >=237: return 'E'
    else: return 'F'
def grade_subject_125(score):
    #math,kh
    if score>=125: return 'A'
    elif score>=100 : return 'B'
    elif score>=87.5 : return 'C'
    elif score>=75 : return 'D'
    elif score>=62.5 : return 'E'
    else: return 'F'
def grade_subject_75(score):
    #kh,bio,chem,phy,math,his,geo,moral
    if score>=75: return 'A'
    elif score>=60 : return 'B'
    elif score>=52.5 : return 'C'
    elif score>=45 : return 'D'
    elif score>=37.5 : return 'E'
    else: return 'F'
def grade_subject_50(score):
    #his,eng,envir
    if score>=50: return 'A'
    elif score>=40 : return 'B'
    elif score>=35 : return 'C'
    elif score>=30 : return 'D'
    elif score>=25 : return 'E'
    else: return 'F'
#Main (output)
#Note new datatype using []
'''
Example: Result=kh[0],math[1],bio[1],his[2],chem[3],phy[4],eng[5],total[6 or -1]
        Result=(60),(125),(50),(50),(75),(75),(50),(485)
'''
Result=info()
kh=Result[0];Total=Result[-1]
if kh <=75:
    math,bio,his,chem,phy,eng=Result[1:-1]
    print (f"Total: {Total:<20} Grade: {grade_cal(Total)}")
    print (f"Khmer: {kh:<20} Grade: {grade_subject_75(kh)}")
    print (f"Math: {math:<20} Grade: {grade_subject_125(math)}")
    print (f"Biology: {bio:<20} Grade: {grade_subject_75(bio)}")
    print (f"History: {his:<20} Grade: {grade_subject_50(his)}")
    print (f"Chemistry: {chem:<20} Grade: {grade_subject_75(chem)}")
    print (f"Physic: {phy:<20} Grade: {grade_subject_75(phy)}")
    print (f"English: {eng:<20} Grade: {grade_subject_50(eng)}")
else:
    math,envir,his,geo,moral,eng=Result[1:-1]
    print (f"Total: {Total:<20} Grade: {grade_cal(Total)}")
    print (f"Khmer: {kh:<20} Grade: {grade_subject_125(kh)}")
    print (f"Math: {math:<20} Grade: {grade_subject_75(math)}")
    print (f"Enviroment Science: {envir:<20} Grade: {grade_subject_50(envir)}")
    print (f"History: {his:<20} Grade: {grade_subject_75(his)}")
    print (f"Georaphy: {geo:<20} Grade: {grade_subject_75(geo)}")
    print (f"Moral Civics: {moral:<20} Grade: {grade_subject_75(moral)}")
    print (f"English: {eng:<20} Grade: {grade_subject_50(eng)}")