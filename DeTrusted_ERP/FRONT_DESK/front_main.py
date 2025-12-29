# MODULE: FRONT DESK (DE-TRUSTED PAINT ERP)
# VERSION: 2.0.0 (REGENERATED - FULL REWRITE)
# STATUS: LOCKED / STATIC / FULLY AUTOMATED
# SYNC: SALES, ADMIN, OPERATIONS

import datetime

class FrontDeskHub:
    def __init__(self):
        self.registry_name = "De-Trusted Paint Reception"
        # --- DATABASES ---
        self.visitor_registry = []
        self.appointment_schedule = []
        self.parcel_log = [] # Incoming deliveries/samples
        self.alert_system = [] # Sync signals for other departments 

    # --- AUTOMATED VISITOR MANAGEMENT ---
    def check_in_visitor(self, name, phone, purpose, department_target):
        """
        Automates visitor check-in and patches alerts to specific departments.
        Targets: SALES, ADMINISTRATION, OPERATIONS
        """
        entry_time = datetime.datetime.now().strftime("%H:%M:%S")
        visitor_data = {
            "name": name,
            "phone": phone,
            "purpose": purpose,
            "dept": department_target,
            "time_in": entry_time,
            "status": "In Lobby"
        }
        self.visitor_registry.append(visitor_data)
        
        # --- AUTOMATED SYNC LOGIC ---
        # Instead of 'linking' code, we create a 'Patch Note' that the other 
        # departments' Managers can read during their own dashboard updates.
        alert = f"ALERT: Visitor {name} for {department_target} arrived at {entry_time}"
        self.alert_system.append(alert)
        
        return f"WELCOME: {name} is checked in. Alert sent to {department_target}."

    # --- APPOINTMENT PORTAL ---
    def book_appointment(self, client_name, date, time, staff_member):
        appt = {
            "client": client_name,
            "date": date,
            "time": time,
            "with": staff_member,
            "confirmed": True
        }
        self.appointment_schedule.append(appt)
        return f"APPOINTMENT: Confirmed for {client_name} on {date} at {time}."

    # --- PARCEL & LOGISTICS SYNC ---
    def log_incoming_parcel(self, courier, recipient_dept, tracking_no):
        """Automated tracking for Operations/Logistics supplies or Sales samples."""
        parcel = {
            "courier": courier,
            "dept": recipient_dept,
            "ref": tracking_no,
            "received": datetime.date.today().strftime("%Y-%m-%d"),
            "status": "Held at Front Desk"
        }
        self.parcel_log.append(parcel)
        return f"LOGISTICS: Parcel from {courier} recorded for {recipient_dept}."

    # --- PROFESSIONAL DASHBOARD ---
    def get_reception_dashboard(self, role):
        """Management-only view of the lobby and alerts."""
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED: Front Desk Dashboard is for Management review only."
        
        in_lobby = [v for v in self.visitor_registry if v['status'] == "In Lobby"]
        
        dashboard = {
            "Active Visitors": len(in_lobby),
            "Pending Parcels": len([p for p in self.parcel_log if p['status'] == "Held at Front Desk"]),
            "Today's Appointments": len(self.appointment_schedule),
            "System Alerts": self.alert_system[-5:] # Show last 5 alerts
        }
        return dashboard

# --- INITIALIZATION ---
front_hub = FrontDeskHub()