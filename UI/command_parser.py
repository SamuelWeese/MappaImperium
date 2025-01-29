import random
# TODO move out of UI folder
def starts_with(string: str):
    if not string or len(string) <= 0:
        return None
    return string[0]

# eventually should be replaced with class of dice
def roll_dice(words: list)->str:
    if not words:
        return "You need to pass an argument to roll dice!"
    total = 0
    out_string = ""
    while words:
        current_total = 0
        parts = words[0].split("d")
        if len(parts) != 2:
            out_string += f"{words[0]} is not valid syntax! Use [number of dice]d[number of sides]!\n"
            words.pop(0)
            continue
        # Below is operating on the assumption the user is doing this correctly
        # Needs to be fixed TODO
        num_dice, num_side = 0,0
        try:
            num_dice = int(parts[0])
            num_side = int(parts[1])
        except ValueError as e:
            out_string += f"{words[0]} is not valid syntax!  Use [number of dice]d[number of sides], where the number of dice and number of sides are both valid numbers!"
        out_string += f"{words[0]} rolled... "
        for _ in range(num_dice):
            roll_value = random.randint(1, num_side)
            out_string += str(roll_value) + " "
            current_total += roll_value
        out_string += f"\n...for a total of {current_total}\n"
        total += current_total
        words.pop(0)
    out_string += f"For a grand total of: {total}"
    return out_string

def command_parsing(command: str)->str:
    if len(command) < 2:
        # Send text out Command too short!
        return "Command too short!"
    command = command.lower()
    words = command[1:].split()
    match words[0]:
        case "r" | "roll":
            return roll_dice(words[1:])
    return "Command is not valid!"