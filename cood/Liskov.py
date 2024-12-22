class Bird:
    def eat(self):
        pass
class Flying_Bird(Bird):
    def fly(self):
        pass
class swan(Flying_Bird):
    def eat(self):
        return "i can eat "
    def FLying_Brid(self):
        return "i can fly "
class penguin(Bird):
    def eat(self):
        return "i can eat "
   
obj1=Bird()
obj2=Flying_Bird()
obj3=swan()
obj4=penguin()
print(obj3.eat(), obj3. FLying_Brid())
print(obj4.eat())