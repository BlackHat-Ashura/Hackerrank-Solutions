def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(number):
        print("{0:{WIDTH}d} {0:{WIDTH}o} {0:{WIDTH}X} {0:{WIDTH}b}".format(i+1, WIDTH=width))
