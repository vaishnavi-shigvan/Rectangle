'''
Write a python class Rectangle.The class will have instance variables length & width & a method which will compute the area of a rectangle.Include the constructor & other required methods to set & get class attributes .Also,include a method isSquare(),which returns a boolean value indicating if the shape is a square(Hint:use @property)

'''

class rectangle:
    def __init__(self, l=' ',w=''):
     self.__length = l
     self.__width = w

    @property    
    def length(self):
     return self.__length

    @length.setter
    def length(self,value):
     self.__length = value

    @property    
    def width(self):
     return self.__width

    @width.setter
    def width(self,value):
     self.__width = value 
        
    def rectarea(self):
     print("area of rectangle is:",(self.__length*self.__width))

    def isSquare(self):
     if(self.__length == self.__width):
       return True
     else:
       return False

rect = rectangle()
rect.length = float(input('Enter length:'))
rect.width  = float(input('Enter breadth:'))
rect.rectarea()

