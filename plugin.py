import streamlit as st

st.title("🎮 CoachMine - Assistant personnel de jeu")

# Liste des jeux
jeux_disponibles = ["FC 24", "Minecraft", "Fortnite"]

jeu = st.selectbox("Choisis ton jeu", jeux_disponibles)

if jeu == "FC 24":
    st.subheader("Entre tes stats FC 24")
    buts_marques = st.number_input("Combien de buts as-tu marqué ?", min_value=0, step=1)
    buts_encaisses = st.number_input("Combien de buts as-tu encaissé ?", min_value=0, step=1)
    matches_joues = st.number_input("Combien de matchs as-tu joué ?", min_value=1, step=1)
    
    if st.button("Analyser mes stats"):
        ratio_buts = buts_marques / matches_joues
        st.write(f"Tu as un ratio de {ratio_buts:.2f} buts par match.")
        
        if ratio_buts > 1:
            st.success("Excellent ! Tu es un buteur redoutable.")
        elif ratio_buts > 0.5:
            st.info("Bon travail, continue à t'améliorer.")
        else:
            st.warning("Tu peux encore progresser, travaille tes attaques !")
        
        if buts_encaisses > buts_marques:
            st.error("Attention, ta défense laisse à désirer, essaie de renforcer ta défense.")
        else:
            st.success("Ta défense est solide, bravo !")

elif jeu == "Minecraft":
    st.subheader("Indique tes besoins Minecraft")
    heures_jeu = st.number_input("Combien d'heures jouées ?", min_value=0, step=1)
    nb_constructions = st.number_input("Combien de constructions as-tu faites ?", min_value=0, step=1)
    
    if st.button("Analyser mes données"):
        if heures_jeu > 100:
            st.success("Tu es un vrai vétéran Minecraft !")
        else:
            st.info("Continue à jouer pour maîtriser toutes les astuces.")
        
        if nb_constructions > 10:
            st.success("Bravo pour tes nombreuses constructions !")
        else:
            st.warning("Essaie de construire plus pour améliorer tes compétences.")

elif jeu == "Fortnite":
    st.subheader("Entre tes statistiques Fortnite")
    victoires = st.number_input("Nombre de victoires", min_value=0, step=1)
    parties_jouees = st.number_input("Nombre de parties jouées", min_value=1, step=1)
    
    if st.button("Analyser mes stats"):
        taux_victoire = victoires / parties_jouees
        st.write(f"Ton taux de victoire est de {taux_victoire:.2%}")
        
        if taux_victoire > 0.3:
            st.success("Très bon taux de victoire, tu es un pro !")
        elif taux_victoire > 0.1:
            st.info("Bon début, continue à t'entraîner.")
        else:
            st.warning("Ne te décourage pas, améliore ta stratégie !")

else:
    st.write("Choisis un jeu pour commencer.")
