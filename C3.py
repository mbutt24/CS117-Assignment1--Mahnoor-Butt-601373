# Decimal to binary: function using repeated division by 2 (no bin())

# Takes a decimal number n and returns its binary form as a string
def decimal_to_binary(n):
    # Special case: the loop below would not run for 0
    if n == 0:
        return "0"
    binary = ""
    # Keep dividing by 2 until the number becomes 0
    while n > 0:
        # n % 2 is the remainder (0 or 1), which is the next binary digit
        # It is added to the front because the last remainder is the first digit
        binary = str(n % 2) + binary
        # n // 2 is the division without decimals
        n = n // 2
    return binary

# Test the function with the sample numbers
print("decimal_to_binary(15) ->", decimal_to_binary(15))
print("decimal_to_binary(35) ->", decimal_to_binary(35))
