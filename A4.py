# Logic gates: prints the AND, OR and XOR output for two input bits

# Taking the two input bits A and B
a = int(input("Enter A: "))
b = int(input("Enter B: "))

# Both bits must be either 0 or 1, otherwise error is shown
if (a == 0 or a == 1) and (b == 0 or b == 1):
    # AND gives 1 only when both inputs are 1
    if a == 1 and b == 1:
        AND = 1
    else:
        AND = 0

    # OR gives 1 when at least one input is 1
    if a == 1 or b == 1:
        OR = 1
    else:
        OR = 0

    # XOR gives 1 only when the inputs are different
    if a != b:
        XOR = 1
    else:
        XOR = 0

    print("AND =", AND)
    print("OR =", OR)
    print("XOR =", XOR)
else:
    print("Bits must be 0 or 1")
