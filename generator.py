# For the first version, this script automatically generates random images of Elmo by selecting from 3 variables.


import numpy as np
import math
import PIL
from PIL import Image #for image manipulation
import os 



directory = ''

# images aare opened, note they must be resized for mask to work properly
elmoOriginal = Image.open("elmo.jpg")
elmoOriginal.resize((512, 512))
elmoCopy = []



for i in os.listdir('mustache'):
    for j in os.listdir('glasses'):
        if i.endswith('.jpg') or i.endswith('.png'):
            mustache = Image.open(os.path.join('mustache',i))
            mustache.resize((512,512))

        if j.endswith('jpg') or j.endswith('.png'):
            glasses = Image.open(os.path.join('glasses',j))
            glasses.resize((512,512))

        elmoCopy.append(elmoOriginal.copy())
        elmoCopy[-1].paste(mustache,(120,100),mustache)
        elmoCopy[-1].paste(glasses,(120,-30),glasses)
        elmoCopy[-1].show()

        
        
        




# for i in os.listdir('mustache'):
#     if i.endswith('.jpg') or i.endswith('.png'):
            
#             mustache = Image.open(os.path.join('mustache',i))
#             mustache.resize((512,512))

#             elmoCopy.append(elmoOriginal.copy())
#             elmoCopy[-1].paste(mustache,(0,0),mustache)
#             elmoCopy[-1].show()


# for j  in os.listdir('glasses'):
#         if j.endswith('.jpg') or j.endswith('.png'):
            
#             glasses = Image.open(os.path.join('glasses',j))
#             glasses.resize((512,512))

#             elmoCopy.append(elmoOriginal.copy())
#             elmoCopy[-1].paste(glasses,(0,0),glasses)
#             elmoCopy[-1].show()



# for i in os.listdir('hats')




# glasses = Image.open("glasses.png")
# glasses.resize((512,512))

# hat = Image.open("hat.png")
# hat.resize((512,512))


# Doing manually to learn how library works - note will have to tweak second parameter in function to get locatino correct

# background.paste(mustache, (0,0), mustache)
# background.paste(glasses, (0,0), glasses)
# background.paste(hat, (0,0), hat)

