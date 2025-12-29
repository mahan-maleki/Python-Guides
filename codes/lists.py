my_list = [0, 1, 2, 3, 4]
values = ["Hello", "Hi", 1, -1, 3.14576, True]

print(my_list)
print(values)
print(values[0])
print(len(my_list))
print(len("Hello World ! How are You ?"))

greeting = "Hello World ! How are You ?"

print(greeting.count("H"))

last_number = my_list.pop()
print(last_number)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(values)

values.remove("Hi")
print(values)