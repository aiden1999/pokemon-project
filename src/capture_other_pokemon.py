import streamlit as st
import pandas as pd
import random
import math

# import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("data/pokemon_v2.csv")
pokemon_names = df["name"].tolist()
catch_rate = df["catch_rate"]

st.header("Dashboard")
st.markdown("Can you catch them all?")


with st.form("dashboard_form"):
    st.subheader("Pokemon you wish to capture")

    # Form inputs
    name = st.selectbox(
        "Search Pokémon",
        options=pokemon_names,
        help="Start typing to see suggestions",
    )

    pokeball = st.selectbox(
        "Select Poké Ball",
        [
            "Poké Ball",
            "Great Ball",
            "Ultra Ball",
            "Safari Ball",
            "Master Ball",
        ],
    )

    pokemon_state = st.selectbox(
        "Pokémon state",
        ["None", "Frozen", "Asleep", "Paralyzed", "Burned", "Poisoned"],
    )

    hpmax = st.number_input("HPmax", min_value=1, step=1)
    hpcurrent = st.slider("Current hitpoints (HP)%", 1, 100, 50)

    # Poke ball stats
    if pokeball == "Poké Ball":
        bf = 8
        bn = 255
        bd = 200

    if pokeball == "Great Ball":
        bf = 12
        bn = 200
        bd = 150

    if pokeball == "Ultra Ball" or pokeball == "Safari Ball":
        bf = 12
        bn = 150
        bd = 150

    if pokeball == "Master Ball":
        bn = 1

    pn = {
        "Frozen": 25,
        "Asleep": 25,
        "Paralyzed": 12,
        "Burned": 12,
        "Poisoned": 12,
        "None": 0,
    }

    # first capture loop
    capture_prob1 = pn[pokemon_state] / (bn * 2)
    submitted = st.form_submit_button("Submit")

    # second capture loop
    m = random.randint(1, 256)
    hp_actual = math.ceil(hpmax * (hpcurrent / 100))

    f = min(
        255,
        max(1, int(hpmax * 255 * 4 / (hp_actual * bn))),
    )
    capture_prob2 = f / m

    capture_prob2_est = f / 256

    # capture_prob3 = pn[pokemon_state] / (bn + 1) + (
    #     (catch_rate + 1) / (bn + 1) * ((bf + 1) / 256)
    # )

    capture_prob_total = 1 - (1 - capture_prob1) * (1 - capture_prob2_est)


# Build
outcomes = ["Capture", "Fail"]
values = [capture_prob_total, 1 - capture_prob_total]
colors = ["green", "red"]
data = pd.DataFrame({"Outcome": outcomes, "Probability": values})


# Plotly horizontal bar
fig = px.bar(
    data,
    x="Probability",
    y="Outcome",
    orientation="h",
    color="Outcome",
    color_discrete_map={"Capture": "green", "Fail": "red"},
    text="Probability",
)

# chart
fig.update_layout(
    xaxis=dict(range=[0, 1], title="Probability"),
    yaxis=dict(title=""),
    height=200,
)
fig.update_traces(texttemplate="%{text:.2%}", textposition="inside")


def info_card(pkm):
    st.write(f"{pkm['name']} (#{pkm['pokedex_number']})")
    st.image(pkm["image_url"])


if submitted:
    if pokeball == "Master Ball":
        st.success(f"100% success chance with a Master Ball!")
    else:
        named_row = df.loc[df["name"] == name]
        pokemon_dict = named_row.iloc[0].to_dict()
        pokemon_1 = info_card(pokemon_dict)
        # st.info(f"Estimated capture probability1: {capture_prob1:.2%}")
        # st.info(f"Estimated capture probability2: {capture_prob2_est:.2%}")
        st.info(f"You have {capture_prob_total:.2%} chance to catch {name}")
        # st.progress(capture_prob_total)
        # st.image(pkm["image_url"])
        st.plotly_chart(fig, use_container_width=True)
