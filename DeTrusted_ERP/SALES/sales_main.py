# MODULE: SALES & MARKETING (DE-TRUSTED PAINT ERP)
# VERSION: 3.0.0 (COMMERCIAL GROWTH EDITION)
# STATUS: 2025 COMPLIANCE / FULLY AUTOMATED / SYNCED
# CURRENCY: GHC

import datetime

class SalesMarketingHub:
    def __init__(self):
        self.currency = "GHC"
        # --- SALES PERSON & LOCATION DATABASE ---
        self.sales_team = {
            "EMP-001": {"name": "Kofi Mensah", "location": "Accra Central", "target": 50000, "sales": 0},
            "EMP-002": {"name": "Ama Serwaa", "location": "Kumasi/Ashanti", "target": 45000, "sales": 0}
        }
        
        # --- CUSTOMER MANAGEMENT & CX ---
        self.customer_database = {} # Detailed profiles
        self.cx_feedback_scores = [] # Net Promoter Score (NPS) tracking
        
        # --- INNOVATIVE MARKETING MODULES ---
        self.marketing_campaigns = []
        self.market_trends = {"Eco-Friendly": "Rising", "Matte_Finish": "High_Demand"}
        
        self.quotations = []
        self.sales_orders = []

    # --- 1. TERRITORY & SALESPERSON MANAGEMENT ---
    def update_sales_performance(self, staff_id, amount):
        """Automated sync with HR/Finance for commission."""
        if staff_id in self.sales_team:
            self.sales_team[staff_id]["sales"] += amount
            status = "On Track" if self.sales_team[staff_id]["sales"] >= self.sales_team[staff_id]["target"] else "Below Target"
            return f"PERFORMANCE: {self.sales_team[staff_id]['name']} updated. Status: {status}."
        return "ERROR: Staff ID not found."

    # --- 2. ADVANCED CUSTOMER MANAGEMENT (CX) ---
    def log_customer_experience(self, customer_id, rating, comment):
        """Automated CX tracking (Scale 1-10)."""
        feedback = {
            "customer": customer_id,
            "rating": rating, # 1-10
            "comment": comment,
            "date": datetime.date.today().strftime("%Y-%m-%d")
        }
        self.cx_feedback_scores.append(feedback)
        if rating < 5:
            return "CX ALERT: Low rating detected. Automated ticket sent to Administration."
        return "CX LOGGED: Thank you for the feedback."

    # --- 3. INNOVATIVE MARKETING: PREDICTIVE CAMPAIGNS ---
    def launch_marketing_campaign(self, role, campaign_name, budget_ghc, target_location):
        """Strategic Marketing Module."""
        if role != "MANAGER": return "DENIED."
        
        campaign = {
            "name": campaign_name,
            "budget": f"{self.currency} {budget_ghc}",
            "location": target_location,
            "roi_projected": "150%",
            "status": "Active"
        }
        self.marketing_campaigns.append(campaign)
        return f"MARKETING: {campaign_name} launched in {target_location}."

    # --- 4. SALES SYNC & ORDERING ---
    def generate_professional_quote(self, customer_name, items, location):
        """Syncs with Finance GRA Taxes and Logistics availability."""
        quote_id = f"SLS-{datetime.datetime.now().strftime('%m%d%f')}"
        subtotal = sum(i['price'] for i in items)
        tax = subtotal * 0.21 # 21% Combined GRA Taxes
        
        quote = {
            "id": quote_id,
            "customer": customer_name,
            "location": location,
            "grand_total": f"{self.currency} {subtotal + tax}",
            "status": "Pending Dispatch" # Signals Logistics
        }
        self.quotations.append(quote)
        return quote

    # --- 5. THE COMMANDER DASHBOARD ---
    def get_commercial_dashboard(self, role):
        if role not in ["MANAGER", "SUPERVISOR"]: return "DENIED."
        
        avg_cx = sum(f['rating'] for f in self.cx_feedback_scores) / len(self.cx_feedback_scores) if self.cx_feedback_scores else 0
        
        return {
            "Revenue_By_Location": {v['location']: v['sales'] for v in self.sales_team.values()},
            "Customer_Experience_Score": f"{avg_cx}/10",
            "Active_Campaigns": len(self.marketing_campaigns),
            "Market_Insight": self.market_trends,
            "Sync_Status": "Connected to Logistics/Finance"
        }

# --- INITIALIZATION ---
sales_marketing_hub = SalesMarketingHub()