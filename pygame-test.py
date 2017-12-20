import pygame, string

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

if joystick_count <= 0:
    print("No joysticks detected. Bye.")
    exit()

if joystick_count > 1:
    print("Multiple joysticks detected.")
    print("Please select the joystick you want to use by typing the appropriate number:")
    for i in range(joystick_count):
        print("{}:\t{}".format(i, pygame.joystick.Joystick(i).get_name()))
    
    loop = True
    while loop:
        #try:
        selection = int(input("Enter joystick number: "))
        # I'll get these lines working later I guess
        # except ValueError:
            # print("Try writing a number this time.")
        if selection not in range(joystick_count):
            print("That wasn't a number we're expecting. Try again.")
        else:
            loop = False

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
