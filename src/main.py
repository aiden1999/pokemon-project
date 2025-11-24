import pandas as pd
import streamlit as st


def main():
    # df = pd.read_csv("./pokemon_v2.csv")
    # example:
    # home_page = st.page("path/to/home_page.py", title="Home Page")
    # list pages here
    # ...
    home_page = st.Page(
        "../src/pages/homepage.py", title="Home", icon=":material/home:"
    )
    top_ranks = st.Page(
        "../src/pages/top_rank.py", title="Top Ranks", icon=":material/trophy:"
    )
    pages = st.navigation([home_page, top_ranks])
    pages.run()


if __name__ == "__main__":
    main()
