from PIL import Image

img = Image.open('MantraLounge.jpg')
area = (140, 140, 410, 410)
cropped_img = img.crop(area)

img.show()
cropped_img.show()
