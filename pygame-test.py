import pygame, string
from pathlib import Path

pygame.init()
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
selection = 0

if joystick_count <= 0:
    print("No joysticks detected. Bye.")
    exit()

if joystick_count > 1:
    print("Multiple joysticks detected.")
    print("Please select the joystick you want to use by typing the appropriate number:")

    joystick_not_selected = True
    while joystick_not_selected:
        for i in range(joystick_count):
            print("{}:\t{}".format(i, pygame.joystick.Joystick(i).get_name()))

        joystick_number = input("Enter joystick number: ")

        if not str.isnumeric(joystick_number):
            print("Try writing a number this time.")
            continue

        selection = int(joystick_number)
        if selection not in range(joystick_count):
            print("That wasn't a number we're expecting. Try again.")
            continue

        joystick_not_selected = False

joy = pygame.joystick.Joystick(selection)
joy.init()

button_mappings = ["LIGHT", "MEDIUM", "HEAVY", "SPECIAL"]
mapping_key = ""
next_button = True
player = 1 if int(input("Player Number? (1, 2): ")) > 1 else 0

while len(mapping_key) < 4:
    if next_button:
        print(button_mappings[len(mapping_key)], end=': ', flush=True)
        next_button = False
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            button = event.__dict__["button"] # See https://www.pygame.org/docs/ref/event.html
            print("Button {}".format(button))
            mapping_key += string.ascii_lowercase[button]
            next_button = True

print("mapping_key:", mapping_key)

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
