f = open("data-types.py")

print(f.read())
print(f.read())

f.seek(0)

print(f.read())
print(f.readlines())

f.close()

with open("data-types.py") as f:
    print(f.read())
    print(f.readlines())