import streamlit as st

# ─── SETTRADE CREDENTIALS ─────────────────────────────────────────────────────
# ใส่ค่าทั้งหมดใน .streamlit/secrets.toml (local) หรือ Streamlit Cloud Secrets
APP_ID     = st.secrets["APP_ID"]
APP_SECRET = st.secrets["APP_SECRET"]
BROKER_ID  = st.secrets["BROKER_ID"]
APP_CODE   = st.secrets["APP_CODE"]

# ─── AI API ───────────────────────────────────────────────────────────────────
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
