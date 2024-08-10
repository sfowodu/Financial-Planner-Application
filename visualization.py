import matplotlib.pyplot as plt
import streamlit as st


def plot_savings_projection(years, future_savings):
    plt.figure(figsize=(10, 5))
    plt.plot(range(years + 1), future_savings, marker='o')
    plt.title('Savings Projection Over Time')
    plt.xlabel('Years')
    plt.ylabel('Future Savings')
    plt.grid(True)
    st.pyplot(plt)
