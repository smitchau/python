print("=============================MAKE QUEZE============================")

dict1 = {}

for i in range(3):
    que = input(f"enter question :")
    ans = input("enter ans :")
    dict1.update({que:ans})

print(dict1)

print("=============================PLAY QUEZE============================")

count = 1
score = 0
for i in dict1:
    print(f'Queze {count} : {i}')
    user = input("ENTER ANS : ")

    if user == dict1[i]:
        score += 5
        print("your score is : ",score)
    else:
        score -= 10
        print("your score is : ",score)

    count += 1
