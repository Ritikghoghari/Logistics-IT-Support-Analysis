import pandas as pd
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO

# Paths to the user's CSV files
csv_dir = r"c:\Users\Allah o akbar\Desktop\Data Analyst Project"
csv_issues = os.path.join(csv_dir, "_2_Most_Common_IT_Issues_Reported_Helps_the_IT_Department_know_w_202602250144.csv")
csv_open_tickets = os.path.join(csv_dir, "_3_Open_Tickets_Alert_By_Department_Shows_how_many_open_support__202602250145.csv")
csv_devices = os.path.join(csv_dir, "_1_Support_Tickets_by_Device_Model_Useful_to_see_which_hardware__202602250144.csv")

# Create charts directory
charts_dir = os.path.join(csv_dir, "Warehouse_IT_Project", "charts")
os.makedirs(charts_dir, exist_ok=True)

# 1. Bar Chart: Most Common Issues
df_issues = pd.read_csv(csv_issues)
plt.figure(figsize=(10, 6))
# Only take top 5 issues for the chart
top_issues = df_issues.head(5)
plt.bar(top_issues['issue_category'], top_issues['incident_count'], color=['#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6'])
plt.title('Top 5 Most Common IT Issues Reported', fontsize=16)
plt.xlabel('Issue Category', fontsize=12)
plt.ylabel('Number of Incidents', fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()
chart1_path = os.path.join(charts_dir, "common_issues_bar.png")
plt.savefig(chart1_path)
plt.close()

# 2. Pie Chart: Open Tickets by Department
df_open = pd.read_csv(csv_open_tickets)
plt.figure(figsize=(8, 8))
plt.pie(df_open['open_tickets'], labels=df_open['department'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Open Tickets Distribution by Department', fontsize=16)
plt.tight_layout()
chart2_path = os.path.join(charts_dir, "open_tickets_pie.png")
plt.savefig(chart2_path)
plt.close()

# 3. Bar Chart: Tickets by Device Model
df_devices = pd.read_csv(csv_devices)
plt.figure(figsize=(10, 6))
plt.barh(df_devices['model'], df_devices['total_tickets'], color='#34495e')
plt.title('Total Support Tickets by Device Model', fontsize=16)
plt.xlabel('Total Tickets', fontsize=12)
plt.ylabel('Device Model', fontsize=12)
plt.gca().invert_yaxis()
plt.tight_layout()
chart3_path = os.path.join(charts_dir, "device_tickets_bar.png")
plt.savefig(chart3_path)
plt.close()

# Helper function to convert image to base64 for embedding in HTML
def img_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

# Generate HTML Report
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Logistics IT Support Analysis</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #333;
            line-height: 1.6;
            margin: 0 auto;
            max-width: 900px;
            padding: 20px;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2980b9;
            margin-top: 30px;
        }}
        .summary-box {{
            background-color: #f8f9fa;
            border-left: 5px solid #e74c3c;
            padding: 15px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .chart-container {{
            text-align: center;
            margin: 30px 0;
        }}
        .chart-container img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .sql-snippet {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', Courier, monospace;
            overflow-x: auto;
            border-left: 4px solid #2ecc71;
        }}
    </style>
</head>
<body>

    <h1>Logistics IT Support Analysis</h1>
    <p><strong>Prepared for:</strong> FIEGE Logistics | Key User / System Administrator Application Portfolio</p>
    <p><strong>Focus:</strong> IT Equipment Tracking, Error Analysis, and Controlling Metrics</p>

    <!-- SECTION 1 -->
    <h2>1. Identifying Critical Hardware Failures</h2>
    <p>We tracked the total number of IT support incidents across various warehouse device models to identify potential hardware replacement needs.</p>
    
    <div class="sql-snippet">
<pre>
SELECT d.model, COUNT(t.ticket_id) AS total_tickets
FROM Devices d
JOIN Support_Tickets t ON d.device_id = t.device_id
GROUP BY d.model
ORDER BY total_tickets DESC;
</pre>
    </div>

    <div class="chart-container">
        <img src="{img_to_base64(chart3_path)}" alt="Tickets by Device Model">
    </div>

    <div class="summary-box">
        <strong>Management Insight (Actionable Recommendation):</strong><br>
        The data clearly highlights that the Zebra TC52 and Zebra MC9300 mobile scanners generate the vast majority of our IT support workload (125 and 115 tickets respectively). As a Key User, I recommend prioritizing "Troubleshooting Training" for these specific models. If the failure rate of the legacy TC52 continues, we should consider budgeting for newer models in the next fiscal year.
    </div>

    <!-- SECTION 2 -->
    <h2>2. Top IT Issues / Error Analysis</h2>
    <p>To reduce the load on 1st-level support, we analyzed the root causes of all reported IT issues.</p>
    
    <div class="sql-snippet">
<pre>
SELECT issue_category, COUNT(ticket_id) AS incident_count,
       ROUND(COUNT(ticket_id) * 100.0 / (SELECT COUNT(*) FROM Support_Tickets), 1) AS percentage_of_total
FROM Support_Tickets
GROUP BY issue_category
ORDER BY incident_count DESC;
</pre>
    </div>

    <div class="chart-container">
        <img src="{img_to_base64(chart1_path)}" alt="Top 5 Most Common Incident Issue Categories">
    </div>

    <div class="summary-box">
        <strong>Management Insight (Actionable Recommendation):</strong><br>
        Currently, "Screen Broken" (21.1%) and "No Wi-Fi Connection" (14.9%) are in the top 3 issues. 
        <ul>
            <li><strong>Action 1:</strong> To mitigate broken screens, we should enforce the use of heavy-duty rubber cases and install screen protectors on all mobile scanners.</li>
            <li><strong>Action 2:</strong> To address the Wi-Fi dropouts, we need to instruct employees to soft-reset localized access points, or investigate Wi-Fi dead zones in the warehouse (especially in the Outbound area).</li>
        </ul>
    </div>

    <!-- SECTION 3 -->
    <h2>3. Active Support Workload by Department</h2>
    <p>By monitoring the active (open) tickets by department, we ensure operational continuity and prevent bottlenecks in the logistics process.</p>

    <div class="sql-snippet">
<pre>
SELECT e.department, COUNT(t.ticket_id) AS open_tickets
FROM Employees e
JOIN Support_Tickets t ON e.employee_id = t.employee_id
WHERE t.status = 'Open'
GROUP BY e.department
ORDER BY open_tickets DESC;
</pre>
    </div>

    <div class="chart-container">
        <img src="{img_to_base64(chart2_path)}" alt="Open Tickets by Department">
    </div>

    <div class="summary-box">
        <strong>Management Insight (Actionable Recommendation):</strong><br>
        The <span style="color: #e74c3c;">Returns department</span> currently has the highest number of unresolved IT issues (12 open tickets). Since Returns processing relies heavily on immediate scanner syncing, any delay here creates a backlog of unsellable inventory. I recommend immediately dispatching an IT resource to the Returns floor to clear this backlog and investigate if there is a systemic issue (such as a faulty WMS syncing station) causing this spike.
    </div>

</body>
</html>
"""

report_path = os.path.join(csv_dir, "Warehouse_IT_Project", "Logistics_IT_Support_Analysis.html")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Report successfully generated at: {report_path}")
