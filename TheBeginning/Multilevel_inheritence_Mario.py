class Mario():

    def move(self):
        print("Im moving")


class Shroom():

    def eat_shroom(self):
        print("eat mushroom")


class BigMario(Mario, Shroom):
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()
