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
        if age < 0:
            raise ValueError("Age cannot be negative.")
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

    def get_profile(self):
        """Return a formatted pet profile."""
        return (
            f"🐾 Name: {self.__name}\n"
            f"   Type: {self.__animal_type}\n"
            f"   Age:  {self.__age} years old"
        )

