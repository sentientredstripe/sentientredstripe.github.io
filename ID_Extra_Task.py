# As you are aware their are different forms of ID
#
# Examples are shown below
#
# Social security Number of the form   '123-45-6790' 11 characters
# Mass Drivers License number of the form    'S 1 2 3 4 5 6 7 8' 8 characters
# Green Card of the form   '123-456-789' 11 characters
# US Department of Defense of the form   'DD-1234-DD-567' 14 characters
#
# You are to create a Python program that accepts some form of Id
# Based on the 4 choices above you are to determine which type of ID has been entered in.
# We will assume the ID entered is one of the 4 listed above.
#
# Next if It is Social security Number then display last 4 digits
# If it is the Mass License Number display first 3 digits after the letter S
# If it is a Green Card display the first two and last two digits
# If it is a Department of Defense display the middle 4 digits
#
# Enjoy!


#     012345678910 --> 10 characters
#SSN: 123-45-6789
#             012345678 --> 8 characters
#Mass Driver: S12345678
#            012345678910 --> 10 characters
#Green Card: 123-456-789
#        01234567890123 --> 13 characters
#US DoD: DD-1234-DD-567


userID = input("Enter your ID number: ")

if len(userID) == 13:
    print("DoD")
elif len(userID) == 10:
    print("Mass Driver's")
elif len(userID) == 13 and userID[6] == int:
    print("Green Card")
else:
    print("SSN")