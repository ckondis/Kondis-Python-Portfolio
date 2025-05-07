# 🐕 Basic Streamlit Dog Breeds App
Welcome to the **Basic Streamlit Dog Breeds App!** This app, developed with Python and Streamlit, demonstrates how interactive data visualizations and user-driven filtering can be easily implemented. Using Streamlit, the app loads a dataset of dog breeds and presents an **interactive table for users to explore.** Through features like dropdowns, sliders, and radio buttons, users can filter the data based on attributes such as breed, weight, and age. The app showcases how to build a **dynamic, user-focused interface** for data analysis and exploration.

# 📌 Purpose
This app provides an interactive interface for exploring a CSV file containing data on various dog breeds. The app enables dynamic updates to the dataset, allowing for real-time data exploration. It is designed to facilitate efficient data filtering and visualization for users looking to analyze specific subsets of information, making it useful for anyone interested in examining dog breed data or applying similar techniques to other datasets. 

# ⚙️ Setup & Installation
To run the app locally on your device, follow these steps:

1.Download the main.py and the data folder with all included files. The easiest way to do this is by donwloading the entire basic_streamlit_app folder from this portfolio.
2. Open the folder in Visual Sutdio Code or another code editor that supports a Python environment.
3. Make sure you have all the necessary Python libraries installed (steamlit, pandas,):

<img width="172" alt="Screenshot 2025-05-07 at 1 02 38 PM" src="https://github.com/user-attachments/assets/7763c034-b85e-465b-a44d-af8818fbfe2f" />

4. After installing the required libraries, open the terminal. In VS code, you can do this by clicking on the second box icon in the top right (with a bolded bottom half).

<img width="109" alt="Screenshot 2025-05-07 at 1 02 44 PM" src="https://github.com/user-attachments/assets/b161234c-4b3a-415b-9cef-2fd11d7412bf" />

5. Once the terminal box appears type in "Streamlit Run" with the file path leading to the basic_streamlit_app and main.py (Streamlit Run basic_streamlit_app/main.py). Adjust the file path if you downloaded or renamed the files differently.
6. Once the command is entered, your default web browser should automatically open the app. If it doesn't, copy and paste the local URL provided in the terminal into your browser.
8. Once the app is up and running, you’ll be able to interact with the data and explore the different dog breeds.
---
## Python Library Versions Used
- **Streamlit:** 1.41.1
- **Pandas:** 2.2.3

# 📊 App Features

### 🧩 Interactive Filters:
- **Breed Selection:** Choose from a list of dog breeds to filter and view specific breed information.
- **Weight Group:** Select a weight (kg) range to explore dogs that fall within that weight group.
- **Age Group:** Choose from different age groups to view data about dogs in that age range.
- **Examples:**  
<img width="725" alt="Screenshot 2025-05-07 at 1 07 40 PM" src="https://github.com/user-attachments/assets/cbadcfc5-ba80-4899-81b5-b6b1e784f50a" />

<img width="728" alt="Screenshot 2025-05-07 at 1 07 45 PM" src="https://github.com/user-attachments/assets/baa3d776-1770-4c3b-9abc-e76ea83898af" />

### 📑 Outputs:
- View the filtered dataset in an interactive Streamlit dataframe, which dynamically displays relevant columns such as breed, weight, color, and gender based on applied user filters.
- Each component (selectbox, slider, and radio button) triggers real-time re-rendering of the dataset using Streamlit’s reactive framework, ensuring the displayed data reflects the most recent user input.
- **Example:**

<img width="541" alt="Screenshot 2025-05-07 at 1 08 31 PM" src="https://github.com/user-attachments/assets/83c54ba9-eb26-4ed1-8381-3c83b9abbcdd" />

# 📚 References & Resources
- **Streamlit Resources:** https://streamlit.io
- **Pandas Resources:** https://pandas.pydata.org
