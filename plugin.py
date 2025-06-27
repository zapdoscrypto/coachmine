import streamlit as st

st.set_page_config(page_title="CoachMine", page_icon="🎮")
st.title("🎮 CoachMine - Ton assistant perso de jeu")

jeux_disponibles = [
    "FC 24", "Minecraft", "Fortnite"
]

jeu = st.selectbox("Choisis ton jeu", jeux_disponibles)

def encouragement(msg):
    st.markdown(f"✅ **{msg}**")

def conseil(msg):
    st.markdown(f"💡 *{msg}*")

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

    if st.button("Analyse ton jeu"):
        ratio_buts = buts_marques / matches_joues
        ratio_passes = passes_decisives / matches_joues
        fautes = fautes_commises + cartons_jaunes * 2 + cartons_rouges * 5

        st.write(f"- Buts/match : {ratio_buts:.2f}")
        st.write(f"- Passes décisives/match : {ratio_passes:.2f}")
        st.write(f"- Possession : {possessions}%")
        st.write(f"- Discipline (score fautes) : {fautes}")

        if ratio_buts >= 1:
            encouragement("Tu es une vraie machine à marquer ! Continue à dominer le terrain !")
        elif ratio_buts >= 0.5:
            encouragement("Très bon attaquant, tu fais la différence régulièrement !")
        else:
            conseil("Travaille ta finition pour transformer plus d’occasions en buts.")

        if ratio_passes >= 0.5:
            encouragement("Tu fais briller ton équipe avec tes passes décisives !")

        if fautes <= 5:
            encouragement("Ton fair-play est exemplaire, bravo !")
        else:
            conseil("Attention à la discipline, trop de fautes peuvent coûter cher.")

        if dribbles_reussis >= 10:
            encouragement("Tes dribbles sont redoutables !")

elif jeu == "Minecraft":
    st.subheader("Entre tes données Minecraft")
    heures_jeu = st.number_input("Heures jouées ?", 0)
    nb_constructions = st.number_input("Constructions réalisées ?", 0)
    nb_campagnes = st.number_input("Campagnes survie terminées ?", 0)
    nb_objets_crees = st.number_input("Objets créés ?", 0)
    nb_mob_tues = st.number_input("Mobs tués ?", 0)
    nb_redstone = st.number_input("Circuits redstone construits ?", 0)
    nb_fermes = st.number_input("Fermes automatiques construites ?", 0)
    nb_mines_explorees = st.number_input("Mines explorées ?", 0)

    if st.button("Analyse ton aventure"):
        st.write(f"- Heures jouées : {heures_jeu}")
        st.write(f"- Constructions : {nb_constructions}")
        st.write(f"- Survie : {nb_campagnes}")

        if heures_jeu >= 100:
            encouragement("Vétéran Minecraft, tu domines l’univers cube par cube !")
        if nb_constructions >= 20:
            encouragement("Architecte créatif, tes bâtiments sont impressionnants !")
        if nb_redstone >= 5:
            encouragement("Maître de la redstone, l’ingénierie n’a plus de secrets pour toi !")

elif jeu == "Fortnite":
    st.subheader("Stats Fortnite")
    victoires = st.number_input("Victoires", 0)
    parties_jouees = st.number_input("Parties jouées", 1)
    tirs_touches = st.number_input("Tirs touchés", 0)
    tirs_rates = st.number_input("Tirs ratés", 0)
    eliminations = st.number_input("Éliminations", 0)

    if st.button("Analyse ton shoot"):
        win_rate = victoires / parties_jouees
        precision = tirs_touches / (tirs_touches + tirs_rates) if (tirs_touches + tirs_rates) > 0 else 0

        st.write(f"Taux de victoire : {win_rate:.2%}")
        st.write(f"Précision de tir : {precision:.2%}")
        st.write(f"Éliminations totales : {eliminations}")

        if win_rate > 0.2:
            encouragement("Beaucoup de top 1, tu gères la storm comme un pro !")
        else:
            conseil("Travaille ta stratégie pour survivre plus longtemps.")

        if precision > 0.4:
            encouragement("Tir de sniper ! Tu vises avec précision.")
        else:
            conseil("Améliore ta visée pour faire plus de dégâts.")
