# Parent Class
class Animal:
    def eat(self):
        return "This animal is eating"

# Parent Class
class CanFly:
    def fly(self):
        return "This animal can fly"

# Child Class
class Bird(Animal, CanFly):
    def chirp(self):
        return "The bird chirps"

def main():
    bird = Bird()
    print(bird.eat())    # This animal is eating
    print(bird.fly())    # This animal can fly
    print(bird.chirp())  # The bird chirps

main()
