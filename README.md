# 📦 Logistics IT Support & Hardware Analysis

**Portfolio Project**  
**Role:** Key User / System Administrator (Logistics IT)  
**Technologies Used:** SQL (SQLite), Python (Pandas, Matplotlib), Data Visualization, IT Support Analytics  

👉 **[Click Here to Download & View the Full Logistics IT Support Report](https://raw.githubusercontent.com/Ritikghoghari/Logistics-IT-Support-Analysis/main/Logistics_IT_Support_Analysis.html)** (Download the `.html` file and open it in your browser to see the charts and SQL insights).

---

## 🎯 Project Overview
This project simulates the environment of a modern logistics warehouse handling daily IT support requests. It is designed to showcase my ability to manage IT hardware lifecycles, write analytical SQL queries, and optimize 1st-level support workflows.

The database consists of **6 months of IT support logs**, tracking 450+ incidents across 150 hardware devices (mobile scanners, label printers, and tablets).

### 🔍 Key Objectives
1. **Error Analysis:** Identify the most frequent and critical IT issues to reduce 1st-level support volume.
2. **Hardware Reliability:** Track hardware models to discover which devices require replacement or repair most often.
3. **Controlling & Reporting:** Monitor open support tickets by warehouse department to ensure operational continuity (picking, packing, returns).
4. **Resolution Efficiency:** Calculate average ticket resolution times to evaluate IT support KPIs.

---

## 🛠️ Project Architecture

### 1. Database Generation (`setup.py`)
I wrote a Python script to generate a relational SQL database (`warehouse_it_support.db`) containing three core tables:
* **Employees:** Warehouse staff assigned to specific departments and shifts.
* **Devices:** The IT equipment inventory (e.g., Zebra TC52 Scanners, Brother Label Printers).
* **Support_Tickets:** The central logging table for IT issues, tracking the status (Open/Closed), timestamps, and issue categories.

### 2. Analytical SQL Queries (`queries.sql`)
The core of the analysis relies on SQL. I formulated advanced queries using `JOIN`, `GROUP BY`, `AVG()`, and date functions to answer specific business questions.
*(You can view the raw SQL scripts in the `queries.sql` file).*

### 3. Data Visualization & Reporting (`generate_report.py`)
To make the data actionable for Logistics Management, the SQL results were exported into CSVs and processed using **Pandas and Matplotlib**. The script auto-generates professional charts and compiles them into a clean HTML presentation with actionable recommendations.

---

## 📊 Key Findings & Management Insights

Below is a summary of the insights derived from the SQL controlling report:

### 🚨 1. Critical Hardware Failures
* **Finding:** The Zebra TC52 and Zebra MC9300 mobile scanners accounted for the vast majority of all IT support tickets (>50%).
* **Action:** I recommend prioritizing "Troubleshooting Training" for these specific models. If the failure rate of the legacy TC52 continues, logistics budgeting should allocate funds for newer models in the next fiscal year.

### ⚠️ 2. Top IT Issues (Root Cause Analysis)
* **Finding:** "Screen Broken" (21.1%) and "No Wi-Fi Connection" (14.9%) were the most commonly reported errors.
* **Action:** To mitigate broken screens, the warehouse must enforce the use of heavy-duty rubber cases. To address Wi-Fi dropouts, IT must audit Wi-Fi dead zones, particularly in high-mobility areas like Outbound dispatch.

### 📈 3. Active Incident Bottlenecks
* **Finding:** The *Returns* department consistently had the highest number of unresolved / open IT issues.
* **Action:** Because Returns processing relies heavily on immediate scanner syncing, any IT delay creates a backlog of unsellable inventory. I recommend immediately dispatching an IT resource to the Returns floor to investigate potential systemic issues (such as a faulty WMS syncing station).

---

## 🚀 How to Run the Project Locally
If you would like to run this analysis on your own machine:

1. Clone the repository: `git clone https://github.com/Ritikghoghari/Logistics-IT-Support-Analysis.git`
2. Run the setup script to generate a fresh SQLite database: `python setup.py`
3. Execute the SQL queries using DB Browser for SQLite on the newly created `.db` file.
4. Export your SQL results to CSV inside the directory, and run `python generate_report.py` to compile the visual HTML report.

---
*Created by Ritik Ghoghari - Open to work as a Key User / System Administrator in Logistics.*
