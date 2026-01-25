#Chapter 8, Assignment 1

fav_mov=["1.Jujutsu Kaisen","2.Moonknight","3.Last Christmas ","4.The Witcher ","5.La La land"]
file_path="Movies List.txt"

with open(file_path,"w") as List:
    for mov in fav_mov:
        List.write(mov + "\n")

with open(file_path,"r") as name:
    movies=name.read()
    print("\n===Favorite Movie===\n")
    print(movies)