import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="For Arni ❤️", layout="centered")

# ---------- PREMIUM CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
}
.main {
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 30px;
}
h1, h2, h3 {
    text-align: center;
    color: #6a0036;
}
.question {
    font-size: 28px;
    font-weight: bold;
    margin-top: 30px;
}
button {
    border-radius: 30px !important;
    height: 3.2em;
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🌸 A Flower From My Heart 🌸</h1>", unsafe_allow_html=True)

canvas = st.empty()

# ---------- FLOWER DRAW ----------
def draw_flower(size, glow=False):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis("off")

    theta = np.linspace(0, 2*np.pi, 400)

    for i in range(8):
        r = size * np.sin(3 * theta)
        x = r * np.cos(theta + i)
        y = r * np.sin(theta + i)
        ax.plot(x, y, color="#ff4d6d", linewidth=2, alpha=0.9)

        if glow:
            ax.plot(x, y, color="#ffb3c6", linewidth=6, alpha=0.2)

    ax.plot(0, 0, "o", color="gold", markersize=12)
    canvas.pyplot(fig)
    plt.close(fig)

# ---------- BLOOM ANIMATION ----------
def bloom():
    for s in np.linspace(0.3, 2.0, 25):
        draw_flower(s, glow=True)
        time.sleep(0.06)

# ---------- TYPE EFFECT ----------
def type_text(text, speed=0.04):
    box = st.empty()
    current = ""
    for c in text:
        current += c
        box.markdown(f"<h3>{current}</h3>", unsafe_allow_html=True)
        time.sleep(speed)

# ---------- SESSION ----------
if "bloomed" not in st.session_state:
    st.session_state.bloomed = False

# ---------- START ----------
if not st.session_state.bloomed:
    st.markdown("<h3>Click the flower to bloom 🌸</h3>", unsafe_allow_html=True)
    if st.button("🌸 Bloom the Flower"):
        bloom()
        st.session_state.bloomed = True

# ---------- AFTER BLOOM ----------
if st.session_state.bloomed:
    type_text("Arni ❤️", 0.08)

    type_text(
        "Like this flower, my feelings bloomed quietly,\n"
        "but they grew stronger with every passing day.",
        0.03
    )

    st.markdown(
        "<div class='question'>Will you be mine forever? 💍</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # YES
    with col1:
        if st.button("YES 💖"):
            st.balloons()
            type_text(
                "You chose love.\n"
                "A lifetime of trust, care,\n"
                "and endless togetherness begins now ❤️",
                0.03
            )

    # NO
    with col2:
        if st.button("NO 😌"):
            st.snow()
            type_text(
                "That’s okay.\n"
                "Some flowers bloom later.\n"
                "In 1–2 years, I’ll be driving an expensive car,\n"
                "living the life I worked for 😎🚗",
                0.03
            )
