#  @TheWorldFoundry


import pygame
import random

KEY_MARKER = "KEY:"
name_output = "textimage.txt"
name = "input.png"

img = pygame.image.load(name)

keys = " abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+[]{};\'\"\\|,.<>/?"

special = ":="  # do not use for keys

keys_pos = 0
key = {}
val = {}
out_lines = []
for y in xrange(0, img.get_height()):
    row = ""
    for x in xrange(0, img.get_width()):
        r,g,b,a = img.get_at((x,y))
        
        if str([r,g,b]) not in val:
            val[str([r,g,b])] = keys[keys_pos%len(keys)]
            key[str(keys[keys_pos%len(keys)])] = (r,g,b)
            keys_pos += 1
        row = row+(val[str([r,g,b])])        
    out_lines.append(row)
    
    
out_lines.append(KEY_MARKER)
for k in key:
    print key[k]
    
    R = format(key[k][0],'x').rjust(2,'0')
    G = format(key[k][1],'x').rjust(2,'0')
    B = format(key[k][2],'x').rjust(2,'0')
    
    h = str(R)+str(G)+str(B) #('{:X}{:X}{:X}').format(key[k][0],key[k][1],key[k][2])
    out_lines.append(k+"="+h+"ff")

with open(name_output, 'w') as f:
    for line in out_lines:
        f.write(line)
        f.write('\n')
