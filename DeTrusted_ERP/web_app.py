import streamlit as st
import datetime
# Importing your existing logic from your folders
from HR.hr_main import hr_desk
from FRONT_DESK.front_main import front_hub

# 1. VISUAL THEME (Matches your screenshot)
st.set_page_config(page_title="De-Trusted Paint ERP", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1621; color: white; }
    .card { 
        padding: 20px; 
        border-radius: 10px; 
        background-color: #1a2332; 
        margin-bottom: 20px;
        min-height: 180px;
    }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #1f2937; color: white; border: 1px solid #374151; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGIN GATE
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("DE-TRUSTED PAINT ERP")
    st