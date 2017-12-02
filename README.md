# brief-karate-set
A button setting program for the game Brief Karate Foolish, written in Python
-----

### Background

Brief Karate Foolish shipped without config. This project aims to be a decent replacement.

However, there *is* a way to change the effects joystick buttons have - there is the config file located in `./Brief Karate Foolish/System/SFWinKey.TXT` that basically describes (in Japanese unfortunately) how to set the buttons. Basically, buttons 1, 2, 3... on your joystick (as reported on Windows in Devices and Printers) are represented by letters in the config file as a, b, c... and so on. The first 4 letters correspond to Light, Medium, Heavy and Special respectively, at least for Brief Karate Foolish.

So to set buttons 1, 4, 6, and 2 to L, M, H and SP respectively, one would write  
`adfb[wxyz]`

I am currently unsure of the use of the last 4 letters in the 8 letter string. I think they're unused buttons that the engine requires to be set - in fact, the default `SFWinKey.TXT` describes that the first six buttons as LK, MK, HK, LP, MP, HP/Pose (?). The last two buttons I am not sure of, though they may be reserved for select/start, so further investigation is important. However, it might be that those buttons are completely unused, as the `wxyz` actually comes from a "support" page on the developer's website for the game: http://dcs.ciao.jp/brief/suport.html

-----

### Program plan

This program will take joystick input, handling it with PyGame, and write a file named `SFWinKey.TXT` into the System subdirectory in the Brief Karate Foolish directory.

To make it easy, make the button setting automatically move down a list so people don't have to keep clicking. To achieve that, you should also make sure that the game only records when a *new* button is pressed down, so as to slightly help with sloppily pianoing the buttons while setting.

I've included the entire original `SFWinKey.TXT` (including the instructions) as `defaultconfig.txt`, and that will be used for a "Restore Defaults" option.

Package the program with py2exe or something similar (maybe PyInstaller). Read up on that.

-----

### Build Instructions

You should probably run `git clone https://github.com/denizgenc/briefkarateset.git` , then build, following these steps:

1. Run py2exe/PyInstaller
2. ...
3. PROFIT!

Most people should just download the builds I make though. Make sure to add a **Download** header for those peeps.

-----

### TODO:

- Learn the basics of joystick handling through PyGame
- Learn how to package Python projects as executables.
    - Add a **Download** header once a build is created.
- Create a basic text based version of this button config
- Make a GUI version eventually.
    - Maybe have an input display that shows you when the buttons are being pressed? That would be good.
    - It would also be good to make the GUI navigable with the joystick. POV hat/Y-axis to change selections, any button to interact with a selected element.
