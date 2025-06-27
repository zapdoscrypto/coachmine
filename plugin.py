import streamlit as st

st.set_page_config(page_title="CoachMine", page_icon="🎮")
st.title("🎮 CoachMine - Ton assistant perso de jeu")

jeux_disponibles = [
    "FC 24", "Minecraft", "Fortnite",
    "Call of Duty", "League of Legends", "Valorant", "Apex Legends"
]

jeu = st.selectbox("Choisis ton jeu", jeux_disponibles)

def encouragement(msg):
    st.markdown(f"✅ **{msg}**")

def conseil(msg):
    st.markdown(f"💡 *{msg}*")

# ------------------------
# FC 24
# ------------------------
if jeu == "FC 24":
    st.subheader("Entre tes statistiques FC 24")
    buts_marques = st.number_input("Buts marqués ?", 0)
    buts_encaisses = st.number_input("Buts encaissés ?", 0)
    passes_decisives = st.number_input("Passes décisives ?", 0)
    tirs_cadres = st.number_input("Tirs cadrés ?", 0)
    possessions = st.slider("Possession moyenne (%)", 0, 100, 50)
    fautes_commises = st.number_input("Fautes commises ?", 0)
    cartons_jaunes = st.number_input("Cartons jaunes ?", 0)
    cartons_rouges = st.number_input("Cartons rouges ?", 0)
    interceptions = st.number_input("Interceptions ?", 0)
    dribbles_reussis = st.number_input("Dribbles réussis ?", 0)
    penalties_marques = st.number_input("Pénalties marqués ?", 0)
    matches_joues = st.number_input("Matchs joués ?", 1, step=1)

    if st.button("Analyser FC 24"):
        ratio_buts = buts_marques / matches_joues
        if ratio_buts >= 1:
            encouragement("Tu es une vraie machine à marquer !")
        elif ratio_buts >= 0.5:
            encouragement("Solide attaquant ! Continue comme ça.")
        else:
            conseil("Travaille ta finition pour marquer plus souvent.")

# ------------------------
# Minecraft
# ------------------------
elif jeu == "Minecraft":
    st.subheader("Entre tes données Minecraft")
    heures_jeu = st.number_input("Heures jouées ?", 0)
    constructions = st.number_input("Constructions terminées ?", 0)
    redstone = st.number_input("Circuits Redstone ?", 0)
    mobs_tues = st.number_input("Mobs tués ?", 0)

    if st.button("Analyser Minecraft"):
        if constructions >= 10:
            encouragement("Architecte confirmé, beau travail !")
        if redstone >= 5:
            encouragement("Maître ingénieur Redstone !")
        if mobs_tues >= 100:
            encouragement("Chasseur légendaire !")

# ------------------------
# Fortnite
# ------------------------
elif jeu == "Fortnite":
    st.subheader("Stats Fortnite")
    victoires = st.number_input("Victoires", 0)
    parties = st.number_input("Parties jouées", 1)
    tirs_touches = st.number_input("Tirs touchés", 0)
    tirs_rates = st.number_input("Tirs ratés", 0)

    if st.button("Analyser Fortnite"):
        precision = tirs_touches / (tirs_touches + tirs_rates) if (tirs_touches + tirs_rates) > 0 else 0
        winrate = victoires / parties
        st.write(f"Précision de tir : {precision:.2%}")
        st.write(f"Taux de victoire : {winrate:.2%}")
        if precision > 0.4:
            encouragement("Tireur d'élite !")
        else:
            conseil("Travaille ta précision au tir.")

# ------------------------
# Call of Duty
# ------------------------
elif jeu == "Call of Duty":
    st.subheader("Stats CoD")
    kills = st.number_input("Éliminations", 0)
    deaths = st.number_input("Morts", 1)
    kd = kills / deaths
    st.write(f"Ratio K/D : {kd:.2f}")
    if kd > 1:
        encouragement("Tu domines tes parties !")
    else:
        conseil("Améliore ton positionnement et ta réactivité.")

# ------------------------
# League of Legends
# ------------------------
elif jeu == "League of Legends":
    st.subheader("Stats LoL")
    kills = st.number_input("Kills", 0)
    assists = st.number_input("Assists", 0)
    deaths = st.number_input("Deaths", 1)
    cs = st.number_input("Creep Score (CS)", 0)

    if st.button("Analyser LoL"):
        kda = (kills + assists) / deaths
        st.write(f"KDA : {kda:.2f}")
        if kda > 3:
            encouragement("Tu joues proprement !")
        else:
            conseil("Joue plus safe et communique avec ton équipe.")

# ------------------------
# Valorant
# ------------------------
elif jeu == "Valorant":
    st.subheader("Stats Valorant")
    headshots = st.number_input("Headshots", 0)
    kills = st.number_input("Kills", 0)
    deaths = st.number_input("Deaths", 1)

    if st.button("Analyser Valorant"):
        accuracy = headshots / kills if kills > 0 else 0
        kd = kills / deaths
        st.write(f"Précision headshot : {accuracy:.2%}")
        st.write(f"Ratio K/D : {kd:.2f}")
        if accuracy > 0.3:
            encouragement("Tirs précis, bien joué !")
        else:
            conseil("Travaille ton aim sur le terrain d’entraînement.")

# ------------------------
# Apex Legends
# ------------------------
elif jeu == "Apex Legends":
    st.subheader("Stats Apex")
    parties = st.number_input("Parties jouées", 1)
    victoires = st.number_input("Victoires", 0)
    knockdowns = st.number_input("Knockdowns", 0)

    if st.button("Analyser Apex"):
        winrate = victoires / parties
        st.write(f"Taux de victoire : {winrate:.2%}")
        st.write(f"Knockdowns totaux : {knockdowns}")
        if winrate > 0.2:
            encouragement("Tu domines les squads !")
        else:
            conseil("Sois plus stratégique pour survivre jusqu’au bout.")
