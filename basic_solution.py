# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

# Main
def main():
    dog = Dog("Buddy")

    print(dog.speak())  # Buddy barks

main()