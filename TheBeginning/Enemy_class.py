class Enemy:
    life = 3

    def attack(self):
        self.life -= 1
        print("Ouch!", self.life, " life left")

        if self.life <= 0:
            print("I'm dead :(")


enemy1 = Enemy()
enemy1.attack()
enemy1.attack()
enemy1.attack()

enemy2 = Enemy()
enemy2.attack()

