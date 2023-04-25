import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

def get_all_employees():
  return EMPLOYEES

def get_single_employee(id):
  requested_employee = None
  
  for employee in EMPLOYEES:
    if employee["id"] == id:
      requested_employee = employee
      
  return requested_employee

def create_employee(employee):
  max_id = EMPLOYEES[-1]["id"]
  
  new_id = max_id + 1
  
  employee["id"] = new_id
  
  EMPLOYEES.append(employee)
  
  return employee

def delete_employee(id):
  employee_index = -1
  
  for index, location in enumerate(EMPLOYEES):
    if location["id"] == id:
      employee_index = index
  
  if employee_index >= 0:
    EMPLOYEES.POP(employee_index)
    
def update_employee(id, new_employee):
    # Iterate the employeeS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break

def get_all_employees():
  with sqlite3.connect("./kennel.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        a.id,
        a.name
    FROM employee a
    """)
    
    employees = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      employee = Employee(row['id'], row['name'])
      
      employees.append(employee.__dict__)
      
      
  return employees

def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()
        
        employee = Employee(data['id'], data['name'])
        
        return employee.__dict__
