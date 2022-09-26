#  @TheWorldFoundry


import pygame
import random

KEY_MARKER = "KEY:"
name = "textimage.txt"
#  There MUST be a key marker

level_input = open(name, 'r+')
lines = level_input.read().split("\n")
level_input.close()

key_index = -1
for line in lines:
    key_index += 1
    if line == KEY_MARKER:
        break

img = pygame.Surface((len(lines[0]),key_index),pygame.SRCALPHA)

key = {}

i = 0
while i < len(lines):
    if lines[i] == KEY_MARKER:
        j = i+1
        while j < len(lines):
            rgba = []
            kv = lines[j].split("=")
            if len(kv) > 1:
                for k in (0,2,4,6):
                    decimal = int(kv[1][k:k+2], 16)
                    rgba.append(decimal)
                key[str(kv[0])] = rgba
                print (kv[0], " = ", key[str(kv[0])])
            j += 1
        i = j
    i += 1

i = 0
while i < len(lines):
    if lines[i] == KEY_MARKER:
        i = len(lines)  # break
    else:
        row = 0
        for c in lines[i]:
            if c != ' ':
                img.set_at((row, i), key[str(c)])
            row += 1
    i += 1

pygame.image.save(img, "imgtxtoutput_"+str(random.randint(1000000000,9999999999))+".png")        