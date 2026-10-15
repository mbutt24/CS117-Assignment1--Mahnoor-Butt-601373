# Sensor readings: counts readings above 3.2 V and finds highest, lowest and average

# The sensor readings are fixed, so they are stored in a tuple
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

# Start highest and lowest with the first reading, then compare the rest to it
above = 0
highest = readings[0]
lowest = readings[0]
total = 0

# One loop does all the work
for reading in readings:
    # (a) count the readings above 3.2 V
    if reading > 3.2:
        above = above + 1
    # (b) update the highest reading if this one is bigger
    if reading > highest:
        highest = reading
    # (c) update the lowest reading if this one is smaller
    if reading < lowest:
        lowest = reading
    # keep adding to get the sum for the average
    total = total + reading

# (d) average = sum / number of readings (len gives the number of readings)
average = total / len(readings)

# round(average, 2) keeps 2 digits after the decimal point
print("Readings above 3.2 V:", above)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 2), "V")
