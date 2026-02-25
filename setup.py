import sqlite3
import random
from datetime import datetime, timedelta
import os

# Ensure we are saving in the correct directory
db_path = os.path.join(os.path.dirname(__file__), 'warehouse_it_support.db')

print(f"Generating database at: {db_path}")

# Connect to SQLite (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Create Tables
cursor.executescript('''
DROP TABLE IF EXISTS Support_Tickets;
DROP TABLE IF EXISTS Devices;
DROP TABLE IF EXISTS Employees;

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    department TEXT,
    shift TEXT
);

CREATE TABLE Devices (
    device_id TEXT PRIMARY KEY,
    device_type TEXT,
    model TEXT,
    purchase_date DATE,
    status TEXT
);

CREATE TABLE Support_Tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id TEXT,
    employee_id INTEGER,
    issue_category TEXT,
    reported_date DATETIME,
    resolution_date DATETIME,
    status TEXT,
    FOREIGN KEY (device_id) REFERENCES Devices(device_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
''')

# 2. Generate Employees
first_names = ["Lukas", "Leon", "Finn", "Paul", "Jonas", "Lena", "Mia", "Hannah", "Emma", "Sofia", "Markus", "Thomas", "Andreas", "Michael", "Daniel", "Julia", "Sarah", "Laura", "Anna", "Lisa"]
last_names = ["Muller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann"]
departments = ["Inbound", "Outbound", "Inventory", "Returns"]
shifts = ["Morning", "Evening", "Night"]

employees = []
for i in range(1, 51):
    employees.append((
        random.choice(first_names),
        random.choice(last_names),
        random.choice(departments),
        random.choice(shifts)
    ))
cursor.executemany("INSERT INTO Employees (first_name, last_name, department, shift) VALUES (?, ?, ?, ?)", employees)

# 3. Generate Devices
device_models = {
    "Mobile Scanner": ["Zebra TC52", "Honeywell CT40", "Zebra MC9300"],
    "Label Printer": ["Zebra ZT411", "Brother TD-4D"],
    "Tablet": ["iPad 10th Gen", "Samsung Galaxy Tab Active3"]
}
statuses = ["Active", "Active", "Active", "In Repair", "Decommissioned"]

devices = []
base_date = datetime(2021, 1, 1)

for i in range(1, 151):
    dev_id = f"DEV-{i:03d}"
    dtype = random.choices(["Mobile Scanner", "Label Printer", "Tablet"], weights=[70, 20, 10])[0]
    model = random.choice(device_models[dtype])
    purch_date = base_date + timedelta(days=random.randint(0, 730))
    status = random.choice(statuses)
    
    devices.append((dev_id, dtype, model, purch_date.strftime("%Y-%m-%d"), status))
    
cursor.executemany("INSERT INTO Devices (device_id, device_type, model, purchase_date, status) VALUES (?, ?, ?, ?, ?)", devices)

# 4. Generate Support Tickets (Past 6 Months)
issue_categories = {
    "Mobile Scanner": ["Battery Dying Fast", "Screen Broken", "Won't Scan Barcode", "App Crashing", "No Wi-Fi Connection"],
    "Label Printer": ["Paper Jam", "Faded Print", "Connection Lost", "Out of Labels"],
    "Tablet": ["Screen Broken", "Battery Dying Fast", "App Crashing", "Software Update Required"]
}

tickets = []
end_date = datetime.now()
start_date = end_date - timedelta(days=180)

for i in range(1, 451): # 450 tickets
    dev = random.choice(devices)
    dev_id = dev[0]
    dtype = dev[1]
    
    emp_id = random.randint(1, 50)
    issue = random.choice(issue_categories[dtype])
    
    rep_date = start_date + timedelta(days=random.randint(0, 180), hours=random.randint(6, 22), minutes=random.randint(0, 59))
    
    is_open = random.random() < 0.08 # 8% open
    if is_open:
        status = "Open"
        res_date = None
    else:
        status = "Closed"
        # Add random resolution time between 10 mins and 3 days
        res_date = rep_date + timedelta(minutes=random.randint(10, 4320))
        
    tickets.append((
        dev_id,
        emp_id,
        issue,
        rep_date.strftime("%Y-%m-%d %H:%M:%S"),
        res_date.strftime("%Y-%m-%d %H:%M:%S") if res_date else None,
        status
    ))

cursor.executemany("INSERT INTO Support_Tickets (device_id, employee_id, issue_category, reported_date, resolution_date, status) VALUES (?, ?, ?, ?, ?, ?)", tickets)

conn.commit()
conn.close()

print("Done! Database successfully generated.")
