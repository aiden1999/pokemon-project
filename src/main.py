import streamlit as st


def main():
    home_page = st.Page(
        "../src/pages/homepage.py", title="Home", icon=":material/home:"
    )
    comparison_page = st.Page("pages/comparison/comparison.py", title="Comparison Page")
    top_ranks = st.Page(
        "../src/pages/top_rank.py",
        title="Top Ranks",
        icon="star",
    )
    
    pages = st.navigation([top_ranks, comparison_page])
    pages.run()


if __name__ == "__main__":
    main()
