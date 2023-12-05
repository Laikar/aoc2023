import string

with open('input.txt', 'r') as file:
    raw_input = file.read()
split = raw_input.split("\n")


def chart_at(x, y):

    return split[y][x] if 0 <= y <= len(split) - 1 and 0 <= x <= len(split[y])-1 else "."


def next_to_gear(start_x, end_x, numline):

    for x in range(start_x - 1, end_x + 2):
        for y in range(numline - 1, numline + 2):
            # print(f"y: {y}")
            print(f"x: {x}, y: {y}, char: {chart_at(x,y)}")
            if chart_at(x, y) is "*":
                return x,y
    return -1,-1


output = 0
gears = {}
for y, line in enumerate(split):
    line_enumerator = enumerate(line)
    # print(f"\ny: {y}", end="")
    for x, char in line_enumerator:
        # print(f"{x},", end="")
        if char in string.digits:
            start_x = x
            num = 0
            while char in string.digits:
                num *= 10
                num += int(char)
                last_x = x
                if x < len(line) - 1:
                    x, char = next(line_enumerator)
                else:
                    char = "."
            print(f"num '{num}' on line '{y}' starting at '{start_x}' with length '{last_x+1-start_x}'")
            gear_cords = next_to_gear(start_x, last_x or start_x, y)
            if gear_cords is not (-1, -1):
                gears.setdefault(gear_cords, []).append(num)
for gear_cords, parts in gears.items():
    if len(parts) is 2:
        output += parts[0] * parts[1]
print(output)
