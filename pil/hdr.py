#-*- coding: utf-8 -*-

import PIL
from PIL import Image, ImageFilter
class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"
    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds
    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)

simg = 'example.png'
dimg = 'demo_blur.png'
image = Image.open(simg)
size = image.size
blur_pixels = 20
new_size = (blur_pixels * 2 + size[0], blur_pixels * 2 + size[1])
image_blur = Image.new('RGBA', new_size)
image_blur.paste(image, (blur_pixels, blur_pixels), image)
result_image = image_blur.copy()
bounding = (0,0,new_size[0], new_size[1])
image_blur = image_blur.filter(MyGaussianBlur(radius=blur_pixels, bounds=bounding))
image_blur_little = image_blur.filter(MyGaussianBlur(radius=2, bounds=bounding))


import math
def merge_blur(*imgs):
    blur_factor = 1.0
    size = len(imgs)
    pixels = [img.load() for img in imgs]
    def trans(c, s):
        s += 100
        s = min(255, s)
        f = (math.cos(s / 255 * 2 * math.pi) + 1) * 0.5
        return [f * v for v in c]
    for x in range(imgs[0].size[0]):
        for y in range(imgs[0].size[1]):
            colors = [pixel[x, y] for pixel in pixels]
            c = [0,0,0]
            for i in range(3):
                c[i] = colors[0][i] * 0.2 + colors[1][i] * blur_factor + colors[2][i] * blur_factor
            '''
            strength = sum(c) / 3.
            c = trans(c, strength)
            '''
            c.append(255)
            pixels[0][x, y] = tuple([int(v) for v in c])
merge_blur(result_image, image_blur, image_blur_little)
#result_image = Image.blend(result_image, image_blur, 1)
image_blur.save('blur.png')
result_image.save(dimg)
'''
bounding = (blur_pixels, blur_pixels, blur_pixels + size[0], blur_pixels + size[1])
image = image.resize(new_size)
print new_size
image = image.filter(MyGaussianBlur(radius=blur_pixels, bounds=bounding))
image.save(dimg)
print dimg, 'success'
'''