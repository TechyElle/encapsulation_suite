from modules.pet import Pet


def prompt_for_pet(pet_number):
    """Register one pet, re-prompting until age is valid."""
    pet = Pet()

    print(f"\n--- Register Pet {pet_number} ---")
    pet_name = input("Enter pet name: ")
    pet.set_name(pet_name)

    animal_type = input("Enter pet type: ")
    pet.set_animal_type(animal_type)

    while True:
        try:
            age_input = input("Enter pet age (years): ")
            age = int(age_input)
            pet.set_age(age)
            break
        except ValueError:
            print("Invalid age. Age must be a non-negative integer.")

    return pet


def main():
    """Pet Clinic demo."""
    pet_one = prompt_for_pet(1)
    pet_two = prompt_for_pet(2)

    print("\n--- Pet Profiles ---")
    print(pet_one.get_profile())
    print()
    print(pet_two.get_profile())


if __name__ == "__main__":
    main()

