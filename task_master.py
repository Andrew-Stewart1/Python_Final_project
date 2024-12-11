import sqlite3
from datetime import date

#connecting to the database with conn and cursor
conn = sqlite3.connect('to_do_list.db')
cursor = conn.cursor()

def add_to_do_list(item_to_do, description)
  date = datetime.now().strftime('%Y-%m-%d')
  cursor.execute(
    "INSET INTO to_do_list (item_to_do, description, progress, date) VALUES ()",
    (item_to_do, description, progress, date))
  conn.commit()

def update_to_do_list_progress(to_do_id, progress_update):
  cursor.execute(
    "UPDATE to_do_list SET progress = ? WHERE id = ?",
    (progress_update, to_do_id)
conn.commit()

def view_to_do_list():
  cursor.execute("SELECT * FROM to_do_list")
  to_do_list = cursor.fetchall()

def delete_to_do_list(to_to_id):
    cursor.execute("DELETE FROM to_do_list WHERE id = ?",
    (to_do_id))
conn.commit()

                 
  
    
