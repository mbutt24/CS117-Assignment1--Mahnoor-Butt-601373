# Current direction: tells the direction of current flow from its sign

# Taking the current value from the user
current = float(input("Enter current value: "))

# Checking positive first, then negative, otherwise it must be zero
if (current > 0):
    print("Current flows from A to B")
elif(current < 0):
    print("Current flows from B to A")
else:
    print("No current flows")
