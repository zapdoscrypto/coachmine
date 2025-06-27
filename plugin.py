import streamlit as st

st.set_page_config(page_title="CoachFC – Ton assistant IA FC 24", layout="centered")

st.title("⚽ CoachFC – Assistant IA pour EA SPORTS FC 24")

with st.form("fc24_form"):
    result = st.selectbox("🏆 Résultat du match :", ["Victoire", "Défaite", "Nul"])
    goals_scored = st.number_input("⚽ Buts marqués", 0, 20)
    goals_conceded = st.number_input("🧤 Buts encaissés", 0, 20)
    shots = st.number_input("🥅 Tirs effectués", 0, 50)
    possession = st.slider("⏱️ Possession (%)", 0, 100)
    passes = st.number_input("📊 Passes réussies", 0, 1000)
    corners = st.number_input("🚩 Corners obtenus", 0, 20)
    faults = st.number_input("🚨 Fautes commises", 0, 20)
    star_player = st.text_input("🌟 Joueur star du match")
    rating = st.slider("📈 Note du match (1 à 10)", 1, 10)
    defense_type = st.selectbox("🛡️ Type de défense :", ["Manuelle", "Automatique"])
    submitted = st.form_submit_button("Analyser le match")

if submitted:
    tips = []

    # 🧠 Vérification cohérence du score
    if result == "Victoire" and goals_scored <= goals_conceded:
        tips.append("❗ Tu dis avoir gagné, mais tu as marqué moins ou autant que ton adversaire 🤔")
    if result == "Défaite" and goals_scored >= goals_conceded:
        tips.append("❗ Tu dis avoir perdu, mais tu as marqué plus ou égal... tu es sûr ?")

    # 📊 Analyse des stats
    if result == "Victoire":
        tips.append("🟢 Belle victoire ! Continue comme ça.")
    elif result == "Défaite":
        tips.append("🔴 Revois ta tactique défensive.")
    else:
        tips.append("🟡 Match nul, tout reste à jouer.")

    if goals_scored == 0:
        tips.append("⚠️ Aucun but, travaille ta finition.")
    elif goals_scored >= 3:
        tips.append("🔥 Super attaque, tu as fait mal à l’adversaire.")

    if goals_conceded > 2:
        tips.append("🚨 Tu encaisses trop. Travaille ta défense.")
    elif goals_conceded == 0:
        tips.append("🧤 Clean sheet 👏")

    if shots < 5:
        tips.append("📉 Tu tires trop peu. Crée plus d’occasions.")
    elif shots >= 10:
        tips.append("🚀 Gros volume de tirs, bien joué.")

    if possession < 40:
        tips.append("🕰️ Tu n’as pas assez eu le ballon.")
    elif possession > 60:
        tips.append("💎 Tu as contrôlé le match, excellent.")

    if passes < 300:
        tips.append("🧩 Passe plus souvent pour créer du jeu.")
    elif passes > 700:
        tips.append("📶 Jeu collectif solide !")

    if faults > 5:
        tips.append("🚨 Trop de fautes, attention aux cartons.")

    if corners >= 5:
        tips.append("🚩 Tu as eu des corners, profite-en mieux.")

    if rating <= 5:
        tips.append("📉 Match difficile, tu peux mieux faire.")
    elif rating >= 8:
        tips.append("📈 Performance exceptionnelle !")

    if star_player:
        tips.append(f"🌟 {star_player} a porté l'équipe. Bravo !")

    if defense_type == "Manuelle":
        tips.append("🎮 Tu joues en manuel, respect.")
    else:
        tips.append("🧠 Défense auto ? Essaie le manuel pour progresser.")

    # 💬 Affichage des conseils
    st.success("✅ Analyse générée !")
    st.write("### Conseils personnalisés :")
    for tip in tips:
        st.write("•", tip)
