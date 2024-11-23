import json
from models import PrivateHouse, Apartment

class HousePriceAnalyzer:
    """
    a class to analyze and calculate the estimated price of a property 
    (either a private house or an apartment) based on predefined coefficients.

    attributes:
        coefficients (dict): Dictionary containing price coefficients loaded from a JSON file.

    methods:
        __init__(coefficients_path): Initializes the analyzer by loading coefficients from a JSON file.
        calculate_price(property_obj): Calculates the estimated price of the given property.
    """


    def __init__(self, coefficients_path="data/coefficients.json"):
        """
        initializes the HousePriceAnalyzer by loading coefficients from a JSON file.

        params:
            coefficients_path (str): The path to the JSON file containing the coefficients.
        """

        with open(coefficients_path, 'r') as file:
            self.coefficients = json.load(file)

    def calculate_price(self, property_obj):
        """
        Calculates the estimated price of a property.

        The calculation varies depending on whether the property is a `PrivateHouse` 
        or an `Apartment`, using specific coefficients and multipliers.

        Params:
            property_obj (PrivateHouse or Apartment): The property for which the price is to be calculated.

        Returns:
            float: The estimated price of the property.

        Raises:
            KeyError: If a required coefficient is missing in the JSON file.
        """

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
            garage_price = self.coefficients["garage_price"] if property_obj.garage else 0
            price = floor_multiplier * price + garage_price

        return price * location_multiplier
