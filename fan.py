class Fan:
    """A class representing a fan with speed, radius, color, and on/off state."""

    # Constants for fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        """Initialize a Fan object with default or specified values."""
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        """Return the current speed of the fan."""
        return self.__speed

    def set_speed(self, speed):
        """Set the speed of the fan."""
        self.__speed = speed

    def get_radius(self):
        """Return the radius of the fan."""
        return self.__radius

    def set_radius(self, radius):
        """Set the radius of the fan."""
        self.__radius = radius

    def get_color(self):
        """Return the color of the fan."""
        return self.__color

    def set_color(self, color):
        """Set the color of the fan."""
        self.__color = color

    def get_on(self):
        """Return whether the fan is on."""
        return self.__on

    def set_on(self, on):
        """Set whether the fan is on."""
        self.__on = on

    def __str__(self):
        """Return a string representation of the fan."""
        status = "on" if self.__on else "off"
        return (f"Fan[speed={self.__speed}, radius={self.__radius}, "
                f"color={self.__color}, on={status}]")


def test_fan():
    """Test program that creates and displays two Fan objects."""

    # Create first fan: max speed, radius 10, yellow, on
    fan1 = Fan(Fan.FAST, 10, "yellow", True)

    # Create second fan: medium speed, radius 5, blue, off
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    # Display fan1 properties
    print("Fan 1:")
    print(f"  Speed: {fan1.get_speed()}")
    print(f"  Radius: {fan1.get_radius()}")
    print(f"  Color: {fan1.get_color()}")
    print(f"  On: {fan1.get_on()}")

    # Display fan2 properties
    print("\nFan 2:")
    print(f"  Speed: {fan2.get_speed()}")
    print(f"  Radius: {fan2.get_radius()}")
    print(f"  Color: {fan2.get_color()}")
    print(f"  On: {fan2.get_on()}")


if __name__ == "__main__":
    test_fan()
