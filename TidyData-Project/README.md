# 📊 Tidy Data Project: U.S. Federal R&D Spending Analysis (1976–2017)

## 🔍 Project Overview:

In this project, I analyzed spending patterns and trends of the U.S. federal government across 14 agencies from 1976 to 2017. Using tidy data principles, I cleaned and transformed the dataset to improve variable extraction and ensure a structured format.

**Key Steps:**
- ✔️ Organized each variable into a column, each observation into a row, and each observational unit into a table.
- ✔️ Utilized Pandas to manipulate variables while preserving observations for further analysis.
- ✔️ Applied tidy data principles to streamline analysis, reduce errors, and improve efficiency.
- ✔️ Created visualizations, pivot tables, and aggregations to better understand federal spending behaviors.

---
## ⚙️ Project Setup Instructions:

🛠 **1. Open the Project**
📂 Locate the Tidy Data Project folder on GitHub and open the Jupyter Notebook labeled "Tidy Data Project".

🏗 **2. Install Required Packages**
Ensure you have the following Python packages installed: pandas, matplotlib.pyplot, and seaborn 

<img width="452" alt="Screenshot 2025-03-17 at 9 03 07 PM" src="https://github.com/user-attachments/assets/eeb04080-f537-4602-b2d9-3b277279f6e5" />

Run the import lines in the first section of the notebook or manually install them via VS Code Extensions.

📂 **3. Upload the Dataset**
Place the CSV file in a location accessible by VS Code or Jupyter Notebook.
Verify the dataset is correctly loaded by running df.head(), it should look like the image below:

<img width="703" alt="Screenshot 2025-03-17 at 9 03 23 PM" src="https://github.com/user-attachments/assets/6b1600ce-8ef7-4fe3-b858-16f15e56351a" />

▶️ **4. Run the Notebook**
If packages are installed and df.head() displays the data correctly, proceed by executing all cells in order.
Code cells will output results, while Markdown cells provide explanations.

---
## 📜 Dataset Description:

- 📊 The original dataset used in this project can be found at this link: https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12
- 📌 **Source:** American Association for the Advancement of Science Historical Trends 

The link shows in detail how the data was cleaned, the process included: 
- ✔️ Extracting department names from the Fiscal Year column.
- ✔️ Standardizing year values and converting to monetary values.
- ✔️ Merging GDP, federal budget, and agency spending datasets into one comprehensive dataset.

---
## 📚 References & Resources:

- 📖 **Pandas Cheat Sheet:** https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- 📖 **Tidy Data Paper:** https://vita.had.co.nz/papers/tidy-data.pdf
- 📖 **Data to Viz:** https://www.data-to-viz.com
