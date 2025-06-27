import streamlit as st

st.title("🎮 CoachMine - Assistant de jeu")

# Liste des jeux disponibles
jeux_disponibles = {
    "FC 24": [
        "Analyse de match",
        "Conseils techniques",
        "Statistiques joueurs"
    ],
    "Minecraft": [
        "Conseils de construction",
        "Astuces de survie",
        "Commandes utiles"
    ],
    "Fortnite": [
        "Stratégies de combat",
        "Construction rapide",
        "Gestion de l’inventaire"
    ],
}

# Barre de recherche avec autocomplétion
jeu_choisi = st.selectbox("Recherche un jeu", options=[""] + list(jeux_disponibles.keys()))

if jeu_choisi:
    st.subheader(f"Tu as choisi : {jeu_choisi}")

    questions = jeux_disponibles.get(jeu_choisi, [])
    if questions:
        question_choisie = st.selectbox("Choisis une question", options=questions)
        if question_choisie:
            # Affiche des réponses simples (à personnaliser)
            if jeu_choisi == "FC 24":
                if question_choisie == "Analyse de match":
                    st.write("Analyse détaillée de ta dernière partie FC 24.")
                elif question_choisie == "Conseils techniques":
                    st.write("Voici quelques conseils pour améliorer ta technique sur FC 24...")
                elif question_choisie == "Statistiques joueurs":
                    st.write("Statistiques des joueurs les plus performants dans FC 24.")
            elif jeu_choisi == "Minecraft":
                if question_choisie == "Conseils de construction":
                    st.write("Construis ta base avec ces astuces Minecraft.")
                elif question_choisie == "Astuces de survie":
                    st.write("Survis plus longtemps avec ces astuces Minecraft.")
                elif question_choisie == "Commandes utiles":
                    st.write("Utilise /give, /weather, /time set pour t’aider.")
            elif jeu_choisi == "Fortnite":
                if question_choisie == "Stratégies de combat":
                    st.write("Gagne tes combats avec ces stratégies Fortnite.")
                elif question_choisie == "Construction rapide":
                    st.write("Construis vite pour te protéger sur Fortnite.")
                elif question_choisie == "Gestion de l’inventaire":
                    st.write("Organise bien ton inventaire pour être efficace.")
    else:
        st.write("Désolé, pas encore d’info pour ce jeu.")
else:
    st.write("Tape ou sélectionne un jeu dans la liste ci-dessus.")
