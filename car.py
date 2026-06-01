class Car:
    """A class representing a car with year model, make, and current speed."""

    def __init__(self, year_model, make):
        """Initialize a Car object with year model and make. Speed defaults to 0."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        """Increase the car's speed by 5."""
        self.__speed += 5

    def brake(self):
        """Decrease the car's speed by 5."""
        self.__speed -= 5

    def get_speed(self):
        """Return the current speed of the car."""
        return self.__speed


def test_car():
    """Test program that demonstrates car acceleration and braking."""

    # Create a car object
    car = Car(2024, "Toyota")

    print(f"Car: {car._Car__year_model} {car._Car__make}")
    print("\nAccelerating 5 times:")

    # Call accelerate 5 times and display speed
    for i in range(5):
        car.accelerate()
        print(f"  After acceleration #{i + 1}: {car.get_speed()} mph")

    print("\nBraking 5 times:")

    # Call brake 5 times and display speed
    for i in range(5):
        car.brake()
        print(f"  After brake #{i + 1}: {car.get_speed()} mph")


if __name__ == "__main__":
    test_car()
