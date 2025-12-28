# for checking the type of any data:
integer = 1
float_num = 1.0
string = "Hello World"

type(string)
type(integer)
type(float_num)

# ----| for example and showing:
print(type(integer))
print(type(float_num))
print(type(string))

# some useful string methods in python:
name = "mahan"

upper = name.upper() #this makes string uppercase like: mahan -> MAHAN
lower = name.lower() #this makes string lowercase like: MAHAN or Mahan -> mahan

# ----| for check is lower or upper:
check_isLower = lower.islower() #for checking lowercase
check_isupper = upper.isupper() #for checking uppercase


# replace method:
question = "Are You a Python String?"

q_result = question.replace("?", "!")

print(question, q_result)


# split method:
likes = "pizza, programming, iran, family, game, python"

split_res = likes.split(", ")
print(split_res)


# **** methods don't change the original value and just return a value
