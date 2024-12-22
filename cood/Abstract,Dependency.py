from abc import ABC ,abstractmethod
class Veical(ABC):
    @abstractmethod 
    def start(self):
        pass
    @abstractmethod 
    def Stop(self):
        
        pass
class car(Veical):
    def start(self):
        return "car starting "
    def Stop(self):
        
        return"car stoping"
class Bike(Veical):
    def start(self):
        return "Bike starting "
    def Stop(self):
        
        return"bike stoping"
car1=car()
     
bike=Bike()
print(car1.start(),car1.Stop())
print(bike.start(),bike.Stop())