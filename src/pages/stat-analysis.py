"""
# 4 As a USER I want to be able to view a comparison of stats from multiple Pokemon SO THAT I can easily identify strategic templates like 'glass cannons' or 'tanks'
"""

# DONE Be able to select 2 different stats
# DONE Show scatter plot of pokemon across the two stats
# DONE Show pokemon name when hovering over a plot
# Have everything fit the defined colour scheme

# Be able to select pokemon from graph
# Select pre-set graphs to show strategic templates


import streamlit as st
import pandas as pd
import plotly.express as px
from pages.top_rank import load_data

st.set_page_config(layout="centered")
st.title("Statistic comparison")


manual, pre_set = st.tabs(["Manual Analysis", "Explore pre-set roles"])
df = load_data()

columns = [
    "hp",
    "attack",
    "defense",
    "sp_attack",
    "sp_defense",
    "speed",
    "total_points",
]

display_columns_dict = {
    "hp": "Health Points",
    "attack": "Attack",
    "defense": "Defense",
    "sp_attack": "Special Attack",
    "sp_defense": "Special Defense",
    "speed": "Speed",
    "total_points": "Total Points",
}
# type list generated with DeepSeek AI because typing them out would have been tedious
type_list = (
    "Normal",
    "Fire",
    "Water",
    "Electric",
    "Grass",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy",
)

with manual:

    stat_input_X = st.selectbox(
        label="X-axis stat ",
        options=columns,
        help="Select your first statistic from the dropdown ",
        index=None,
        placeholder="Select an option from the dropdown",
        format_func=lambda x: display_columns_dict[x],
    )

    stat_input_Y = st.selectbox(
        label="Y-axis stat ",
        options=columns,
        help="Select your second statistic from the dropdown",
        index=None,
        placeholder="Select an option from the dropdown",
        format_func=lambda x: display_columns_dict[x],
    )

    has_type_input = st.selectbox(
        label="Highlight Pokemon which have this type",
        options=type_list,
        help="Select a type from the dropdown and it will be highlighted on the graph",
        index=None,
        placeholder="Type to search for a type, or select an option from the dropdown",
    )
    if stat_input_X != None and stat_input_Y != None:
        fig = px.scatter(
            df,
            x=stat_input_X,
            y=stat_input_Y,
            color=(df["type_1"] == has_type_input) | (df["type_2"] == has_type_input),
            labels=display_columns_dict,
            hover_name="name",
            hover_data=("type_1", "type_2"),
            color_discrete_map={True: "Red"},
        )
        fig.update_traces(showlegend=False)
        selection = st.plotly_chart(fig, on_select="rerun")
    else:
        st.error(
            "^^^ Select options in the boxes up there! ^^^",
        )

    try:
        selected_name = selection["selection"]["points"][0]["hovertext"]
        row_of_selected = df.loc[df["name"] == selected_name]
        image_url = row_of_selected["image_url"].iloc[0]

        st.subheader(f"You've selected {selected_name}")
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_url, width=300)
        with col2:
            metric_set_1, metric_set_2 = st.columns(2)
            with metric_set_1:
                st.metric("Health: ", row_of_selected["hp"].iloc[0])
                st.metric("Attack: ", row_of_selected["attack"].iloc[0])
                st.metric("Defense: ", row_of_selected["defense"].iloc[0])
            with metric_set_2:
                st.metric("Special Attack: ", row_of_selected["sp_attack"].iloc[0])
                st.metric("Special Defense: ", row_of_selected["sp_defense"].iloc[0])
                st.metric("Speed: ", row_of_selected["speed"].iloc[0])
    except:
        st.write("Select something!")


with pre_set:

    role = st.selectbox(
        label="Choose a role:",
        options=["Wall", "Sweeper", "Pivot", "Lead"],
        help="Roles are key strategic positions in a battle team which each fulfil a necessary purpose!",
        index=None,
        placeholder="Pick a role...",
    )

    if role == "Wall":
        stat_input_X_2 = "hp"
        stat_input_Y_2 = "defense"
    elif role == "Sweeper":
        stat_input_X_2 = "attack"
        stat_input_Y_2 = "speed"
    elif role == "Pivot":
        stat_input_X_2 = "hp"
        stat_input_Y_2 = "speed"
    elif role == "Lead":
        stat_input_X_2 = "speed"
        stat_input_Y_2 = "defense"

    has_type_input_2 = st.selectbox(
        label="Highlight Pokemon which have this type",
        options=type_list,
        help="Select a type from the dropdown and it will be highlighted on the graph",
        index=None,
        placeholder="Type to search for a type, or select an option from the dropdown",
        key=3,
    )

    if stat_input_X_2 != None and stat_input_Y_2 != None:
        fig = px.scatter(
            df,
            x=stat_input_X_2,
            y=stat_input_Y_2,
            color=(df["type_1"] == has_type_input_2)
            | (df["type_2"] == has_type_input_2),
            labels=display_columns_dict,
            hover_name="name",
            hover_data=("type_1", "type_2"),
            color_discrete_map={True: "Red"},
        )
        fig.update_traces(showlegend=False)
        selection = st.plotly_chart(fig, on_select="rerun", key=2)
    else:
        st.error(
            "^^^ Select options in the boxes up there! ^^^",
        )

    try:
        selected_name = selection["selection"]["points"][0]["hovertext"]
        row_of_selected = df.loc[df["name"] == selected_name]
        image_url = row_of_selected["image_url"].iloc[0]

        st.subheader(f"You've selected {selected_name}")
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_url, width=300)
        with col2:
            metric_set_1, metric_set_2 = st.columns(2)
            with metric_set_1:
                st.metric("Health: ", row_of_selected["hp"].iloc[0])
                st.metric("Attack: ", row_of_selected["attack"].iloc[0])
                st.metric("Defense: ", row_of_selected["defense"].iloc[0])
            with metric_set_2:
                st.metric("Special Attack: ", row_of_selected["sp_attack"].iloc[0])
                st.metric("Special Defense: ", row_of_selected["sp_defense"].iloc[0])
                st.metric("Speed: ", row_of_selected["speed"].iloc[0])
    except:
        st.write("Select something!")


# with open("team-comp.txt", "r") as test:
#     hello = test.readlines()

#     st.write("hello")
