from analyzer import HousePriceAnalyzer
from models import PrivateHouse, Apartment
import json

def load_locations_from_json(file_path):
    """
    Reads a JSON file and extracts all locations from the 'location_coefficients' key.

    Parameters:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of all location names (keys from 'location_coefficients').
    """
    try:
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Extract locations from the 'location_coefficients' key
        locations = list(data.get("location_coefficients", {}).keys())
        return locations

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return []


def get_private_house_input(locations):
    """
    Collects and validates input for a private house.

    Prompts the user to enter the house's details, including area, location, garden size,
    garage presence, and number of floors. Validates the location against the predefined list 
    and returns a `PrivateHouse` object.

    Returns:
        PrivateHouse: An object representing the private house with user-supplied details.
    """


    print("\n--- Enter Private House Details ---")
    area = float(input("Enter the house area (sqm): "))


    print("Availble locations:")
    for loc in locations:
        print(f"- {loc}")
    location = input("Enter the location from the list above: ").strip().lower()
    
    if not(location in locations):
        location = "NaN"

    
    
    garden_area = float(input("Enter the garden area (sqm): "))
    garage = input("Does it have a garage? (yes/no): ").strip().lower() == "yes"
    num_floors = int(input("Enter the number of floors: "))
    return PrivateHouse(area, location, garden_area, garage, num_floors)


def get_apartment_input(locations):
    """
    Collects and validates input for an apartment.

    Prompts the user to enter the apartment's details, including area, location, floor,
    , total number of floors and garage. Validates the location against the predefined list 
    and returns an `Apartment` object.

    Returns:
        Apartment: An object representing the apartment with user-supplied details.
    """


    print("\n--- Enter Apartment Details ---")
    area = float(input("Enter the apartment area (sqm): "))

    print("Availble locations:")
    for loc in locations:
        print(f"- {loc}")
    location = input("Enter the location from the list above: ").strip().lower()
    
    if not(location in locations):
        location = "NaN"

    floor = int(input("Enter the apartment's floor: "))
    total_floors = int(input("Enter the total number of floors: "))
    garage = input("Does it have a garage? (yes/no): ").strip().lower() == "yes"
    return Apartment(area, location, floor, total_floors, garage)


def main():
    # This is the main function of Bishkek House Pricing Anylyzer program!


    print("Welcome to the Bishkek House Pricing Analyzer!")
    analyzer = HousePriceAnalyzer()

    locations = load_locations_from_json("data/coefficients.json")

    while True:
        property_type = input("\nEnter property type (private_house/apartment): ").strip().lower()

        if property_type == "private_house":
            property_obj = get_private_house_input(locations)
        elif property_type == "apartment":
            property_obj = get_apartment_input(locations)
        else:
            print("Invalid property type! Please enter 'private_house' / 'apartment'.")
            continue


        try:
            price = analyzer.calculate_price(property_obj)
            print(f"\nThe estimated price for the {property_type} is: ${price:,.2f}\n")
        except KeyError as e:
            print(f"Error occured during the calculations: {e}")


        exit_option = input("Do you want to calculate another property? (yes/no): ").strip().lower()
        if exit_option != "yes":
            break

    print("Thank you for using the Bishkek House Pricing Analyzer!")


if __name__ == "__main__":
    main()
