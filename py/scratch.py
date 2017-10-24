__author__ = 'BHS-programing'
def findAverage(cost, items):
    average = cost/items
    print("Average item cost is $ "+ str(average))

def costDisplay(cost):
    print("Total cost of items is $" + str(cost))


numItemsPurchased = int(input("How many items? "))

totalCostItems = 0

for numItemsPurchased in range(numItemsPurchased):
    itemCost = float(input("Enter the cost of the item: $"))
    totalCostItems = totalCostItems + itemCost

costDisplay(totalCostItems)
findAverage(totalCostItems, numItemsPurchased)