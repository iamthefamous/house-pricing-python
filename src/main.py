from data.load_data import load_coefficients
from core.house_analyzer import HouseAnalyzer
from models.house import House

def main():
    coefficients = load_coefficients()
    analyzer = HouseAnalyzer(coefficients)

    # Example inputs
    property_type = input("Enter property type (private_house/apartments): ").strip()
    location = input("Enter location (downtown/suburb/outskirts): ").strip()
    area = float(input("Enter area in square meters: "))
    rooms = int(input("Enter number of rooms: "))
    construction_year = int(input("Enter construction year: "))

    additional_features = {}
    if property_type == "private_house":
        additional_features["yard"] = bool(int(input("Does it have a yard? (1 for Yes, 0 for No): ")))
        additional_features["garage"] = bool(int(input("Does it have a garage? (1 for Yes, 0 for No): ")))
    elif property_type == "apartments":
        additional_features["floor"] = input("Enter floor level (low/mid/high): ").strip()
        additional_features["elevator"] = bool(int(input("Does it have an elevator? (1 for Yes, 0 for No): ")))

    house = House(property_type, location, area, rooms, construction_year, **additional_features)
    price = analyzer.calculate_price(house)
    print(f"Estimated price for the {property_type}: {price:.2f} USD")

if __name__ == "__main__":
    main()
