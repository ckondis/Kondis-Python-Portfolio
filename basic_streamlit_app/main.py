import streamlit as st
import pandas as pd

st.title("Dog Breeds")

st.text("This app presents a data frame of the Dogs dataset, found in the data folder, and offers multiple interactive filtering options for users to explore the data in greater detail.")

st.header("Now, let's look at different types of dogs!")

df = pd.read_csv("data/dogs_dataset.csv")

st.subheader("Here's the dataset loaded from a CSV file:")
st.dataframe(df)

#Select box for a certain dog breed, outputs each unique dog within that breed

st.subheader("Select a dog breed in the drop down bar to see dogs with this breed type:")
Breed = st.selectbox("Select a Breed", df["Breed"].unique())
filtered_df = df[df["Breed"] == Breed]
st.write(f"Dogs in {Breed} breed group:")
st.dataframe(filtered_df)

#Slider for dog weight, outputs dog breeds within that weight group

st.subheader("Select a weight (kg) to see dogs that fit within this weight group:")
weight = st.slider("Select Dog Weight:", min_value=int(df["Weight (kg)"].min()), max_value=int(df["Weight (kg)"].max()))
dogs_in_range = df[df["Weight (kg)"] == weight]
st.write(f"Dogs that weigh {weight} lbs:")
if not dogs_in_range.empty:
    st.write(dogs_in_range[["Breed", "Weight (kg)"]])
else:
    st.write("No dogs found in this weight range.")


#Radio Buttons for ages of different dogs, outputs other column data of dogs found in that age

st.subheader("Select an age to learn more about dogs currently with this age:")
age_groups_sorted = sorted(df["Age (Years)"].unique())
age_group = st.radio("Select Dog Age Group:", age_groups_sorted)
dogs_in_age_group = df[df["Age (Years)"] == age_group]
st.write(f"Dogs that are {age_group} years old:")
if not dogs_in_age_group.empty:
    st.write(dogs_in_age_group[["Weight (kg)", "Breed", "Color", "Gender"]])
else:
    st.write("No dogs found in this age group.")

