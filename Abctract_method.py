# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:50:56 2023

@author: ascom
"""

"""
An abstract class can be considered a blueprint for other classes. 
It allows you to create a set of methods that must be created within 
any child classes built from the abstract class.

A class that contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation.

By default, Python does not provide abstract classes. Python comes with a module that 
provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
"""

# Python program showing 
# abstract base class work 

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
