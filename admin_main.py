# MODULE: ADMINISTRATION (DE-TRUSTED PAINT ERP)
# VERSION: 3.0.0 (OFFICE OPERATIONS EDITION)
# STATUS: FULLY AUTOMATED / PROFESSIONAL
# CURRENCY: GHC

import datetime

class AdministrationDept:
    def __init__(self):
        self.currency = "GHC"
        # --- OFFICE DATABASES ---
        self.fleet_management = {} # {Vehicle_Plate: {Status, Last_Service}}
        self.utility_tracker = []   # Electricity, Water, Internet logs
        self.procurement_requests = [] # Office supplies, furniture, etc.
        self.maintenance_log = []   # AC repairs, plumbing, painting
        self.cleaning_schedule = "Automated: Daily @ 6:00 AM"

    # --- FLEET & TRANSPORT AUTOMATION ---
    def register_vehicle(self, role, plate_no, model):
        if role != "MANAGER":
            return "DENIED: Manager required to register assets."
        self.fleet_management[plate_no] = {
            "model": model,
            "status": "Available",
            "last_service": datetime.date.today().strftime("%Y-%m-%d")
        }
        return f"ASSET: Vehicle {plate_no} added to Fleet."

    def request_vehicle(self, staff_id, plate_no, destination):
        if plate_no in self.fleet_management and self.fleet_management[plate_no]["status"] == "Available":
            self.fleet_management[plate_no]["status"] = f"In Use by {staff_id}"
            return f"APPROVED: Vehicle {plate_no} dispatched to {destination}."
        return "ERROR: Vehicle unavailable."

    # --- UTILITY & BILLING (GHC) ---
    def log_utility_bill(self, role, utility_type, amount):
        """Automated tracking for Electricity (ECG), Water (GWCL), etc."""
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "DENIED: Access restricted."
        
        bill = {
            "type": utility_type,
            "cost": f"{self.currency} {amount}",
            "date": datetime.date.today().strftime("%Y-%m-%d"),
            "status": "Logged for Payment"
        }
        self.utility_tracker.append(bill)
        return f"UTILITY: {utility_type} bill of {amount} {self.currency} recorded."

    # --- PROCUREMENT PORTAL ---
    def create_requisition(self, staff_id, item, quantity, estimated_cost):
        """Standard Office Procurement Workflow."""
        req = {
            "id": f"REQ-{len(self.procurement_requests) + 101}",
            "staff": staff_id,
            "item": item,
            "qty": quantity,
            "est_cost": f"{self.currency} {estimated_cost}",
            "approved": False
        }
        self.procurement_requests.append(req)
        return f"SUCCESS: Requisition {req['id']} submitted for approval."

    # --- ADMINISTRATION DASHBOARD ---
    def get_admin_ops_dashboard(self, role):
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED."

        dashboard = {
            "Total Fleet Assets": len(self.fleet_management),
            "Vehicles In Use": len([v for v in self.fleet_management.values() if "In Use" in v['status']]),
            "Pending Requisitions": len([r for r in self.procurement_requests if not r['approved']]),
            "Monthly Utility Spend": "Calculated from Tracker",
            "Next Cleaning": self.cleaning_schedule
        }
        return dashboard

# --- INITIALIZATION ---
admin_dept = AdministrationDept()