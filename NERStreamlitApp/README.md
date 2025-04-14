# 🔍 Custom Named Entity Recognition with Streamlit and spaCy

## 💼  Project Overview
This Streamlit app is an interactive tool designed to explore Named Entity Recognition (NER) using the spaCy library. It allows users to process text and identify named entities using spaCy's pre-trained models and allows users to define their own custom entity rules using pattern matching. Whether you're experimenting with NLP or customizing entity detection for domain-specific use cases (like brands, product types, or subjects), this app provides an intuitive platform to get started.

## 📖  What is spaCy NER?

**What is spaCy:**

spaCy is an open-source Python library for Natural Language Processing, built for production use. It supports tasks like information extraction, text classification, and pre-processing for deep learning. Some features of spaCy work rule-based while others rely on trained pipelines, statistical models that predict linguistic annotation.

**Tokenization:**

spaCy tokenizes text by first splitting on whitespace, then applying language-specific rules to handle exceptions and to separate punctuation (e.g. “don’t” -> “do” + “n’t”) but (“U.S.” remains “U.S.”). It processes each substring left to right checking for the tokenizer exception rules and prefix, suffix, or infix rules to split punctation (e.g. quotes, commas, periods). 

**Named Entity Recognition (NER):**

NER identities and classifies real-world named objects such as:

- People (PERSON)
- Organizations (ORG)
- Locations (GPE, LOC)
- Dates and Times (DATE, TIME)
- Money, Products, and more

spaCy uses a statistical model, in this case en_core_web_sm, to predict entities in a document, recognizing different types of named entities. The document is formed by the tokenizer and is modified by the pipeline components. Pipeline components can be added by making rule-based modifications to the document. 

This app enhances the built-in NER pipeline by letting you define custom rules via spaCy’s EntityRuler (expands document entities through token-based rules or exact phrase matches). You can target specific words or phrases and assign them a custom label and entity description, such as:

- Label: PLANT
- Patterns: Rose, Fern, Tree
- Description: Types of Plants

These patterns and labels when then be recognized and highlighted alongside spaCy’s standard NER output. 

## 🚀 How to Run the App Locally

Download the NER_App.py file from this Python portfolio and open the file in Visual Sutdio Code or a similar code editor platform. Once in Visual Studio naviagte to the top right and open the terminal field. It will be the second option of the following icons below:

<img width="112" alt="Screenshot 2025-04-13 at 1 15 13 PM" src="https://github.com/user-attachments/assets/351819fb-4783-4849-995b-6c8a21dd2a16" />

From there write the following command in the terminal space "streamlit run NERStreamlitApp/NER_App.py." This command may need to be edited depending on the folder order of your personal environment. However, it should be "streamlit run" followed the folder name then the NER_App.py file name. This will automatically open the streamlit app on your local browser, it will also provide a URL with the local link.

## 📚 Required Libraries

In order to run the app locally on a python development environment you will need to make sure you have the following libraries installed on your platform: Streamlit, spaCy, Pandas, and io. Included in the NER_App.py file is code to install these required libraries:

<img width="177" alt="Screenshot 2025-04-10 at 3 11 13 PM" src="https://github.com/user-attachments/assets/99ffb74d-04cd-4a9b-95f4-72d9c436cef2" />

Make sure you see no errors in the output of these lines before continuing on with running the app. 

## 🌐 Deployed Version
You can try the app live here:

👉 Live App: https://kondis-python-portfolio-ner.streamlit.app

## ✨ App Features

**📄 Text Processing:**

- Upload or Enter Text: Upload your own .txt files, write custom text, or choose from sample options provided.
- Define Custom Entities: Create your own entity rules by entering a label, an optional description, and (comma-separated) patterns

**📊 NER Analysis:**
  
- Displays detected named entities from both spaCy's model and your custom rules.
- Explains each entity with its label, description, and matched pattern.

**🎨 Highlighted Text Output:**

- See your processed text with entities visually highlighted by type. 
- Custom entities appear with a distinct orange background.

## 💡 Example Usage
**Here’s how you might define a custom rule:**

- Label: ELECTRONICS
- Description: Electronic gadgets and products
- Patterns: phone, laptop, television

<img width="305" alt="Screenshot 2025-04-13 at 1 44 32 PM" src="https://github.com/user-attachments/assets/df306266-5c96-4b1a-857b-efb2c7273e97" />

**When analyzing a sentence like:**

"I bought a new phone and a television during the sale."

**These terms will be highlighted as ELECTRONICS:**

<img width="617" alt="Screenshot 2025-04-13 at 1 48 32 PM" src="https://github.com/user-attachments/assets/bd1a7f89-87b6-42de-b0c0-c0c3574ccc30" />

<img width="828" alt="Screenshot 2025-04-13 at 1 44 42 PM" src="https://github.com/user-attachments/assets/ff5a7276-bb91-4944-98b5-0f319a2097e2" />


## 📊  References
- spaCy 101: https://spacy.io/usage/spacy-101
- Entity Ruler: https://spacy.io/api/entityruler
- The Basics of spaCy: https://spacy.pythonhumanities.com/01_01_install_and_containers.html
- spaCy Library Architecture: https://spacy.io/api
