with open('input.txt', 'r') as file:
    raw_input = file.read()

bag_contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def possible_game(gamestring):
    for round in gamestring.split(";"):
        for action in round.split(','):
            amount, color = action.lstrip().split(" ")
            if int(amount) > bag_contents[color]:
                return False
    return True


output = 0
for line in raw_input.split("\n"):
    idString,gameString = line.split(":")
    game_id = int(idString.split(" ")[1])
    output += game_id if possible_game(gameString) else 0
print(output)
