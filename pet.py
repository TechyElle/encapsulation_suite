class Pet:
    """A class representing a pet with name, animal type, and age."""

    def __init__(self):
        """Initialize a Pet object with empty attributes."""
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        """Set the name of the pet."""
        self.__name = name

    def set_animal_type(self, animal_type):
        """Set the type of animal the pet is."""
        self.__animal_type = animal_type

    def set_age(self, age):
        """Set the age of the pet."""
        self.__age = age

    def get_name(self):
        """Return the name of the pet."""
        return self.__name

    def get_animal_type(self):
        """Return the type of animal the pet is."""
        return self.__animal_type

    def get_age(self):
        """Return the age of the pet."""
        return self.__age


def main():
    """Interactive program to create a pet and display its information."""

    # Create a pet object
    pet = Pet()

    # Prompt user for pet information
    name = input("What is your pet's name? ")
    pet.set_name(name)

    animal_type = input("What type of animal is your pet? ")
    pet.set_animal_type(animal_type)

    age = int(input("How old is your pet? "))
    pet.set_age(age)

    # Display the pet's information
    print("\nPet Information:")
    print(f"  Name: {pet.get_name()}")
    print(f"  Animal Type: {pet.get_animal_type()}")
    print(f"  Age: {pet.get_age()}")


if __name__ == "__main__":
    main()
