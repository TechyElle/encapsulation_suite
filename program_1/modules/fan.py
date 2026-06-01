class Fan:
    """A class representing a fan with speed, radius, color, and on/off state."""

    # Constants for fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False, room_name=""):
        """Initialize a Fan object with default or specified values."""
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
        self._room_name = room_name

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

    def toggle_power(self):
        """Flip the power state of the fan."""
        self.set_on(not self.get_on())

    @staticmethod
    def _speed_label(speed):
        if speed == Fan.SLOW:
            return "SLOW"
        if speed == Fan.MEDIUM:
            return "MEDIUM"
        return "FAST"

    def __repr__(self):
        power_status = "ON" if self.get_on() else "OFF"
        return (
            "Fan("
            f"room={self._room_name!r}, "
            f"speed={self._speed_label(self.get_speed())}, "
            f"radius={self.get_radius()}, "
            f"color={self.get_color()}, "
            f"power={power_status}"
            ")"
        )

    def __str__(self):
        """Return a string representation of the fan."""
        status = "on" if self.__on else "off"
        return (
            f"Fan[speed={self.__speed}, radius={self.__radius}, "
            f"color={self.__color}, on={status}]"
        )

