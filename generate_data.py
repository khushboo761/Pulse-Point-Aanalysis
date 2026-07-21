import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

OUT = "/home/claude/tableau_data"
os.makedirs(OUT, exist_ok=True)

# ─────────────────────────────────────────────
# 1. clients.csv
# ─────────────────────────────────────────────
industries = ["Pharma", "Fintech", "E-Commerce"]
regions = ["North", "South", "East", "West", "Central"]
tiers = ["Platinum", "Gold", "Silver"]

client_names = [
    "AuraMed Pharma", "BioVista Labs", "CureAxis Inc", "DeltaRx Corp", "EvoHealth",
    "FluxPay Solutions", "GreenLedger", "HorizonBank", "IndiPay", "JetCredit",
    "KartZone", "LunaShop", "MegaMart", "NexCart", "OmniRetail"
]

clients = pd.DataFrame({
    "client_id": [f"CLT{str(i).zfill(3)}" for i in range(1, 16)],
    "client_name": client_names,
    "industry": ["Pharma"] * 5 + ["Fintech"] * 5 + ["E-Commerce"] * 5,
    "region": np.random.choice(regions, 15),
    "contract_value": np.random.choice([500000, 750000, 1000000, 1500000, 2000000], 15),
    "tier": ["Platinum"] * 4 + ["Gold"] * 6 + ["Silver"] * 5,
    "onboard_year": np.random.choice([2020, 2021, 2022, 2023], 15),
    "account_manager": np.random.choice(["Priya S", "Rohan M", "Ayesha K", "Dev P", "Sneha T"], 15)
})

clients.to_csv(f"{OUT}/clients.csv", index=False)
print("✓ clients.csv")

# ─────────────────────────────────────────────
# 2. pharma_sales.csv  (monthly, 2022–2024)
# ─────────────────────────────────────────────
pharma_client_ids = [f"CLT{str(i).zfill(3)}" for i in range(1, 6)]
drugs = ["Atorvastatin", "Metformin", "Amlodipine", "Omeprazole", "Sertraline",
         "Lisinopril", "Losartan", "Pantoprazole", "Levothyroxine", "Metoprolol"]
drug_class = {
    "Atorvastatin": "Cardiovascular", "Metformin": "Diabetes", "Amlodipine": "Cardiovascular",
    "Omeprazole": "GI", "Sertraline": "CNS", "Lisinopril": "Cardiovascular",
    "Losartan": "Cardiovascular", "Pantoprazole": "GI", "Levothyroxine": "Endocrine",
    "Metoprolol": "Cardiovascular"
}
territories = ["TER-N1", "TER-N2", "TER-S1", "TER-S2", "TER-E1", "TER-E2", "TER-W1", "TER-W2"]

rows = []
months = pd.date_range("2022-01-01", "2024-12-01", freq="MS")
rep_ids = [f"REP{str(i).zfill(2)}" for i in range(1, 21)]

for client_id in pharma_client_ids:
    assigned_reps = np.random.choice(rep_ids, 4, replace=False)
    assigned_drugs = np.random.choice(drugs, 4, replace=False)
    for rep in assigned_reps:
        territory = np.random.choice(territories)
        for drug in assigned_drugs:
            base_rx = np.random.randint(200, 800)
            target_rx = int(base_rx * np.random.uniform(0.9, 1.2))
            for month in months:
                # add seasonality + trend + noise
                seasonal = 1 + 0.15 * np.sin((month.month - 3) * np.pi / 6)
                trend = 1 + 0.005 * ((month.year - 2022) * 12 + month.month)
                noise = np.random.normal(1, 0.08)
                rx_vol = max(50, int(base_rx * seasonal * trend * noise))
                rows.append({
                    "client_id": client_id,
                    "rep_id": rep,
                    "territory": territory,
                    "drug": drug,
                    "drug_class": drug_class[drug],
                    "month": month.strftime("%Y-%m-%d"),
                    "rx_volume": rx_vol,
                    "target_rx": target_rx,
                    "calls_made": np.random.randint(20, 80),
                    "samples_distributed": np.random.randint(10, 50)
                })

pharma_sales = pd.DataFrame(rows)
pharma_sales.to_csv(f"{OUT}/pharma_sales.csv", index=False)
print(f"✓ pharma_sales.csv  ({len(pharma_sales):,} rows)")

# ─────────────────────────────────────────────
# 3. fintech_txns.csv  (daily, 2023–2024)
# ─────────────────────────────────────────────
fintech_client_ids = [f"CLT{str(i).zfill(3)}" for i in range(6, 11)]
channels = ["UPI", "Net Banking", "Credit Card", "Debit Card", "Wallet"]
statuses = ["Success", "Success", "Success", "Success", "Failed", "Pending"]  # weighted
failure_reasons = ["Insufficient Funds", "Network Timeout", "Bank Declined", "Invalid OTP", None]

rows = []
dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")
user_pool = [f"USR{str(i).zfill(5)}" for i in range(1, 5001)]

for date in dates:
    n_txns = np.random.randint(200, 600)
    for _ in range(n_txns):
        status = random.choice(statuses)
        channel = np.random.choice(channels, p=[0.45, 0.15, 0.20, 0.12, 0.08])
        amount = round(np.random.lognormal(6, 1.2), 2)
        rows.append({
            "txn_id": f"TXN{len(rows)+1:08d}",
            "date": date.strftime("%Y-%m-%d"),
            "client_id": random.choice(fintech_client_ids),
            "user_id": random.choice(user_pool),
            "channel": channel,
            "amount": min(amount, 500000),
            "status": status,
            "failure_reason": random.choice(failure_reasons) if status == "Failed" else None,
            "processing_time_ms": np.random.randint(200, 5000) if status != "Failed" else np.random.randint(5000, 30000)
        })

fintech_txns = pd.DataFrame(rows)
fintech_txns.to_csv(f"{OUT}/fintech_txns.csv", index=False)
print(f"✓ fintech_txns.csv  ({len(fintech_txns):,} rows)")

# ─────────────────────────────────────────────
# 4. monthly_revenue.csv  (all 15 clients, 2022–2024)
# ─────────────────────────────────────────────
rows = []
for _, client in clients.iterrows():
    base_rev = client["contract_value"] / 12
    churn_risk_base = {"Platinum": 0.03, "Gold": 0.08, "Silver": 0.15}[client["tier"]]
    for month in pd.date_range("2022-01-01", "2024-12-01", freq="MS"):
        growth = 1 + 0.004 * ((month.year - 2022) * 12 + month.month)
        noise = np.random.normal(1, 0.06)
        revenue = round(base_rev * growth * noise, 2)
        cost = round(revenue * np.random.uniform(0.55, 0.72), 2)
        churn_score = round(min(1.0, churn_risk_base + np.random.normal(0, 0.05)), 2)
        rows.append({
            "client_id": client["client_id"],
            "month": month.strftime("%Y-%m-%d"),
            "revenue": max(0, revenue),
            "cost": max(0, cost),
            "gross_margin": round((revenue - cost) / revenue * 100, 1) if revenue > 0 else 0,
            "churn_score": max(0, churn_score),
            "churn_flag": 1 if churn_score > 0.6 else 0,
            "nps_score": np.random.randint(20, 95),
            "support_tickets": np.random.randint(0, 25)
        })

monthly_revenue = pd.DataFrame(rows)
monthly_revenue.to_csv(f"{OUT}/monthly_revenue.csv", index=False)
print(f"✓ monthly_revenue.csv  ({len(monthly_revenue):,} rows)")

# ─────────────────────────────────────────────
# 5. rep_performance.csv  (quarterly, pharma reps)
# ─────────────────────────────────────────────
rows = []
quarters = ["2022-Q1","2022-Q2","2022-Q3","2022-Q4",
            "2023-Q1","2023-Q2","2023-Q3","2023-Q4",
            "2024-Q1","2024-Q2","2024-Q3","2024-Q4"]

for rep in rep_ids:
    client_id = random.choice(pharma_client_ids)
    base_score = np.random.uniform(55, 90)
    for q in quarters:
        calls = np.random.randint(80, 300)
        deals = int(calls * np.random.uniform(0.15, 0.40))
        score = round(min(100, base_score + np.random.normal(0, 5)), 1)
        rows.append({
            "rep_id": rep,
            "client_id": client_id,
            "quarter": q,
            "calls_made": calls,
            "deals_closed": deals,
            "conversion_rate": round(deals / calls * 100, 1),
            "revenue_generated": round(deals * np.random.uniform(8000, 25000), 2),
            "performance_score": score,
            "rank_bucket": "Top" if score >= 80 else ("Mid" if score >= 65 else "Low"),
            "training_hrs": np.random.randint(0, 20)
        })

rep_performance = pd.DataFrame(rows)
rep_performance.to_csv(f"{OUT}/rep_performance.csv", index=False)
print(f"✓ rep_performance.csv  ({len(rep_performance):,} rows)")

print("\n✅ All 5 CSVs generated in:", OUT)
print("\nRow counts summary:")
for name, df in [("clients", clients), ("pharma_sales", pharma_sales),
                  ("fintech_txns", fintech_txns), ("monthly_revenue", monthly_revenue),
                  ("rep_performance", rep_performance)]:
    print(f"  {name:25s}: {len(df):>7,} rows  ×  {len(df.columns):>2} columns")
