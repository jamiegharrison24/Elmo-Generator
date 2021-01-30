# For the first version, this script automatically generates random images of Elmo by selecting from 3 variables.


import numpy as np
import math
import PIL
from PIL import Image #for image manipulation
import os 



directory = ''

# images aare opened, note they must be resized for mask to work properly
elmo = Image.open("elmo.jpg")
elmo.resize((512, 512))


for i in os.listdir('Mustache'):
    if i.endswith('.jpg') or i.endswith('.png'):
            mustache = Image.open(i)
            mustache.resize((512,512))
            elmoCopy = elmo.copy()
            elmo.paste(mustache,(0,0),mustache)
            elmo.show()




# glasses = Image.open("glasses.png")
# glasses.resize((512,512))

# hat = Image.open("hat.png")
# hat.resize((512,512))


# Doing manually to learn how library works - note will have to tweak second parameter in function to get locatino correct

# background.paste(mustache, (0,0), mustache)
# background.paste(glasses, (0,0), glasses)
# background.paste(hat, (0,0), hat)

