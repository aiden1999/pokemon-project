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

# Page config with Pokemon favicon
st.set_page_config(
    page_icon="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png",
    layout="wide",
)

# Header with Pokemon styling
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(
        """
    <h1 style='text-align: center; color: #3B4CCA; text-shadow: 2px 2px #FFDE00;'>
        <img src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png' height='50'> 
        Pokémon Data Explorer
    </h1>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <p style='text-align: center; font-size: 1.2em; color: #FF0000; font-weight: bold;'>
    Your complete guide to the world of Pokémon! Gotta catch 'em all!
    </p>
    """,
        unsafe_allow_html=True,
    )

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
top_n_of_pokemon = pokemon_df.nlargest(top_n, selected_stat)[
    ["name", selected_stat]
]
fig = px.bar(
    top_n_of_pokemon,
    x="name",
    y=selected_stat,
    color="name",
    labels={selected_stat: selected_stat.capitalize(), "name": "Pokémon Name"},
)
st.plotly_chart(fig)

# Sidebar with Pokemon styling
st.sidebar.image(
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    width=100,
)
