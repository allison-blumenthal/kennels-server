import sqlite3
import json

from models import Customer

# CUSTOMERS = [
#     {
#         "id": 1,
#         "name": "Ryan Tanay",
#         "owner": False
#     }
# ]

# def get_all_customers():
#     return CUSTOMERS

# def get_single_customer(id):
#     requested_customer = None
    
#     for customer in CUSTOMERS:
#         if customer["id"] == id:
#             requested_customer = customer
            
#     return requested_customer

# def create_customer(customer):
#   max_id = CUSTOMERS[-1]["id"]
  
#   new_id = max_id + 1
  
#   customer["id"] = new_id
  
#   CUSTOMERS.append(customer)
  
#   return customer

# def delete_customer(id):
#   customer_index = -1
  
#   for index, loccation in enumerate(CUSTOMERS):
#     if loccation["id"] == id:
#       customer_index = index
  
#   if customer_index >= 0:
#     CUSTOMERS.POP(customer_index)
    
# def update_customer(id, new_customer):
#     # Iterate the CUSTOMERS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, customer in enumerate(CUSTOMERS):
#         if customer["id"] == id:
#             # Found the customer. Update the value.
#             CUSTOMERS[index] = new_customer
#             break

#sql statements
def get_all_customers():
  with sqlite3.connect("./kennel.sqlite3") as conn:
    
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        c.id,
        c.name,
        c.address,
        c.email,
        c.password
    FROM customer c
    """)
    
    customers = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      
      customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])
      
      customers.append(customer.__dict__)
      
  return customers


def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()
        
        customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password'])
        
        return customer.__dict__

def get_customer_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return customers
