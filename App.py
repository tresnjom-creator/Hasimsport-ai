import streamlit as st

# Podešavanje izgleda stranice
st.set_page_config(page_title="Hasimsport AI Simulator", layout="centered")

st.title("⚽ Hasimsport: SP 2026 AI Predviđanja")
st.write("Dobrodošli u Monte Carlo simulator fudbalskih mečeva.")

st.markdown("---")

# Privremena lista ekipa (kasnije ćemo pravu listu vući preko API-ja)
ekipe = ["Brazil", "Francuska", "Engleska", "Španija", "Argentina", "Njemačka"]

# Red sa dva padajuća menija za izbor timova
col1, col2 = st.columns(2)

with col1:
    domacin = st.selectbox("Izaberi prvog protivnika:", ekipe, index=0)

with col2:
    gost = st.selectbox("Izaberi drugog protivnika:", ekipe, index=1)

st.markdown("---")

# Dugme za pokretanje simulacije
if st.button("Pokreni AI Simulaciju 🚀"):
    if domacin == gost:
        st.warning("Ista ekipa ne može igrati sama protiv sebe! Izaberi drugog protivnika.")
    else:
        st.success(f"Pokrećem analizu za meč: {domacin} vs {gost}...")
        # Ovdje će u sljedećem koraku doći naš matematički model
        st.info("Matematički model i Poissonova distribucija se učitavaju...")
