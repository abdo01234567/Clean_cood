from abc import ABC, abstractmethod 


class Shape(ABC):

	@abstractmethod
	def number_sides (self): #عددالاضلاع
		pass 


class Triangle(Shape):

	# overriding abstract method 
	def  number_sides(self):
		print("Triangle:Ihave 3 sides") 

        
      

class square(Shape): 

	# overriding abstract method 
	def  number_sides(self): 
		print("square:Ihave 4 sides") 


class rectangular(Shape):
	def  number_sides(self): 
		print("square:Ihave 4 sides") 

    
    

	# overriding abstract method 






# Driver code 
R = Triangle() 
R. number_sides() 

 

R = square() 
R. number_sides() 

K = rectangular() 
K. number_sides() 
