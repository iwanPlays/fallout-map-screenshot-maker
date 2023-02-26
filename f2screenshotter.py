# note: arrow keys move 32x24 pixels (max) but its unreliable
# pip install pynput
# move to bottom left of map

from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
from PIL import ImageOps
from pynput.keyboard import Key, Controller
import time
import PIL

# https://stackoverflow.com/questions/64197868/

kb = Controller()
def press(button):
    kb.press(button)
    kb.release(button)

# https://note.nkmk.me/en/python-pillow-concat-images/

def concat_hori(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def concat_vert(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

# 1. goto bottom left of screen

#???

# 2. take base screen

time.sleep(1)
print('5', flush=True)
time.sleep(1)
print('4', flush=True)
time.sleep(1)
print('3', flush=True)
time.sleep(1)
print('2', flush=True)
time.sleep(1)
print('1', flush=True)
time.sleep(1)
print('go!', flush=True)

#base_debug = base

#red = Image.new('RGB', (1920,1),(255,0,0)) #debug red line
factor = 8 #vertical speed

rows = []

# initial 1920 width
row_width = 1920

while True:

    space_vert = 0
    
    base = ImageGrab.grab(bbox=(1920-row_width,0,1920,979))

    # GO UP
    while True:

        new_vert = ImageGrab.grab(bbox=(1920-row_width,0,1920,24*factor))
        new_join = new_vert
        
        # check whether new_vert and old_vert are identical (break)
        if space_vert == 0:
            old_vert = new_vert
        else:
            if new_vert == old_vert:
                break

        for n in range(factor):
            press(Key.up)
            time.sleep(.025)
        time.sleep(.45)
        
        # top line of the last check
        old_top = old_vert.crop((0, 0, row_width, 1))
        
        for n in range(24*factor):
            new_line = new_vert.crop((0, n, row_width, n+1))
            if new_line == old_top:
                print('new_join at ' + str(n))
                new_join = new_vert.crop((0, 0, row_width, n))
                break
        
        #base_debug = concat_vert(red, base_debug)
        #base_debug = concat_vert(new_join, base_debug)
        base = concat_vert(new_join, base)
    
        space_vert += 1 * factor
    
        print('space_vert: ' + str(space_vert))
    
        old_vert = new_vert
    
    rows.append(base)
        
    # GO RIGHT

    old_h = ImageGrab.grab(bbox=(0,0,1920,979))

    for n in range(60):
        press(Key.right)
        time.sleep(.05)
    time.sleep(.45)

    new_h = ImageGrab.grab(bbox=(0,0,1920,979))

    # top line of the last check
    old_h_right = old_h.crop((1919,0,1920,979))

    if new_h.crop((1919,0,1920,979)) == old_h.crop((1919,0,1920,979)):
        break
    
    # wishful reset since perfect scroll 60*32 = 1920, but unlikely
    row_width = 1920

    #compare cols
    for n in range(1920):
        new_col = new_h.crop((n,0,n+1,979))
        if new_col == old_h_right:
            row_width = 1920 - (n + 1)
            print('row_width: ' + str(row_width))
            base = new_h.crop((1920 - row_width, 0, 1920, 979))
            break

    # GO DOWN
    for n in range(space_vert + 10):
        press(Key.down)
        time.sleep(.025)
    time.sleep(.45)

# set final image internal
final = rows[0]
print(str(final.width) + 'x' + str(final.height))
if len(rows) > 1:
    for row in rows[1:]:
        print(str(row.width) + 'x' + str(row.height))
        final = concat_hori(final, row)

print(len(rows))

# write final image    
timestr = time.strftime("%Y%m%d-%H%M%S")
final.save("f2map-"+timestr+".png")
#base_debug.save("f2map-"+timestr+"_debug.png")
print('image size:  ' + str(final.width) + 'x' + str(final.height))
#print('debug size:  ' + str(base_debug.width) + 'x' + str(base_debug.height))

#with Image.open('MANUAL.png') as im:
#    print('MANUAL size: ' + str(im.width) + 'x' + str(im.height))