import os
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO


# Load data
@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(
        os.path.dirname(script_dir), "data", "pokemon_v2.csv"
    )
    return pd.read_csv(file_path)


# Load Pokemon data
pokemon_df = load_data()

# Pokemon type colors for visualizations
type_colors = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD",
}

# Page config with Pokemon favicon
st.set_page_config(
    page_icon="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png",
    layout="wide",
)

# Custom CSS for better centering
st.markdown(
    """
<style>
    .center-image {
        display: flex;
        justify-content: center;
    }
    .featured-pokemon {
        text-align: center;
        padding: 1rem;
    }
</style>
""",
    unsafe_allow_html=True,
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

# Display random featured Pokémon at the top - using a more balanced layout
if "image_url" in pokemon_df.columns:
    featured_pokemon = pokemon_df.sample(1).iloc[0]

    # Use a more balanced column layout with empty columns on sides for centering
    col_left, col_img, col_info, col_right = st.columns([2, 1, 2, 2])

    with col_img:
        st.markdown('<div class="center-image">', unsafe_allow_html=True)
        try:
            response = requests.get(featured_pokemon["image_url"], timeout=5)
            img = Image.open(BytesIO(response.content))
            st.image(img, width=200)
        except:
            st.image(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png",
                width=200,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_info:
        st.markdown('<div class="featured-pokemon">', unsafe_allow_html=True)
        st.markdown(f"### Featured Pokémon: {featured_pokemon['name']}")

        # Show species if available
        if "species" in featured_pokemon and pd.notna(
            featured_pokemon["species"]
        ):
            st.write(f"**Species:** {featured_pokemon['species']}")

        # Show Japanese name if available
        if "japanese_name" in featured_pokemon and pd.notna(
            featured_pokemon["japanese_name"]
        ):
            st.write(f"**Japanese Name:** {featured_pokemon['japanese_name']}")

        # Show German name if available
        if "german_name" in featured_pokemon and pd.notna(
            featured_pokemon["german_name"]
        ):
            st.write(f"**German Name:** {featured_pokemon['german_name']}")

        # Display type badges
        type_html = ""
        if "type_1" in featured_pokemon and pd.notna(
            featured_pokemon["type_1"]
        ):
            type1 = featured_pokemon["type_1"]
            type_html += f"""<span style="background-color: {type_colors.get(str(type1).lower(), '#777')}; 
                            color: white; padding: 3px 10px; border-radius: 10px; margin-right: 5px;">
                            {type1}</span>"""

        if "type_2" in featured_pokemon and pd.notna(
            featured_pokemon["type_2"]
        ):
            type2 = featured_pokemon["type_2"]
            type_html += f"""<span style="background-color: {type_colors.get(str(type2).lower(), '#777')}; 
                            color: white; padding: 3px 10px; border-radius: 10px;">
                            {type2}</span>"""

        st.markdown(f"**Types:** {type_html}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Sidebar with Pokemon styling
st.sidebar.image(
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
    width=100,
)
