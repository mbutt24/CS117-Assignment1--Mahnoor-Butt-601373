# Resistors in series: reads each resistor and prints the total resistance

# Ask how many resistors there are, so we know how many times to loop
count = int(input("How many resistors? "))

# total starts at 0 and the value of each resistor is added to it
total = 0

# Loop from 1 to count, i is the resistor number (R1, R2, ...)
for i in range(1, count + 1):
    # str(i) converts the number to text so it can be joined with "Enter R"
    resistance = float(input("Enter R" + str(i) + ": "))
    # Series formula: R_total = R1 + R2 + ...
    total = total + resistance


print("Total resistance =", total, "ohm")
