class Parent():

    def last_name(self):
        print('Sharma')


class Child(Parent):  # I'm inheriting the parent class

    def first_name(self):
        print('Jyoti Ranjan')

    # def last_name(self):  # I can override the inherited method.
    #     print('Das')


jyoti = Child()
print(jyoti.first_name())
print(jyoti.last_name())

