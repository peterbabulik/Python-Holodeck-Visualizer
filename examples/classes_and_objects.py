"""
Classes and Objects Example for pyMeow

This example demonstrates object-oriented programming concepts in Python,
showing how classes define blueprints for objects with attributes and methods.

When loaded in pyMeow:
- Class definitions appear as special container blocks
- Methods within classes are shown as nested FunctionBlocks
- The __init__ constructor is clearly visible
- Object instantiation and method calls are visualized
- The relationship between classes and their instances is clear

This example helps learners understand:
- What classes and objects are
- How to define class attributes and methods
- The concept of self and instance variables
- Object instantiation and method calling
- Inheritance basics

The visual blocks make the abstract concept of OOP more concrete,
showing the structure and relationships clearly.
"""

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, species):
        """Initialize an animal with a name and species."""
        self.name = name
        self.species = species
        self.is_hungry = True
    
    def speak(self):
        """Make the animal speak (generic sound)."""
        print(self.name + " makes a sound")
    
    def eat(self, food):
        """Feed the animal."""
        print(self.name + " is eating " + food)
        self.is_hungry = False
    
    def sleep(self):
        """Make the animal sleep."""
        print(self.name + " is sleeping... Zzz")
    
    def info(self):
        """Display information about the animal."""
        print("Name:", self.name)
        print("Species:", self.species)
        print("Hungry:", self.is_hungry)


class Dog(Animal):
    """Dog class that inherits from Animal."""
    
    def __init__(self, name, breed):
        """Initialize a dog with a name and breed."""
        # Call parent class constructor
        super().__init__(name, "Canine")
        self.breed = breed
        self.tricks = []
    
    def speak(self):
        """Dogs bark!"""
        print(self.name + " says: Woof! Woof!")
    
    def add_trick(self, trick):
        """Teach the dog a new trick."""
        self.tricks.append(trick)
        print(self.name + " learned: " + trick)
    
    def perform_tricks(self):
        """Show all the tricks the dog knows."""
        if len(self.tricks) > 0:
            print(self.name + " can do these tricks:")
            for trick in self.tricks:
                print("- " + trick)
        else:
            print(self.name + " doesn't know any tricks yet")


class Cat(Animal):
    """Cat class that inherits from Animal."""
    
    def __init__(self, name, color):
        """Initialize a cat with a name and color."""
        super().__init__(name, "Feline")
        self.color = color
        self.mood = "neutral"
    
    def speak(self):
        """Cats meow!"""
        print(self.name + " says: Meow!")
    
    def purr(self):
        """Make the cat purr."""
        self.mood = "happy"
        print(self.name + " is purring contentedly")
    
    def scratch(self, object):
        """Cat scratches something."""
        print(self.name + " scratches the " + object)
        self.mood = "playful"


class Student:
    """A simple Student class for managing student records."""
    
    def __init__(self, name, age, grade):
        """Initialize a student."""
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = []
        self.grades = {}
    
    def add_subject(self, subject):
        """Add a subject to the student's curriculum."""
        self.subjects.append(subject)
        self.grades[subject] = 0
    
    def set_grade(self, subject, grade):
        """Set the grade for a specific subject."""
        if subject in self.subjects:
            self.grades[subject] = grade
            print("Grade updated for", subject)
        else:
            print("Subject not found!")
    
    def get_average_grade(self):
        """Calculate the average grade across all subjects."""
        if len(self.grades) > 0:
            total = sum(self.grades.values())
            average = total / len(self.grades)
            return average
        return 0
    
    def report_card(self):
        """Print the student's report card."""
        print("\n=== Report Card ===")
        print("Student:", self.name)
        print("Age:", self.age)
        print("Grade Level:", self.grade)
        print("\nSubject Grades:")
        for subject in self.subjects:
            grade = self.grades[subject]
            print("- " + subject + ":", grade)
        avg = self.get_average_grade()
        print("Average Grade:", avg)


# Example usage of the classes

# Create animal objects
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Orange")

# Use animal methods
print("=== Pet Introduction ===")
my_dog.info()
my_cat.info()

print("\n=== Pet Sounds ===")
my_dog.speak()
my_cat.speak()

print("\n=== Feeding Time ===")
my_dog.eat("dog food")
my_cat.eat("fish")

print("\n=== Teaching Tricks ===")
my_dog.add_trick("sit")
my_dog.add_trick("roll over")
my_dog.add_trick("fetch")
my_dog.perform_tricks()

print("\n=== Cat Activities ===")
my_cat.purr()
my_cat.scratch("sofa")

# Create and use student object
print("\n=== Student Management ===")
student1 = Student("Alice", 15, 10)
student1.add_subject("Math")
student1.add_subject("Science")
student1.add_subject("English")

student1.set_grade("Math", 95)
student1.set_grade("Science", 88)
student1.set_grade("English", 92)

student1.report_card()