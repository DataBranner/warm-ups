def convert(integer, base=2):
    if integer == 0:
        return((0, 0))
    running = integer
    binary = [] # reverse this at the end
    while running > 0:
        binary.append(str(running%base))
        running = running // base
    return (integer, ''.join(reversed(binary)))

