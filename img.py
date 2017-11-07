from PIL import Image, ImageFilter
import ImageEnhance
from ocr.ocr import image_to_string
import sys

fname = sys.argv[1]

im = Image.open(fname)

size_tuple = [im.size[0] *2, im.size[1]*2]
im = im.resize(size_tuple)

contr = ImageEnhance.Contrast(im)
im = contr.enhance(3)

brght = ImageEnhance.Brightness(im)
im = brght.enhance(2)

im= im.filter(ImageFilter.SHARPEN)

im = im.convert('1')

im.show()

im.save("test_processed.jpeg")

print image_to_string(Image.open('test_processed.jpeg'))

