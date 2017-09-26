#Speedy Overnight Delivery service does not accept packages heavier than
#27 kilograms or larger than 0.1 cubic meters (100,000 cubic centimeters).
#Create a Package Check application that asks the user to input:
#weight of the package
#height of the package
#length of the package
#width of the package
#Display an appropriate message if the package does not meet the requirements (e.g., too large, too heavy, or both)

packageWeight = float(input("Enter the package weight in KGs: "))
packageHeight = float(input("Enter the package height in CMs: "))
packageLength = float(input("Enter the package length in CMs: "))
packageWidth = float(input("Enter the package length in CMs: "))

packageVolume = packageHeight * packageWidth * packageLength

if packageVolume > 100000:
  print("Package with entered dimensions of " + str(packageWidth) + " x " + str(packageHeight) + " x " + str(packageLength) + " CMs is too large.")
else:
  print("Package dimensions of " + str(packageWeight) + " x " + str(packageHeight) +" X "+ str(packageLength) + " are OK.")
  
if packageWeight > 27:
  print("Package with entered weight of " + str(packageWeight) + "KGs is too heavy.")
else: 
  print("Package with entered weight of " +str(packageWeight) + "KGs is OK.")