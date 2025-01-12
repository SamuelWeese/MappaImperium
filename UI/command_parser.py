import random

def roll_dice(words: list):
    if not words:
        return "You need to pass an argument to roll dice!"
    out_string = "You rolled...\n"
    while words:
        parts = words[0].split("d")
        # Below is operating on the assumption the user is doing this correctly
        # Needs to be fixed TODO
        num_dice = int(parts[0])
        num_side = int(parts[1])
        out_string += f"{words[0]} rolled..." + (" " + str(randint(1, num_side)) for _ in range(num_dice)) +"\n"
        words.pop(0)
    return out_string


def command_parsing(command: str, text_out=None):
    if len(command) < 2:
        # Send text out Command too short!
        text_out("Command too short!")
        return False
    if command[0] != command_symbol:
        return False
    command = command.lower()
    words = split(command[0:])
    match words[0]:
        case "r" | "roll":
            text_out(roll_dice(words[1:]))
        case _:
            text_out("Command is not valid!")
    return True