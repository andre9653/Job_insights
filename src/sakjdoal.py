def viagemNoTempo(a, b, c):
    # temps = [a, b, c]
    control = a - b == 0 or b - a == 0
    control2 = a - c == 0 or c - a == 0
    control3 = b - c == 0 or c - b == 0
    possivel = "N"
    if control or control2 or control3:
        possivel = "S"
    return possivel


print(viagemNoTempo(31, 110, 79))
