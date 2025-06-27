import streamlit as st

st.title("🎮 CoachMine - Assistant personnel de jeu")

jeux_disponibles = [
    "FC 24", "Minecraft", "Fortnite",
    "Call of Duty", "League of Legends",
    "Valorant", "Apex Legends"
]

jeu = st.selectbox("Choisis ton jeu", jeux_disponibles)

if jeu == "FC 24":
    st.subheader("Entre tes statistiques FC 24")
    buts_marques = st.number_input("Buts marqués ?", min_value=0, step=1)
    buts_encaisses = st.number_input("Buts encaissés ?", min_value=0, step=1)
    passes_decisives = st.number_input("Passes décisives ?", min_value=0, step=1)
    tirs_cadres = st.number_input("Tirs cadrés ?", min_value=0, step=1)
    possessions = st.slider("Possession moyenne (%)", 0, 100, 50)
    fautes_commises = st.number_input("Fautes commises ?", min_value=0, step=1)
    cartons_jaunes = st.number_input("Cartons jaunes ?", min_value=0, step=1)
    cartons_rouges = st.number_input("Cartons rouges ?", min_value=0, step=1)
    interceptions = st.number_input("Interceptions ?", min_value=0, step=1)
    passes_reussies = st.number_input("Passes réussies ?", min_value=0, step=1)
    dribbles_reussis = st.number_input("Dribbles réussis ?", min_value=0, step=1)
    penalties_marques = st.number_input("Pénalties marqués ?", min_value=0, step=1)
    matches_joues = st.number_input("Matchs joués ?", min_value=1, step=1)

    if st.button("Analyser mes stats"):
        ratio_buts = buts_marques / matches_joues
        ratio_passes = passes_decisives / matches_joues
        st.write(f"Ratio buts/match : {ratio_buts:.2f}")
        st.write(f"Ratio passes décisives/match : {ratio_passes:.2f}")
        st.write(f"Tirs cadrés : {tirs_cadres}")
        st.write(f"Possession moyenne : {possessions}%")
        st.write(f"Fautes commises : {fautes_commises}")
        st.write(f"Cartons jaunes : {cartons_jaunes}, Cartons rouges : {cartons_rouges}")
        st.write(f"Interceptions : {interceptions}")
        st.write(f"Passes réussies : {passes_reussies}")
        st.write(f"Dribbles réussis : {dribbles_reussis}")
        st.write(f"Pénalties marqués : {penalties_marques}")

        if ratio_buts > 1:
            st.success("Buteur exceptionnel !")
        elif ratio_buts > 0.5:
            st.info("Bon attaquant.")
        else:
            st.warning("Peux progresser en attaque.")

        if passes_decisives > 5:
            st.success("Excellent passeur !")

        if fautes_commises > 10 or cartons_jaunes > 3 or cartons_rouges > 0:
            st.error("Attention discipline !")
        else:
            st.success("Bon fair-play.")

        if interceptions > 10:
            st.success("Bonne récupération de balle.")

        if dribbles_reussis > 10:
            st.success("Bon dribbleur.")

        if penalties_marques > 5:
            st.success("Pénalty killer !")

elif jeu == "Minecraft":
    st.subheader("Entre tes données Minecraft")
    heures_jeu = st.number_input("Heures jouées ?", min_value=0, step=1)
    nb_constructions = st.number_input("Constructions réalisées ?", min_value=0, step=1)
    nb_campagnes = st.number_input("Campagnes survie terminées ?", min_value=0, step=1)
    nb_objets_crees = st.number_input("Objets créés ?", min_value=0, step=1)
    nb_mob_tues = st.number_input("Mobs tués ?", min_value=0, step=1)
    nb_redstone = st.number_input("Circuits redstone construits ?", min_value=0, step=1)
    nb_fermes = st.number_input("Fermes automatiques construites ?", min_value=0, step=1)
    nb_herbes_recoltees = st.number_input("Plantes/herbes récoltées ?", min_value=0, step=1)
    nb_mines_explorees = st.number_input("Mines explorées ?", min_value=0, step=1)

    if st.button("Analyser mes données"):
        if heures_jeu > 100:
            st.success("Vétéran Minecraft !")
        else:
            st.info("Continue à jouer.")

        if nb_constructions > 10:
            st.success("Constructeur prolifique !")

        if nb_campagnes > 5:
            st.success("Expert survie.")

        if nb_redstone > 0:
            st.success("As de la redstone.")

        if nb_fermes > 0:
            st.success("Agriculteur organisé.")

        if nb_herbes_recoltees > 50:
            st.success("Bonne récolte !")

        if nb_mines_explorees > 5:
            st.success("Explorateur aguerri.")

elif jeu == "Fortnite":
    st.subheader("Entre tes stats Fortnite")
    victoires = st.number_input("Nombre de victoires", min_value=0, step=1)
    parties_jouees = st.number_input("Nombre de parties jouées", min_value=1, step=1)
    tirs_touches = st.number_input("Tirs touchés", min_value=0, step=1)
    tirs_rates = st.number_input("Tirs ratés", min_value=0, step=1)
    construction_rapide = st.selectbox("Rapide en construction ?", ["Oui", "Non"])
    gestion_inventaire = st.selectbox("Bonne gestion inventaire ?", ["Oui", "Non"])
    eliminations = st.number_input("Nombre d'éliminations", min_value=0, step=1)
    temps_survie = st.number_input("Temps moyen de survie (minutes)", min_value=0, step=1)
    dommages_infliges = st.number_input("Dommages infligés", min_value=0, step=1)

    if st.button("Analyser mes stats"):
        taux_victoire = victoires / parties_jouees
        taux_precision = tirs_touches / (tirs_touches + tirs_rates) if (tirs_touches + tirs_rates) > 0 else 0
        st.write(f"Taux de victoire : {taux_victoire:.2%}")
        st.write(f"Taux de précision : {taux_precision:.2%}")
        st.write(f"Eliminations totales : {elimations}")
        st.write(f"Temps moyen de survie : {temps_survie} minutes")
        st.write(f"Dommages infligés : {dommages_infliges}")

        if taux_victoire > 0.3:
            st.success("Excellent taux de victoire !")
        elif taux_victoire > 0.1:
            st.info("Bon début, continue !")
        else:
            st.warning("Travaille ta stratégie.")

        if taux_precision > 0.5:
            st.success("Bonne précision !")
        else:
            st.warning("Améliore ta précision.")

        if construction_rapide == "Oui":
            st.success("Construction rapide, bon point !")
        else:
            st.info("Travaille ta construction.")

        if gestion_inventaire == "Oui":
            st.success("Bonne gestion d’inventaire.")
        else:
            st.info("Optimise ton inventaire.")

elif jeu == "Call of Duty":
    st.subheader("Entre tes stats Call of Duty")
    kills = st.number_input("Eliminations (kills)", min_value=0, step=1)
    morts = st.number_input("Morts", min_value=0, step=1)
    headshots = st.number_input("Tirs à la tête (headshots)", min_value=0, step=1)
    parties_jouees = st.number_input("Parties jouées", min_value=1, step=1)
    temps_jeu = st.number_input("Temps de jeu (heures)", min_value=0, step=1)
    precision_tir = st.slider("Précision de tir (%)", 0, 100, 50)
    assists = st.number_input("Assists", min_value=0, step=1)

    if st.button("Analyser mes stats"):
        kd_ratio = kills / morts if morts > 0 else kills
        accuracy = headshots / kills if kills > 0 else 0
        st.write(f"K/D Ratio : {kd_ratio:.2f}")
        st.write(f"Taux headshots : {accuracy:.2%}")
        st.write(f"Précision de tir : {precision_tir}%")
        st.write(f"Assists : {assists}")

        if kd_ratio > 2:
            st.success("Excellent K/D ratio !")
        elif kd_ratio > 1:
            st.info("Bon K/D ratio.")
        else:
            st.warning("Travaille ta stratégie.")

        if accuracy > 0.3:
            st.success("Très bonne précision aux headshots !")
        else:
            st.info("Travaille ta précision.")

elif jeu == "League of Legends":
    st.subheader("Entre tes stats League of Legends")
    kills = st.number_input("Kills", min_value=0, step=1)
    deaths = st.number_input("Morts", min_value=0, step=1)
    assists = st.number_input("Assists", min_value=0, step=1)
    parties_jouees = st.number_input("Parties jouées", min_value=1, step=1)
    win_rate = st.slider("Taux de victoire (%)", 0, 100, 50)
    damage_dealt = st.number_input("Dégâts infligés", min_value=0, step=1)
    gold_earned = st.number_input("Or gagné", min_value=0, step=1)

    if st.button("Analyser mes stats"):
        kda = (kills + assists) / deaths if deaths > 0 else kills + assists
        st.write(f"KDA : {kda:.2f}")
        st.write(f"Taux de victoire : {win_rate}%")
        st.write(f"Dégâts infligés : {damage_dealt}")
        st.write(f"Or gagné : {gold_earned}")

        if kda > 4:
            st.success("Excellent KDA !")
        elif kda > 2:
            st.info("Bon KDA.")
        else:
            st.warning("Travaille ta stratégie.")

        if win_rate > 60:
            st.success("Très bon taux de victoires !")
        elif win_rate > 40:
            st.info("Taux correct.")
        else:
            st.warning("Travaille pour progresser.")

elif jeu == "Valorant":
    st.subheader("Entre tes stats Valorant")
    kills = st.number_input("Kills", min_value=0, step=1)
    deaths = st.number_input("Morts", min_value=0, step=1)
    assists = st.number_input("Assists", min_value=0, step=1)
    parties_jouees = st.number_input("Parties jouées", min_value=1, step=1)
    headshot_percentage = st.slider("Pourcentage de headshots (%)", 0, 100, 30)
    clutch_wins = st.number_input("Nombre de clutch wins", min_value=0, step=1)
    ability_usage = st.selectbox("Utilises-tu bien tes capacités ?", ["Oui", "Non"])

    if st.button("Analyser mes stats"):
        kdr = kills / deaths if deaths > 0 else kills
        st.write(f"K/D Ratio : {kdr:.2f}")
        st.write(f"Taux de headshots : {headshot_percentage}%")
        st.write(f"Clutch wins : {clutch_wins}")

        if ability_usage == "Oui":
            st.success("Bonne utilisation des capacités !")
        else:
            st.info("Travaille l’utilisation de tes capacités.")

        if kdr > 2:
            st.success("Excellent K/D ratio !")
        elif kdr > 1:
            st.info("Bon K/D ratio.")
        else:
            st.warning("Travaille ta stratégie.")

        if headshot_percentage > 40:
            st.success("Très bon taux de headshots !")
        else:
            st.info("Améliore ta précision.")

elif jeu == "Apex Legends":
    st.subheader("Entre tes stats Apex Legends")
    kills = st.number_input("Kills", min_value=0, step=1)
    parties_jouees = st.number_input("Parties jouées", min_value=1, step=1)
    victoires = st.number_input("Victoires", min_value=0, step=1)
    temps_jeu = st.number_input("Temps de jeu (heures)", min_value=0, step=1)
    distance_courue = st.number_input("Distance courue (mètres)", min_value=0, step=1)
    headshots = st.number_input("Tirs à la tête (headshots)", min_value=0, step=1)

    if st.button("Analyser mes stats"):
        kd_ratio = kills / (parties_jouees - victoires) if (parties_jouees - victoires) > 0 else kills
        taux_victoire = victoires / parties_jouees
        st.write(f"K/D Ratio approximatif : {kd_ratio:.2f}")
        st.write(f"Taux de victoires : {taux_victoire:.2%}")
        st.write(f"Distance courue : {distance_courue} mètres")
        st.write(f"Headshots : {headshots}")

        if kd_ratio > 2:
            st.success("Excellent K/D ratio !")
        elif kd_ratio > 1:
            st.info("Bon K/D ratio.")
        else:
            st.warning("Travaille ta stratégie.")

        if taux_victoire > 0.3:
            st.success("Bon taux de victoires !")
        else:
            st.info("Travaille pour gagner plus.")

else:
    st.write("Choisis un jeu pour commencer.")
