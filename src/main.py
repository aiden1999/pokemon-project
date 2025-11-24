import streamlit as st


def main():
    comparison_page = st.Page(
        "pages/comparison/comparison.py", title="Comparison Page", icon="⚖️"
    )
    top_ranks = st.Page(
        "../src/pages/top_rank.py",
        title="Top Ranks",
        icon="⭐",
    )
    pages = st.navigation([top_ranks, comparison_page])
    pages.run()


if __name__ == "__main__":
    main()
