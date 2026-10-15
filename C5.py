# Star-Delta transformation: converts a star network to its equivalent delta network

# ra, rb, rc are the three resistors of the star (Y) network
def star_to_delta(ra, rb, rc):
    # The numerator is the same for all three delta resistors,
    # so it is calculated only once: RaRb + RbRc + RcRa
    numerator = ra * rb + rb * rc + rc * ra
    # Each delta resistor = numerator / the star resistor opposite to it
    rab = numerator / rc
    rbc = numerator / ra
    rca = numerator / rb
    # Return the three delta resistors rounded to 2 decimal places
    return round(rab, 2), round(rbc, 2), round(rca, 2)

# Test
print("star_to_delta(15, 25, 35) ->", star_to_delta(15, 25, 35))
