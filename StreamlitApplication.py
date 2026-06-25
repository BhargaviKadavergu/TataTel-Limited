import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Science Calculator", page_icon="📊")

st.title("📊 Data Science Calculator")

st.write("Enter numbers separated by commas.")

numbers = st.text_input(
    "Numbers",
    "10,20,30,40,50"
)

if st.button("Calculate"):
    try:
        data = np.array([float(x.strip()) for x in numbers.split(",")])

        st.subheader("Results")

        st.write("Count:", len(data))
        st.write("Sum:", np.sum(data))
        st.write("Mean:", np.mean(data))
        st.write("Median:", np.median(data))
        st.write("Minimum:", np.min(data))
        st.write("Maximum:", np.max(data))
        st.write("Standard Deviation:", np.std(data))

        df = pd.DataFrame({"Values": data})
        st.subheader("Data")
        st.dataframe(df)

        st.subheader("Chart")
        st.line_chart(df)

    except Exception as e:
        st.error(f"Error: {e}")