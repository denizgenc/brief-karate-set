from inputs import get_gamepad
from pathlib import Path

gamepad_mappings = {"BTN_NORTH" : 'c',
                    "BTN_WEST" : 'd',
                    "BTN_TR" : 'f',
                    "BTN_TL" : 'e',
                    "BTN_SOUTH" : 'a',
                    "BTN_EAST" : 'b',
                    "ABS_RZ255" : 'i', #not correct
                    "ABS_Z255" : 'j', #not correct
                    "BTN_START" : 'g',
                    "BTN_MODE" : 'o', #not correct
                    "BTN_SELECT" : 'h',
                    "ABS_HAT0X1" : 'k', #not correct
                    "ABS_HAT0X-1" : 'l', #not correct
                    "ABS_HAT0Y1" : 'm', #not correct
                    "ABS_HAT0Y-1" : 'n'} #not correct

button_mappings = ["LIGHT", "MEDIUM", "HEAVY", "SPECIAL"]
mapping_key = ""
next_button = True
player = 1 if int(input("Player Number? (1, 2): ")) > 1 else 0

while len(mapping_key) < 4:
    if next_button:
        print(button_mappings[len(mapping_key)], end=': ', flush=True)
        next_button = False
    events = get_gamepad()
    for event in events:
        if event.ev_type == "Key" and event.state == 1:
            print(event.code)
            mapping_key += gamepad_mappings[event.code]
            next_button = True
        if event.ev_type == "Absolute" and event.state is not 0:
            print(event.code, event.state)
            mapping_key += gamepad_mappings[event.code + str(event.state)]
            next_button = True

default_path = "defaultpath.txt"
default_path_exists = Path(default_path).is_file()
my_path = open(default_path).read() if default_path_exists else input("please provide the path for SFWinKey.TXT: ")
with open(my_path if default_path_exists else "defaultconfig.txt", encoding="utf-8") as f:
    file = f.readlines()
    file[player] = mapping_key + "wxyz" + "\n"

if default_path_exists:
    if input("write to \"" + my_path + "\" ? (Y/ n): ") not in 'yY':
        my_path = input("please enter a new path: ")
        if input("set \"" + my_path + "\" as the new default? (Y/ n): ") in 'yY':
            open(default_path, 'w+').write(my_path)
            print("new default path saved successfully.")
else:
    open(default_path, 'w+').write(my_path)

open(my_path, 'w+', encoding="utf-8").write("".join(file))
print("saved successfully.")
