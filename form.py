from tkinter import *

base = Tk()
base.geometry('500x700')
base.title("Registration Form")

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
label_8.place(x=70, y=420)
entry_8 = Entry(base)
entry_8.place(x=240, y=420)

label_9 = Label(base, text="Password:", width=20, font=("bold", 10))
label_9.place(x=70, y=470)
entry_9 = Entry(base)
entry_9.place(x=240, y=470)



Button(base, text='Submit', width=20, bg='brown', fg='white').place(x=180, y=570)
# it will be used for displaying the registration form onto the window
base.mainloop()
print("Registration form is created successfully...")
