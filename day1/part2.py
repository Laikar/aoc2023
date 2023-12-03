import string

with open('input.txt', 'r') as file:
    raw_input = file.read()
parsed_input = raw_input
words2digits={
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}
for num, replacement in words2digits.items():
    parsed_input = parsed_input.replace(num, replacement)
output_num = 0
for line in parsed_input.split("\n"):
    first = None
    last = None
    for char in line:
        if char in string.digits:
            if not first:
                first = int(char)
            last = int(char)
    output_num += (first * 10 + last)
print(output_num)

