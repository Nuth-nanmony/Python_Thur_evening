#practices 2
def p2():
    scores=[]
    for i in range(5):
        num=float(input("Enter Score: "))
        scores.append(num)

    for j in range(len(scores)):
        print(f"{j+1}.Student Score: {scores[j]}")

    print("Total: ",sum(scores))
    print("Average: ",sum(scores)/len(scores))
    print("Highest: ",max(scores))
    print("Lowest: ",min(scores))
p2()