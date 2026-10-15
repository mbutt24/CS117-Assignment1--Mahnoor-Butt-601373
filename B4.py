# Continuous discharge analysis: finds the longest streak of strictly decreasing voltages

# Hardcoded voltage readings taken every minute
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

# streak = readings in the current falling run, start = where that run began
# longest = biggest streak found so far, best_start/best_end = its positions
streak = 1
start = 0
longest = 1
best_start = 0
best_end = 0

# Start from the second reading so each one can be compared with the one before
for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        # Voltage dropped, so the streak continues
        streak = streak + 1
    else:
        # Voltage did not drop (equal or higher), so the streak breaks
        # and a new streak starts from this reading
        streak = 1
        start = i
    # If this streak is the longest so far, remember its length and position
    # (> not >= so the first streak is kept when two are equal)
    if streak > longest:
        longest = streak
        best_start = start
        best_end = i

# Use the saved positions to get the starting and ending voltages
print("Longest continuous drop:", longest, "minutes")
print("Started at:", voltages[best_start], "V")
print("Ended at:", voltages[best_end], "V")
