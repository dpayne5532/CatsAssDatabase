import tkinter as tk
from tkinter import ttk
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('asset_management.db')
cursor = conn.cursor()

# Create Employee and Asset tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                    EmployeeID INTEGER PRIMARY KEY,
                    EmployeeName TEXT NOT NULL,
                    DepartmentID INTEGER,
                    Position TEXT,
                    Email TEXT,
                    Phone TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Assets (
                    AssetID INTEGER PRIMARY KEY,
                    AssetName TEXT NOT NULL,
                    AssetType TEXT NOT NULL,
                    SerialNumber TEXT,
                    PurchaseDate TEXT,
                    PurchaseCost REAL,
                    AssignedToEmployeeID INTEGER
                )''')
conn.commit()

# Function to fetch employees from the database and display in the treeview
def load_employees():
    tree.delete(*tree.get_children())
    cursor.execute('SELECT * FROM Employees')
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

# Function to add a new employee to the database
def add_employee():
    name = name_entry.get()
    department_id = department_id_entry.get()
    position = position_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    cursor.execute('INSERT INTO Employees(EmployeeName, DepartmentID, Position, Email, Phone) VALUES (?, ?, ?, ?, ?)',
                   (name, department_id, position, email, phone))
    conn.commit()
    load_employees()

# Function to fetch assets from the database and display in the treeview
def load_assets():
    tree.delete(*tree.get_children())
    cursor.execute('SELECT * FROM Assets')
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

# Function to add a new asset to the database
def add_asset():
    name = asset_name_entry.get()
    asset_type = asset_type_entry.get()
    serial_number = serial_number_entry.get()
    purchase_date = purchase_date_entry.get()
    purchase_cost = purchase_cost_entry.get()
    assigned_to_employee_id = assigned_to_employee_id_entry.get()
    cursor.execute('INSERT INTO Assets(AssetName, AssetType, SerialNumber, PurchaseDate, PurchaseCost, AssignedToEmployeeID) VALUES (?, ?, ?, ?, ?, ?)',
                   (name, asset_type, serial_number, purchase_date, purchase_cost, assigned_to_employee_id))
    conn.commit()
    load_assets()

# Create the main window
root = tk.Tk()
root.title('IT Asset Management')

# Create the notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(pady=10)

# Create the Employees tab
employees_frame = ttk.Frame(notebook)
notebook.add(employees_frame, text='Employees')

# Create the treeview for displaying employees
tree = ttk.Treeview(employees_frame, columns=('EmployeeID', 'EmployeeName', 'DepartmentID', 'Position', 'Email', 'Phone'))
tree.heading('#0', text='EmployeeID')
tree.heading('#1', text='Name')
tree.heading('#2', text='DepartmentID')
tree.heading('#3', text='Position')
tree.heading('#4', text='Email')
tree.heading('#5', text='Phone')
tree.pack(expand=True, fill='both')

# Load employees initially
load_employees()

# Create the Add Employee section
add_employee_frame = ttk.LabelFrame(employees_frame, text='Add Employee')
add_employee_frame.pack(pady=10)

tk.Label(add_employee_frame, text='Name:').grid(row=0, column=0, padx=5, pady=2)
name_entry = tk.Entry(add_employee_frame)
name_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(add_employee_frame, text='Department ID:').grid(row=1, column=0, padx=5, pady=2)
department_id_entry = tk.Entry(add_employee_frame)
department_id_entry.grid(row=1, column=1, padx=5, pady=2)

tk.Label(add_employee_frame, text='Position:').grid(row=2, column=0, padx=5, pady=2)
position_entry = tk.Entry(add_employee_frame)
position_entry.grid(row=2, column=1, padx=5, pady=2)

tk.Label(add_employee_frame, text='Email:').grid(row=3, column=0, padx=5, pady=2)
email_entry = tk.Entry(add_employee_frame)
email_entry.grid(row=3, column=1, padx=5, pady=2)

tk.Label(add_employee_frame, text='Phone:').grid(row=4, column=0, padx=5, pady=2)
phone_entry = tk.Entry(add_employee_frame)
phone_entry.grid(row=4, column=1, padx=5, pady=2)

add_employee_button = tk.Button(add_employee_frame, text='Add Employee', command=add_employee)
add_employee_button.grid(row=5, columnspan=2, pady=5)

# Create the Assets tab
assets_frame = ttk.Frame(notebook)
notebook.add(assets_frame, text='Assets')

# Create the treeview for displaying assets
asset_tree = ttk.Treeview(assets_frame, columns=('AssetID', 'AssetName', 'AssetType', 'SerialNumber', 'PurchaseDate', 'PurchaseCost', 'AssignedToEmployeeID'))
asset_tree.heading('#0', text='AssetID')
asset_tree.heading('#1', text='Name')
asset_tree.heading('#2', text='Type')
asset_tree.heading('#3', text='Serial Number')
asset_tree.heading('#4', text='Purchase Date')
asset_tree.heading('#5', text='Purchase Cost')
asset_tree.heading('#6', text='Assigned To')
asset_tree.pack(expand=True, fill='both')

# Load assets initially
load_assets()

# Create the Add Asset section
add_asset_frame = ttk.LabelFrame(assets_frame, text='Add Asset')
add_asset_frame.pack(pady=10)

tk.Label(add_asset_frame, text='Name:').grid(row=0, column=0, padx=5, pady=2)
asset_name_entry = tk.Entry(add_asset_frame)
asset_name_entry.grid(row=0, column=1, padx=5, pady=2)

tk.Label(add_asset_frame, text='Type:').grid(row=1, column=0, padx=5, pady=2)
asset_type_entry = tk.Entry(add_asset_frame)
asset_type_entry.grid(row=1, column=1, padx=5, pady=2)

tk.Label(add_asset_frame, text='Serial Number:').grid(row=2, column=0, padx=5, pady=2)
serial_number_entry = tk.Entry(add_asset_frame)
serial_number_entry.grid(row=2, column=1, padx=5, pady=2)

tk.Label(add_asset_frame, text='Purchase Date:').grid(row=3, column=0, padx=5, pady=2)
purchase_date_entry = tk.Entry(add_asset_frame)
purchase_date_entry.grid(row=3, column=1, padx=5, pady=2)

tk.Label(add_asset_frame,text='Purchase Cost:').grid(row=4, column=0, padx=5, pady=2)
purchase_cost_entry = tk.Entry(add_asset_frame)
purchase_cost_entry.grid(row=4, column=1, padx=5, pady=2)

tk.Label(add_asset_frame, text='Assigned To Employee ID:').grid(row=5, column=0, padx=5, pady=2)
assigned_to_employee_id_entry = tk.Entry(add_asset_frame)
assigned_to_employee_id_entry.grid(row=5, column=1, padx=5, pady=2)

add_asset_button = tk.Button(add_asset_frame, text='Add Asset', command=add_asset)
add_asset_button.grid(row=6, columnspan=2, pady=5)

root.mainloop()