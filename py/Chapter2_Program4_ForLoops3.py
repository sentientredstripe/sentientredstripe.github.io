# __author__ = 'BHS-programing'
# # Create a program    Save it as ForLoop3.py        ( 5 Points )
# #
# # 1st:
# # You will ask for how many items a person is purchasing.
# #
# # Based on this amount, write a loop which will accept this many inputs and determine the total of all items and their average.
# #
# # Display these values as output.
# #
# # 2nd:
# # Next write the code that simulates tossing a coin 100 times.
# # Determine and count the number of heads and number of tails tossed.
# # Display these amounts.

# numItemsPurchased = int(input("How many items? "))
# totalCostItems = 0

# for numItemsPurchased in range(numItemsPurchased):
#     itemCost = float(input("Enter the cost of the item: $"))
#     totalCostItems = totalCostItems + itemCost
    
# print("Total cost of items is $" + str(totalCostItems))
# totalCostItemsAverage = totalCostItems/numItemsPurchased
# print("Average cost of items is $" + str(totalCostItemsAverage))

#----------------------------------------------------------------

# Next write the code that simulates tossing a coin 100 times.
# Determine and count the number of heads and number of tails tossed.
# Display these amounts.

import random
heads = 0 #heads = 1
tails = 0 #tails = 2

for coinFlip in range(0,100):
    coinFlipResult = random.randint(1,2)
    if coinFlipResult == 1:
        heads = heads + 1
    elif coinFlipResult == 2:
        tails = tails + 1 

print("Heads: " + str(heads))
print("Tails: " + str(tails))
    