# Parallel resistance: function that finds the equivalent of resistors in parallel

# Takes a list of resistor values and returns the equivalent resistance
def parallel_resistance(resistors):
    # total adds up 1/R1 + 1/R2 + ...
    total = 0
    for resistance in resistors:
        total = total + 1 / resistance
    # 1 / R_eq = total, so R_eq = 1 / total (rounded to 2 decimal places)
    return round(1 / total, 2)

# Test the function with the sample lists
print("parallel_resistance([20, 50]) ->", parallel_resistance([20, 50]))
print("parallel_resistance([110, 230, 370]) ->", parallel_resistance([110, 230, 370]))
