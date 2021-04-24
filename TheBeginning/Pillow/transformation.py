from PIL import Image

bike_rear = Image.open('bike_rear.jpg')
bike_wheel = Image.open('bike_wheel.jpg')

print(bike_wheel.size)
resize_wheel = bike_wheel.resize((400, 400))
flip_wheel = bike_wheel.transpose(Image.FLIP_LEFT_RIGHT)
rotate_wheel = bike_wheel.transpose(Image.ROTATE_90)

resize_wheel.show()
flip_wheel.show()
rotate_wheel.show()

