import json

# Load animal data
with open("animals_data.json", "r") as f:
    animals = json.load(f)

# Load the HTML template
with open("animals_template.html", "r") as f:
    template = f.read()

# Generate HTML cards
animal_cards = ""
for animal in animals:
    name = animal.get("name", "Unknown")
    taxonomy = animal.get("taxonomy", {})
    characteristics = animal.get("characteristics", {})

    scientific_name = taxonomy.get("scientific_name", "Unknown")
    location = ", ".join(animal.get("locations", []))
    distinctive = characteristics.get("distinctive_feature", "Not available")
    lifespan = characteristics.get("lifespan", "Not available")
    slogan = characteristics.get("slogan", "No slogan provided.")

    animal_cards += f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text"><strong>Scientific Name:</strong> {scientific_name}</p>
        <p class="card__text"><strong>Location:</strong> {location}</p>
        <p class="card__text"><strong>Feature:</strong> {distinctive}</p>
        <p class="card__text"><strong>Life Span:</strong> {lifespan}</p>
        <p class="card__text"><strong>Slogan:</strong> {slogan}</p>
    </li>
    """

# Add the Step Summary card
animal_cards += """
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

# Insert into the template
final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_cards)

# Save to output.html
with open("output.html", "w") as f:
    f.write(final_html)

print("✅ Web page generated: output.html")
