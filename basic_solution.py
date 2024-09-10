# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.breed} {self.name} barks"

# Main
def main():
    dog = Dog("Buddy", "Pitbull")

    # Buddy barks
    print(dog.speak())

main()