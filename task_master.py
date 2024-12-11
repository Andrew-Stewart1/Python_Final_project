import sqlite3
from datetime import date

#connecting to the database with conn and cursor
conn = sqlite3.connect('to_do_list.db')
cursor = conn.cursor()

def add_task(item_to_do, description)
  date = datetime.now().strftime('%Y-%m-%d')
  cursor.execute(
    "INSET INTO to_do_list (item_to_do, description, progress, date) VALUES ()",
    (item_to_do, description, progress, date))
  conn.commit()

  
    
