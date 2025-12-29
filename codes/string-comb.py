# basic way to combine some strings together:
name = "mahan"
family_name = "maleki"

print("Hello" + " " + name + " " + family_name)

# other old way to do this:
age = 16
float_num = 3.14

greeting = "Hello %s %s. your age is %i . this is a float number -> %f" % (name, family_name, age, float_num)
print(greeting)

# format string way:
format_method = "Hello {} {}. you are {}.".format(name, family_name, age)
print(format_method)

pro_format_method = "Hello {name} {family}. you are {sen:1.1f}.".format(name=name, family=family_name, sen=float_num)
print(pro_format_method)

# f string method:

f_string = f"Hello {name} {family_name}. you are {float_num:1.1f} years old."
print(f_string)