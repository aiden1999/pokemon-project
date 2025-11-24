import streamlit as st


def main():
    home_page = st.Page(
        "../src/pages/homepage.py", title="Home", icon=":material/home:"
    
    comparison_page = st.Page(
        "pages/comparison/comparison.py", title="Comparison Page", icon="⚖️"
    )
    top_ranks = st.Page(
        "../src/pages/top_rank.py",
        title="Top Ranks",
        icon="⭐",
    )
    capture_other_pokemon = st.Page(
        "../src/pages/capture_other_pokemon.py", title="Catch a pokemon!"
    )
    pages = st.navigation([home_page, top_ranks, comparison_page, capture_other_pokemon])
    pages.run()


if __name__ == "__main__":
    main()
