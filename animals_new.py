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
    
class Kangaroo(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Dog Barks!!\n")

class Lion(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("cat meow!!\n")

class Dog(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Horse Neigh!!\n")
        
class Cat(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Rabbit Grunt!!\n")

class Monkey(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Cow Moo!!\n")

class Horse(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Tiger Growl!!\n")

class Cow(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Elephant Trumpets\n")

class Duck(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Lion Roar!\n")

class Goat(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name=name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Wolf Howl!!\n")

class Peacock(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Deer Grunt\n")
        
kangaroo = Kangaroo("Dog",5,2,2)
kangaroo.info()
kangaroo.speak()

goat = Goat("Cat",4,2,2)
goat.info()
goat.speak()

dog = Dog("Horse",4,2,2)
dog.info()
dog.speak()

cat = Cat("Rabbit",4,2,2)
cat.info()
cat.speak()

lion = Lion("Cow",4,2,2)
lion.info()
lion.speak()

monkey = Monkey("Tiger",2,2,2)
monkey.info()
monkey.speak()

horse = Horse("Lion",4,2,2)
horse.info()
horse.speak()

cow = Cow("Elephant",4,2,2)
cow.info()
cow.speak()

duck = Duck("Wolf",2,2,2)
duck.info()
duck.speak()

peacock = Peacock("Deer",4,2,2)
peacock.info()
peacock.speak()
