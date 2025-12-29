import streamlit as st
import hmac

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(page_title="DE-TRUSTED PAINT ERP", layout="wide")

# Initialize Security State
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

# --- 2. SECURITY SYSTEM ---
def check_password():
    def password_entered():
        # Updated Credentials
        credentials = {"SUPERVISOR": "Admin@2025", "STAFF": "Paint@Staff"}
        if hmac.compare_digest(st.session_state["pass_input"], credentials.get(st.session_state["role_input"], "")):
            st.session_state["password_correct"] = True
            st.session_state["user_role"] = st.session_state["role_input"]
            st.rerun() # Forces the dashboard to activate immediately
        else:
            st.error("❌ Invalid Password")

    if not st.session_state["password_correct"]:
        st.title("🔐 DE-TRUSTED ERP LOGIN")
        st.selectbox("Select Role", ["STAFF", "SUPERVISOR"], key="role_input")
        st.text_input("Password", type="password", key="pass_input", on_change=password_entered)
        return False
    return True

# --- 3. MAIN INTERFACE ---
if check_password():
    # Sidebar Navigation
    st.sidebar.title(f"👤 {st.session_state['user_role']} MENU")
    
    # Restricted Menu Logic
    if st.session_state["user_role"] == "SUPERVISOR":
        menu = ["🏠 Home Hub", "📊 Admin & HR", "🏗️ Production", "💰 Sales", "💸 Finance", "🚚 Logistics", "📦 Warehousing"]
    else:
        menu = ["🏠 Home Hub", "🏗️ Production", "💰 Sales", "📦 Warehousing"]
    
    choice = st.sidebar.radio("Navigate:", menu)
    
    if st.sidebar.button("🔒 Log Out"):
        st.session_state["password_correct"] = False
        st.rerun()

    # --- 4. DEPARTMENT MODULES ---
    if choice == "🏠 Home Hub":
        st.title("🎨 DE-TRUSTED PAINT ERP — EXECUTIVE HUB")
        st.write(f"Welcome to the 2025 Command Center. All records are in **GHC**.")
        st.info("Select a module from the sidebar to begin.")

    elif choice == "📊 Admin & HR":
        st.title("📊 Administration & HR")
        st.write("Manage staff and payroll in **GHC**.")
        st.text_input("Staff Name")
        st.number_input("Salary (GHC)", min_value=0.0)

    elif choice == "🏗️ Production":
        st.title("🏗️ Production Desk")
        st.selectbox("Select Paint Category", ["Oil Paint", "Water Base", "Auto Paint"])
        st.number_input("Batch Size (Litres)", step=1)

    elif choice == "💰 Sales":
        st.title("💰 Sales & Marketing")
        st.write("Generate GHC Invoices.")
        st.text_input("Customer Name")
        st.number_input("Total Sale (GHC)")

    elif choice == "💸 Finance":
        # Supervisor Only
        st.title("💸 Finance & Accounts")
        st.metric("Total Revenue", "GHC 0.00")
        st.metric("Net Profit", "GHC 0.00")

    elif choice == "🚚 Logistics":
        # Supervisor Only
        st.title("🚚 Logistics & Fleet")
        st.text_input("Vehicle Number")
        st.number_input("Fuel Cost (GHC)")

    elif choice == "📦 Warehousing":
        st.title("📦 Inventory Control")
        st.number_input("Raw Material Stock (Kgs)")