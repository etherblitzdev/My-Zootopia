import json

def load_data(file_path):
    """Loads a JSON file and returns its content"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animal_info(animal_list):
    """Prints formatted info for each animal"""
    for animal in animal_list:
        # Name
        name = animal.get("name")
        if name:
            print(f"Name: {name}")

        # Diet (always inside characteristics)
        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            print(f"Diet: {diet}")

        # Location (first from list)
        locations = animal.get("locations", [])
        if isinstance(locations, list) and locations:
            print(f"Location: {locations[0]}")

        # Type (inside characteristics, sometimes missing)
        typ = animal.get("characteristics", {}).get("type")
        if typ:
            print(f"Type: {typ}")

        print()  # Blank line between animals

# Load and process data
animals_data = load_data("animals_data.json")
if isinstance(animals_data, list):
    print_animal_info(animals_data)
else:
    print("Expected a list of animals in the JSON file.")
