import streamlit as st
from datetime import date
st.title("§14a Imsys-Prüfung")
geraetetyp = st.selectbox("Gerätetyp", ["Wärmepumpe", "Klimagerät", "Wallbox", "Stromspeicher", "Sonstiges"])
leistung = st.number_input("Leistung (kW)", min_value=0.0)
datum = st.date_input("Inbetriebnahme", value=date.today())
steuerung = st.checkbox("Steuerung vorhanden?")
vertrag = st.checkbox("§14a-Vereinbarung abgeschlossen?")
netz = st.selectbox("Netzebene", ["6 (Ortsnetz)", "7 (Hausanschluss)", "andere"])
ausnahme = st.checkbox("Ausnahmefall?")
if st.button("▶ Prüfen"):
    fehler = []
    if geraetetyp == "Sonstiges": fehler.append("Gerätetyp ungültig")
    if leistung <= 4.2: fehler.append("Leistung zu gering")
    if datum < date(2024,1,1): fehler.append("Inbetriebnahme vor 2024")
    if not steuerung: fehler.append("Keine Steuerung")
    if not vertrag: fehler.append("Kein §14a-Vertrag")
    if netz not in ["6 (Ortsnetz)", "7 (Hausanschluss)"]: fehler.append("Falsche Netzebene")
    if ausnahme:
        st.warning("⚠ Ausnahme – Einzelfall prüfen")
    elif fehler:
        st.error("❌ Nicht berechtigt:")
        for f in fehler: st.markdown(f"- {f}")
    else:
        st.success("✅ Berechtigt für kostenlosen Einbau")
