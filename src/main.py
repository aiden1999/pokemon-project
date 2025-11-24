import streamlit as st


def main():
    # example:
    # home_page = st.page("path/to/home_page.py", title="Home Page")
    # list pages here
    # ...
    comparison_page = st.Page("pages/comparison/comparison.py", title="Comparison Page")

    pages = st.navigation([comparison_page])
    pages.run()


if __name__ == "__main__":
    main()
