from xml.dom.minidom import Element


class Animals:
    def __init__(self, legs, eyes, ears):
        self.__legs = legs
        self.__eyes = eyes
        self.__ears = ears
    
    def info(self, name):
        print(name, " Info:")
        print("Legs: ", self.__legs)
        print("Eyes: ", self.__eyes)
        print("Ears: ", self.__ears)
    
    def speak(self): 
        pass
    
class Dog(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Dog Barks!!\n")

class Cat(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("cat meow!!\n")

class Horse(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Horse Neigh!!\n")
        
class Rabbit(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Rabbit Grunt!!\n")

class Cow(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Cow Moo!!\n")

class Tiger(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Tiger Growl!!\n")

class Elephant(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Elephant Trumpets\n")

class Lion(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Lion Roar!\n")

class Wolf(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name=name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Wolf Howl!!\n")

class Deer(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Deer Grunt\n")
        
Dog = Dog("Dog",5,2,2)
Dog.info()
Dog.speak()

Cat = Cat("Cat",4,2,2)
Cat.info()
Cat.speak()

Horse = Horse("Horse",4,2,2)
Horse.info()
Horse.speak()

Rabbit = Rabbit("Rabbit",4,2,2)
Rabbit.info()
Rabbit.speak()

Cow = Cow("Cow",4,2,2)
Cow.info()
Cow.speak()

Tiger = Tiger("Tiger",2,2,2)
Tiger.info()
Tiger.speak()

Lion = Lion("Lion",4,2,2)
Lion.info()
Lion.speak()

Elephant = Elephant("Elephant",4,2,2)
Elephant.info()
Elephant.speak()

Wolf = Wolf("Wolf",2,2,2)
Wolf.info()
Wolf.speak()

Deer = Deer("Deer",4,2,2)
Deer.info()
Deer.speak()
