# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child Class
class Dog:
    def speak(self):
        return f"{self.name} barks"

# Main
def main():
    dog = Dog("Buddy")

    # Buddy barks
    print(dog.speak())

main()