class Property:
    """
    base class for shared attributes between properties.

    attributes:
        area (float): The total area of the property in square meters.
        location (str): The location of the property.
    """


    def __init__(self, area, location):
        """
        initializes the common attributes for all properties.

        params:
            area (float): The total area of the property in square meters.
            location (str): The location of the property.
        """
        self.area = area
        self.location = location


class PrivateHouse(Property):
    """
    model for a private house, extending the base `Property` class.

    attributes:
        area (float): The total area of the house in square meters.
        location (str): The location of the house.
        garden_area (float): The area of the garden in square meters.
        garage (bool): Whether the house has a garage (True/False).
        num_floors (int): The number of floors in the house.
    """


    def __init__(self, area, location, garden_area, garage, num_floors):
        """
        initializes a `PrivateHouse` object with specific attributes.

        params:
            area (float): The total area of the house in square meters.
            location (str): The location of the house.
            garden_area (float): The area of the garden in square meters.
            garage (bool): Whether the house has a garage (True/False).
            num_floors (int): The number of floors in the house.
        """


        super().__init__(area, location)
        self.garden_area = garden_area
        self.garage = garage
        self.num_floors = num_floors

    def __repr__(self):
        return (f"PrivateHouse(area={self.area}, location='{self.location}', "
                f"garden_area={self.garden_area}, garage={self.garage}, "
                f"num_floors={self.num_floors})")


class Apartment(Property):
    """
    model for an apartment, extending the base `Property` class.

    attributes:
        area (float): The total area of the apartment in square meters.
        location (str): The location of the apartment.
        floor (int): The specific floor where the apartment is located.
        total_floors (int): The total number of floors in the building.
        garage (bool): Whether the apartment has access to a garage (True/False).
    """


    def __init__(self, area, location, floor, total_floors, garage):
        """
        initializes an `Apartment` object with specific attributes.

        Params:
            area (float): The total area of the apartment in square meters.
            location (str): The location of the apartment.
            floor (int): The specific floor where the apartment is located.
            total_floors (int): The total number of floors in the building.
            garage (bool): Whether the apartment has access to a garage (True/False).
        """
        super().__init__(area, location)
        self.floor = floor
        self.total_floors = total_floors
        self.garage = garage

    def __repr__(self):
        return (f"Apartment(area={self.area}, location='{self.location}', "
                f"floor={self.floor}, total_floors={self.total_floors}, garage={self.garage})")
