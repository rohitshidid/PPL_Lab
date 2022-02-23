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
        print("Kangaroo's Growl!!\n")

class Lion(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Lions's Roar!!\n")

class Dog(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Dog's bark!!\n")
        
class Cat(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Cat's Meow!!\n")

class Monkey(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Monkey's Chatter!!\n")

class Horse(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)

    def speak(self):
        print("Horse's Neigh!!\n")

class Cow(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Cow's Moo!!\n")

class Duck(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Duck's Quack!!\n")

class Goat(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name=name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Goats's Baa!!\n")

class Peacock(Animals):
    def __init__(self, name, legs, eyes, ears):
        super().__init__(legs, eyes, ears)
        self.name = name

    def info(self):
        Animals.info(self, self.name)
        
    def speak(self):
        print("Peacock's Scream!!\n")
        
kangaroo = Kangaroo("Kangaroo",5,2,2)
kangaroo.info()
kangaroo.speak()

goat = Goat("Goat",4,2,2)
goat.info()
goat.speak()

dog = Dog("Dog",4,2,2)
dog.info()
dog.speak()

cat = Cat("Cat",4,2,2)
cat.info()
cat.speak()

lion = Lion("Lion",4,2,2)
lion.info()
lion.speak()

monkey = Monkey("Monkey",2,2,2)
monkey.info()
monkey.speak()

horse = Horse("Horse",4,2,2)
horse.info()
horse.speak()

cow = Cow("Cow",4,2,2)
cow.info()
cow.speak()

duck = Duck("Duck",2,2,2)
duck.info()
duck.speak()

peacock = Peacock("Peacock",4,2,2)
peacock.info()
peacock.speak()
