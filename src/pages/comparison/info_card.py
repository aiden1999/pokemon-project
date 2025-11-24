import streamlit as st


class InfoCard:
    def __init__(self, pkm) -> None:
        st.subheader(f"{pkm["name"]} (#{pkm["pokedex_number"]})")
        st.image(pkm["image_url"])
        st.write(pkm["species"])
        st.write(f"Generation {pkm["generation"]}")
        if pkm["status"] != "Normal":
            st.write(pkm["status"])
        match pkm["type_number"]:
            case 1:
                st.write(pkm["type_1"])
            case 2:
                st.write(f"{pkm["type_1"]}/{pkm["type_2"]}")
        st.write(f"Height: {pkm["height_m"]}m | Weight: {pkm["weight_kg"]}kg")
        match pkm["abilities_number"]:
            case 0:
                st.write("Abilities: None")
            case 1:
                if pkm["ability_hidden"] == "":
                    st.write(f"Ability: {pkm["ability_1"]}")
                else:
                    st.write(f"Ability: {pkm["ability_hidden"]} (hidden)")
            case 2:
                if pkm["ability_hidden"] == "":
                    st.write(f"Abilities: {pkm["ability_1"]}, {pkm["ability_2"]}")
                else:
                    st.write(
                        f"Abilities: {pkm["ability_1"]}, {pkm["ability_hidden"]} (hidden)"
                    )
            case 3:
                st.write(
                    f"Abilities: {pkm["ability_1"]}, {pkm["ability_2"]}, {pkm["ability_hidden"]} (hidden)"
                )

        st.divider()

        st.write(f"HP: {pkm["hp"]}")
        st.write(f"Attack: {pkm["attack"]}")
        st.write(f"Defense: {pkm["defense"]}")
        st.write(f"Special Attack: {pkm["sp_attack"]}")
        st.write(f"Special Defense: {pkm["sp_defense"]}")
        st.write(f"Speed: {pkm["speed"]}")
        st.write(f"Total: {pkm["total_points"]}")

        st.divider()

        st.write(f"Base Friendship: {pkm["base_friendship"]}")
        st.write(f"Base Experience: {pkm["base_experience"]}")
        st.write(f"Growth Rate: {pkm["growth_rate"]}")
        match pkm["egg_type_number"]:
            case 0:
                st.write("Egg Type: None")
            case 1:
                st.write(f"Egg Type: {pkm["egg_type_1"]}")
            case 2:
                st.write(f"Egg Types: {pkm["egg_type_1"]}, {pkm["egg_type_2"]}")
        if pkm["egg_cycles"] == "":
            st.write(f"Egg Cycles: {pkm["egg_cycles"]}")
        if pkm["percentage_male"] == "":
            st.write("Gender: a secret third thing")
        else:
            percentage_female = 100 - pkm["percentage_male"]
            st.write(
                f"Gender: {pkm["percentage_male"]}% male, {percentage_female}% female"
            )

        st.divider()

        st.write("When defending:")
        type_keys = [
            "against_normal",
            "against_fire",
            "against_water",
            "against_electric",
            "against_grass",
            "against_ice",
            "against_fight",
            "against_poison",
            "against_ground",
            "against_flying",
            "against_psychic",
            "against_bug",
            "against_rock",
            "against_ghost",
            "against_dragon",
            "against_dark",
            "against_steel",
            "against_fairy",
        ]
        type_dict = {key: value for key, value in pkm.items() if key in type_keys}
        for pkm_type in type_dict:
            type_str = pkm_type.replace("against_", "").title()
            st.write(f"{type_str} does x{type_dict[pkm_type]} damage")
