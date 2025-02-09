import streamlit as st
import pandas as pd

st.title("Dog Breeds") #Displays title 

st.text("This app presents a data frame of the Dogs dataset, found in the data folder, and offers multiple interactive filtering options for users to explore the data in greater detail.")

st.header("Now, let's look at different types of dogs!") #Displays header

df = pd.read_csv("data/dogs_dataset.csv") # Reads in CSV file from the data/ folder, stores in a dataframe

st.subheader("Here's the dataset loaded from a CSV file:")
st.dataframe(df) #Displays dataset as an interactive table 

#Select box for a certain dog breed, outputs each unique dog within that breed

st.subheader("Select a dog breed in the drop down bar to see dogs with this breed type:") #Displays subheader
Breed = st.selectbox("Select a Breed", df["Breed"].unique()) #Creates dropdown with unique dog breeds from the dataset
filtered_df = df[df["Breed"] == Breed] #Filters dataset to only include rows where breed column matches selected breed
st.write(f"Dogs in {Breed} breed group:") #Displays text showing breed group being filtered for
st.dataframe(filtered_df) #Displays filtered data in a table format

#Slider for dog weight, outputs dog breeds within that weight group

st.subheader("Select a weight (kg) to see dogs that fit within this weight group:") #Displays subheader
weight = st.slider("Select Dog Weight:", min_value=int(df["Weight (kg)"].min()), max_value=int(df["Weight (kg)"].max())) #Creates slider with user input for dog's weight, slider range set to min/max of weights in dataset
dogs_in_range = df[df["Weight (kg)"] == weight] #Filters dataset to find dogs which match selected weight
st.write(f"Dogs that weigh {weight} kgs:") #Displays text showing selected weight 
if not dogs_in_range.empty: #Checks if there are gods that match selected weight
    st.write(dogs_in_range[["Breed", "Weight (kg)"]])
else:
    st.write("No dogs found in this weight range.") #If match exists displays breed and weight columns otherwise says weight not found


#Radio Buttons for ages of different dogs, outputs other column data of dogs found in that age

st.subheader("Select an age to learn more about dogs currently with this age:") #Displays subheader
age_groups_sorted = sorted(df["Age (Years)"].unique()) #Extract all unique ages from dataset, sorts them in ascending order
age_group = st.radio("Select Dog Age Group:", age_groups_sorted) #Creates radio button selections for users to choose an age, displays sorted age choices
dogs_in_age_group = df[df["Age (Years)"] == age_group] #Filters dataset to find dogs that match selected age
st.write(f"Dogs that are {age_group} years old:") #Displays text indicating which age group is being shown
if not dogs_in_age_group.empty: #If match exists, displays dogs weight, breed, color, and gender
    st.write(dogs_in_age_group[["Weight (kg)", "Breed", "Color", "Gender"]])
else:
    st.write("No dogs found in this age group.") #If no dog matches the selected age displays not found message

