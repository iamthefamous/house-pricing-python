import json
from models import PrivateHouse, Apartment

class HousePriceAnalyzer:
    def __init__(self, coefficients_path="data/coefficients.json"):
        with open(coefficients_path, 'r') as file:
            self.coefficients = json.load(file)

    def calculate_price(self, property_obj):
        base_price = self.coefficients["base_price"]
        area_price = property_obj.area * self.coefficients["area_coefficient"]
        location_multiplier = self.coefficients["location_coefficients"].get(property_obj.location, 1)
        price = base_price + area_price

        if isinstance(property_obj, PrivateHouse):
            garden_price = property_obj.garden_area * self.coefficients["garden_coefficient"]
            garage_price = self.coefficients["garage_price"] if property_obj.garage else 0
            floor_price = property_obj.num_floors * self.coefficients["floor_coefficient"]
            price += garden_price + garage_price + floor_price

        elif isinstance(property_obj, Apartment):
            floor_multiplier = (1 + (property_obj.floor / property_obj.total_floors))
            price *= floor_multiplier

        return price * location_multiplier
