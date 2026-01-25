fruit = True
while fruit:
    fruits=["Apple","Banana","Orange","StarFruit","Graph"]
    fruits[2] = "Pineapple"
    fruits.extend(["Coconut","Mango"])
    for num in range(1,11):
        print (num,fruits)
    ch=input("Chose the right fruit: ")
    if ch.lower() == 'mango': 
        fruit = False
    else: True