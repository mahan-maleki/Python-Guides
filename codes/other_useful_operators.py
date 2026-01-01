for i in range(10):
    print(i)

for i in range(6):
    for j in range(6):
        print(i, j)

l = ["jadi", 5, "sara"]

print(enumerate(l))

for i, a in enumerate(l):
    print(i, a)

esm = ['mahan', 'jadi', 'ali']
famil = ['maleki', 'mir', 'godarz']

for x in zip(esm, famil):
    print(x)

print('mahan' in esm)

print(max(1, 2, 6, 4, 3, 5))
print(min(1, 2, 6, 0, 4, 3, 5))

# random number :

from random import randint

print(randint(1, 6))    # it's like a dice