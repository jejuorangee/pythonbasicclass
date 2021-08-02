class Korean:
    country = 'korea'

#    def __init__(self, name, age, address):
#        self.name = name
#        self.age = age
#        self.address = address

    @classmethod
        def trip(cls,country):
            if cls.country == country:
                print('domastic')
            else:
                print('abroad')

Korean.trip('korea')
Korean.trip('america')
# man = Korean('Hong', 35, 'seoul')
# korean.name
# print(man.name)
# print(Korean.country)