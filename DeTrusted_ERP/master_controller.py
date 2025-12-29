import sys
import os
# Importing your completed modules
from HR.hr_main import hr_desk
from FRONT_DESK.front_main import front_hub

class ERPController:
    def __init__(self):
        self.user_name = "Director"
        self.user_role = "SUPERVISOR"

    def run_daily_ops(self):
        while True: # This keeps the interface from closing
            os.system('cls' if os.name == 'nt' else 'clear') # Cleans the screen
            print("\n--- DE-TRUSTED PAINT ERP LOGIN SUCCESSFUL ---")
            print(f"User: {self.user_name} | Role: {self.user_role} | Status: Online")
            print("[SYSTEM UPDATE: 2025-12-29]")
            
            # Displaying the Dashboard Overview
            print("\n--- MANAGEMENT DASHBOARD ---")
            print(front_hub.get_reception_dashboard(self.user_role))
            print(hr_desk.get_hr_dashboard(self.user_role))
            
            print("\n--- MAIN MENU ---")
            print("1. FRONT DESK")
            print("2. HR MODULE")
            print("3. FINANCE / SALES")
            print("X. EXIT SYSTEM")
            
            choice = input("\nSelect Department (1-3) or X to Exit: ").upper()
            
            if choice == "1":
                self.run_front_desk()
            elif choice == "2":
                self.run_hr_module()
            elif choice == "X":
                print("Closing System...")
                break
            else:
                input("Invalid selection. Press Enter to try again.")

    def run_hr_module(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n--- HR MANAGEMENT INTERFACE ---")
            print("1. Onboard New Employee")
            print("2. HR Dashboard (Stats)")
            print("B. Back to Main Menu")
            
            sub_choice = input("\nSelect Action: ").upper()
            if sub_choice == "1":
                name = input("Enter Full Name: ")
                pos = input("Enter Position: ")
                sal = input("Enter Base Salary (GHC): ")
                print("\n" + hr_desk.onboard_new_employee(self.user_role, name, pos, sal))
                input("\nPress Enter to continue...")
            elif sub_choice == "2":
                print("\n", hr_desk.get_hr_dashboard(self.user_role))
                input("\nPress Enter to continue...")
            elif sub_choice == "B":
                break

    def run_front_desk(self):
        # Similar logic for Front Desk
        input("\nFront Desk Interface Loading... Press Enter to go back.")
        return

if __name__ == "__main__":
    erp = ERPController()
    erp.run_daily_ops()