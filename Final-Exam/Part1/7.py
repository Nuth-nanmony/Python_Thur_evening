#View Record

import pyodbc

path="Final-Exam/Part1/school.accdb"

db= (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    rf"DBQ={path};"
)

try:
    conn=pyodbc.connect(db)
    cursor=conn.cursor()
    cursor.execute("SELECT StudentID, [Name], Age, Course FROM Students")
    rows = cursor.fetchall()
    if rows:
        print(
        f"""
                Students Display\n
        {'ID':<5}{'Name':<20}{'Age':<5}{'Course':<15} 
        """)
        for row in rows:
            print(
        f"""
        {row.StudentID:<5}{row.Name:<20}{row.Age:<5}{row.Course:<15}
        """)
    else:print("No Record")

except pyodbc.Error as e:
    print("Error Display")
    print(e)
conn.close()