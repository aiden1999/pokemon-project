import pandas as pd
import streamlit as st


def main():
    # df = pd.read_csv("./pokemon_v2.csv")
    # example:
    # home_page = st.page("path/to/home_page.py", title="Home Page")
    # list pages here
    # ...
    top_ranks = st.page(
        "../src/pages/top_rank.py",
        title="Top Ranks",
        icon="star",
    )
    pages = st.navigation([top_ranks])
    pages.run()
    # pages = st.navigation([list, pages, here])
    # pages.run()


if __name__ == "__main__":
    main()
