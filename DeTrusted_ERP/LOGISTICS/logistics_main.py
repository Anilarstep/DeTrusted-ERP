# MODULE: LOGISTICS & FLEET (DE-TRUSTED PAINT ERP)
# VERSION: 3.5.0 (FINAL COMPLETE EDITION)
# STATUS: LOCKED / 2025 COMPLIANT
# SYNC: PRODUCTION, SALES, FRONT DESK

import datetime

class LogisticsTower:
    def __init__(self):
        self.currency = "GHC"
        # --- FLEET DATABASE ---
        self.fleet = {
            "VAN-01": {"type": "Delivery Van", "status": "Available", "driver": "K. Boateng", "fuel": "Full"},
            "TRK-01": {"type": "Heavy Truck", "status": "In Transit", "driver": "A. Mensah", "fuel": "Half"},
            "VAN-02": {"type": "Delivery Van", "status": "Maintenance", "driver": "Unassigned", "fuel": "Empty"}
        }
        
        # --- SHIPMENT & DELIVERY TRACKING ---
        self.active_shipments = []
        self.delivery_history = []

    # --- 1. DISPATCH MANAGEMENT ---
    def dispatch_delivery(self, role, order_id, destination, vehicle_id):
        """Automates the dispatch of paint orders to clients."""
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED: Only Management can dispatch fleet."
        
        if vehicle_id not in self.fleet or self.fleet[vehicle_id]["status"] != "Available":
            return f"ERROR: Vehicle {vehicle_id} is not available for dispatch."
        
        # Update Vehicle Status
        self.fleet[vehicle_id]["status"] = "In Transit"
        
        shipment_data = {
            "order_ref": order_id,
            "destination": destination,
            "vehicle": vehicle_id,
            "driver": self.fleet[vehicle_id]["driver"],
            "dispatch_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "On Route"
        }
        self.active_shipments.append(shipment_data)
        return f"DISPATCH SUCCESS: Order {order_id} is now On Route via {vehicle_id}."

    # --- 2. SHIPMENT TRACKING & UPDATES ---
    def update_delivery_status(self, order_id, new_status):
        """Updates status: 'Delivered', 'Delayed', or 'Returned'."""
        for shipment in self.active_shipments:
            if shipment["order_ref"] == order_id:
                shipment["status"] = new_status
                if new_status == "Delivered":
                    shipment["completion_time"] = datetime.datetime.now().strftime("%H:%M")
                    self.delivery_history.append(shipment)
                    # Return vehicle to Available pool
                    self.fleet[shipment["vehicle"]]["status"] = "Available"
                return f"TRACKING: Order {order_id} updated to {new_status}."
        return "ERROR: Order ID not found in active shipments."

    # --- 3. FLEET & LOGISTICS DASHBOARD ---
    def get_logistics_dashboard(self, role):
        """Real-time view of fleet and delivery efficiency."""
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED: Logistics Dashboard is locked."
        
        available_vehicles = [k for k, v in self.fleet.items() if v["status"] == "Available"]
        
        dashboard = {
            "Total Fleet Count": len(self.fleet),
            "Vehicles Available": available_vehicles,
            "Active Shipments": len(self.active_shipments),
            "Completed Deliveries Today": len(self.delivery_history),
            "System Status": "LOGISTICS TOWER ONLINE"
        }
        return dashboard

# --- INITIALIZATION ---
logistics_tower = LogisticsTower()