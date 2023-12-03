with open('input.txt', 'r') as file:
    raw_input = file.read()


def cube_power(gamestring):
    min_colors = {
        "red": None,
        "green": None,
        "blue": None
    }
    for round in gamestring.split(";"):
        for action in round.split(','):
            amount, color = action.lstrip().split(" ")
            amount = int(amount)
            if min_colors[color] is None or min_colors[color] < amount:
                min_colors[color] = amount
    return min_colors["red"] * min_colors["green"] * min_colors["blue"]


output = 0
for line in raw_input.split("\n"):
    idString, gameString = line.split(":")
    game_id = int(idString.split(" ")[1])
    output += cube_power(gameString)
print(output)
