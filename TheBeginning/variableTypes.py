class Girl:
    gender = 'female'
    '''
        Class variables are common to the entire class
        They stay the same for each object
    '''

    def __init__(self, name):
        self.name = name

    '''
        Instance variables are not common
        They differ from each object
    '''


v = Girl('Vibha')
s = Girl('Sharin')

print(v.gender)
print(v.name)

print(s.gender)
print(s.name)

