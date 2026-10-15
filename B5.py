# Resistor tolerance sorting: bins measured 100 ohm resistors until 0 is entered

# Running counts for each bin, all start at 0
tol_1 = 0
tol_5 = 0
reject = 0

# Read the first value before the loop so the while condition can check it
measured = float(input("Enter measured resistance (0 to stop): "))

# Keep going until the user enters 0
while measured != 0:
    if measured >= 99.0 and measured <= 101.0:
        # Within 1% of 100 ohm
        tol_1 = tol_1 + 1
    elif measured >= 95.0 and measured <= 105.0:
        # Within 5% but not 1%, because the 1% case was checked first
        tol_5 = tol_5 + 1
    else:
        # Outside 95 to 105 ohm
        reject = reject + 1
    # Read the next value, otherwise the loop would never end
    measured = float(input("Enter measured resistance (0 to stop): "))

# The loop has stopped, so print the final counts
print("1% tolerance:", tol_1)
print("5% tolerance:", tol_5)
print("Reject:", reject)
