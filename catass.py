import tkinter as tk
from tkinter import ttk
import sqlite3

def on_tree_select(event):
    selected_item = tree.selection()[0]
    item_values = tree.item(selected_item, 'values')
    # Populate entry fields with selected item values
    asset_name_entry.delete(0, tk.END)
    asset_name_entry.insert(0, item_values[1])
    asset_type_entry.delete(0, tk.END)
    asset_type_entry.insert(0, item_values[2])
    serial_number_entry.delete(0, tk.END)
    serial_number_entry.insert(0, item_values[3])
    purchase_date_entry.delete(0, tk.END)
    purchase_date_entry.insert(0, item_values[4])
    purchase_cost_entry.delete(0, tk.END)
    purchase_cost_entry.insert(0, item_values[5])
    assigned_to_employee_id_entry.delete(0, tk.END)
    assigned_to_employee_id_entry.insert(0, item_values[6])

def load_assets():
    tree.delete(*tree.get_children())
    cursor.execute('SELECT * FROM Assets')
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

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

def edit_asset():
    selected_item = tree.selection()[0]
    asset_id = tree.item(selected_item, 'values')[0]
    name = asset_name_entry.get()
    asset_type = asset_type_entry.get()
    serial_number = serial_number_entry.get()
    purchase_date = purchase_date_entry.get()
    purchase_cost = purchase_cost_entry.get()
    assigned_to_employee_id = assigned_to_employee_id_entry.get()
    cursor.execute('UPDATE Assets SET AssetName=?, AssetType=?, SerialNumber=?, PurchaseDate=?, PurchaseCost=?, AssignedToEmployeeID=? WHERE AssetID=?',
                   (name, asset_type, serial_number, purchase_date, purchase_cost, assigned_to_employee_id, asset_id))
    conn.commit()
    load_assets()

conn = sqlite3.connect('asset_management.db')
cursor = conn.cursor()

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

root = tk.Tk()
root.title('IT Asset Management')

tree = ttk.Treeview(root, columns=('AssetID', 'AssetName', 'AssetType', 'SerialNumber', 'PurchaseDate', 'PurchaseCost', 'AssignedToEmployeeID'), selectmode='browse')
tree.heading('#0', text='AssetID')
tree.heading('#1', text='Name')
tree.heading('#2', text='Type')
tree.heading('#3', text='Serial Number')
tree.heading('#4', text='Purchase Date')
tree.heading('#5', text='Purchase Cost')
tree.heading('#6', text='Assigned To')
tree.pack(expand=True, fill='both')

tree.bind('<<TreeviewSelect>>', on_tree_select)

load_assets()

add_asset_frame = ttk.LabelFrame(root, text='Add/Edit Asset')
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

tk.Label(add_asset_frame, text='Purchase Cost:').grid(row=4, column=0, padx=5, pady=2)
purchase_cost_entry = tk.Entry(add_asset_frame)
purchase_cost_entry.grid(row=4, column=1, padx=5, pady=2)

tk.Label(add_asset_frame, text='Assigned To Employee ID:').grid(row=5, column=0, padx=5, pady=2)
assigned_to_employee_id_entry = tk.Entry(add_asset_frame)
assigned_to_employee_id_entry.grid(row=5, column=1, padx=5, pady=2)

add_asset_button = tk.Button(add_asset_frame, text='Add Asset', command=add_asset)
add_asset_button.grid(row=6, columnspan=2, pady=5)

edit_asset_button = tk.Button(add_asset_frame, text='Edit Asset', command=edit_asset)
edit_asset_button.grid(row=7, columnspan=2, pady=5)

root.mainloop()

