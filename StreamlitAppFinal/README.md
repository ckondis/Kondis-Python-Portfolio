# 🏙️ **Metropolitan Area Investment Analyzer**
Welcome to the **Metropolitan Area Investment Analyzer** — a real estate analytics tool designed to help investors, developers, movers,
and data enthusiasts gain a deeper understanding of U.S. metropolitan housing markets. Whether you're researching for an investment opportunity, completing a real estate coursework project, 
or deciding where to move next, this tool provides **accessible and visual insights** into **housing market dynamics** across the country.

# 📌 **Purpose**
This interactive Streamlit app aims to **simplify metro-level** real estate analysis by integrating Zillow housing data, demographic trends, and investment indicators into a single platform. 
Whether you're looking to identify high-growth markets, compare metro-level dynamics, or visualize housing value trends, this tool offers an intuitive, data-driven experience to support smarter decision-making.

# 🚨 **Problem It Solves**
Navigating vast real estate datasets across different regions can be overwhelming and time-consuming. Many tools focus on individual zip codes or raw datasets without providing a comprehensive metro-level view. 
This app bridges that gap by:

- Aggregating housing and demographic data at the metro level
- Providing easy-to-use filtering and comparison tools
- Offering instant visual insights to support investment research

# ⚙️ **Setup & Installation**
Follow these steps to run the app locally on your machine:

1. Download the main_app.py, the data folder with all included files, and the requirements.txt. The easiest way to do this is by donwloading the entire StreamlitAppFinal folder from this portfolio. 
2. Open the folder in Visual Sutdio Code or another code editor that supports a Python environment.
3. Make sure you have all the necessary Python libraries installed (steamlit, pandas, plotly, re):
<img width="214" alt="Screenshot 2025-05-07 at 9 03 53 AM" src="https://github.com/user-attachments/assets/c59357e7-8327-4370-9bae-432ca7bf797a" />

4. After installing the required libraries, open the terminal. In VS code, you can do this by clicking on the second box icon in the top right (with a bolded bottom half).
<img width="115" alt="Screenshot 2025-05-07 at 9 07 57 AM" src="https://github.com/user-attachments/assets/5d79c12d-7fad-4f70-a52d-2bab9df81612" />

5. Once the terminal box appears type in "Streamlit Run" with the file path leading to the StreamlitAppFinal and main_app.py (Streamlit Run StreamlitAppFinal/main_app.py). Adjust the file path if you downloaded or renamed the files differently.
6. Once the command is entered, your default web browser should automatically open the app. If it doesn't, copy and paste the local URL provided in the terminal into your browser.
7. If the app is running succesfully you should see the following at the top of the Home Page:
<img width="752" alt="Screenshot 2025-05-07 at 9 22 25 AM" src="https://github.com/user-attachments/assets/be05df62-acd0-4c36-827f-7073799204c9" />

8. Once you're on the app, follow the on-screen instructions to explore the different metrics and pages!

## Python Library Versions Used
- **Streamlit:** 1.41.1
- **Pandas:** 2.2.3
- **Plotly:** 5.24.1

## Deployed App
- Access the app on **Streamlit Community Cloud** via this link: https://kondis-python-portfolio-final-app.streamlit.app/ 

# ✨ **App Features**
### 🧩 User Inputs:
Users can interact with the app through several customizable inputs:
- State and Metro Area Selection: Choose a specific U.S. state and metropolitan area to analyze.
- **Timeframe Filters:**
  - Select monthly or yearly views for time-based metrics.
  - Choose specific years to narrow down trend analysis.
- **Comparison Metro Areas:**
  - Add additional metros for side-by-side comparisons of trends and data visualizations.
- **Demographic Variables:**
  - Choose from statistics such as median age, total population, and more to view demographic influences on housing trends.
- **Notes Section:**
  - Input personal notes and observations while exploring the app. These notes are saved and accessible in the final section for easy reference and report preparation.
- **Example:**

<img width="302" alt="Screenshot 2025-05-07 at 9 51 44 AM" src="https://github.com/user-attachments/assets/15505f55-8101-46f7-bdd5-928c5717761d" />

### 🛠️ Main Functions
- Real-time data filtering based on user inputs.
- Dynamic visualizations that respond to selections in state, metro, and timeframe.
- Educational content embedded within each tab to provide context and support informed analysis.
- Persistent notes system to help users retain key insights and observations as they navigate through the app.
- Sections Included: Median List Price Over Time, Zillow Home Value Index (ZHVI), Home Value Growth Rate, Sale-to-List Price Ratio, Market Heat Index, New Homeowner Income Comparison, and Demographic Overview

### 📊 Outputs
Each section generates a visualization or KPI (Key Performance Indicator) card, allowing for clear and actionable insights:
- Line charts, bar graphs, and data tables visualize housing trends over time.
- KPI cards summarize current values, growth rates, or comparisons for quick interpretation.
- Side-by-side comparisons enable deeper understanding of market differences across metro areas.

- **Example:**
<img width="708" alt="Screenshot 2025-05-07 at 9 51 58 AM" src="https://github.com/user-attachments/assets/11491a90-a355-4b46-b632-f0bdb9e19429" />

# 📚 References & Resources
1. **US Census Data Resources:** https://data.census.gov
2. **Zillow Research Data:** https://www.zillow.com/research/data/
3. **Libaries:** Streamlit (https://streamlit.io), Pandas (https://pandas.pydata.org/docs/user_guide/), Plotly Express (https://plotly.com/python/plotly-express/)
