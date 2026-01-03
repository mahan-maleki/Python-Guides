def hello():
    print("Hello World !")

hello()


def greet(name):
    '''
    this function will greet the user with the given name
    :param name:
    :return:
    '''
    print(f"Hello, {name}!")

greet("Mahan")


def sum_two_num(a, b):
    return a + b

sum_two = sum_two_num(2, 9)
print(sum_two)