import streamlit as st
import datetime

st.set_page_config(page_title="Coachmine & CoachFC", layout="centered")

st.title("🧠 Coach Assistant IA")
tab1, tab2 = st.tabs(["⛏️ Minecraft", "⚽ FC 24"])

# -------------------- MINECRAFT --------------------
with tab1:
    st.subheader("Coachmine – Minecraft Bedrock")

    with st.form("minecraft_form"):
        deaths = st.number_input("😵 Combien de fois es-tu mort ?", min_value=0, max_value=100, step=1)
        mobs_killed = st.number_input("🧟 Combien de monstres as-tu tué ?", min_value=0, max_value=200, step=1)
        tools_used = st.selectbox("🛠️ Outil le plus utilisé ?", ["Bois", "Pierre", "Fer", "Diamant", "Netherite"])
        explored_nether = st.checkbox("🌋 As-tu exploré le Nether ?")
        slept_last_night = st.checkbox("🛏️ As-tu dormi cette nuit dans le jeu ?")
        submitted_mc = st.form_submit_button("Analyser ma session Minecraft")

    if submitted_mc:
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

        st.success("✅ Coaching Minecraft généré !")
        st.write("### Conseils :")
        for tip in feedback:
            st.write(f"- {tip}")

        with open("minecraft_session_log.txt", "a") as f:
            f.write(f"Session {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Morts: {deaths}, Mobs: {mobs_killed}, Outil: {tools_used}, Nether: {explored_nether}, Dormi: {slept_last_night}\n")
            f.write(f"Conseils: {' | '.join(feedback)}\n\n")

        st.caption("✅ Session enregistrée dans minecraft_session_log.txt")

# -------------------- FC 24 --------------------
with tab2:
    st.subheader("CoachFC – EA SPORTS FC 24")

    with st.form("fc24_form"):
        result = st.selectbox("🏆 Résultat du match :", ["Victoire", "Défaite", "Nul"])
        goals_scored = st.number_input("⚽ Buts marqués", min_value=0, max_value=20, step=1)
        goals_conceded = st.number_input("🧤 Buts encaissés", min_value=0, max_value=20, step=1)
        shots = st.number_input("🥅 Tirs effectués", min_value=0, max_value=50, step=1)
        possession = st.slider("⏱️ Possession (%)", min_value=0, max_value=100, step=1)
        defense_type = st.selectbox("🛡️ Type de défense :", ["Manuelle", "Automatique"])
        submitted_fc = st.form_submit_button("Analyser ma session FC 24")

    if submitted_fc:
        tips = []

        if result == "Victoire":
            tips.append("🟢 Bien joué, tu as gagné ! Essaie de garder cette dynamique.")
        elif result == "Défaite":
            tips.append("🔴 Reste calme après une défaite. Analyse ce qui n'a pas fonctionné.")
        else:
            tips.append("🟡 Un nul, ce n’est pas une défaite !")

        if goals_scored < 1:
            tips.append("⚠️ Tu n’as pas marqué… travaille ta finition.")
        elif goals_scored >= 3:
            tips.append("🔥 Attaque puissante !")

        if goals_conceded > 3:
            tips.append("🛑 Tu encaisses trop. Travaille ta défense ou change de tactique.")
        elif goals_conceded == 0:
            tips.append("🧤 Super clean sheet !")

        if shots < 5:
            tips.append("📉 Trop peu de tirs. Crée plus d'occasions.")
        elif shots >= 10:
            tips.append("🚀 Gros volume de tirs !")

        if possession < 40:
            tips.append("🕰️ Tu as peu eu le ballon, joue plus court.")
        elif possession >= 60:
            tips.append("💎 Très bon contrôle du match.")

        if defense_type == "Manuelle":
            tips.append("🎮 Bravo, tu joues en manuel. Tu maîtrises le jeu !")
        else:
            tips.append("🧠 En auto ? Essaye le manuel pour progresser.")

        st.success("✅ Coaching FC 24 généré !")
        st.write("### Conseils :")
        for tip in tips:
            st.write(f"- {tip}")

        with open("fc24_session_log.txt", "a") as f:
            f.write(f"Match {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} – {result}\n")
            f.write(f"Buts: {goals_scored}, Encaissés: {goals_conceded}, Tirs: {shots}, Possession: {possession}%, Défense: {defense_type}\n")
            f.write(f"Conseils: {' | '.join(tips)}\n\n")

        st.caption("✅ Session enregistrée dans fc24_session_log.txt")
