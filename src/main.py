import pandas as pd
import streamlit as st


def main():
    st.title("Pokemon data exploration")  # can change this
    df = pd.read_csv("./pokemon_v2.csv")
    st.write("hello world")  # placeholder


if __name__ == "__main__":
    main()
