'''
Apparently the official name for this junk is "Doc String". Typically put at the beginning of code.
Also known as a multi-line comment, used to conve information from coder to reader.

"Adventure Game"
Author: Tanner Woodruff
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

# Welcome message and introduction.
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

#LET'S GOOOOOO IT'S PYTHON TIME
## Maybe I should consider speaking with the data science sector of the college? See if that's interesting?
###Shut up- focus on the class.

# "CTRL + /" IS A COMMENT SHORTCUT

# Asking the user/player for their name.
name = input("Tell us your name, traveller. ")

'''
# Concatenate strings to create a personalized message
print("Welcome, " + name + "! Your journey begins now.")
'''
# OR Use an f-string to display the same message in a more readable way.
print(f'Welcome, {name}. Your journey begins now.\n')

# Describe the starting area
starting = '''

'''


#Ask for first decision.
decision = input('Do you wanna take the path? (Y/N) ').lower()
'''
while decision not in ["yes", "no"]:
    print("Confused, you stand still, unsure of what to do.")
    ##Option for the user to make a new decision.
    decision = input("Do you want to take the path? (yes or no): ").lower()
'''
#   DEBUGGING STUFFS.
##  The debuging tool shown here in VSCode with Python, with the "step into" and "step over" buttons is...
##  according to Hadzik, "Pretty universal."


# Respond based on the player's decision
if decision == 'y':
    print(f"We can work with that, {name}. We'll work with that.")
    print('Robert Frost would be proud- you took the road less traveled.')
elif decision == 'n':
    print(f"Dang {name}, you're kind of a coward, aren't you?")
    print("Fine. We'll wait.")
else: print("That wasn't one of the options, dipstick. Try again. Maybe read the directions this time.")

# LOOP TIME WOOOOOOOOOOOOOOOO

# ## THIS MEANS TO UPDATE THE VARIABLE WHILE RUNNING THE LOOP UNTIL VAL IS GREATER THAN 6...
# number = 1
# while number < 6:
#    print(number)
#    number += 1

# FOR LOOP: used when you know how many times the loop needs to be done
# WHILE LOOP: used when number of loops is UNKNOWN. This runs until a condition is met.

'''
Run code. Make sure it works. Take a screenshot. Send the screenshot.
ALSO GITHUB REPOSITORY URL'''
