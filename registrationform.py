from tkinter import *
from sklearn.preprocessing import LabelEncoder
from sleepprediction import train_linear_regression_model
import pymysql
def predict_sleep_duration(model, features):
    return model.predict([features])[0]

trained_model = train_linear_regression_model()
Le_gender = LabelEncoder()
base = Tk()
base.geometry('500x900')
base.title("Registration Form")
def calculate_bmi(height, weight): 
    # Convert height to meters
    height_in_meters = height / 100

    # Calculate BMI
    bmi = weight / (height_in_meters ** 2)

    # Encode BMI category
    if bmi < 18.5:
        return 0  # Underweight
    elif 18.5 <= bmi < 25:
        return 1  # Normal weight
    elif 25 <= bmi < 30:
        return 2  # Overweight
    else:
        return 3  # Obese
def onSubmit():
    height = float(entry_5.get())
    weight = float(entry_6.get())
    bmi_category = calculate_bmi(height, weight)
    gender = var.get()
    if(gender == 'male'):
        gender_encoded=1
    else:
        gender_encoded=0
    input_data = [
        gender_encoded,
        int(entry_4.get()),  # Age
        60,  # Physical Activity Level (you might want to get this value from the form)
        bmi_category,
        int(entry_7.get()),  # Systole
        int(entry_8.get()),  # Diastole
        int(entry_9.get()),  # Heart Rate
        int(entry_10.get())  # Daily Steps
    ]
    prediction = predict_sleep_duration(trained_model,input_data)

    # Display the prediction
    print(f'Predicted Sleep Duration: {prediction:.2f} hours')
    gender=gender_encoded
    print(bmi_category)
    age=int(entry_4.get())
    Systole=int(entry_7.get())
    Diastole=print(int(entry_8.get()))
    Heartrate=int(entry_9.get())
    daily_steps=int(entry_10.get())
    password=entry_11.get()
    name=entry_1.get()
    email=entry_2.get()
    logintodb(name,email,password,gender,age,height,weight,Systole,Diastole,Heartrate,daily_steps,prediction)
    open_login_form()
def open_login_form():
    base.withdraw()  # Hide the Registration Form
    from login import app as login_app
    login_app.deiconify()
    login_app.mainloop()
def logintodb(full, email,passw,gender_val, age_val, height_val, weight_val, systole_val, diastole_val,Heartrate,daily_steps,prediction):
    db = None 
    try:
        db = pymysql.connect(
        host="localhost",
        user="root",
        password="arijeet",
        database="Driver_info"
        )
        cursor = db.cursor()



        # Insert data into the table
        insert_query = "INSERT INTO health_data (full_name,email,age,height,weight,systolic_pressure,diastolic_pressure,physical_activity_level,heart_rate,daily_steps,pass,sleep_duration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
        data = (full, email, age_val, height_val, weight_val, systole_val, diastole_val, 60, Heartrate, daily_steps, passw, prediction)


        cursor.execute(insert_query, data)
        db.commit()

        print("Data inserted successfully")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()
label_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=33)

label_1 = Label(base, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=120)

entry_1 = Entry(base)
entry_1.place(x=240, y=120)

label_2 = Label(base, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=170)

entry_2 = Entry(base)
entry_2.place(x=240, y=170)

label_3 = Label(base, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=220)
var = IntVar()
Radiobutton(base, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(base, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)



label_4 = Label(base, text="Age:", width=20, font=("bold", 10))
label_4.place(x=70, y=270)
entry_4 = Entry(base)
entry_4.place(x=240, y=270)

label_5 = Label(base, text="Height:", width=20, font=("bold", 10))
label_5.place(x=70, y=320)
entry_5 = Entry(base)
entry_5.place(x=240, y=320)

label_6 = Label(base, text="Weight:", width=20, font=("bold", 10))
label_6.place(x=70, y=370)
entry_6 = Entry(base)
entry_6.place(x=240, y=370)

label_7 = Label(base, text="Systole:", width=20, font=("bold", 10))
label_7.place(x=70, y=420)
entry_7 = Entry(base)
entry_7.place(x=240, y=420)

label_8 = Label(base, text="Diastole:", width=20, font=("bold", 10))
label_8.place(x=70, y=470)
entry_8 = Entry(base)
entry_8.place(x=240, y=470)

label_9 = Label(base, text="Heart rate:", width=20, font=("bold", 10))
label_9.place(x=70, y=540)
entry_9 = Entry(base)
entry_9.place(x=240, y=540)

label_10=Label(base, text="Daily Steps" ,width=20, font=("bold" ,10))
label_10.place(x=70, y=590)
entry_10= Entry(base)
entry_10.place(x=240,y=590)

label_11=Label(base, text="Password" ,width=20, font=("bold" ,10))
label_11.place(x=70, y=640)
entry_11= Entry(base)
entry_11.place(x=240,y=640)

submit_button = Button(base, text='Submit', width=20, bg='brown', fg='white', command=onSubmit)
submit_button.place(x=180, y=690)
# it will be used for displaying the registration form onto the window
base.mainloop()
print("Registration form is created successfully...")

