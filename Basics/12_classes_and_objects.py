# working with classes and objects

# A "Class" is like a blueprint for creating objects.
# An "Object" is an instance created from the blueprint.

# Let's create a blueprint for a Dog
class Dog:
    
    # This is a special method called when a new Dog object is created.
    # It initializes the object's attributes (variables).
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    # This is a method (a function inside a class) that the Dog can do
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
        
    def show_info(self):
        print(f"Dog Info -> Name: {self.name}, Breed: {self.breed}, Age: {self.age}")


print("--- Creating our first object ---")
# Now we create an actual Dog object using the blueprint
my_dog = Dog("Buddy", "Golden Retriever", 3)

# We can access the variables inside our object using a dot (.)
print("My dog's name is:", my_dog.name)

# We can call the methods we defined
my_dog.bark()
my_dog.show_info()


print("\n--- Creating a second object ---")
# We can use the same blueprint to make a completely different dog
neighbor_dog = Dog("Lucy", "Poodle", 5)

neighbor_dog.bark()
neighbor_dog.show_info()
