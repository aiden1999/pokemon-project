import streamlit as st
import pandas as pd
from pages.comparison.info_card import InfoCard

df = pd.read_csv("./pokemon_v2.csv")
pokemon_names = df["name"].to_list()

st.title("Pokemon Comparison")
with st.form("comparison_1_form"):
    st.subheader("Choose Pokemon for comparison")
    # Form inputs
    name = st.selectbox(
        "Search Pokémon",
        options=pokemon_names,
        help="Start typing to see suggestions",
    )
    submitted = st.form_submit_button("Select")

if submitted:
    named_row = df.loc[df["name"] == name]
    pokemon_dict = named_row.iloc[0].to_dict()
    pokemon_1 = InfoCard(pokemon_dict)
