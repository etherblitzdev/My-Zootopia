import json

# Step 1: Load JSON data
def load_data(file_path):
    """Loads a JSON file and returns its content"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# Step 2: Generate formatted animal info string
def generate_animal_info(animal_list):
    """Generates HTML list items with Name, Diet, Location, and Type for each animal"""
    output = ""
    for animal in animal_list:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations", [])
        typ = animal.get("characteristics", {}).get("type")

        # Start list item
        output += '<li class="cards__item">\n'

        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if isinstance(locations, list) and locations:
            output += f"Location: {', '.join(locations)}<br/>\n"
        if typ:
            output += f"Type: {typ}<br/>\n"

        # Close list item
        output += "</li>\n"

    return output

# Step 3: Inject animal info into HTML template
def inject_into_template(template_path, output_path, animal_info):
    """Replaces placeholder in HTML template and writes final HTML file"""
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(final_html)

# Step 4: Orchestrate full flow
def main():
    animals_data = load_data("animals_data.json")
    if not isinstance(animals_data, list):
        print("Expected a list of animals in the JSON file.")
        return

    animal_info = generate_animal_info(animals_data)
    inject_into_template("animals_template.html", "animals.html", animal_info)
    print("✅ animals.html generated successfully.")

if __name__ == "__main__":
    main()
