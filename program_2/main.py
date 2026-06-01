from modules.car import Car


def main():
    """Race Tracker demo."""
    car_1 = Car(2020, "Honda", driver_name="Ava")
    car_2 = Car(2018, "Ford", driver_name="Noah")

    max_speed_car_1 = 0
    max_speed_car_2 = 0

    print("--- Race Start ---")

    for action_number in range(1, 6):
        car_1.accelerate()
        max_speed_car_1 = max(max_speed_car_1, car_1.get_speed())
        print(f"\nAction {action_number}: Car 1 accelerate")
        print(car_1.status())

        car_2.accelerate()
        max_speed_car_2 = max(max_speed_car_2, car_2.get_speed())
        print(f"\nAction {action_number}: Car 2 accelerate")
        print(car_2.status())

    for action_number in range(1, 6):
        car_1.brake()
        print(f"\nAction {action_number}: Car 1 brake")
        print(car_1.status())

        car_2.brake()
        print(f"\nAction {action_number}: Car 2 brake")
        print(car_2.status())

    print("\n--- Race Results ---")
    if max_speed_car_1 > max_speed_car_2:
        winner_driver_name = car_1._driver_name
        print(f"Winner: {winner_driver_name} with {max_speed_car_1} mph")
    elif max_speed_car_2 > max_speed_car_1:
        winner_driver_name = car_2._driver_name
        print(f"Winner: {winner_driver_name} with {max_speed_car_2} mph")
    else:
        print(f"It's a tie! Both reached {max_speed_car_1} mph")



if __name__ == "__main__":
    main()

