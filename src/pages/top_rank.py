import os
import pandas as pd
import streamlit as st
import plotly.express as px


# Load data
@st.cache_data
def load_data():
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct path to the CSV file relative to the script location
    file_path = os.path.join(
        os.path.dirname(script_dir), "data", "pokemon_v2.csv"
    )
    return pd.read_csv(file_path)


pokemon_df = load_data()

# Header
st.set_page_config(layout="wide")
# Title
st.title("Pokémon Data Explorer")
# Sidebar for user inputs
st.sidebar.header("Filter Options")
# Filter by any stats
stats_options = [
    "hp",
    "attack",
    "defense",
    "speed",
    "sp_attack",
    "sp_defense",
]
selected_stat = st.sidebar.selectbox("Select Stat to Filter By", stats_options)

# Display the filtered data
# Top N Pokémon based on the selected stat
st.subheader(f"Top 10 Pokémon by {selected_stat.capitalize()}")
top_n = 10
top_pokemon = pokemon_df.nlargest(top_n, selected_stat)[
    ["name", selected_stat]
]
fig = px.bar(
    top_pokemon,
    x="name",
    y=selected_stat,
    color="name",
    labels={selected_stat: selected_stat.capitalize(), "name": "Pokémon Name"},
)
st.plotly_chart(fig)
