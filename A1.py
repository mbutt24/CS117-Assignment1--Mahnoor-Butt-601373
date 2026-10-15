# Fuse check: finds the current using Ohm's law and tells if the fuse will blow

# Taking voltage and resistance from the user 
voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohm): "))

# Resistance can't be zero or negative, so checking it first
if(resistance <= 0):
    print("Invalid resistance")
else:
    # Ohm's law: I = V / R
    current = voltage / resistance
    print("Current =", current, "A")
    # More than 2 A means the fuse blows, otherwise the circuit is safe
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
