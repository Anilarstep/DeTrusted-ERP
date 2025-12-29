import streamlit as st
import hmac

# 1. Page Configuration
st.set_page_config(page_title="DE-TRUSTED PAINT ERP", layout="wide")

# 2. Security & Role Access Logic
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

def check_password():
    def password_entered():
        # Cleanly formatted credentials for Role Access
        credentials = {
            "SUPERVISOR": "Admin@2025", 
            "STAFF": "Paint@Staff"
        }
        
        if hmac.compare_digest(st.session_state["pass_input"], credentials.get(st.session_state["role_input"], "")):
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = st.session_state["role_input"]
            st.rerun()
        else:
            st.error("❌ Invalid Password")

    if not st.session_state["password_correct"]:
        st.title("🔐 DE-TRUSTED ERP LOGIN")
        st.selectbox("Select Role", ["STAFF", "SUPERVISOR"], key="role_input")
        st.text_input("Password", type="password", key="pass_input", on_change=password_entered)
        st.info("Please enter your credentials to access the GHC financial modules.")
        return False
    return True

# 3. Main Dashboard Interface
if check_password():
    st.title("🎨 DE-TRUSTED PAINT ERP — EXECUTIVE HUB")
    st.sidebar.write(f"Logged in as: **{st.session_state['user_role']}**")
    
    if st.sidebar.button("🔒 Log Out"):
        st.session_state["password_correct"] = False
        st.rerun()

    # Define the grid for the 6 modules
    col1, col2 = st.columns(2)

    with col1:
        # Module 1: Administration & HR
        with st.expander("📊 Administration & HR", expanded=True):
            st.write("Manage staff payroll and records in **GHC**.")
            if st.button("Enter 📊 Administration"):
                st.info("Opening HR Module...")

        # Module 2: Production Desk
        with st.expander("🏗️ Production Desk", expanded=True):
            st.write("Log paint batches and chemical recipes.")
            if st.button("Enter 🏗️ Production"):
                st.info("Opening Production...")

        # Module 3: Finance & Accounts (Restricted to SUPERVISOR)
        if st.session_state["user_role"] == "SUPERVISOR":
            with st.expander("💰 Finance & Accounts", expanded=True):
                st.write("View P&L and GHC tax statements.")
                if st.button("Enter 💰 Finance"):
                    st.info("Opening Finance...")
        else:
            st.warning("💰 Finance: Access Restricted to Supervisor")

    with col2:
        # Module 4: Sales & Marketing
        with st.expander("💰 Sales & Marketing", expanded=True):
            st.write("Record sales and customer data.")
            if st.button("Enter 💰 Sales"):
                st.info("Opening Sales...")

        # Module 5: Warehousing & Inventory
        with st.expander("📦 Warehousing", expanded=True):
            st.write("Monitor raw materials and stock levels.")
            if st.button("Enter 📦 Warehousing"):
                st.info("Opening Warehousing...")

        # Module 6: Logistics & Fleet (Restricted to SUPERVISOR)
        if st.session_state["user_role"] == "SUPERVISOR":
            with st.expander("🚚 Logistics & Fleet", expanded=True):
                st.write("Track delivery trucks and fuel consumption.")
                if st.button("Enter 🚚 Logistics"):
                    st.info("Opening Logistics...")
        else:
            st.warning("🚚 Logistics: Access Restricted to Supervisor")