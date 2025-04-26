"""
Generates an HTML page with animal information cards from JSON data.
"""

import json

# Constants
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "output.html"
REPLACEMENT_STRING = "__REPLACE_ANIMALS_INFO__"
STEP_SUMMARY_CONTENT = """
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

def get_skin_types(animals_data):
    """Extracts all unique skin types from animal data.
    
    Args:
        animals_data (list): List of animal dictionaries
        
    Returns:
        list: Sorted list of unique skin types
    """
    skin_types = set()
    for animal in animals_data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    return sorted(skin_types)

def serialize_animal(animal_data):
    """Formats animal data into HTML card format.
    
    Args:
        animal_data (dict): Animal data dictionary
        
    Returns:
        str: Formatted HTML card as string
    """
    return f'''
    <li class="cards__item">
        <div class="card__title">{animal_data.get("name", "Unknown")}</div>
        <p class="card__text"><strong>Scientific Name:</strong> {animal_data.get("taxonomy", {}).get("scientific_name", "Unknown")}</p>
        <p class="card__text"><strong>Location:</strong> {", ".join(animal_data.get("locations", []))}</p>
        <p class="card__text"><strong>Feature:</strong> {animal_data.get("characteristics", {}).get("distinctive_feature", "Not available")}</p>
        <p class="card__text"><strong>Life Span:</strong> {animal_data.get("characteristics", {}).get("lifespan", "Not available")}</p>
        <p class="card__text"><strong>Slogan:</strong> {animal_data.get("characteristics", {}).get("slogan", "No slogan provided.")}</p>
    </li>
    '''.strip()

def generate_html(cards_content, template_path, output_path):
    """Generates final HTML file by populating template.
    
    Args:
        cards_content (str): Formatted HTML cards
        template_path (str): Path to template file
        output_path (str): Output file path
        
    Returns:
        str: Path to generated HTML file
    """
    with open(template_path, "r") as template_file:
        template = template_file.read()
    
    populated_template = template.replace(REPLACEMENT_STRING, cards_content)
    
    with open(output_path, "w") as output_file:
        output_file.write(populated_template)
    
    return output_path

def main():
    """Main execution flow for HTML generation."""
    # Load data
    with open("animals_data.json", "r") as data_file:
        animals = json.load(data_file)
    
    # Generate animal cards
    animal_cards = [serialize_animal(animal) for animal in animals]
    
    # Add step summary card
    animal_cards.append(STEP_SUMMARY_CONTENT.strip())
    
    # Generate final HTML
    html_path = generate_html(
        "\n".join(animal_cards),
        TEMPLATE_FILE,
        OUTPUT_FILE
    )
    
    # Show summary
    print(f"✅ Web page generated: {html_path}")
    print(f"📊 Found skin types: {', '.join(get_skin_types(animals))}")

if __name__ == "__main__":
    main()
