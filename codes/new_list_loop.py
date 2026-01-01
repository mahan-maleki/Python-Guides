l = [0, 3.14, 523, 345]

# this is a normal way to do it:
first_new_l = []

for n in l:
    first_new_l.append(n * 2)

print(first_new_l)

# this is a faster way to do it:
second_new_l = [x * 2 for x in l]
print(second_new_l)

# condition example of this way:
adad = 5

res = "Fard" if adad % 2 != 0 else "Zoj"
print(res)