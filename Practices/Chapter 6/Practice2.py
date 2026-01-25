scores = {"Alice":90 , "Bob":85 , "Charlie":92}

for name,score in scores.items():
    if score > 85:
        print(name,score)

scores["Ny"] =  87
scores["Bob"] = 88

print(f"\nUpdate \n{scores}")