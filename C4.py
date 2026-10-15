# Loaded voltage divider: finds the unloaded and loaded output voltage

# vs = supply voltage, r1 and r2 = divider resistors, rl = load resistor
def loaded_divider(vs, r1, r2, rl):
    # Unloaded voltage: normal voltage divider formula
    unloaded = vs * r2 / (r1 + r2)
    # The load is in parallel with r2, so first find their parallel equivalent
    r_parallel = (r2 * rl) / (r2 + rl)
    # Loaded voltage: voltage divider formula using r_parallel instead of r2
    loaded = vs * r_parallel / (r1 + r_parallel)
    # Return both values as a pair, rounded to 2 decimal places
    return round(unloaded, 2), round(loaded, 2)

# Test the function with the sample values
print("loaded_divider(13, 1350, 1100, 500) ->", loaded_divider(13, 1350, 1100, 500))
