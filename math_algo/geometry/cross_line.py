


line_1 = [2, 3, 4]
line_2 = [1, 7, 3]

def cross_line(line1, line2):
    a1 = line_1[0]
    b1 = line_1[1]
    c1 = line_1[2]

    a2 = line_2[0]
    b2 = line_2[1]
    c2 = line_2[2]

    x = -(c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    y = -(a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

    if (a1 * b2 - a2 * b1) == 0:
        return 0

    return x, y

print(cross_line(line_1, line_2))