# Course: CS 30
# Period: 1
# Date created: 2/10/21
# Date last modified: 2/10/23
# Name: Volodymyr Akulov
# Description: RPG Simple menu


# Menu border
print(15*"-"+"Main Menu"+15*"-")

# prompt
x = input("Inventory\nMap\nInteract\n\nExit\n\n")

# checking the input and anwsering
if x.lower() == "inventory":
    print("\nDisplays inventory")
elif x.lower() == "map":
    print("\nDisplays map")

# exit option
elif x.lower() == "exit":
    print("\nYou have exited the game")
elif x.lower() == "interact":
    print("\nYou interacted with the environment")
else:
    print("\nInvalid action try again")
