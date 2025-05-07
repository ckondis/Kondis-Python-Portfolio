import streamlit as st        #Imports Streamlit library 
import pandas as pd           #Imports Pandas library
import re                     #Regular expressions (searchers for regular expression patterns in strings)
import plotly.express as px   #Imports plotly express library for additonal visualization methods

#Loads datasets in from Data folder and assigns values
df_demographics = pd.read_csv("StreamlitAppFinal/data/us-cities-demographics.csv", delimiter=";") #Uploads demographic data by semicolon-seperated document
df_for_sale_inventory = pd.read_csv("StreamlitAppFinal/data/ForSaleInventory.csv") #Loads ForSaleInventory CSV
df_home_value = pd.read_csv("StreamlitAppFinal/data/HomeValues.csv") #Loads HomeValues CSV
df_house_growth = pd.read_csv("StreamlitAppFinal/data/HouseGrowth.csv") #Loads HouseGrowth CSV
df_market_heat = pd.read_csv("StreamlitAppFinal/data/Market_Heat_Index.csv") #Loads Market_Heat_Index CSV
df_medianlistprice = pd.read_csv("StreamlitAppFinal/data/MedianListPrice.csv") #Loads MedianListPrice CSV
df_new_homeowner_income = pd.read_csv("StreamlitAppFinal/data/NewHomeownerIncome.csv") #Loads NewHomeOwnerIncome CSV
df_saletolist = pd.read_csv("StreamlitAppFinal/data/SaletoListRatio.csv") #Loads saletoListRatio CSV


st.sidebar.header("📍 Explore by Location") #Creates sidebar section title
st.sidebar.markdown("Use the dropdowns below to explore housing trends in a specific U.S. metro area.") #Adds in description for filters

state_metro_df = df_new_homeowner_income[["StateName", "RegionName"]].drop_duplicates() #Extracts unique state and metro combinations for dropdown filters
states = sorted(state_metro_df["StateName"].dropna().unique()) #Gets list of unique states
selected_state = st.sidebar.selectbox("Select a State", states) #Lets users choose a state
filtered_metros = state_metro_df[state_metro_df["StateName"] == selected_state]["RegionName"].dropna().unique() #Filters list of metro areas based on state selected by user
selected_metro = st.sidebar.selectbox("Select a Metro Area", sorted(filtered_metros)) #Lets users choose a metro area based on selected state

# --- Sidebar Notes Section ---
st.sidebar.markdown("📝 **Take Notes While You Explore**") #Adds sidebar heading

if 'all_notes' not in st.session_state: #Checks if 'all notes' list is already stored in session state
    st.session_state.all_notes = [] #If not, intializes 'all notes' as an empty list to store notes

user_note = st.sidebar.text_area( 
    "Jot down insights, questions, or next steps here:",
    key="note_input", #Sets a unique key for the widget to track its value in session state
    height=150
) #Creates a text area in the sidebar for user to input notes, adds label

if user_note and (len(st.session_state.all_notes) == 0 or user_note != st.session_state.all_notes[-1]): #Checks if the note is new and not a duplicate of the last one
    if user_note.strip() != "": #Ensures note is not empty spaces
        st.session_state.all_notes.append(user_note.strip()) #Adds the note to the session state list

st.sidebar.markdown(
    """
    <p style='font-size: 12px; color: #888;'>
        *Tip: Press <strong>Command + Enter</strong> (or <strong>Ctrl + Enter</strong> on Windows) to save your note. After you have entered a note <strong>it will be stored and displayed on the last tab</strong>,
        so feel free to delete the text after saving and start a new note!*
    </p>
    """,
    unsafe_allow_html=True
) #Adds custom written description below text area in sidebar


st.markdown("""
    <div style='text-align: center; padding: 20px 10px;'>
        <h1 style='font-size: 48px; color: #2E86C1;'>🏙️ Metropolitan Area Investment Analyzer</h1>
    </div>
""", unsafe_allow_html=True) #Adds custom title formatting on main page

st.markdown("""
    <div style='text-align: center; padding: 10px 0 30px 0;'>
        <p style='font-size: 16px; color: #444; max-width: 800px; margin: auto;'>
            An interactive dashboard for exploring U.S. housing markets at the metro level. 
            Use data-driven insights—from price trends to demographic patterns—to identify investment opportunities, 
            compare regions, and make smarter real estate decisions.
        </p>
        <h2 style='color: #117A65; margin-top: 20px;'>🔍 Select a Category to Explore</h2>
    </div> 
""", unsafe_allow_html=True) #Adds custom written description on main page

tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([ #Creates a tabbed interface
    "🏠 Home", #List of tab titles
    "📈 Median List Price Over Time",
    "🏡 Zillow Home Value Index (ZHVI) by Metro",
    "📊 Home Value Growth Rate",
    "🏦 Sale-to-List Ratio",
    "🧭 Market Heat Index",
    "💰 New Homeowner Income Comparison",
    "👥 Demographic Overview",
    "📝 Your Notes"
])

with tab0: #Start of tab0 content
    st.markdown("""
    <div style='text-align: center; padding: 10px 10px; max-width: 700px; margin: auto;'>
        <h3 style='color:#117A65;'>📌  How to Get Started</h3>
        <ul style='font-size: 16px; color: #444; text-align: left; display: inline-block;'>
            <li>Select a State and Metro area using the sidebar on the left. You can switch the State or Metro area on the sidebar at any time to see new information.</li>
            <li>Navigate through the tabs above to explore different market metrics. Scroll to the right on the bar above to see all eight tabs.</li>
            <li>Use the Notes tab to jot down insights or ideas as you analyze. Your notes will be saved and recorded on the last tab for viewing.</li>
        </ul>
    </div> 
    """, unsafe_allow_html=True) #Custom written description on main page


with tab1: #Start of tab1 content
    # --- Section 1: Median List Price ---
    st.markdown(f"### 📌 Analyzing: `{selected_metro}`, `{selected_state}`") #Shows currently selected State and Metro from sidebar user input
    st.subheader("📈 Median List Price Over Time") #Adds subheader
    st.markdown(
        "*The **median list price** is the midpoint of all active home listings in an area. "
        "It helps track pricing trends without being skewed by luxury or distressed listings. "
        "The average United States home list price is **$403,700.*** "
    ) #Adds description


    metro_data_price = df_medianlistprice[df_medianlistprice["RegionName"] == selected_metro] #Filter median list price data to only selected metro area
    date_columns_price = metro_data_price.columns[6:] #Identify date columns (time-series data)
    melted_price = metro_data_price.melt(id_vars=["RegionName"], value_vars=date_columns_price,
                                        var_name="Date", value_name="Median List Price") #Convert wide-format data into long format for time series plotting (one column for data, one column for values)
    melted_price["Date"] = pd.to_datetime(melted_price["Date"]) #Convert date strings to datetime objects
    melted_price = melted_price.dropna(subset=["Median List Price"]) #Drop missing values
    melted_price["Year"] = melted_price["Date"].dt.year #Extract year from the new date column for filtering by year


    year_options_price = ["Over Time"] + sorted(melted_price["Year"].unique().astype(str)) #Converts unique years to strings, sorts in ascending order
    selected_year_price = st.selectbox("Select a view for Median List Price (U.S. Dollars):", year_options_price, key="price") #Creates dropdown for user to pick a year or over time to control graph

    if selected_year_price != "Over Time": #If the user selects a specific year instead of Over Time
        filtered_price = melted_price[melted_price["Year"] == int(selected_year_price)] #Filter dataset to include only rows for that year
    else:
        filtered_price = melted_price #Otherwise if Over Time is selected use full dataset

    if filtered_price.empty: #Check if the filtered dataset is empty
        st.warning(f"No data available for the selected year: {selected_year_price}") #If empty show prompted message
    else:
        st.line_chart(filtered_price.set_index("Date")["Median List Price"]) #Displays line chart of media list price over time

    st.markdown("---") #Horizontal line separator



with tab2:  #Start of tab2 content
    st.markdown(f"### 📌 Analyzing: `{selected_metro}`, `{selected_state}`") #Shows currently selected State and Metro from sidebar user input
    # --- Section 2: Home Value (ZHVI) by Metro ---
    st.subheader("🏡 Zillow Home Value Index (ZHVI) by Metro") #Adds subheader
    st.markdown("""
    *This section shows the **Zillow Home Value Index (ZHVI)**, which reflects the typical home value in each metro area. ZHVI is a smoothed, **seasonally adjusted index** that reflects changes in the mid-tier home price segment over time.  
    Unlike simple median sale prices, it estimates the value of a "typical" home by controlling for **outliers and market volatility**, making it a reliable indicator of long-term housing trends and **price appreciation** in local markets.*
    """) #Adds written description


    metro_data_value = df_home_value[df_home_value["RegionName"] == selected_metro] #Filter data for the selcted metro
    date_columns_value = metro_data_value.columns[6:] #Get all date columns
    melted_value = metro_data_value.melt(id_vars=["RegionName"], value_vars=date_columns_value,
                                        var_name="Date", value_name="Home Value") #Convert date columns to long format for time series


    melted_value = melted_value[melted_value["Date"].str.match(r"\d{4}-\d{2}-\d{2}")] #Keep only rows where date matches YYYY-MM-DD format

    melted_value["Date"] = pd.to_datetime(melted_value["Date"]) #Convert date column to datetime objects (Pandas turns text to date objects for operations)

    melted_value = melted_value.dropna(subset=["Home Value"]) # Drop NaN values for Home Value

    melted_value["Year"] = melted_value["Date"].dt.year # Extract Year from the Date column

    monthly_avg_value = melted_value.groupby([melted_value["Date"].dt.to_period("M")])["Home Value"].mean().reset_index() #Groups melted data by month and calculates monthly average home value
    monthly_avg_value["Date"] = monthly_avg_value["Date"].dt.to_timestamp() #Converts period to full datetime format

    st.line_chart(monthly_avg_value.set_index("Date")["Home Value"]) #Creates line plot of home value over time

    # --- Home Value Table ---
    st.subheader("📊 Metro-Level Monthly Home Values (USD)") #Adds subheader
    st.markdown(
        "*_This table displays **monthly home values** across metros, based on the **Zillow Home Value Index (ZHVI), a seasonally adjusted measure of typical home values**._*"
    ) #Adds written description


    year_options_value = sorted(melted_value["Year"].unique().astype(str)) #Creates a list of available years from the data for dropdown selection
    selected_year_value = st.selectbox("Select a Year for Monthly Average Home Value Table:", year_options_value, key="value") #Adds dropdown menu to select a year for filtering

    filtered_value = melted_value[melted_value["Year"] == int(selected_year_value)] # Filter the data based on selected year for the table


    monthly_avg_value_table = filtered_value.groupby([filtered_value["Date"].dt.to_period("M")])["Home Value"].mean().reset_index() #Group filtered data by month and calculate average home value
    monthly_avg_value_table["Date"] = monthly_avg_value_table["Date"].dt.to_timestamp() #Converts period data to full datetime format

    st.dataframe(monthly_avg_value_table[["Date", "Home Value"]]) # Show the table with just Date and Home Value

    # --- Total Average Home Value Box ---
    average_home_value = monthly_avg_value_table["Home Value"].mean() #Computes home value average for selected year's date
    average_home_value = round(average_home_value, 2) #Rounds the average to two decimal places

    st.markdown(f"""
        <div style="padding: 10px; background-color: #f0f0f5; border-radius: 5px; 
                    display: flex; justify-content: space-between; align-items: center;">
            <h3 style="font-size: 1.2em;">🏡 Total Average Home Value for {selected_year_value}:</h3>
            <h2 style="color: #0072C6;">${average_home_value:,}</h2>
        </div> 
    """, unsafe_allow_html=True) #Displays total average home value for the year in a custom text box

    st.markdown("---") #Horizontal line separator


with tab3: #Start of tab3 content

    st.markdown(f"### 📌 Analyzing: `{selected_metro}`, `{selected_state}`") #Shows currently selected State and Metro from sidebar user input
    st.markdown("## Home Value Growth Rate Comparison (Jan - Mar 2025)") #Adds title
    st.markdown("""
        *The **home value growth rate** reflects the **average percentage change** in home prices over the past **three months** for each metro area. 
        It also highlights the **most recent month’s growth**, helping you identify emerging trends and evaluate short-term **market momentum**. 
        A **positive growth rate** indicates an increase in home values, suggesting market expansion, 
        while a **negative growth rate** signals a decrease, suggesting potential market contraction or slowing growth.*
        """)#Adds written description

    def match_city_to_metro(city, metro): 
        if isinstance(city, str) and isinstance(metro, str): #Checks if both city and metro are strings
            city_normalized = city.lower().replace(",", "").strip() #Normalize city string converting to lowercase, removes commas and blank spaces
            metro_normalized = metro.lower().replace(",", "").strip() #Normalize metro string converting to lowercase, removes commas and blank spaces
            if city_normalized in metro_normalized: #First trys to match city name as a substring within the metro name
                return True
            city_words = city_normalized.split() #If first option fails, split the city name into separate words and check if any match metro name
            return any(word in metro_normalized for word in city_words)
        return False #Retruns false if either city or metro is not a string


    comparison_metros = st.multiselect("Select or type in additional metro areas for comparison:", df_house_growth['Metro'].unique(), default=[]) #Displays a multi-select dropdown for user to choose additional metro areas

    selected_metros_for_kpi = [selected_metro] + comparison_metros # Combines the selected metro with any additional metros the user chooses

    df_house_growth_melted = df_house_growth.melt(id_vars=["Metro", "City"], value_vars=["2025-04-30", "2025-06-30", "2026-03-31"],  # Reshape the house growth data to have 'Date' and 'Growth Percentage' columns
                                            var_name="Date", value_name="Growth Percentage")  # Reshape the data to long format

    df_house_growth_melted["Date"] = pd.to_datetime(df_house_growth_melted["Date"])  # Convert 'Date' to datetime

    df_house_growth_selected_metros = df_house_growth_melted[ # Filter data to include only the selected metros or cities
        df_house_growth_melted['Metro'].apply(lambda metro: any(match_city_to_metro(city, metro) for city in selected_metros_for_kpi)) | #Checks each metro in Metro column of dataframe to see if any cities in list match
        df_house_growth_melted['City'].isin(selected_metros_for_kpi)  # Include selected metros or cities
    ]
    kpi_data = df_house_growth_selected_metros.groupby(["Metro", "City"]).agg({ # Group by Metro and City to calculate the mean and sum of growth percentages
        "Growth Percentage": ["mean", "sum"]}).reset_index()  # Calculate mean and sum of growth percentages

    
    for metro in selected_metros_for_kpi: # Iterate through each selected metro to display KPIs
        metro_data = df_house_growth_selected_metros[
            (df_house_growth_selected_metros['Metro'].apply(lambda metro_name: match_city_to_metro(metro, metro_name))) |
            (df_house_growth_selected_metros['City'] == metro)  # Filter data to include selected metro
        ]

        avg_growth = metro_data["Growth Percentage"].mean()  # Calculate average growth percentage
        if not pd.isna(avg_growth):  # Check if the average growth is a valid number
            avg_growth = round(avg_growth, 2)

        recent_growth_row = metro_data[metro_data["Date"] == pd.to_datetime("2026-03-31")] # Get the most recent growth value for March 2026
        if not recent_growth_row.empty:  # If data exists for March 2026
            recent_growth = recent_growth_row["Growth Percentage"].values[0].round(2) #Round to 2 decimal places
            recent_growth_display = f"{recent_growth}%" #Format the growth percentage for display
        else:
            recent_growth_display = "Not Enough Data"  # Display message if data is missing

        # Display KPI metrics side by side for each metro
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=f"Average Growth Rate ({metro})", value=f"{avg_growth}%")  # Displays average growth
        with col2:
            st.metric(label=f"March 2026 Growth Rate({metro})", value=recent_growth_display)  # Displays most recent growth value

    st.markdown("---")  # Horizontal line separator



with tab4: #Start of tab4 content

    st.markdown(f"### 📌 Analyzing: `{selected_metro}`, `{selected_state}`") #Shows currently selected State and Metro from sidebar user input
    st.markdown("## 🏦 Sale-to-List Ratio: Market Mood Gauge") #Adds title
    st.markdown(
        "*_This gauge shows the most recent **sale-to-list price ratio**, which compares the final **sale price** of homes to their original **list price**._* "
        "*_A ratio **above 100%** suggests homes are selling for **more than asking**, indicating a competitive, **seller-friendly market**._* "
        "*_Ratios **below 100%** suggest **buyers have more negotiating power**._*"
    ) #Adds written explanation

    date_columns = df_saletolist.columns[5:]  # Selects all date columns (starts after non-date columns)
    df_saletolist_melted = df_saletolist.melt(
        id_vars=["RegionName", "StateName"],  #Uses RegionName and StateName as identifiers
        value_vars=date_columns, #Melts on date columns
        var_name="Date", #New column name is set as "Date"
        value_name="Sale_to_List_Ratio" #New column name for the values in the melted columns
    )
    df_saletolist_melted["Date"] = pd.to_datetime(df_saletolist_melted["Date"]) #Transforms Date column into datetime format

    df_saletolist_selected = df_saletolist_melted[df_saletolist_melted["RegionName"] == selected_metro] #Filters the melted data for the selected metro

    if not df_saletolist_selected.empty: #Check there is data in selected metro
        latest_row = df_saletolist_selected.sort_values("Date").iloc[-1] #Sort by date and use most recent row
        latest_ratio = latest_row["Sale_to_List_Ratio"] #Extracts the most recent sale-to-list ratio
        latest_date = latest_row["Date"].strftime("%B %Y") #Formats the date into a string format

        if latest_ratio < 0.97: #If the ratio is below 97
            emoji = "📉" #If True display the following
            mood = "Cold Market"
            color = "red"
        elif 0.97 <= latest_ratio <= 1.00:  #If the ratio is between 97 and 100
            emoji = "⚖️" #If True display the following
            mood = "Balanced Market"
            color = "orange"
        else: # If the ratio is above 100
            emoji = "🔥" #If True display the following
            mood = "Hot Market"
            color = "green"

        st.markdown(f"""
        <div style='padding: 1rem; border-radius: 10px; background-color: #f9f9f9; border-left: 6px solid {color};'>
            <h3>{emoji} {mood}</h3>
            <p style='font-size: 1.2rem;'>Most recent Sale-to-List Ratio for <strong>{selected_metro}</strong> ({latest_date}): <strong>{latest_ratio:.2%}</strong></p>
        </div>
        """, unsafe_allow_html=True) #Displays value in custom box
    else:
        st.info(f"⚠️ Limited data available for **{selected_metro}**, **{selected_state}**. Try another metro area to view Sale-to-List Ratio insights.") #If there is no data found display limited data message
    
    st.markdown("""
        * **Cold Market (📉)**: When the sale-to-list ratio is below 97%, it indicates that homes are generally selling below their asking prices, signaling a buyer’s market with less competition and potentially more negotiation power for buyers.
  
        * **Balanced Market (⚖️)**: A sale-to-list ratio between 97% and 100% suggests a balanced market, where supply and demand are relatively equal, giving both buyers and sellers similar levels of negotiating power.

        * **Hot Market (🔥)**: A sale-to-list ratio above 100% indicates a seller’s market, where homes are selling for more than the asking price, often due to high demand and low inventory, leading to competitive bidding among buyers.
        """) #Adds written description
    
    st.markdown("---") #Horizontal line separator


with tab5: #Start of tab5 content

    st.markdown(f"### 📌 Analyzing: `{selected_metro}`, `{selected_state}`") #Shows currently selected State and Metro from sidebar user input
    st.markdown("## 🧭 Market Heat Index") #Adds heading
    st.markdown("""
        *The **Market Heat Index** is a metric that gauges the level of real estate **demand relative to the supply** of homes in a given market. It helps evaluate how **competitive a market is** by comparing the number of buyers actively seeking homes with the available **inventory for sale**.*
        """) #Adds written description


    date_columns = [col for col in df_market_heat.columns if re.match(r"\d{4}-\d{2}-\d{2}", str(col))]
    df_market_heat_melted = df_market_heat.melt( #Identifies columns with date format
        id_vars=["RegionName", "StateName"], #Use RegionName and StateName as identifiers
        value_vars=date_columns, #Only transform date columns
        var_name="Date", #New column "Date" will hold date values
        value_name="HeatIndex" #New column Heat Index will contain heat index values
    )
    df_market_heat_melted["Date"] = pd.to_datetime(df_market_heat_melted["Date"]) #Converts Date column to datetime format

    main_metro = selected_metro  # Sets the main metro based on user selection in sidebar

    all_metros = sorted(df_market_heat_melted["RegionName"].unique()) #Gets a sorted list of all available mtros
    comparison_metro = st.selectbox("Compare with another metro", [m for m in all_metros if m != main_metro]) #Creates dropdown to select a second metro for comparison

    df_main = df_market_heat_melted[df_market_heat_melted["RegionName"] == main_metro] #Filters melted data for the main metro
    df_comp = df_market_heat_melted[df_market_heat_melted["RegionName"] == comparison_metro] #Filters melted data for the comparison metro

    df_main_recent = df_main.sort_values("Date", ascending=False).head(3).sort_values("Date") #Gets the latest 3 months for the main metro, sorted chonologically
    df_comp_recent = df_comp.sort_values("Date", ascending=False).head(3).sort_values("Date") #Gets the latest 3 months for the comparison metro, sorted chonologically


    st.subheader(f"🔥 Market Heat Index (0-100): {main_metro} vs {comparison_metro}") #Adds subheader with user selected metros

    col1, col2 = st.columns(2) #Creates two side-by-side columns for layout

    with col1:
        st.markdown(f"**{main_metro}**") #Displays the name of the main metro
        for row in df_main_recent.itertuples(): #Iterates through each recent row
            st.metric(label=row.Date.strftime("%b %Y"), value=f"{row.HeatIndex:.1f}" if pd.notna(row.HeatIndex) else "N/A") #Displays month and heat index or NaN

    with col2:
        st.markdown(f"**{comparison_metro}**") #Displays the name of the comparison metro
        for row in df_comp_recent.itertuples(): #Iterates through each recent row
            st.metric(label=row.Date.strftime("%b %Y"), value=f"{row.HeatIndex:.1f}" if pd.notna(row.HeatIndex) else "N/A") #Displays month and heat index or NaN
    st.markdown("""
        *A **higher value** on the **Market Heat Index** indicates a **hotter market**, where **demand exceeds supply**, often leading to **higher home prices** and **faster sales**. Conversely, a **lower value** suggests a **cooler market** with **less competition**, where prices may stabilize or decline due to **less buyer activity**.*
        """) #Adds written description
    st.markdown("---") #Horizontal line separator


with tab6: #Start of tab6 content

    st.markdown(f"### 📌 Analyzing: `{selected_metro}`, `{selected_state}`") #Shows currently selected State and Metro from sidebar user input
    st.markdown("### 💰 New Homeowner Income Comparison") #Adds heading
    st.markdown("""
        *This section compares **Zillow's New Homeowner Income** metric for the selected metro area and a comparison metro, using the latest available data.  
        This metric reflects the **estimated annual income** of individuals or households who have recently purchased homes. It provides insight into the **economic profile of new buyers** in each region and helps assess affordability across metros.*
        """) #Adds written description

    date_columns_income = [col for col in df_new_homeowner_income.columns if re.match(r"\d{4}-\d{2}-\d{2}", str(col))]
    df_income_melted = df_new_homeowner_income.melt( #
        id_vars=["RegionName", "StateName"], #Uses RegionName and StateName as identifiers
        value_vars=date_columns_income, #Melt the date columns 
        var_name="Date", #New Date column for transformed date values
        value_name="NewHomeownerIncome" #New Homeowner Income column for transformed income values
    )
    df_income_melted["Date"] = pd.to_datetime(df_income_melted["Date"]) #Converts date strings to datetime format

    main_metro = selected_metro  # Uses the metro the user selected in the sidebar

    all_metros = sorted(df_income_melted["RegionName"].unique()) #Selects all unique metros in the dataset
    comparison_metro = st.selectbox("Compare with another metro", [m for m in all_metros if m != main_metro]) #Allows users to choose a second metro to compare

    df_main_income = df_income_melted[df_income_melted["RegionName"] == main_metro] #Find income data for main metro selected
    df_comp_income = df_income_melted[df_income_melted["RegionName"] == comparison_metro] #Find income data for comparison metro selected

    latest_date_income = df_main_income["Date"].max() #Find the most recent date for main metro

    if pd.isna(latest_date_income): #Check is the latest date is missing or invalid
        latest_date_income_str = "No valid data" #Display message if no valid data is available
    else:
        latest_date_income_str = latest_date_income.strftime('%b %Y') #If the date is valid format to month year format 

    df_main_latest_income = df_main_income[df_main_income["Date"] == latest_date_income] #Filters the main metro's data to include rows from most recent month
    df_comp_latest_income = df_comp_income[df_comp_income["Date"] == latest_date_income] #Filters the comparison metro's data to include rows from most recent month

    bar_data = pd.DataFrame({ #Creates a new DataFrame to hold chart values
        'RegionName': [main_metro, comparison_metro], #First column is names of two metros being compared
        'NewHomeownerIncome': [
            df_main_latest_income["NewHomeownerIncome"].values[0] if not df_main_latest_income.empty else None, #Second column holds new homeowner income values for main metro
            df_comp_latest_income["NewHomeownerIncome"].values[0] if not df_comp_latest_income.empty else None #Second column holds comparison homeowner income values for main metro
        ]
    })
    fig = px.bar(bar_data, x="RegionName", y="NewHomeownerIncome", color="RegionName",
                labels={'NewHomeownerIncome': 'New Homeowner Income ($)', 'RegionName': 'Metro Area'},
                title=f'💰 New Homeowner Income (Latest Month: {latest_date_income_str})') #Uses plotly to create a grouped bar chart, adds axis labels and title

    fig.update_layout(title=f"💰 New Homeowner Income Comparison: {main_metro} vs {comparison_metro}", 
                    xaxis_title='Metro Area', yaxis_title='Income ($)', barmode='group') #Title includes metro names, places bars side by side 

    for i, row in bar_data.iterrows(): #Loops over each row of bar_data to annotate chart
        fig.add_annotation(
            x=row['RegionName'],
            y=row['NewHomeownerIncome'],
            text=f"${row['NewHomeownerIncome']:.0f}", #Formats value as integer dollar amount
            showarrow=True,
            arrowhead=2,
            ax=0,
            ay=-40,
            font=dict(size=12, color="black", family="Arial"),
            align="center" #Adds a styled format to label, with label right above matching bar
        )

    st.plotly_chart(fig) # Display the bar chart

    st.subheader(f"💰 New Homeowner Income (Latest Month: {latest_date_income_str})") #Adds section heading

    col1, col2 = st.columns(2) #Creates two side-by-side columns for the two metrics

    with col1: #First column displays main metro's home owner income
        value = df_main_latest_income["NewHomeownerIncome"].values[0] if not df_main_latest_income.empty else None #Finds home owner value for main metro
        st.metric(label=main_metro, value=f"${value:.0f}" if pd.notna(value) else "N/A") #Display N/A if data is missing

    with col2: #Second column displays comparison metro's home owner income
        value = df_comp_latest_income["NewHomeownerIncome"].values[0] if not df_comp_latest_income.empty else None #Finds home owner value for comparison metro
        st.metric(label=comparison_metro, value=f"${value:.0f}" if pd.notna(value) else "N/A") #Display N/A if data is missing
    
    st.markdown("---") #Horizontal line separator



with tab7: #Start of tab7 content
    st.markdown("## 👥 Demographic Overview") #Adds section heading
    st.markdown(
        "_Explore key demographic statistics for the selected metro area (**chosen below, not in the sidebar**) — "
        "this distinction is due to the deeper geographic coverage in the Census demographic dataset. "
        "These stats provide valuable context on the population's composition and lifestyle._"
        ) #Adds written description
    
    states = sorted(df_demographics['State'].unique()) #Gets a sorted list of all unique states in the dataset
    selected_state = st.selectbox('Select State', states) #Lets the user pick a state from a dropdown bar

    cities_in_state = df_demographics[df_demographics['State'] == selected_state]['City'].unique() #Filter cities list by chosen state
    selected_city = st.selectbox('Select City', cities_in_state) #Lets the user pick a city from the filtered list

    #Filter the demographic data for the selected state and city
    filtered_data = df_demographics[(df_demographics['State'] == selected_state) & 
                                (df_demographics['City'] == selected_city)] #Subset data to the selected state and city

    #Group by 'City' and 'State' and aggregate the demographic columns
    aggregated_data = filtered_data.groupby(['City', 'State']).agg({
        'Median Age': 'mean', #Takes the mean of the numeric columns to avoid duplicates
        'Male Population': 'sum',
        'Female Population': 'sum',
        'Total Population': 'sum',
        'Number of Veterans': 'sum',
        'Foreign-born': 'sum',
        'Average Household Size': 'mean',
        'Count': 'sum'  #Sum up the 'Count' for aggregated information
    }).reset_index() #Reset index for clean display

    #Reorder and select columns to display
    aggregated_data = aggregated_data[['City', 'State', 'Median Age', 'Male Population', 
                                   'Female Population', 'Total Population', 'Number of Veterans', 
                                   'Foreign-born', 'Average Household Size']]

    st.write(f"### Demographic Information for {selected_city}, {selected_state}") #Adds subheading of selected city and state
    st.dataframe(aggregated_data) #Displays summarized data frame

    demographic_columns = ['Median Age', 'Male Population', 'Female Population', 
                       'Total Population', 'Number of Veterans', 'Foreign-born', 
                       'Average Household Size'] # Let the user filter for specific demographic info

    selected_demographic = st.selectbox('Select Specific Demographic Metric:', demographic_columns) #Dropdown box to select a specific metric

    if selected_demographic in filtered_data.columns: #Checks if the selected metric is available in the data
        demographic_value = filtered_data[selected_demographic].values[0] #Retrieves the specific value
        st.markdown(f"""
        <div style="background-color: #f9f9f9; padding: 1rem; border-radius: 10px; 
                display: flex; justify-content: space-between; align-items: center; 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <h3 style="font-size: 1.5rem; color: #333;">{selected_demographic}</h3>
            <span style="font-size: 2rem; font-weight: bold; color: #007BFF;">{demographic_value}</span>
            </div>
        """, unsafe_allow_html=True) # Display selected demographic value in a box below the table
    else:
        st.warning("No data available for the selected demographic info.") #Displays message if the metric is not available

    st.markdown("---")  # Horizontal line separator


with tab8: #Start of tab8 content
    if st.session_state.all_notes: #Only display notes if there are any saved in the session state
        st.markdown("---") # Horizontal line separator
        st.markdown("### 📚 Your Notes") #Adds heading

        for i, note in enumerate(st.session_state.all_notes, 1): #Loop through all notes and index them
            st.markdown(f""" 
            <div style='background-color: #f9f9f9; padding: 15px; border-left: 5px solid #2E86C1; border-radius: 5px; margin-bottom: 10px;'>
                <strong>Note {i}:</strong><br>{note.replace('\n', '<br>')}
            </div>
            """, unsafe_allow_html=True) #Styles each note as a seperate card