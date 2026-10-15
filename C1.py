# Current and power: two functions using Ohm's law and the power formula

# Returns the current using Ohm's law: I = V / R
def ohms_current(v, r):
    return v / r

# Returns the power using P = I squared x R
def power_dissipated(i, r):
    return i * i * r

# Call the functions with V = 12 V and R = 6 ohm
# (the result is printed outside the function, as the question asks)
current = ohms_current(12, 6)
power = power_dissipated(current, 6)
print("Current =", current, "A")
print("Power =", power, "W")
