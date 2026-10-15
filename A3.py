# Resistor colour code: prints the digit for the colour of the first band

# Taking the colour and converting it to lowercase so "Red" and "red" both work
colour = input("Enter band colour: ")
colour = colour.lower()

# Comparing the colour with each known colour one by one
if colour == "black":
    print("Digit = 0")
elif colour == "brown":
    print("Digit = 1")
elif colour == "red":
    print("Digit = 2")
elif colour == "orange":
    print("Digit = 3")
elif colour == "yellow":
    print("Digit = 4")
elif colour == "green":
    print("Digit = 5")
elif colour == "blue":
    print("Digit = 6")
elif colour == "violet":
    print("Digit = 7")
elif colour == "grey":
    print("Digit = 8")
elif colour == "white":
    print("Digit = 9")
else:
    # Runs when the colour matched none of the above
    print("Invalid colour")
