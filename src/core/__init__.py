class House:
    def __init__(self, street, company, year_of_production, number_of_floors):
        self.street = street
        self.company = company
        self.year_of_production = year_of_production
        self.number_of_floors = number_of_floors


class Flat(House):
    def __init__(self, street, company, year_of_production, number_of_floors, flat_rooms, flat_n_floor, number_m3):
        super().__init__(street, company, year_of_production, number_of_floors)
        self.flat_rooms = flat_rooms
        self.flat_n_floor = flat_n_floor
        self.number_m3 = int(number_m3)


class HouseAnalyzer:
    def apartmentDetails(self):
        """
        Asks user input for details as options for an apartment
        and returns the precise details for the given apartment.
        """
        print("Enter details for the apartment:")
        street = input("Street name: ")
        company = input("Construction company: ")
        year = input("Year of production: ")
        floors = int(input("Number of floors in the building: "))
        flat_rooms = int(input("Number of rooms in the flat: "))
        flat_floor = int(input("Floor number of the flat: "))
        area = int(input("Flat area in m³: "))

        flat = Flat(street, company, year, floors, flat_rooms, flat_floor, area)
        print("\nApartment Details:")
        print(f"Street: {flat.street}")
        print(f"Company: {flat.company}")
        print(f"Year of Production: {flat.year_of_production}")
        print(f"Number of Floors: {flat.number_of_floors}")
        print(f"Flat Rooms: {flat.flat_rooms}")
        print(f"Flat Floor: {flat.flat_n_floor}")
        print(f"Flat Area: {flat.number_m3} m³")

    def privateHouseDetails(self):
        """
        Asks user input for details of a private house
        and returns the precise details for the house.
        """
        print("Enter details for the private house:")
        street = input("Street name: ")
        company = input("Construction company: ")
        year = input("Year of production: ")
        floors = int(input("Number of floors in the house: "))

        house = House(street, company, year, floors)
        print("\nPrivate House Details:")
        print(f"Street: {house.street}")
        print(f"Company: {house.company}")
        print(f"Year of Production: {house.year_of_production}")
        print(f"Number of Floors: {house.number_of_floors}")

    def run(self):
        """
        Displays the menu and allows the user to choose
        between entering apartment or private house details.
        """
        print("1. Apartments")
        print("2. Private House")
        
        option = input("Choose your option: ")
        if option == "1":
            self.apartmentDetails()
        elif option == "2":
            self.privateHouseDetails()
        else:
            print("Invalid option. Please try again.")

# Example usage
analyzer = HouseAnalyzer()
analyzer.run()
