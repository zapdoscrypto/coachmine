import streamlit as st

st.title("🎮 CoachMine - Assistant personnel de jeu")

jeux_disponibles = ["FC 24", "Minecraft", "Fortnite"]

jeu = st.selectbox("Choisis ton jeu", jeux_disponibles)

if jeu == "FC 24":
    st.subheader("Entre tes statistiques FC 24")
    buts_marques = st.number_input("Combien de buts as-tu marqué ?", min_value=0, step=1)
    buts_encaisses = st.number_input("Combien de buts as-tu encaissé ?", min_value=0, step=1)
    passes_decisives = st.number_input("Combien de passes décisives ?", min_value=0, step=1)
    tirs_cadres = st.number_input("Combien de tirs cadrés ?", min_value=0, step=1)
    possessions = st.slider("Pourcentage moyen de possession (%)", 0, 100, 50)
    fautes_commises = st.number_input("Combien de fautes as-tu commises ?", min_value=0, step=1)
    cartons_jaunes = st.number_input("Nombre de cartons jaunes ?", min_value=0, step=1)
    cartons_rouges = st.number_input("Nombre de cartons rouges ?", min_value=0, step=1)
    matches_joues = st.number_input("Combien de matchs as-tu joué ?", min_value=1, step=1)
    
    if st.button("Analyser mes stats"):
        ratio_buts = buts_marques / matches_joues
        ratio_passes = passes_decisives / matches_joues
        st.write(f"Ratio buts par match : {ratio_buts:.2f}")
        st.write(f"Ratio passes décisives par match : {ratio_passes:.2f}")
        st.write(f"Taux de tirs cadrés : {tirs_cadres} sur {buts_marques + tirs_cadres} tirs (approx.)")
        st.write(f"Possession moyenne : {possessions}%")
        
        if ratio_buts > 1:
            st.success("Excellent, tu es un buteur redoutable !")
        elif ratio_buts > 0.5:
            st.info("Bon travail, continue à t'améliorer.")
        else:
            st.warning("Tu peux progresser en attaque.")
        
        if passes_decisives > 5:
            st.success("Très bon distributeur de ballons !")
        
        if fautes_commises > 10 or cartons_jaunes > 3 or cartons_rouges > 0:
            st.error("Attention, discipline à travailler !")
        else:
            st.success("Bon comportement sur le terrain.")
        
        if buts_encaisses > buts_marques:
            st.error("La défense doit être renforcée.")
        else:
            st.success("Ta défense est solide.")

elif jeu == "Minecraft":
    st.subheader("Entre tes données Minecraft")
    heures_jeu = st.number_input("Combien d'heures jouées ?", min_value=0, step=1)
    nb_constructions = st.number_input("Nombre de constructions réalisées ?", min_value=0, step=1)
    nb_campagnes = st.number_input("Nombre de campagnes de survie complétées ?", min_value=0, step=1)
    nb_objets_crees = st.number_input("Nombre d’objets créés ?", min_value=0, step=1)
    nb_mob_tues = st.number_input("Nombre de mobs tués ?", min_value=0, step=1)
    nb_redstone = st.number_input("Nombre de circuits redstone construits ?", min_value=0, step=1)
    
    if st.button("Analyser mes données"):
        if heures_jeu > 100:
            st.success("Tu es un vétéran Minecraft !")
        else:
            st.info("Continue à jouer pour progresser.")
        
        if nb_constructions > 10:
            st.success("Beau travail en construction !")
        else:
            st.warning("Essaie de construire plus.")
        
        if nb_campagnes > 5:
            st.success("Tu maîtrises bien la survie.")
        
        if nb_redstone > 0:
            st.success("Tu es un expert en redstone !")
        else:
            st.info("Découvre la redstone pour automatiser tes constructions.")

elif jeu == "Fortnite":
    st.subheader("Entre tes stats Fortnite")
    victoires = st.number_input("Nombre de victoires", min_value=0, step=1)
    parties_jouees = st.number_input("Nombre de parties jouées", min_value=1, step=1)
    tirs_touches = st.number_input("Nombre de tirs touchés", min_value=0, step=1)
    tirs_rate = st.number_input("Nombre de tirs ratés", min_value=0, step=1)
    construction_rapide = st.selectbox("Es-tu rapide en construction ?", ["Oui", "Non"])
    gestion_inventaire = st.selectbox("Gères-tu bien ton inventaire ?", ["Oui", "Non"])
    
    if st.button("Analyser mes stats"):
        taux_victoire = victoires / parties_jouees
        taux_precision = tirs_touches / (tirs_touches + tirs_rate) if (tirs_touches + tirs_rate) > 0 else 0
        st.write(f"Taux de victoire : {taux_victoire:.2%}")
        st.write(f"Taux de précision des tirs : {taux_precision:.2%}")
        
        if taux_victoire > 0.3:
            st.success("Excellent taux de victoire !")
        elif taux_victoire > 0.1:
            st.info("Bon début, continue comme ça.")
        else:
            st.warning("Travaille ta stratégie pour t'améliorer.")
        
        if taux_precision > 0.5:
            st.success("Bonne précision de tir !")
        else:
            st.warning("Travaille ton tir pour être plus précis.")
        
        if construction_rapide == "Oui":
            st.success("Ta construction rapide est un atout majeur !")
        else:
            st.info("Travaille ta construction pour mieux te protéger.")
        
        if gestion_inventaire == "Oui":
            st.success("Bonne gestion d’inventaire.")
        else:
            st.info("Améliore ta gestion d’inventaire pour gagner en efficacité.")

else:
    st.write("Choisis un jeu pour commencer.")
