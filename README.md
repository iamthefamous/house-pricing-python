# Bishkek House Pricing Analyzer

**Bishkek House Pricing Analyzer** is a Python-based program that estimates the price of a property (private house or apartment) in Bishkek based on predefined coefficients. The program uses user-provided details about the property, such as area, location, and additional features (e.g., garden, garage, etc.), to calculate an estimated price.  
By:  
Amal Kurbanov  
Alisher Dzhusuev  
Assem Minsizbayeva  
Asylbek Zhunusov  

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Example Output](#example-output)
- [Contributors](#contributors)

---

## Features
- Calculate the price of **private houses** and **apartments**.
- Factor in **property area**, **location**, and other property-specific attributes like:
  - Garden size
  - Garage availability
  - Number of floors (for private houses)
  - Floor level (for apartments)
- Support for **custom coefficients** via JSON configuration.
- Validate input locations against a predefined list.

---

## Technologies Used
- Python 3.12
- JSON (for configuration and location data)

---

## Getting Started

### Prerequisites
- Install Python 3.8 or higher.
- Ensure the JSON file `coefficients.json` is located in the `data/` folder.

### Installation
```bash
git clone https://github.com/iamthefamous/house-pricing-python.git
cd house-pricing-python.git

```

### Usage

1. **Run the Program**:
   - Start the program by executing `main.py`.
   - Choose the property type: `private_house` or `apartment`.

2. **Provide Inputs**:
   - If you choose a **private house**, input:
     - Area of the house in square meters.
     - Location (validated against a predefined list).
     - Garden area in square meters.
     - Garage availability (`yes` or `no`).
     - Number of floors in the house.
   - If you choose an **apartment**, input:
     - Area of the apartment in square meters.
     - Location (validated against a predefined list).
     - Floor of the apartment.
     - Total number of floors in the building.
     - Garage availability (`yes` or `no`).

3. **View the Output**:
   - The program calculates the estimated price and displays it.

4. **Repeat or Exit**:
   - You can calculate another property or exit the program.


### File Descriptions

#### `main.py`
The main file that runs the Bishkek House Pricing Analyzer. Handles:
- User input and interaction.
- Validating location input.
- Displaying the estimated price.

#### `analyzer.py`
Contains the `HousePriceAnalyzer` class, which:
- Reads pricing coefficients from the `coefficients.json` file.
- Calculates property prices based on user inputs.

#### `models.py`
Defines the following classes:
- `Property`: A base class containing shared attributes like area and location.
- `PrivateHouse`: A class for houses, with attributes for garden size, number of floors, and garage.
- `Apartment`: A class for apartments, with attributes for floor, total floors, and garage.

#### `coefficients.json`
A configuration file containing:
- `base_price`: The starting price for all properties.
- `area_coefficient`: A multiplier for the area.
- `garden_coefficient`: A multiplier for garden area.
- `garage_price`: Fixed cost for a garage.
- `floor_coefficient`: Additional cost per floor (private houses).
- `location_coefficients`: Location-specific multipliers.


### Example Output

Welcome to the Bishkek House Pricing Analyzer!

Enter property type (private_house/apartment): private_house

--- Enter Private House Details ---

Enter the house area (sqm): 150

Available locations:
- Center
- Kyrgyzia 1
- Orto-sai village
- Kok jar
- Archa Beshik

...
Enter the location from the list above: Center

Enter the garden area (sqm): 60

Does it have a garage? (yes/no): yes

Enter the number of floors: 2

The estimated price for the private_house is: $340,000.00

Do you want to calculate another property? (yes/no): no

Thank you for using the Bishkek House Pricing Analyzer!
