import string

with open('input.txt', 'r') as file:
    raw_input = file.read()
split = raw_input.split("\n")


def chart_at(x, y):

    return split[y][x] if 0 <= y <= len(split) - 1 and 0 <= x <= len(split[y])-1 else "."


def is_engine_part(start_x, end_x, numline):

    for x in range(start_x - 1, end_x + 2):
        for y in range(numline - 1, numline + 2):
            # print(f"y: {y}")
            print(f"x: {x}, y: {y}, char: {chart_at(x,y)}")
            if chart_at(x, y) not in (string.digits + '.'):
                return True
    return False


output = 0

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

            if is_engine_part(start_x, last_x or start_x, y):
                print("yes")
                output += num
print(output)
