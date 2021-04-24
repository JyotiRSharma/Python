from PIL import Image

img = Image.open('MantraLounge.jpg')
print(img.size)
print(img.format)

img.show()
