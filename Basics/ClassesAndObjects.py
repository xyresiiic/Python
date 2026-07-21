class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def show_info(self):
        print(f"Dog Info -> Name: {self.name}, Breed: {self.breed}, Age: {self.age}")


print("--- Creating our first object ---")
my_dog = Dog("Buddy", "Golden Retriever", 3)

print("My dog's name is:", my_dog.name)

my_dog.bark()
my_dog.show_info()


print("\n--- Creating a second object ---")
neighbor_dog = Dog("Lucy", "Poodle", 5)

neighbor_dog.bark()
neighbor_dog.show_info()
