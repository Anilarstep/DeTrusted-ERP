# MODULE: FINANCE (DE-TRUSTED PAINT ERP)
# VERSION: 2.0.0 (REGENERATED - FULL REWRITE)
# STATUS: LOCKED / STATIC
# CURRENCY: GHC

class FinanceModule:
    def __init__(self):
        self.currency = "GHC"
        
        # --- STANDARD CHART OF ACCOUNTS ---
        self.chart_of_accounts = {
            "1000": "Cash & Bank",
            "1200": "Accounts Receivable (AR)",
            "2000": "Accounts Payable (AP)",
            "4000": "Sales Revenue",
            "5000": "Cost of Goods Sold",
            "6000": "Operating Expenses"
        }

        # --- LEDGERS & RECORDS ---
        self.general_ledger = []
        self.petty_cash_book = []
        self.vouchers = [] # Payment Vouchers
        self.invoices = []
        self.quotes = []
        self.receipts = []

        # --- GRA TAX RATES (Automated) ---
        self.tax_rates = {
            "VAT": 0.15,
            "NHIL": 0.025,
            "GETFUND": 0.025,
            "COVID19": 0.01
        }

    # --- SALES & REVENUE (Quotes, Invoices, Receipts) ---
    def generate_quote(self, customer, items_list):
        quote_id = f"QT-{len(self.quotes) + 101}"
        subtotal = sum(item['price'] for item in items_list)
        quote = {"id": quote_id, "customer": customer, "subtotal": subtotal, "status": "Draft"}
        self.quotes.append(quote)
        return f"Quote {quote_id} generated for {self.currency} {subtotal}"

    def convert_to_invoice(self, quote_id):
        # Automated Tax Calculation (21% Combined GRA Taxes)
        for q in self.quotes:
            if q["id"] == quote_id:
                base = q["subtotal"]
                total_tax = base * sum(self.tax_rates.values())
                invoice = {
                    "inv_id": f"INV-{quote_id}",
                    "amount_base": base,
                    "tax": total_tax,
                    "total": base + total_tax,
                    "status": "UNPAID" # Becomes AR
                }
                self.invoices.append(invoice)
                return f"Invoice generated: Total {self.currency} {invoice['total']} (Inc. GRA Taxes)"

    # --- EXPENDITURE (Petty Cash & Payment Vouchers) ---
    def create_payment_voucher(self, role, payee, amount, category_code):
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED: Cannot generate Payment Vouchers."
        
        pv_id = f"PV-{len(self.vouchers) + 500}"
        voucher = {
            "pv_id": pv_id, "payee": payee, "amount": f"{self.currency} {amount}",
            "account": self.chart_of_accounts.get(category_code, "Unknown"),
            "authorized_by": role
        }
        self.vouchers.append(voucher)
        return f"Voucher {pv_id} authorized."

    # --- FINANCIAL REPORTS & DASHBOARD ---
    def get_dashboard_summary(self, role):
        if role not in ["MANAGER", "SUPERVISOR"]:
            return "ACCESS DENIED."
        
        ar_total = sum(i['total'] for i in self.invoices if i['status'] == "UNPAID")
        return {
            "Total AR": f"{self.currency} {ar_total}",
            "Active Quotes": len(self.quotes),
            "GRA Tax Liability": "Calculated per Invoice"
        }

# --- INITIALIZATION ---
finance_desk = FinanceModule()