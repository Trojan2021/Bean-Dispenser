# Laying out the logic for the dispenser.
# There needs to be a command to select which ingredient, select quantity, press start

ingredients = ["Salt", "Sugar", "Flour"]
units = ["Gallons", "Quarts", "Pints", "Cups"]
lengthIngre = len(ingredients)
lengthUnits = len(units)

print("Ingredients:")
for i in range(lengthIngre):
    print(f"{i + 1}. {ingredients[i]}")

print(
    "\nPlease enter the number cooresponding to the ingredient you would like dispensed"
)
choiceIngre = int(input("Choice: ")) - 1

print(f"\nYou chose {ingredients[choiceIngre]}")
print("Select the units you are measuring in:")
for i in range(lengthUnits):
    print(f"{i + 1}. {units[i]}")

print("\nPlease enter the number cooresponding to the units you would like dispensed")
choiceUnits = int(input("Choice: ")) - 1

print(f"\nYou chose {units[choiceUnits]}")

print("\nPlease enter the amount of units that you would like")
choiceAmount = int(input("Choice: "))

print(f"Dispensing {choiceAmount} {units[choiceUnits]} of {ingredients[choiceIngre]}.")
