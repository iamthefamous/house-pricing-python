from data.load_data import load_coefficients

class HouseAnalyzer:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def calculate_price(self, house):
        base_price = self.coefficients[house.property_type]["base_price"]
        location_multiplier = self.coefficients["location"].get(house.location, 1)
        room_multiplier = self.coefficients["rooms"].get(str(house.rooms), 1)
        area_price = house.area * self.coefficients["area_per_sqm"]

        # Property-type-specific multipliers
        if house.property_type == "private_house":
            yard_multiplier = house.additional_features.get("yard", 1) * self.coefficients["private_house"]["yard_multiplier"]
            garage_multiplier = house.additional_features.get("garage", 1) * self.coefficients["private_house"]["garage_multiplier"]
            construction_year_multiplier = self.coefficients["private_house"]["construction_year_multiplier"]
            return base_price * location_multiplier * room_multiplier * yard_multiplier * garage_multiplier * construction_year_multiplier + area_price

        elif house.property_type == "apartments":
            floor_multiplier = self.coefficients["apartments"]["floor_multiplier"].get(house.additional_features.get("floor", "low"), 1)
            elevator_multiplier = house.additional_features.get("elevator", 1) * self.coefficients["apartments"]["elevator_multiplier"]
            construction_year_multiplier = self.coefficients["apartments"]["construction_year_multiplier"]
            return base_price * location_multiplier * room_multiplier * floor_multiplier * elevator_multiplier * construction_year_multiplier + area_price

        else:
            raise ValueError(f"Unknown property type: {house.property_type}")
