import sqlite3

# Connect to database
conn = sqlite3.connect('4 Database Intigrations/test.db')
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📋 Database Tables:")
for table in tables:
    print(f"  - {table[0]}")

# View employees table
print("\n👥 Employees Table:")
cursor.execute("SELECT * FROM employees;")
employees = cursor.fetchall()

if employees:
    print("ID | Name | Email | Department | Age | Created At")
    print("-" * 80)
    for emp in employees:
        print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4]} | {emp[5]}")
else:
    print("❌ No employees found")

conn.close()
print("\n✅ Database closed")