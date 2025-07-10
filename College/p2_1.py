def display_pattern(n):
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "* " * i)
    # Lower part of the pattern
    for i in range(n - 2, 0, -2):
        print(" " * ((n - i) // 2) + "* " * i)
pattern_size = 5
display_pattern(pattern_size)
