import pandas as pd
import os

# Create folders if they don't exist
for folder in ['HR', 'PRODUCTION', 'SALES']:
    if not os.path.exists(folder):
        os.makedirs(folder)

def save_transaction(module, data):
    filename = f"{module}/transactions.csv"
    df = pd.DataFrame([data])
    df.to_csv(filename, mode='a', header=not os.path.exists(filename), index=False)
    return f"Success: Saved to {module}"