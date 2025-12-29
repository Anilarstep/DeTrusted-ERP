# MODULE: HR (DE-TRUSTED PAINT ERP)
# VERSION: 4.5.0 (FINAL COMPLETE EDITION)
# STATUS: LOCKED / 2025 COMPLIANT
# CURRENCY: GHC

import datetime

class HRModule:
    def __init__(self):
        self.currency = "GHC"
        self.id_counter = 5000  # IDs start from DTP-HR-5001
        
        # --- CORE DATABASES ---
        self.staff_database = {}      # {Staff_ID: {Details}}
        self.salary_advance_logs = [] # Track all advance requests
        self.leave_applications = []  # Track leave status
        self.recruitment_pipeline = [] # Track applicants

    # 1. AUTOMATED ONBOARDING (ID GENERATION)
    def onboard_new_employee(self, role, name, position, base_salary):
        """Generates staff ID and locks entry into database."""
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED: Role must be MANAGER/SUPERVISOR for onboarding."
        
        self.id_counter += 1
        staff_id = f"DTP-HR-{self.id_counter}"
        
        self.staff_database[staff_id] = {
            "name": name,
            "position": position,
            "salary": float(base_salary),
            "joined_date": datetime.date.today().strftime("%Y-%m-%d"),
            "status": "Active"
        }
        return f"SUCCESS: {name} onboarded. Assigned ID: {staff_id}"

    # 2. SALARY ADVANCE PORTAL
    def request_salary_advance(self, staff_id, amount, reason):
        """Portal for employees to request GHC advances."""
        if staff_id not in self.staff_database:
            return "ERROR: Staff ID not found in system."
        
        request = {
            "staff_id": staff_id,
            "name": self.staff_database[staff_id]["name"],
            "amount": float(amount),
            "reason": reason,
            "date": datetime.date.today().strftime("%Y-%m-%d"),
            "authorized": False
        }
        self.salary_advance_logs.append(request)
        return f"SUCCESS: Advance request of {self.currency} {amount} queued for approval."

    # 3. LEAVE & RECRUITMENT MANAGEMENT
    def apply_for_leave(self, staff_id, days):
        self.leave_applications.append({"id": staff_id, "days": days, "status": "Pending"})
        return "Leave application submitted."

    def add_applicant(self, name, position):
        self.recruitment_pipeline.append({"name": name, "position": position, "status": "Interviewing"})
        return f"Recruitment: {name} added to pipeline."

    # 4. HR MANAGEMENT DASHBOARD (SUPERVISOR ONLY)
    def get_hr_dashboard(self, role):
        """Complete snapshot of HR health."""
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED: HR Analytics locked."
        
        active_staff = [s for s in self.staff_database.values() if s['status'] == "Active"]
        total_payroll = sum(s['salary'] for s in active_staff)
        pending_advances = [a for a in self.salary_advance_logs if not a['authorized']]

        dashboard = {
            "Total Headcount": len(active_staff),
            "Monthly Payroll Liability": f"{self.currency} {total_payroll:,.2f}",
            "Pending Salary Advances": len(pending_advances),
            "Open Recruitment Slots": len(self.recruitment_pipeline),
            "Status": "2025 COMPLIANT"
        }
        return dashboard

# --- INITIALIZATION ---
hr_desk = HRModule()