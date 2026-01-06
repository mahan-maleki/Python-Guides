# for making a module and use it in other file you should have a directory like this:

#    Project-Folder
#        |
#        |----   mymod.py
#        |------   myprogram.py

# "mymod.py" is my module and "myprogram.py" is my program file for exampling module system.

# in "mymod.py" we should create a function with any name, like "funky_print" like this:

def funky_print():
    print("Hellooow, I am from a module")


# and then you should go to "myprogram.py" and use this two ways:

# Way 01:

#   import mymod
#   mymod.funky_print()

#or

# Way 02:

#   from mymod import funky_print()
#   funky_print()


# How to create a Package ?

# for making a package you need to create a folder with name of package name.
# you should create an __init__.py file for this that python knows this folder for a package
# and then paste your module files in this folder and next, you can import like this:

# from <package-name> import <module-name>
#       |
#       --->   this is your folder name that should match with your package name