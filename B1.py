# Ohm's law table: current through a 10 ohm resistor for 1 V to 10 V

# The resistor value is fixed
resistance = 10

# range(1, 11) gives 1 to 10 (the last number 11 is not included)
for voltage in range(1, 11):
    # Ohm's law: I = V / R
    current = voltage / resistance
    print("V =", voltage, "V, I =", current, "A")
