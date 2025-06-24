Zootopia with API
A Python-based application that fetches animal data from an API and generates a static HTML page showcasing various animals.

📌 Features
DATA Retrieval: Fetches animal data from a public API.
HTML Generation: Creates a user-friendly HTML page displaying animal information.
Template Usage: Utilizes an HTML template for consistent styling.
🛠️ Installation
To install this project, Clone the Repository:

git clone https://github.com/shinegit1/Zootopia-with-API.git

cd Zootopia-with-API

Create a Virtual Environment (Optional but Recommended):

python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

🚀 Usage
To use this project, Run the following command:

python animals_web_generator.py

Ex. Enter a name of animal: lion

View the output:

Open the generated animals.html file in your web browser to see the list of animals.

📁 Project Structure
Zootopia-with-API/
├── animals_template.html       # HTML template for the default page
├── animals.html                # HTML template for the ouput page
├── animals_web_generator.py    # Main script to fetch data and generate HTML
├── data_fetcher.py             # Module to handle API requests
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
🐍 Dependencies
Python 3.x
Requests library
Python-dotenv
🙌 Acknowledgements
