from PIL import Image
from PIL import ImageFilter

bike_rear = Image.open('bike_rear.jpg')

blur = bike_rear.filter(ImageFilter.BLUR)
detail = bike_rear.filter(ImageFilter.DETAIL)
edges = bike_rear.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()
