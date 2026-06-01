class Car:
    """A car with year model, make, and current speed."""

    def __init__(self, year_model, make, driver_name=""):
        """Initialize a Car object."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__driver_name = driver_name

    def accelerate(self):
        """Increase the car speed by 5."""
        self.__speed += 5

    def brake(self):
        """Decrease the car speed by 5, never below 0."""
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        """Return the current speed of the car."""
        return self.__speed

    def get_driver_name(self):
        """Return the name of the driver."""
        return self.__driver_name

    def status(self):
        """Return the current race status string."""
        return (
            f"Driver: {self.__driver_name} | "
            f"Car: {self.__year_model} {self.__make} | "
            f"Speed: {self.__speed} mph"
        )

