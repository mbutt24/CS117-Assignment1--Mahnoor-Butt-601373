# Smallest and largest resistor: compares three values using only if/elif/else

# Taking the resistor values
r1 = float(input("Enter R1: "))
r2 = float(input("Enter R2: "))
r3 = float(input("Enter R3: "))

# A value is the smallest if it is <= both of the others
# (<= also handles the case when two values are equal)
if r1 <= r2 and r1 <= r3:
    smallest = r1
elif r2 <= r1 and r2 <= r3:
    smallest = r2
else:
    smallest = r3

# A value is the largest if it is >= both of the others
if r1 >= r2 and r1 >= r3:
    largest = r1
elif r2 >= r1 and r2 >= r3:
    largest = r2
else:
    largest = r3

print("Smallest =", smallest, "ohm")
print("Largest =", largest, "ohm")
