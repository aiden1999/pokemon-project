import streamlit as st


def main():
    comparison_page = st.Page(
        "pages/comparison/comparison.py", title="Comparison Page"
    )

    capture_other_pokemon = st.Page(
        "../src/pages/capture_other_pokemon.py", title="Catch a pokemon!"
    )

    top_ranks = st.Page("../src/pages/top_rank.py", title="Top Ranks")
    pages = st.navigation([top_ranks, comparison_page, capture_other_pokemon])
    pages.run()


if __name__ == "__main__":
    main()
