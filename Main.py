#from converter import convert_temperature
#from history import show_history


def main():
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. View History")
    print("5. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        # View history
        if choice == "4":()
        continue

        # Exit
        if choice == "5":
            print("Thank you for using Temperature Converter!")
            break

        # Available units
        units = {
            "1": "C",
            "2": "F",
            "3": "K"
        }

        # Check choice
        if choice not in units:
            print("Invalid choice. Please try again.")
            continue

        try:
            value = float(input("Enter temperature value: "))

            target = input("Convert to (C/F/K): ").upper()

            # Check target unit
            if target not in ("C", "F", "K"):
                print("Invalid target unit.")
                continue

            result = convert_temperature(
                value,
                units[choice],
                target
            )

            print(f"Result: {result:.2f} °{target}")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()