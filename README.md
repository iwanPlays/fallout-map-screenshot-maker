# fallout map screenshot maker aka f2screenshotter.py
A screen capture tool for automatically stitching classic fallout 2 map screenshots into one big map view

Works with Python 3.10

# How to use

    pip install pillow
    pip install pynput

Open the map in BIS Mapper and turn on/off the layers you want

If you have annoying unhidable lime green script tiles delete scripts and refresh using: Shift+A, Enter, Enter, F8, F8

In F8 (play) view, move to the bottom left corner of the map.

BIS Mapper must be running at 1920x1080. On my system it's important that it's in the background.

You will start the script and have 5 seconds to ALT-TAB to BIS Mapper and ensure the cursor (use the arrow, not the green hex-tile - easier to hide) is not in view and that the cursor is not scrolling to the side.

    python f2screenshotter.py
    
After 5s it should start moving up. It is taking screenshots and joining them together. Because an arrow key press is unreliable regarding how many pixel it moves, it constantly checks if the new pixels have already been seen before. Once it detects the same line of pixels, it stops.

Janky stuff.
