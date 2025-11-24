import streamlit as st
from pages.comparison.info_card import InfoCard
from pages.top_rank import load_data

df = load_data()
pokemon_names = df["name"].to_list()

if "pokemon_dict_1" not in st.session_state:
    st.session_state.pokemon_dict_1 = None
if "pokemon_dict_2" not in st.session_state:
    st.session_state.pokemon_dict_2 = None

st.title("Pokémon Comparison")

col1, col2 = st.columns(2)

with col1:
    name_1 = st.selectbox(
        "Search Pokémon",
        options=pokemon_names,
        help="Start typing to see suggestions",
        key="select_1",
    )
    if name_1:
        named_row = df.loc[df["name"] == name_1]
        st.session_state.pokemon_dict_1 = named_row.iloc[0].to_dict()

with col2:
    name_2 = st.selectbox(
        "Search Pokémon",
        options=pokemon_names,
        help="Start typing to see suggestions",
        key="select_2",
    )
    if name_2:
        named_row = df.loc[df["name"] == name_2]
        st.session_state.pokemon_dict_2 = named_row.iloc[0].to_dict()

col1, col2 = st.columns(2)

with col1:
    if st.session_state.pokemon_dict_1:
        InfoCard(st.session_state.pokemon_dict_1, st.session_state.pokemon_dict_2)
with col2:
    if st.session_state.pokemon_dict_2:
        InfoCard(st.session_state.pokemon_dict_2, st.session_state.pokemon_dict_1)
