from PIL import Image

wave = Image.open('RidetheWave_v01.jpg')
mantra = Image.open('MantraLounge.jpg')

area = (300, 10, 844, 554)

wave.paste(mantra, area)

print(wave.size)
print(mantra.size)

wave.show()
