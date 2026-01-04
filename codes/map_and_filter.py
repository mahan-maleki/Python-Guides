def tavan_2(x):
    return x ** 2

a = [1,3,6,4,8,5]

tavan_a = map(tavan_2, a)

print(list(tavan_a))



b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

only_even = filter(lambda x: x % 2 == 0, b)

print(list(only_even))