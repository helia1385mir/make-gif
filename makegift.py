import imageio
import os
images=[]
for gif in os.listdir('gif'):
 image=imageio.imread(f'gif/{gif}')
 images.append(image)
imageio.mimsave('fun.gif',images)