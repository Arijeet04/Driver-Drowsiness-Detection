import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import pymysql as pymysql
from datetime import datetime, timedelta

ctk.set_appearance_mode("light") 


ctk.set_default_color_theme("blue") 

app = ctk.CTk() 
app.geometry("400x500") 
app.title("LOGIN") 

def calculate_next_sleep(wake_up_time, amount_of_sleep_needed):
    wake_up_datetime = datetime.strptime(wake_up_time, "%H:%M")
    
    # Get current local time
    current_local_time = datetime.now()

    # Ensure that all time-related calculations use the local time
    if wake_up_datetime > current_local_time:
        # If the wake-up time is in the future, subtract a day to get the correct time difference
        wake_up_datetime -= timedelta(days=1)

    sleep_time_datetime = wake_up_datetime - timedelta(hours=amount_of_sleep_needed)
    sleep_time = sleep_time_datetime.strftime("%H:%M")
    
    # Calculate time left using the local current time
    time_left = sleep_time_datetime - current_local_time
    
    time_left_str = f"{time_left.seconds // 3600} hours and {(time_left.seconds // 60) % 60} minutes"
    return sleep_time, time_left_str


def login(): 
	db = None 
	try:
		db = pymysql.connect(
        host="localhost",
        user="root",
        password="arijeet",
        database="Driver_info"
        )
		cursor = db.cursor()
	except Exception as e:
		print(f"Error occured: {e}")
	username=user_entry.get()
	password=user_pass.get()

	query="Select * from health_data where full_name=%s AND pass=%s"
	cursor.execute(query,(username,password))
	result = cursor.fetchone()
	if(result):
		last_sleep_time = last_sleep_entry.get()
		query="Select sleep_duration from health_data where full_name=%s AND pass=%s"
		cursor.execute(query,(username,password))
		result=cursor.fetchone()
		amount_of_sleep_needed = result[0]
		next_sleep_time, time_left_str = calculate_next_sleep(last_sleep_time, amount_of_sleep_needed)
		next_sleep_label.configure(text=f"Next Sleep Time: {next_sleep_time}\nTime Left: {time_left_str}")
		
		print("Log in Successful")
		app.after(5000,lambda:app.withdraw())
		from gui import window as gui_window
		gui_window.deiconify()
		gui_window.mainloop()
	else:
		print("Log in not succcessful")
		app.withdraw()
		from registrationform import base as registration
		registration.deiconify()
		registration.mainloop()
	new_window = ctk.CTkToplevel(app) 

	new_window.title("New Window") 

	new_window.geometry("350x150") 

label = ctk.CTkLabel(app,text="WELCOME AGAIN!!!!") 

label.pack(pady=20) 


frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label = ctk.CTkLabel(master=frame,text='LOGIN') 
label.pack(pady=12,padx=10) 

user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 

last_sleep_entry = ctk.CTkEntry(master=frame, placeholder_text="Last Sleep Time (HH:MM)")
last_sleep_entry.pack(pady=12, padx=10)

next_sleep_label = ctk.CTkLabel(master=frame, text="")
next_sleep_label.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 

next_sleep_label = ctk.CTkLabel(master=frame, text="")
next_sleep_label.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 


app.mainloop()
