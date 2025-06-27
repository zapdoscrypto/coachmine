import streamlit as st

st.title("🎮 CoachMine - Assistant de jeu")

# Liste des jeux et questions spécifiques
jeux_disponibles = {
    "FC 24": [
        "Meilleur buteur",
        "Buts marqués",
        "Buts encaissés",
        "Analyse de match",
        "Conseils techniques",
        "Statistiques joueurs"
    ],
    "Minecraft": [
        "Conseils de construction",
        "Astuces de survie",
        "Commandes utiles",
        "Meilleures ressources",
        "Création rapide"
    ],
    "Fortnite": [
        "Stratégies de combat",
        "Construction rapide",
        "Gestion de l’inventaire",
        "Meilleures armes",
        "Zones à éviter"
    ],
}

jeu_choisi = st.selectbox("Recherche un jeu", options=[""] + list(jeux_disponibles.keys()))

if jeu_choisi:
    st.subheader(f"Tu as choisi : {jeu_choisi}")
    questions = jeux_disponibles.get(jeu_choisi, [])
    if questions:
        question_choisie = st.selectbox("Choisis une question", options=questions)
        if question_choisie:
            # Réponses détaillées selon jeu + question
            if jeu_choisi == "FC 24":
                if question_choisie == "Meilleur buteur":
                    st.write("Le meilleur buteur actuel est Lionel Messi avec 30 buts cette saison.")
                elif question_choisie == "Buts marqués":
                    st.write("Tu as marqué 15 buts dans ta dernière saison sur FC 24.")
                elif question_choisie == "Buts encaissés":
                    st.write("Tu as encaissé 8 buts cette saison, améliore ta défense !")
                elif question_choisie == "Analyse de match":
                    st.write("Analyse détaillée : ta possession de balle est à 55%, avec un taux de tirs cadrés de 60%.")
                elif question_choisie == "Conseils techniques":
                    st.write("Travaille ta finition en utilisant les tirs placés et en exploitant les espaces.")
                elif question_choisie == "Statistiques joueurs":
                    st.write("Messi : 30 buts, De Bruyne : 20 passes décisives, Neuer : 15 clean sheets.")
            elif jeu_choisi == "Minecraft":
                if question_choisie == "Conseils de construction":
                    st.write("Utilise la pierre et le bois pour construire une base solide rapidement.")
                elif question_choisie == "Astuces de survie":
                    st.write("Crée toujours un lit et stocke de la nourriture pour survivre aux nuits.")
                elif question_choisie == "Commandes utiles":
                    st.write("Commande /time set day pour passer le jour, /give pour obtenir des items.")
                elif question_choisie == "Meilleures ressources":
                    st.write("Le diamant et l’émeraude sont essentiels pour progresser rapidement.")
                elif question_choisie == "Création rapide":
                    st.write("Utilise la TNT pour déblayer rapidement des zones importantes.")
            elif jeu_choisi == "Fortnite":
                if question_choisie == "Stratégies de combat":
                    st.write("Utilise le build pour te protéger rapidement et prendre l’avantage.")
                elif question_choisie == "Construction rapide":
                    st.write("Pratique les escaliers et murs pour échapper aux tirs ennemis.")
                elif question_choisie == "Gestion de l’inventaire":
                    st.write("Priorise les armes à distance et les soins dans ton inventaire.")
                elif question_choisie == "Meilleures armes":
                    st.write("Le fusil à pompe et le fusil d’assaut sont les plus efficaces actuellement.")
                elif question_choisie == "Zones à éviter":
                    st.write("Évite les zones très peuplées au début pour survivre plus longtemps.")
    else:
        st.write("Pas encore de questions disponibles pour ce jeu.")
else:
    st.write("Tape ou sélectionne un jeu dans la liste ci-dessus.")
