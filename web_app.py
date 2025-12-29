import streamlit as st
import hmac

st.set_page_config(page_title="DE-TRUSTED PAINT ERP", layout="wide")

def check_password():
    """Returns True if the user had the correct password."""
    def password_entered():
        # Passwords for each role
credentials = {"SUPERVISOR": "Admin@2025", "STAFF": "Paint@Staff"}
# This is where you set your passwords
      # The opening bracket { starts the list
        credentials = {
            "SUPERVISOR": "Admin@2025",
            "STAFF": "Paint@Staff"
        }
        # The closing bracket } ends the list
        entered_role = st.session_state["role_choice"]
        entered_pass = st.session_state["password"]
        
        if hmac.compare_digest(entered_pass, credentials.get(entered_role, "")):
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = entered_role
            del st.session_state["password"]  # Remove password from memory
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    # Login UI
    st.title("🔐 DE-TRUSTED ERP LOGIN")
    st.selectbox("Select Your Role", ["STAFF", "SUPERVISOR"], key="role_choice")
    st.text_input("Enter Password", type="password", on_change=password_entered, key="password")
    
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect. Please try again.")
    return False

if check_password():
    # If password is correct, show the Hub
    st.title("🎨 DE-TRUSTED PAINT ERP - EXECUTIVE HUB")
    role = st.session_state["user_role"]
    st.info(f"Currency: GHC | Access Level: {role}")

    if st.sidebar.button("Log Out"):
        st.session_state["password_correct"] = False
        st.rerun()

    if role == "SUPERVISOR":
        st.success("👑 EXECUTIVE ACCESS: Total System Control")
        modules = [
            ("📊 Administration & HR", "Manage staff and GHC salaries."),
            ("🏗️ Production Desk", "Log paint batches and recipes."),
            ("💰 Sales & Marketing", "Record sales and customer data."),
            ("🏦 Finance & Accounts", "View P&L and GHC tax statements."),
            ("🚚 Logistics & Fleet", "Track delivery trucks and fuel."),
            ("📦 Warehousing", "Monitor raw materials and stock.")
        ]
    else:
        st.warning("👤 STAFF ACCESS: View assigned tasks only.")
        modules = [
            ("🏗️ Production Desk", "Log your daily batches."),
            ("💰 Sales & Marketing", "Process new GHC invoices."),
            ("📦 Warehousing", "Update stock levels.")
        ]

    # Grid Display
    cols = st.columns(3)
    for i, (title, desc) in enumerate(modules):
        with cols[i % 3]:
            st.subheader(title)
            st.write(desc)
            if st.button(f"Enter {title}", key=f"btn_{i}"):
                st.info(f"Opening {title}...")