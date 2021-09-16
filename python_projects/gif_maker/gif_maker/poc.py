#!/usr/bin/env python
import imageio
from os import listdir

if __name__ == '__main__':

    image_dir = "L:\\repos\\personal\\python_projects\\gif_maker\\images"
    image_files = [f"{image_dir}\\{x}" for x in listdir(image_dir)]
    images = []

    for i in image_files:
        images.append(imageio.imread(i))
    
    output_file = "./test.gif"

    imageio.mimsave(output_file, images, duration=0.2)
    
    
