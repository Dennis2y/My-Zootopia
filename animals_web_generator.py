import json

# Constants
ANIMALS_DATA_FILE = "animals_data.json"
HTML_TEMPLATE_FILE = "animals_template.html"
OUTPUT_HTML_FILE = "output.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_json_data(file_path):
    """
    Loads JSON data from a given file path.
    
    Args:
        file_path (str): Path to the JSON file.
        
    Returns:
        list: Parsed JSON content as a list of dictionaries.
    """
    with open(file_path, "r") as f:
        return json.load(f)


def load_html_template(file_path):
    """
    Loads HTML template content from a given file path.

    Args:
        file_path (str): Path to the HTML template.

    Returns:
        str: HTML template content as a string.
    """
    with open(file_path, "r") as f:
        return f.read()


def get_skin_types(animals):
    """
    Gets all unique skin types from the animal data.

    Args:
        animals (list): List of animal dictionaries.

    Returns:
        list: Sorted list of unique skin types.
    """
    return sorted({
        animal.get("characteristics", {}).get("skin_type", "Unknown")
        for animal in animals
    })


def serialize_animal(animal):
    """
    Converts one animal's data into an HTML list item.

    Args:
        animal (dict): Dictionary containing animal data.

    Returns:
        str: HTML string of the animal's info.
    """
    name = animal.get("name", "Unknown")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})

    scientific_name = taxonomy.get("scientific_name", "Unknown")
    location = ", ".join(animal.get("locations", []))
    distinctive = characteristics.get("distinctive_feature", "Not available")
    lifespan = characteristics.get("lifespan", "Not available")
    slogan = characteristics.get("slogan", "No slogan provided.")

    return f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text"><strong>Scientific Name:</strong> {scientific_name}</p>
        <p class="card__text"><strong>Location:</strong> {location}</p>
        <p class="card__text"><strong>Feature:</strong> {distinctive}</p>
        <p class="card__text"><strong>Life Span:</strong> {lifespan}</p>
        <p class="card__text"><strong>Slogan:</strong> {slogan}</p>
    </li>
    """


def generate_html(animals, template):
    """
    Generates the final HTML content by inserting all animal cards into the template.

    Args:
        animals (list): List of animal dictionaries.
        template (str): HTML template string.

    Returns:
        str: Final HTML string with animal data inserted.
    """
    animal_cards = "".join([serialize_animal(animal) for animal in animals])

    summary_card = """
    <li class="cards__item">
        <div class="card__title">Step Summary</div>
        <p class="card__text">
            You wrote your first HTML template, congratulations!<br>
            If you open it in the browser, you should see something similar to this:<br><br>
            <em>alt text</em><br><br>
            Happy from the result? We hope you are not.<br>
            Don’t be disappointed, in the next step we’ll fix that.
        </p>
    </li>
    """

    return template.replace(PLACEHOLDER, animal_cards + summary_card)


def main():
    """
    Main function to run the script.
    """
    animals = load_json_data(ANIMALS_DATA_FILE)
    template = load_html_template(HTML_TEMPLATE_FILE)
    final_html = generate_html(animals, template)

    with open(OUTPUT_HTML_FILE, "w") as f:
        f.write(final_html)

    print(f"✅ Web page generated: {OUTPUT_HTML_FILE}")

    # Optional: print available skin types
    skin_types = get_skin_types(animals)
    print("👀 Available Skin Types:", ", ".join(skin_types))


if __name__ == "__main__":
    main()
