import streamlit as st
import random
import datetime

st.set_page_config(page_title="Coachmine - Minecraft AI", layout="centered")

st.title("🧠 Coachmine")
st.subheader("Ton coach IA personnalisé pour Minecraft Bedrock")

with st.form("game_form"):
    deaths = st.number_input("😵 Combien de fois es-tu mort ?", min_value=0, max_value=100, step=1)
    mobs_killed = st.number_input("🧟 Combien de monstres as-tu tué ?", min_value=0, max_value=200, step=1)
    tools_used = st.selectbox("🛠️ Outil le plus utilisé ?", ["Bois", "Pierre", "Fer", "Diamant", "Netherite"])
    explored_nether = st.checkbox("🌋 As-tu exploré le Nether ?")
    slept_last_night = st.checkbox("🛏️ As-tu dormi cette nuit dans le jeu ?")
    submitted = st.form_submit_button("Analyser ma session")

if submitted:
    feedback = []

    if deaths > 5:
        feedback.append("🔴 Tu es mort souvent ! Équipe-toi mieux et évite les zones dangereuses.")
    elif deaths > 0:
        feedback.append("🟡 Quelques morts, c’est normal. Mais sois plus prudent.")
    else:
        feedback.append("🟢 Parfait, aucun décès. GG survivant !")

    if mobs_killed < 3:
        feedback.append("🔴 Pas beaucoup de mobs tués. Cherche plus de donjons ou explore la nuit.")
    elif mobs_killed < 10:
        feedback.append("🟡 Tu peux améliorer ton efficacité en combat.")
    else:
        feedback.append("🟢 Tueur de mobs confirmé !")

    if tools_used in ["Bois", "Pierre"]:
        feedback.append("🔴 Upgrade ton stuff, tu mérites mieux que ça.")
    elif tools_used == "Fer":
        feedback.append("🟡 C’est bien, mais vise le diamant !")
    else:
        feedback.append("🟢 Tu es full stuff, prêt pour le dragon.")

    if not explored_nether:
        feedback.append("🟡 Pense à explorer le Nether. C’est risqué mais essentiel.")
    else:
        feedback.append("🟢 Bien joué, tu as affronté le Nether.")

    if not slept_last_night:
        feedback.append("🔴 Attention aux fantômes si tu dors pas.")
    else:
        feedback.append("🟢 Dormir te garde en vie, continue comme ça.")

    st.success("🧠 Coaching personnalisé généré !")

    st.write("### Résumé de ta session")
    st.write(f"🪦 Morts : {deaths}")
    st.write(f"🧟 Mobs tués : {mobs_killed}")
    st.write(f"🛠️ Outil utilisé : {tools_used}")
    st.write(f"🌋 Nether exploré : {'Oui' if explored_nether else 'Non'}")
    st.write(f"🛏️ Dormi cette nuit : {'Oui' if slept_last_night else 'Non'}")

    st.write("### 📋 Conseils :")
    for tip in feedback:
        st.write(f"- {tip}")

    with open("minecraft_session_log.txt", "a") as f:
        f.write(f"Session {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Morts: {deaths}, Mobs: {mobs_killed}, Outil: {tools_used}, Nether: {explored_nether}, Dormi: {slept_last_night}\n")
        f.write(f"Conseils: {' | '.join(feedback)}\n\n")

    st.caption("✅ Session enregistrée dans minecraft_ses
      sion_log.txt")
