# 🔍 Custom Named Entity Recognition with Streamlit and spaCy

## 🧠 Project Overview
This Streamlit app is an interactive tool designed to explore Named Entity Recognition (NER) using the spaCy library. It allows users to process text and identify named entities using spaCy's pre-trained models and define their own custom entity rules using pattern matching. Whether you're experimenting with NLP or customizing entity detection for domain-specific use cases (like brands, product types, or locations), this app provides a powerful and intuitive platform to get started.

## 🤖 What is spaCy NER?
spaCy is a popular Python library for Natural Language Processing. Its NER pipeline can detect entities like:

- People (PERSON)

- Organizations (ORG)

- Locations (GPE, LOC)

- Dates and Times (DATE, TIME)

- Money, Products, and more

This app enhances the built-in NER pipeline by letting you define custom rules via spaCy's EntityRuler. You can target specific words or phrases and assign them a custom label, such as:

plaintext
Copy
Edit
Label: PLANT
Patterns: rose, tulip, oak tree
These will then be recognized and highlighted alongside spaCy’s standard NER output.

## 🚀 How to Run the App Locally
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/your-username/custom-ner-spacy-app.git
cd custom-ner-spacy-app
Install Required Libraries:

### Make sure you're using Python 3.8 or later. Then install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt, here's what you need:

bash
Copy
Edit
pip install streamlit spacy pandas
python -m spacy download en_core_web_sm
Run the App:

bash
Copy
Edit
streamlit run app.py
Open the app in your browser at http://localhost:8501.

# 🌐 Deployed Version
You can try the app live here:
👉 Live App on Streamlit Share

### ✨ Features
📄 Upload Text: Upload your own .txt files or use provided sample text.

🛠️ Define Custom Entities: Enter a label, description, and patterns (comma-separated) to define custom rules.

### 📊 NER Analysis:

Displays detected named entities from both spaCy's model and your custom rules.

Explains each entity label with a description.

### 🎨 Highlighted Text Output:

Entities are highlighted with different colors for better readability.

Custom entities use a distinctive orange background.

## 💡 Example Usage
Here’s how you might define a custom rule:

Label: ELECTRONICS

Description: Electronic gadgets and products

Patterns: phone, laptop, television

When analyzing a sentence like:

"I bought a new phone and a television during the sale."

These terms will be highlighted as ELECTRONICS.

## 📚 References
Add tutorials, guides, or research articles you referenced here.
