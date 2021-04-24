from PIL import Image

bike_rear = Image.open('bike_rear.jpg')
black_white = bike_rear.convert('L')

black_white.show()
