import string

with open('input.txt', 'r') as file:
    input_string = file.read()
output_num = 0
for line in input_string.split("\n"):
    first = None
    last = None
    for char in line:
        if char in string.digits:
            if not first:
                first = int(char)
            last = int(char)
    output_num += (first * 10 + last)
print(output_num)

