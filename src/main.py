from analyzer import HousePriceAnalyzer
from models import PrivateHouse, Apartment


def get_private_house_input():
    """Gather input for a private house."""
    print("\n--- Enter Private House Details ---")
    area = float(input("Enter the house area (sqm): "))
    location = input("Enter the location (center/suburbs): ").lower()
    garden_area = float(input("Enter the garden area (sqm): "))
    garage = input("Does it have a garage? (yes/no): ").strip().lower() == "yes"
    num_floors = int(input("Enter the number of floors: "))
    return PrivateHouse(area, location, garden_area, garage, num_floors)


def get_apartment_input():
    """Gather input for an apartment."""
    print("\n--- Enter Apartment Details ---")
    area = float(input("Enter the apartment area (sqm): "))
    location = input("Enter the location (center/suburbs): ").lower()
    floor = int(input("Enter the apartment's floor: "))
    total_floors = int(input("Enter the total number of floors: "))
    return Apartment(area, location, floor, total_floors)


def main():
    """Main function to run the House Pricing Analyzer."""
    print("Welcome to the Bishkek House Pricing Analyzer!")
    analyzer = HousePriceAnalyzer()

    while True:
        # Ask for property type
        property_type = input("\nEnter property type (private_house/apartment): ").strip().lower()

        # Get user input for the selected property type
        if property_type == "private_house":
            property_obj = get_private_house_input()
        elif property_type == "apartment":
            property_obj = get_apartment_input()
        else:
            print("Invalid property type! Please enter 'private_house' or 'apartment'.")
            continue

        # Calculate and display the price
        try:
            price = analyzer.calculate_price(property_obj)
            print(f"\nThe estimated price for the {property_type} is: ${price:,.2f}\n")
        except KeyError as e:
            print(f"Error in calculation: {e}")

        # Check if the user wants to continue
        more = input("Do you want to calculate another property? (yes/no): ").strip().lower()
        if more != "yes":
            break

    print("Thank you for using the Bishkek House Pricing Analyzer!")


if __name__ == "__main__":
    main()
