-- 1. Support Tickets by Device Model
-- Useful to see which hardware models break down the most and might need replacing.
SELECT 
    d.model,
    COUNT(t.ticket_id) AS total_tickets
FROM Devices d
JOIN Support_Tickets t ON d.device_id = t.device_id
GROUP BY d.model
ORDER BY total_tickets DESC;


-- 2. Most Common IT Issues Reported
-- Helps the IT Department know what training or resources are needed.
SELECT 
    issue_category,
    COUNT(ticket_id) AS incident_count,
    ROUND(COUNT(ticket_id) * 100.0 / (SELECT COUNT(*) FROM Support_Tickets), 1) AS percentage_of_total
FROM Support_Tickets
GROUP BY issue_category
ORDER BY incident_count DESC;


-- 3. Open Tickets Alert (By Department)
-- Shows how many open support tasks are pending right now.
SELECT 
    e.department,
    COUNT(t.ticket_id) AS open_tickets
FROM Employees e
JOIN Support_Tickets t ON e.employee_id = t.employee_id
WHERE t.status = 'Open'
GROUP BY e.department
ORDER BY open_tickets DESC;


-- 4. Average Ticket Resolution Time (In Hours)
-- Demonstrates monitoring KPIs (Key Performance Indicators) for 1st-Level IT Support.
SELECT 
    issue_category,
    COUNT(ticket_id) AS total_closed_tickets,
    ROUND(AVG((julianday(resolution_date) - julianday(reported_date)) * 24), 2) AS avg_resolution_hours
FROM Support_Tickets
WHERE status = 'Closed'
GROUP BY issue_category
ORDER BY avg_resolution_hours DESC;


-- 5. Hardware Replacement Search
-- Find all Mobile Scanners that are active but were purchased over 3 years ago (Before 2022).
SELECT 
    device_id, 
    model, 
    purchase_date,
    status
FROM Devices 
WHERE device_type = 'Mobile Scanner' 
  AND status = 'Active' 
  AND purchase_date < '2022-01-01'
ORDER BY purchase_date ASC;
