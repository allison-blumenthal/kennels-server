import sqlite3
import json

from models import Location, Animal, Employee

# LOCATIONS = [
#     {
#         "id": 1,
#         "name": "Nashville North",
#         "address": "8422 Johnson Pike"
#     },
#     {
#         "id": 2,
#         "name": "Nashville South",
#         "address": "209 Emory Drive"
#     }
# ]

# def get_all_locations():
#   return LOCATIONS

# def get_single_location(id):
#   requested_location = None
  
#   for location in LOCATIONS:
#     if location["id"] == id:
#       requested_location = location
      
#   return requested_location

# def create_location(location):
#   max_id = LOCATIONS[-1]["id"]
  
#   new_id = max_id + 1
  
#   location["id"] = new_id
  
#   LOCATIONS.append(location)
  
#   return location

# def delete_location(id):
#   location_index = -1
  
#   for index, loccation in enumerate(LOCATIONS):
#     if loccation["id"] == id:
#       location_index = index
  
#   if location_index >= 0:
#     LOCATIONS.POP(location_index)
    
# def update_location(id, new_location):
#     # Iterate the locationS list, but use enumerate() so that
#     # you can access the index value of each item.
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             # Found the location. Update the value.
#             LOCATIONS[index] = new_location
#             break
          
#sql get all locations
def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of row into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of row returned from database
        for row in dataset:

            # Create a location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__) # see the notes below for an explanation on this line of code.

    return locations

#sql get single location
def get_single_location(id):
    
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT	
            l.id,
            l.name,
            l.address
        FROM location l
        WHERE l.id = ?
        """, ( id, ))
           
        # Load the single result into memory
        data = db_cursor.fetchone()
        
        # Create a location instance from the current row
        location = Location(data['id'], data['name'], data['address'])
        
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT	
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ? 
        """, ( id, ))
        
        employees = []
        
         # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            
            employees.append(employee.__dict__)
            
            location.employees = employees

        db_cursor.execute("""
        SELECT	
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id          
        FROM animal a
        WHERE a.location_id = ?
        """, ( id, ))
        
        animals = []
        
         # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['location_id'], row['customer_id'])
            
            animals.append(animal.__dict__)
            
            location.animals = animals
            
    return location.__dict__
