class Animal:

    def Eat(self):
        print("Chew")
    
    def Sleep(self):
        print("Zzz")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
    
class Bird(Animal):
    def __init__(self):
        super().__init__()

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
class Dog(Mammal):
    def __init__(self):
        super().__init__()

    def Eat(self):
        print("bark bark")
    
    def Sleep(self):
        print("woooooooffffff")

class Pelican(Bird):
    def __init__(self):
        super().__init__()

    def Eat(self):
        print("squak")
    
    def Sleep(self):
        print("squaaaaa")

class Shark(Fish):
    def __init__(self):
        super().__init__()
    
    def Eat(self):
        print("nom nom")

    def Sleep(self):
        print("bubble bubble")

def animalToEat(animal):
    animal.Eat()

def main():
    dog = Dog()
    shark = Shark()
    pelican = Pelican()
    bird = Bird()
    mammal = Mammal()
    fish = Fish()
    animal = Animal()

    animal_list = [animal, fish, mammal, bird, pelican, shark, dog]

    for animal in animal_list:
        animalToEat(animal)
    
main()