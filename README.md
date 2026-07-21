# PulsePoint Analytics — Business Performance Intelligence Hub

A cross-industry Tableau dashboard analyzing commercial performance, 
client health, pharma sales effectiveness, and fintech transaction 
quality across 5 interconnected datasets.

🔗 **Live Dashboard:** [View on Tableau Public](https://public.tableau.com/views/PulsePointAnalytics/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Overview

PulsePoint Analytics simulates an enterprise-grade Business Intelligence 
dashboard used at analytics consulting firms to monitor KPIs across 
multiple business verticals. It combines pharma sales rep performance, 
fintech transaction analytics, client churn risk, revenue trends, and 
NPS scoring into a single unified dashboard — built entirely in Tableau 
with 5 cross-joined datasets.

## Key Questions Answered

- Which clients are at highest churn risk and which territories are underperforming?
- How are pharma sales reps tracking against Rx targets by drug and territory?
- What is the transaction failure rate by channel and what are the top failure reasons?
- How is gross margin and revenue trending month over month?
- Which drug classes drive the most prescription volume?
- How does NPS score vary across client tiers?


## Technical Highlights

- **5 datasets joined** — clients, fintech transactions, monthly revenue, 
  pharma sales, and rep performance linked via client_id
- **Tableau Features Used:** LOD expressions, box plots, treemaps, 
  territory heatmaps, revenue forecasting, rep leaderboard, cross-sheet 
  filter actions, parameter controls, KPI cards
- **Cross-industry scope** — pharma and fintech analytics in one unified dashboard
- **Business metrics modeled** — churn score, NPS, gross margin, Rx vs target 
  attainment, transaction failure rate, processing time

---

## Data Sources

| File | Description |
|---|---|
| `clients.csv` | Client master — industry, region, tier, contract value, account manager |
| `fintech_txns.csv` | Transaction records — channel, amount, status, failure reason, processing time |
| `monthly_revenue.csv` | Monthly revenue, cost, gross margin, churn score, NPS, support tickets |
| `pharma_sales.csv` | Rep-level Rx volume vs target by drug, drug class, and territory |
| `rep_performance.csv` | Sales rep details — territory, drug portfolio, monthly performance |

*All datasets are synthetic.*

## Tech Stack

| Tool | Purpose |
|---|---|
| Tableau Public | Dashboard building and publishing |
| Excel / CSV | Data preparation and dataset design |
| SQL/Python | Data Cleaning and Exploratory Data Analysis |

---

## Business Context

This dashboard simulates the kind of BI reporting used by analytics 
consulting firms working with pharma and fintech clients:

- **Pharma vertical** — sales force effectiveness, territory management, 
  Rx attainment tracking
- **Fintech vertical** — payment operations monitoring, failure diagnostics, 
  processing efficiency
- **Client analytics** — churn prediction, NPS tracking, revenue health 
 
