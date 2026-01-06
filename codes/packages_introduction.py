# for view a complete list of python packages, you can visit https://pypi.org website

# in the next step, after choosing a package for use, we should install it; this is able
# with "pip install <package-name>" command.

# for example, for installing "emoji" package we should run -> pip install emoji

# and then, we should import it, like this:

import emoji

# or if you need just a function in this package :

# from emoji import emojize

# this command will import emojize function/void from emoji package

# now we can use package:

message = emoji.emojize("Hello World! I am a Programmer :laptop:")

print(message)

# if you see your terminal or everywhere you run your python program; you will see this:
# Hello World ! I am a Programmer 💻