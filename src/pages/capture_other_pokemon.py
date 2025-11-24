import streamlit as st
import pandas as pd
import random
import math

# import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
import os


# Load data
@st.cache_data
def load_data():
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct path to the CSV file relative to the script location
    file_path = os.path.join(os.path.dirname(script_dir), "data", "pokemon_v2.csv")
    return pd.read_csv(file_path)


df = load_data()

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
    submitted = st.form_submit_button("Catch the pokemon!")

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


# Plotly horizontal bars
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
    width=400,
)
fig.update_traces(texttemplate="%{text:.2%}", textposition="inside")


# Images
def info_card(pkm):
    st.write(f"{pkm['name']} (#{pkm['pokedex_number']})")
    st.image(pkm["image_url"], width=150)


if submitted:
    if pokeball == "Master Ball":
        st.success(f"100% success chance with a Master Ball!")
    else:
        named_row = df.loc[df["name"] == name]
        pokemon_dict = named_row.iloc[0].to_dict()
        # pokemon_1 = info_card(pokemon_dict)
        # st.info(f"Estimated capture probability1: {capture_prob1:.2%}")

        if 1 - (1 - capture_prob1) * (1 - capture_prob2) > 1:
            st.success(f"You caught {name}!")
        else:
            st.error(f"O dear... {name} has escaped")
        # st.info(f"Capture?: {1- (1-capture_prob1) * ( 1-capture_prob2)}")

        # st.info(f"You have {capture_prob_total:.2%} chance to catch {name}")
        # st.progress(capture_prob_total)
        # st.image(pkm["image_url"])
        # st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns([1, 4])
if submitted:
    with col1:
        pokemon_1 = info_card(pokemon_dict)

    with col2:
        st.plotly_chart(fig, use_container_width=True)


# Prob to capture per throw
throws = list(range(1, 11))
probs = []
cumulative = 0
for k in throws:
    prob = (1 - capture_prob_total) ** (k - 1) * capture_prob_total
    cumulative += prob
    probs.append(cumulative)


data = pd.DataFrame({"Throw": throws, "Probability": probs})

fig = px.bar(
    data,
    x="Throw",
    y="Probability",
    text="Probability",
    labels={"Throw": "Throw Number", "Probability": "Chance of Capture"},
    title="Capture probability per no. of throws",
)

# Format bar labels
fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")

# Add a line trace on top of the bars
fig.add_scatter(
    x=data["Throw"],
    y=data["Probability"],
    mode="lines+markers",
    name="Cumulative",
    line=dict(color="red", width=2),
    marker=dict(size=6),
)

# Adjust layout
fig.update_layout(yaxis=dict(range=[0, max(probs) * 1.2]))

if submitted:
    st.plotly_chart(fig, use_container_width=True)
