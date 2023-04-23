# fallout map screenshot maker aka f2screenshotter.py
A screen capture tool for automatically stitching classic fallout 2 map screenshots into one big map view

Works with Python 3.10

# How to use

    pip install pillow
    pip install pynput

Open the map in BIS Mapper and turn on/off the layers you want

If you have annoying unhidable lime green script tiles delete scripts and refresh using: **Shift+A**, Enter, Enter, F8, F8. This also disables scripted behavior, so NPCs won't be moving if they are scripted to do so. Idle animations still play, which might be an issue. Some locations also use scripts to force time of day (modoc rat field, ghost caves) so this helps with that as well.

In F8 (play) view, move to the bottom left corner of the map. While in game mode, you can also press **D** to change time of day.

BIS Mapper must be running at 1920x1080.

You will start the script and have 5 seconds to ALT-TAB to BIS Mapper and ensure the cursor (use the arrow, not the hex-tile - easier to hide; also, after moving the cursor in the interface area, you can use arrows up and then down to get rid of the lingering cursor sprite pixels) is not in view and that the cursor is not scrolling to the side.

    python f2screenshotter.py
    
After 5s it should start moving up. It is taking screenshots and joining them together. Because an arrow key press is unreliable regarding how many pixel it moves, it constantly checks if the new pixels have already been seen before. Once it detects the same line of pixels, it stops.

Janky stuff.

# Result

If you use it right and nothing gets in the way, you get screenshots like this:

![modbrah](https://i.imgur.com/WXzI0nK.png)

If you run this in editor mode, it'll fabricate this kind of fun mess:

![modmain](https://i.imgur.com/Stznb1m.jpg)
