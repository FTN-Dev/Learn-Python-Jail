# rumus buatan sendiri wok.
from PIL import Image, ImageChops

def get_xor(image_1, image_2):

    i1 = ImageChops.invert(image_1)
    i2 = ImageChops.invert(image_2)

    return ImageChops.invert(ImageChops.add(ImageChops.subtract(i2, i1), ImageChops.subtract(i1, i2)))

im2 = Image.open('img/flag_7ae18c704272532658c10b5faad06d74.png')
im1 = Image.open('img/lemur_ed66878c338e662d3473f0d98eedbd0d.png')

im3 = get_xor(im1, im2)
im3.save("imageflag.png")