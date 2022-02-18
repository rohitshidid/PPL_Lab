import math
import turtle

from cv2 import circle
t = turtle.Turtle()


class shape:
    def __init__(self):
        print( "Hey there, I am a shape.")

#--------------------------------------------------------------------------------------

class oval(shape):
    def __init__(self,radius):
        super().__init__()
        self.radi1 = radius
        print('I have to vertices')
        print('I am an oval')

    def __stats__(self):               # Horizontal Oval
        turtle.right(45)
        for loop in range(2):
            turtle.circle(self.radi1,90)
            turtle.circle(self.radi1/2,90)
        turtle.clearscreen()

class round(shape):
    def __init__(self,radius):
        super().__init__()
        self.radi1 = radius
        print('I have to vertices')
        print('I am an circle')

    def __stats__(self):
        my_pen = turtle.Turtle()
        my_pen.circle(self.radi1)
        print('My permieter is',2*math.pi*self.radi1,'units')
        print('My area is',math.pi*(self.radi1**2),'sq.units')
        turtle.clearscreen()
        
#-----------------------------------------------------------------------------------

class polygon(shape):                       # Inheritance
    def __init__(self,sides,side_length):
        super().__init__()
        self.sides = sides
        self.side_length = side_length
        print('I have',sides,'sides.')
        angle = "%.2f"%(360/sides)
        print('The angle between my adjacent edges is',angle,'deg.')
    
    def draw1(self):
        pen = turtle.Turtle()
        angle = 360/self.sides
        for i in range(self.sides):
            pen.backward(self.side_length)
            pen.right(angle)
    
    def draw2(self):
        pen = turtle.Turtle()
        angle = 360/self.sides
        for i in range(self.sides):
            pen.forward(self.side_length)
            pen.right(angle)
    
    def __stats__(self):                #Encapsulation
        perimeter = self.sides*self.side_length
        print('my perimeter is',perimeter,'units.')
        area = "%.2f" % (perimeter/4*self.side_length/math.tan(180/self.sides))
        print('my area is',area,'sq.units.\n')
        

class triangle(polygon):                #multilevel_inheritance
    def __init__(self, side_length,sides = 3 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Triangle.')


class square(polygon):
    def __init__(self, side_length,sides = 4 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Square.')

class pentagon(polygon):
    def __init__(self, side_length,sides = 5 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Pentagon.')

class hexagon(polygon):
    def __init__(self, side_length,sides = 6 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a hexaagon.')

class septagon(polygon):
    def __init__(self, side_length,sides = 7 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Septagon.')

class octagon(polygon):
    def __init__(self, side_length,sides = 8 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Octagon.')

class nonagon(polygon):
    def __init__(self, side_length,sides = 9 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Nonagon.')

class decagon(polygon):
    def __init__(self, side_length,sides = 10 ):
        self.sides = sides
        super().__init__( side_length,sides)
        print('Yes, I am a Decagon.')

#------------------------------------------------------------------------------------------------------------
threed = ['cube','cuboid','cylinder']

class threeD:
    def __init__(self) -> None:
        print('I am a 3-dimensional object')

class cylinder(threeD):
    def __init__(self,radius,height) -> None:
        super().__init__()
        self.radius = radius
        self.height = height
    print('I am a cylinder')

    def __stats__(self):
        my_pen = turtle.Turtle()        
        my_pen.forward(self.height)

        my_pen.circle(self.radius)

        my_pen.setheading(90)
        my_pen.penup()
        my_pen.forward(2*self.radius)
        my_pen.pendown()
        my_pen.setheading(180)

        my_pen.forward(self.height)

        my_pen.circle(self.radius, extent=180)  #  Draw 1/2 of the bottom/circle
        turtle.clearscreen()
        print('my surface area is',2*math.pi*self.radius*(self.radius+self.height))
        print('My volume is',math.pi*(self.radius**2)*self.height)


class cuboid(threeD):
    def __init__(self,side1,side2,side3) -> None:
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if(side1==side2==side3):
            print('I have 8 faces and all my sides are equal')
            print('I am a cube.')
        else:
            print('I have 8 faces and my sides are unequal')
            print('I am a cuboid.')
        
        
    def __stats__(self):
        my_pen = turtle.Turtle()
# forming front rectangle face
        for i in range(2):
            my_pen.forward(self.side1)
            my_pen.left(90)
            my_pen.forward(self.side2)
            my_pen.left(90)
  
        # bottom left side
        my_pen.goto(1/2*self.side3,1/2*self.side3)
  
# forming back rectangle face
        for i in range(2):
            my_pen.forward(self.side1)
            my_pen.left(90)
            my_pen.forward(self.side2)
            my_pen.left(90)
# bottom right side
        my_pen.goto(1/2*self.side3 + self.side1,1/2*self.side3)
        my_pen.goto(self.side1,0)
  
# top right side
        my_pen.goto(self.side1,self.side2)
        my_pen.goto(self.side1+1/2*self.side3,self.side3*(1/2)+self.side2)
  
# top left side
        my_pen.goto(1/2*self.side3,1/2*self.side3+self.side2)
        my_pen.goto(0,self.side2)
        turtle.clearscreen()

        print('my surface area is',2*(self.side1**2+self.side2**2+self.side3**2),'sq.units')
        print('my surface area is',(self.side1*self.side2*self.side3),'cu.units')

#-------------------------------------------------------------------------------------------------

circle = round(100)
circle.__stats__()

oval = oval(100)
oval.__stats__()

#------------------------------------------------------------------------------------------------------------

for i in range(3,11):
    j = 250
    if(i==3):
        poly1 = triangle(i,j-i*18)
    elif(i==4):
        poly1 = square(i,j-i*18)
    elif(i==5):
        poly1 = pentagon(i,j-i*18)
    elif(i==6):
        poly1 = hexagon(i,j-i*18)
    elif(i==7):
        poly1 = septagon(i,j-i*18)
    elif(i==8):
        poly1 = octagon(i,j-i*18)
    elif(i==9):
        poly1 = nonagon(i,j-i*18)
    else:
        poly1 = decagon(i,j-i*18)
    poly1.__stats__()
    if(i%2==1):
        poly1.draw1()
    else:
        poly1.draw2()
    turtle.clearscreen()

#----------------------------------------------------------------------------------------

cyl = cylinder(80,120)
cyl.__stats__()
turtle.clearscreen()

cubo = cuboid(100,100,100)
cubo.__stats__()
cubo = cuboid(100,100,300)
cubo.__stats__()
turtle.clearscreen()