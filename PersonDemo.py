class Person : 
    def who_am_i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person()

boy.who_am_i('jhon', 15, '123-1234', 'toronto')

print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)