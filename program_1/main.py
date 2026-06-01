from modules.fan import Fan


def main():
    """Smart Fan Controller demo."""
    living_room_fan = Fan(speed=Fan.SLOW, radius=10, color="yellow", on=True, room_name="Living Room")
    bedroom_fan = Fan(speed=Fan.MEDIUM, radius=7, color="white", on=False, room_name="Bedroom")
    kitchen_fan = Fan(speed=Fan.FAST, radius=6, color="red", on=True, room_name="Kitchen")

    print("--- Initial fan states ---")
    print(living_room_fan)
    print(bedroom_fan)
    print(kitchen_fan)

    print("\n--- Toggling Bedroom fan power ---")
    bedroom_fan.toggle_power()

    print("\n--- All fans (using __repr__) ---")
    for fan in (living_room_fan, bedroom_fan, kitchen_fan):
        print(fan.__repr__())


if __name__ == "__main__":
    main()

