import pandas as pd
import streamlit as st


def main():
    df = pd.read_csv("./pokemon_v2.csv")
    # example:
    # home_page = st.page("path/to/home_page.py", title="Home Page")
    # list pages here
    # ...

    # pages = st.navigation([list, pages, here])
    # pages.run()


if __name__ == "__main__":
    main()
