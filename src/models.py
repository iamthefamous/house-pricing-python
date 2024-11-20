class Property:
    """Base class for shared attributes between properties."""
    def __init__(self, area, location):
        self.area = area
        self.location = location


class PrivateHouse(Property):
    """Model for a private house."""
    def __init__(self, area, location, garden_area, garage, num_floors):
        super().__init__(area, location)
        self.garden_area = garden_area
        self.garage = garage
        self.num_floors = num_floors

    def __repr__(self):
        return (f"PrivateHouse(area={self.area}, location='{self.location}', "
                f"garden_area={self.garden_area}, garage={self.garage}, "
                f"num_floors={self.num_floors})")


class Apartment(Property):
    """Model for an apartment."""
    def __init__(self, area, location, floor, total_floors):
        super().__init__(area, location)
        self.floor = floor
        self.total_floors = total_floors

    def __repr__(self):
        return (f"Apartment(area={self.area}, location='{self.location}', "
                f"floor={self.floor}, total_floors={self.total_floors})")
