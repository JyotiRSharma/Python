from PIL import Image

mantra = Image.open('MantraLounge.jpg')
r, g, b = mantra.split()

print(mantra.mode)

r.show()
g.show()
b.show()
mantra.show()

# Just adding information about RGB
