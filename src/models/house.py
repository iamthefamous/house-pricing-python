class House:
    def __init__(self, property_type, location, area, rooms, construction_year, **kwargs):
        self.property_type = property_type
        self.location = location
        self.area = area
        self.rooms = rooms
        self.construction_year = construction_year
        self.additional_features = kwargs
