class Car:
    """A class representing a car with year model, make, and current speed."""

    def __init__(self, year_model, make, driver_name=""):
        """Initialize a Car object with year model and make. Speed defaults to 0."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self._driver_name = driver_name

    def accelerate(self):
        """Increase the car's speed by 5."""
        self.__speed += 5

    def brake(self):
        """Decrease the car's speed by 5, never below 0."""
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        """Return the current speed of the car."""
        return self.__speed

    def status(self):
        """Print the car race status."""
        return (
            f"Driver: {self._driver_name} | "
            f"Car: {self.__year_model} {self.__make} | "
            f"Speed: {self.__speed} mph"
        )

