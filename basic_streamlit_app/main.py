import streamlit as st

st.title(Dog Breeds)

st.subheader("Now, let's look at different types of dogs!")

df = pd.read_csv("data/dogs_dataset.csv")

st.write("Here's the dataset loaded from a CSV file:")
st.dataframe(df)


