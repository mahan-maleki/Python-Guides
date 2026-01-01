for _ in [1, 2, 3, 4, 5]:
    pass

for a in [1, 2, 3, 4, 5]:
    if a == 3:
        break
    print(a)

print("I'm done !")

for a in [1, 2, 3, 4, 5]:
    if a == 3:
        continue
    else:
        print(a)