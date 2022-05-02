from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector as sq
import tkinter.messagebox as MessageBox



#back button
master_user="user x"
master_doctor="patient x"
doctor_type="nothing"
doctor_ka_patient = "nooope"




# Button_with hover effect
def bttn(win,x, y, text, ecolor, lcolor,com):
        def on_entera(e):
            myButton1['background'] = ecolor
            myButton1['foreground'] = lcolor

        def on_leavea(e):
            myButton1['background'] = lcolor
            myButton1['foreground'] = ecolor

        myButton1 = Button(win, text=text,
                           width=20,
                           height=2,
                           fg=ecolor,font='Sans 10 bold',
                           border=0,
                           bg=lcolor,
                           activeforeground=lcolor,
                           activebackground=ecolor,
                           command=com)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)


# --------------------------PATIENT REGISTER---------------------------------

def p_reg():
    w = Toplevel()
    w.geometry('350x700+1180+140')
    w.title('patient reg')
    w.resizable(0, 0)
    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w, width=10, height=700, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    Frame(w, width=250, height=600, bg='white').place(x=50, y=50)

    def add_record():
        name_e = e2.get()
        user_e = e1.get()
        contact_e = e6.get()
        age_e = e5.get()
        gender_e = gender.get()
        password_e = e3.get()
        repassword_e = e4.get()
        if (name_e == "" or user_e == "" or contact_e == "" or age_e == "" or password_e == "" or repassword_e == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")
        elif (password_e != repassword_e):
            MessageBox.showinfo("Insert Status", "Password and re-enter password does not match")
        elif (age_e.isdecimal() or contact_e.isdecimal()):

            conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")

            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO p_register VALUES('" + name_e + "','" + user_e + "','" + contact_e + "','" + age_e + "','" + gender_e + "','" + password_e + "','" + repassword_e + "')")
            cursor.execute("commit");
            MessageBox.showinfo("Insert Status", "Inserted successfully");
            cursor.execute("INSERT INTO p_login VALUES('" + user_e + "','" + password_e + "')")
            cursor.execute("commit");
            conn.close()
            w.destroy()
            p_log()



    # label for username
    l1 = Label(w, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=70)

    # e1 entry for username entry
    e1 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=100)

    # label for name
    l2 = Label(w, text='Name', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=140)

    # e2 entry for username entry
    e2 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e2.config(font=l)
    e2.place(x=80, y=170)

    # e3 entry for password entry
    e3 = Entry(w, width=20, border=0, show='*')
    e3.config(font=l)
    e3.place(x=80, y=240)

    # label for password
    l3 = Label(w, text='Password', bg='white')
    l = ('Consolas', 13)
    l3.config(font=l)
    l3.place(x=80, y=210)

    # label for re enter password
    l4 = Label(w, text='Re Enter Password', bg='white')
    l = ('Consolas', 13)
    l4.config(font=l)
    l4.place(x=80, y=280)

    # e4 entry for re password entry
    e4 = Entry(w, width=20, border=0, show='*')
    e4.config(font=l)
    e4.place(x=80, y=310)

    l5 = Label(w, text='Age', bg='white')
    l = ('Consolas', 13)
    l5.config(font=l)
    l5.place(x=80, y=340)

    # e5 entry for age entry
    e5 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e5.config(font=l)
    e5.place(x=80, y=380)

    l6 = Label(w, text='Contact', bg='white')
    l = ('Consolas', 13)
    l6.config(font=l)
    l6.place(x=80, y=410)

    # e6 entry for contact entry
    e6 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e6.config(font=l)
    e6.place(x=80, y=450)

    l6 = Label(w, text='Gender', bg='white')
    l = ('Consolas', 13)
    l6.config(font=l)
    l6.place(x=80, y=480)

    gender = StringVar(w)
    gender.set(NONE)
    gender_rbm = Radiobutton(w, width=7, font='Consolas', variable=gender, text="Male", value='Male', bg='white')
    gender_rbm.place(x=60, y=510)
    gender_rbf = Radiobutton(w, width=7, font='Consolas', variable=gender, text="Female", value="Female", bg='white')
    gender_rbf.place(x=160, y=510)



    # buttons
    bttn(w,80,580,'S U B M I T','white', '#994422',add_record)


    ###lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=122)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=192)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=262)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=402)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=472)

    #print(gender.get())
    w.mainloop()


# ----------------------------PATIENT LOGIN----------------------------------------

def p_log():
    w = Toplevel()
    w.geometry('350x500+1220+260')
    w.title('P A T I E N T   L O G I N ')
    w.resizable(0, 0)

    def reg():
        w.destroy()
        p_reg()


    def p_verify():
        if (e1 == "" or e2 == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")
        else:
            conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
            cursor = conn.cursor()
            cursor.execute("select * from p_login where username=%s and password = %s",
                           (e1.get(), e2.get()))
            row = cursor.fetchone()
            if row == None:
                MessageBox.showinfo("Insert Status", "Invalid password or username")
            else:
                MessageBox.showinfo("Success", "Successfully Login")
                global master_user
                master_user=e1.get()
                #print(master_user)
                conn.close()
                w.destroy()
                p_home()



    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    Frame(w, width=250, height=400, bg='white').place(x=50, y=50)

    l1 = Label(w, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)

    # e1 entry for username entry
    e1 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=230)

    # e2 entry for password entry
    e2 = Entry(w, width=20, border=0, show='*')
    e2.config(font=l)
    e2.place(x=80, y=310)

    l2 = Label(w, text='Password', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=280)

    ###lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)

    img = Image.open('p_icon2.png')
    test = ImageTk.PhotoImage(img)
    image_label = Label(w, width=121, height=137,bg='white')
    image_label.configure(image=test)
    image_label.image = test
    image_label.place(x=110, y=60)

    bttn(w,100, 350, 'L O G I N', 'white', '#994422', p_verify)
    bttn(w,100, 400, 'R E G I S T E R', 'white', '#994422', reg)

    w.mainloop






# ----------------------------------ADMIN LOGIN-----------------------------------------

def ad_log():
    w = Toplevel()
    w.geometry('350x500+1220+260')
    w.title('A D M I N   L O G I N ')

    w.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    Frame(w, width=250, height=400, bg='white').place(x=50, y=50)

    l1 = Label(w, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)

    # e1 entry for username entry
    e1 = Entry(w, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=230)

    # e2 entry for password entry
    e2 = Entry(w, width=20, border=0, show='*')
    e2.config(font=l)
    e2.place(x=80, y=310)

    l2 = Label(w, text='Password', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=280)

    ###lineframe on entry

    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w, width=180, height=2, bg='#141414').place(x=80, y=252)

    img = Image.open('a_icon.jpg')
#    img = img.resize((200, 200), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(img)
    image_label = Label(w, width=121, height=137)
    image_label.configure(image=test)
    image_label.image = test
    image_label.place(x=115, y=50)

    # Command
    def cmd():
        if e1.get() == 'Admin' and e2.get() == 'admin':
            MessageBox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
            w.destroy()
            ad_home()

        else:
            MessageBox.showwarning("LOGIN FAILED", "        PLEASE TRY AGAIN        ")



    bttn(w,100, 350, 'L O G I N', 'white', '#994422', cmd)
    w.mainloop()


# ----------------------------------DOCTOR REGISTER-----------------------------------------

def d_reg():

        w = Toplevel()
        w.geometry('350x750+1050+100')
        w.title('doctor reg')
        w.resizable(0, 0)
        # Making gradient frame
        j = 0
        r = 10
        for i in range(100):
            c = str(222222 + r)
            Frame(w, width=10, height=750, bg="#" + c).place(x=j, y=0)
            j = j + 10
            r = r + 1

        def add_record():
            name_e = e2.get()
            user_e = e1.get()
            contact_e = e6.get()
            age_e = e5.get()
            gender_e = gender.get()
            password_e = e3.get()
            repassword_e = e4.get()
            degree_e = selected.get()
            if (
                    name_e == "" or user_e == "" or contact_e == "" or age_e == "" or password_e == "" or repassword_e == ""):
                MessageBox.showinfo("Insert Status", "All fields are required")
            elif (password_e != repassword_e):
                MessageBox.showinfo("Insert Status", "Password and re-enter password does not match")
            elif (age_e.isdecimal() or contact_e.isdecimal()):

                conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")

                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO d_register VALUES('" + name_e + "','" + user_e + "','" + contact_e + "','" + age_e + "','" + gender_e + "','" + password_e + "','" + repassword_e + "','" + degree_e + "')")
                cursor.execute("commit");
                MessageBox.showinfo("Insert Status", "Inserted successfully");
                cursor.execute("INSERT INTO d_login VALUES('" + user_e + "','" + password_e + "')")
                cursor.execute("commit");
                conn.close()

        Frame(w, width=250, height=650, bg='white').place(x=50, y=50)
        # label for username
        l1 = Label(w, text='Username', bg='white')
        l = ('Consolas', 13)
        l1.config(font=l)
        l1.place(x=80, y=70)

        # e1 entry for username entry
        e1 = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        e1.config(font=l)
        e1.place(x=80, y=100)

        # label for name
        l2 = Label(w, text='Name', bg='white')
        l = ('Consolas', 13)
        l2.config(font=l)
        l2.place(x=80, y=140)

        # e2 entry for username entry
        e2 = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        e2.config(font=l)
        e2.place(x=80, y=170)

        # e3 entry for password entry
        e3 = Entry(w, width=20, border=0, show='*')
        e3.config(font=l)
        e3.place(x=80, y=240)

        # label for password
        l3 = Label(w, text='Password', bg='white')
        l = ('Consolas', 13)
        l3.config(font=l)
        l3.place(x=80, y=210)

        # label for re enter password
        l4 = Label(w, text='Re Enter Password', bg='white')
        l = ('Consolas', 13)
        l4.config(font=l)
        l4.place(x=80, y=280)

        # e4 entry for re password entry
        e4 = Entry(w, width=20, border=0, show='*')
        e4.config(font=l)
        e4.place(x=80, y=310)

        l5 = Label(w, text='Age', bg='white')
        l = ('Consolas', 13)
        l5.config(font=l)
        l5.place(x=80, y=340)

        # e5 entry for age entry
        e5 = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        e5.config(font=l)
        e5.place(x=80, y=380)

        l6 = Label(w, text='Contact', bg='white')
        l = ('Consolas', 13)
        l6.config(font=l)
        l6.place(x=80, y=410)

        # e6 entry for contact entry
        e6 = Entry(w, width=20, border=0)
        l = ('Consolas', 13)
        e6.config(font=l)
        e6.place(x=80, y=450)

        l6 = Label(w, text='Gender', bg='white')
        l = ('Consolas', 13)
        l6.config(font=l)
        l6.place(x=80, y=480)

        gender = StringVar(w)
        gender.set(NONE)
        gender_rbm = Radiobutton(w, width=7, font='Consolas', variable=gender, text="Male", value='Male', bg='white')
        gender_rbm.place(x=60, y=510)
        gender_rbf = Radiobutton(w, width=7, font='Consolas', variable=gender, text="Female", value="Female",
                                 bg='white')
        gender_rbf.place(x=160, y=510)

        # COMBOBOX
        selected = StringVar(w)
        selected.set(' SELECT PRACTICE ')
        degree = ['      GENERAL PHYSICIAN      ', '      ENT     ', '      ORTHOPEDIC     ', '      DENTIST      ']
        option = OptionMenu(w, selected, *degree)
        option.place(x=80, y=570)


        # buttons
        bttn(w, 80, 640, 'S U B M I T', 'white', '#994422', add_record)

        ###lineframe on entry

        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=122)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=192)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=262)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=332)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=402)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=472)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=550)
        Frame(w, width=180, height=2, bg='#141414').place(x=80, y=620)

        w.mainloop()




# -----------------------------DOCTOR LOGIN-------------------------------

def doc_log():
    w1 = Toplevel()
    w1.geometry('350x500+1220+260')
    w1.title('D O C T O R   L O G I N ')
    w1.resizable(0, 0)

    # Making gradient frame
    j = 0
    r = 10
    for i in range(100):
        c = str(222222 + r)
        Frame(w1, width=10, height=500, bg="#" + c).place(x=j, y=0)
        j = j + 10
        r = r + 1

    Frame(w1, width=250, height=400, bg='white').place(x=50, y=50)

    l1 = Label(w1, text='Username', bg='white')
    l = ('Consolas', 13)
    l1.config(font=l)
    l1.place(x=80, y=200)

    # e1 entry for username entry
    e1 = Entry(w1, width=20, border=0)
    l = ('Consolas', 13)
    e1.config(font=l)
    e1.place(x=80, y=230)

    # e2 entry for password entry
    e2 = Entry(w1, width=20, border=0, show='*')
    e2.config(font=l)
    e2.place(x=80, y=310)

    l2 = Label(w1, text='Password', bg='white')
    l = ('Consolas', 13)
    l2.config(font=l)
    l2.place(x=80, y=280)

    ###lineframe on entry

    Frame(w1, width=180, height=2, bg='#141414').place(x=80, y=332)
    Frame(w1, width=180, height=2, bg='#141414').place(x=80, y=252)

    img = Image.open('d_icon3.png')
    test = ImageTk.PhotoImage(img)
    image_label = Label(w1, width=121, height=137, bg='white')
    image_label.configure(image=test)
    image_label.image = test
    image_label.place(x=110, y=60)

   # Command
    def d_verify():

        if (e1 == "" or e2 == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")
        else:
            conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
            cursor = conn.cursor()
            cursor.execute("select * from d_login where username=%s and password = %s",
                           (e1.get(), e2.get()))
            row = cursor.fetchone()
            if row == None:
                MessageBox.showinfo("Insert Status", "Invalid password or username")
            else:
                MessageBox.showinfo("Success", "Successfully Login")
                global master_doctor
                master_doctor = e1.get()
                conn.close()
                w1.destroy()
                d_home()



    bttn(w1,100, 375, 'L O G I N', 'white', '#994422',d_verify)
    w1.mainloop









# -------------------------------HOME PAGE----------------------------------------

def home():

    root1 = Tk()
    root1.resizable(False, False)
    root1.geometry("1535x780+200+100")
    root1.title("HOME")

    canvas1 = Canvas(root1, width=1535, height=775)
    canvas1.pack()

    imagea = Image.open("background21.jpg")
    imageb = ImageTk.PhotoImage(imagea)

    label = Label(root1, image=imageb)
    label.image = imageb

    canvas1.create_image(765, 385, image=imageb)
    tk_img1 = ImageTk.PhotoImage(file="d_icon2.png")
    canvas1.create_image(500, 400, anchor='nw', image=tk_img1)
    tk_img2 = ImageTk.PhotoImage(file="p_icon1.png")
    canvas1.create_image(500, 105, anchor='nw', image=tk_img2)
    bttn(root1, 540, 350, 'P A T I E N T', 'black', '#75E6DA', p_log)
    bttn(root1, 550, 650, 'D O C T O R', 'black', '#75E6DA', doc_log)
    bttn(root1, 1350, 35, 'A D M I N', 'black', '#75E6DA', ad_log)




    root1.mainloop()

def p_sym():


    #print(master_user)
    def submit1():
        history=[]
        sel_symp=[]


        if CheckVar1.get() == "sore throat":
            #print(CheckVar1.get())
            sel_symp.append(CheckVar1.get())
        if CheckVar2.get() == "dry cough":
            #print(CheckVar2.get())
            sel_symp.append(CheckVar2.get())
        if CheckVar3.get() == "runny nose":
            #print(CheckVar3.get())
            sel_symp.append(CheckVar3.get())
        if CheckVar4.get() == "joint/muscle pain":
            #print(CheckVar4.get())
            sel_symp.append(CheckVar4.get())
        if CheckVar5.get() == "inflammed joints":
            #print(CheckVar5.get())
            sel_symp.append(CheckVar5.get())
        if CheckVar6.get() == "grating of joints":
            #print(CheckVar6.get())
            sel_symp.append(CheckVar6.get())
        if CheckVar7.get() == "shoulder tension":
            #print(CheckVar7.get())
            sel_symp.append(CheckVar7.get())
        if CheckVar8.get() == "loss of appetite":
            #print(CheckVar8.get())
            sel_symp.append(CheckVar8.get())
        if CheckVar9.get() == "sensitive to light":
            #print(CheckVar9.get())
            sel_symp.append(CheckVar9.get())
        if CheckVar10.get() == "mouth swelling":
            #print(CheckVar10.get())
            sel_symp.append(CheckVar10.get())
        if CheckVar11.get() == "tooth bleeding":
            #print(CheckVar11.get())
            sel_symp.append(CheckVar11.get())
        if CheckVar12.get() == "tooth pain":
            #print(CheckVar12.get())
            sel_symp.append(CheckVar12.get())





        med_cond=" ".join(history)
        #print(history)
        conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
        my_symp=" ".join(sel_symp)

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO symptoms(p_name,symp) VALUES( '" + master_user + "','"  + my_symp + "')")
        cursor.execute("commit");


        MessageBox.showinfo("Insert Status", "Inserted successfully");
        root.destroy()
        p_desc()

        conn.close()




    root = Toplevel()
    root.geometry("1355x750+200+100")
    root.title("Choose symptoms")

    # Frame1
    frame1 = Frame(root, width=1355, height=50, bg="#D4F1F4")
    frame1.place(x=0, y=0)
    patient_label = Label(frame1, text="USERNAME:"+master_user, width=20, bg="#D4F1F4", font='Verdana')
    patient_label.place(x=10, y=10)
    '''patient_quit = Button(frame1, text="Back", anchor='w', width=10, font='Verdana', activebackground="red",
                          command=root.quit, cursor="hand2", bg="#d4d4d4")
    patient_quit.place(x=1250, y=10)'''
    # Frame2

    frame2 = Frame(root, width=1355, height=904)
    frame2.place(x=0, y=50)
    patient_text = Label(root, text="Choose a Symptom:", font='Verdana', bg="#75E6DA", fg="black")
    patient_text.place(x=10, y=50)
    im = Image.open("d_prec1.jpg")
    pic1 = ImageTk.PhotoImage(im)
    l2 = Label(frame2, image=pic1)
    l2.place(x=-50, y=-20)

    def limit():
        if CheckVar1.get() == "sore throat" or CheckVar2.get() == "dry cough" or CheckVar3.get() == "runny nose":
            C4.config(state=DISABLED)
            C5.config(state=DISABLED)
            C6.config(state=DISABLED)
            C7.config(state=DISABLED)
            C8.config(state=DISABLED)
            C9.config(state=DISABLED)
            C10.config(state=DISABLED)
            C11.config(state=DISABLED)
            C12.config(state=DISABLED)
            global doctor_type
            doctor_type='      ENT     '
        elif CheckVar4.get() == "joint/muscle pain" or CheckVar5.get() == "inflammed joints" or CheckVar6.get() == "grating of joints":
            C1.config(state=DISABLED)
            C2.config(state=DISABLED)
            C3.config(state=DISABLED)
            C7.config(state=DISABLED)
            C8.config(state=DISABLED)
            C9.config(state=DISABLED)
            C10.config(state=DISABLED)
            C11.config(state=DISABLED)
            C12.config(state=DISABLED)

            doctor_type='      ORTHOPEDIC     '
        elif CheckVar7.get() == "shoulder tension" or CheckVar8.get() == "loss of appetite" or CheckVar9.get() == "sensitive to light":
            C4.config(state=DISABLED)
            C5.config(state=DISABLED)
            C6.config(state=DISABLED)
            C1.config(state=DISABLED)
            C2.config(state=DISABLED)
            C3.config(state=DISABLED)
            C10.config(state=DISABLED)
            C11.config(state=DISABLED)
            C12.config(state=DISABLED)

            doctor_type='      GENERAL PHYSICIAN      '
        elif CheckVar10.get() == "mouth swelling" or CheckVar11.get() == "tooth bleeding" or CheckVar12.get() == "tooth pain":
            C4.config(state=DISABLED)
            C5.config(state=DISABLED)
            C6.config(state=DISABLED)
            C7.config(state=DISABLED)
            C8.config(state=DISABLED)
            C9.config(state=DISABLED)
            C1.config(state=DISABLED)
            C2.config(state=DISABLED)
            C3.config(state=DISABLED)

            doctor_type='      DENTIST      '
        else:
            pass

    # Button color change
    off_color = "#6AD5E7"
    on_color = "#4169E1"

    def on_check():
        if CheckVar1.get() == "sore throat":
            C1["bg"] = on_color
        else:
            C1["bg"] = off_color
        if CheckVar2.get() == "dry cough":
            C2["bg"] = on_color
        else:
            C2["bg"] = off_color
        if CheckVar3.get() == "runny nose":
            C3["bg"] = on_color
        else:
            C3["bg"] = off_color
        if CheckVar4.get() == "joint/muscle pain":
            C4["bg"] = on_color
        else:
            C4["bg"] = off_color
        if CheckVar5.get() == "inflammed joints":
            C5["bg"] = on_color
        else:
            C5["bg"] = off_color
        if CheckVar6.get() == "grating of joints":
            C6["bg"] = on_color
        else:
            C6["bg"] = off_color
        if CheckVar7.get() == "shoulder tension":
            C7["bg"] = on_color
        else:
            C7["bg"] = off_color
        if CheckVar8.get() == "loss of appetite":
            C8["bg"] = on_color
        else:
            C8["bg"] = off_color
        if CheckVar9.get() == "sensitive to light":
            C9["bg"] = on_color
        else:
            C9["bg"] = off_color
        if CheckVar10.get() == "mouth swelling":
            C10["bg"] = on_color
        else:
            C10["bg"] = off_color
        if CheckVar11.get() == "tooth bleeding":
            C11["bg"] = on_color
        else:
            C11["bg"] = off_color
        if CheckVar12.get() == "tooth pain":
            C12["bg"] = on_color
        else:
            C12["bg"] = off_color

    # deselect
    def des():
        C1.config(state=NORMAL)
        C1.deselect()
        C1["bg"] = off_color
        C2.config(state=NORMAL)
        C2.deselect()
        C2["bg"] = off_color
        C3.config(state=NORMAL)
        C3.deselect()
        C3["bg"] = off_color
        C4.config(state=NORMAL)
        C4.deselect()
        C4["bg"] = off_color
        C5.config(state=NORMAL)
        C5.deselect()
        C5["bg"] = off_color
        C6.config(state=NORMAL)
        C6.deselect()
        C6["bg"] = off_color
        C7.config(state=NORMAL)
        C7.deselect()
        C7["bg"] = off_color
        C8.config(state=NORMAL)
        C8.deselect()
        C8["bg"] = off_color
        C9.config(state=NORMAL)
        C9.deselect()
        C9["bg"] = off_color
        C10.config(state=NORMAL)
        C10.deselect()
        C10["bg"] = off_color
        C11.config(state=NORMAL)
        C11.deselect()
        C11["bg"] = off_color
        C12.config(state=NORMAL)
        C12.deselect()
        C12["bg"] = off_color

    CheckVar1 = StringVar()
    CheckVar2 = StringVar()
    CheckVar3 = StringVar()
    CheckVar4 = StringVar()
    CheckVar5 = StringVar()
    CheckVar6 = StringVar()
    CheckVar7 = StringVar()
    CheckVar8 = StringVar()
    CheckVar9 = StringVar()
    CheckVar10 = StringVar()
    CheckVar11 = StringVar()
    CheckVar12 = StringVar()

    # image
    img1 = Image.open("sore.jpeg")
    img9_re1 = ImageTk.PhotoImage(img1)

    img2 = Image.open("dry.jpeg")
    img9_re2 = ImageTk.PhotoImage(img2)

    img3 = Image.open("runny.jpeg")
    img9_re3 = ImageTk.PhotoImage(img3)

    img4 = Image.open("joint.jpeg")
    img9_re4 = ImageTk.PhotoImage(img4)

    img5 = Image.open("inflammed.jpeg")
    img9_re5 = ImageTk.PhotoImage(img5)

    img6 = Image.open("grated.jpeg")
    img9_re6 = ImageTk.PhotoImage(img6)

    img7 = Image.open("shoulder.jpeg")
    img9_re7 = ImageTk.PhotoImage(img7)

    img8 = Image.open("apetite.jpeg")
    img9_re8 = ImageTk.PhotoImage(img8)

    img9 = Image.open("light.jpeg")
    img9_re9 = ImageTk.PhotoImage(img9)

    img10 = Image.open("mouth.jpeg")
    img9_re10 = ImageTk.PhotoImage(img10)

    img11 = Image.open("t_bleed.jpeg")
    img9_re11 = ImageTk.PhotoImage(img11)

    img12 = Image.open("tooth.jpeg")
    img9_re12 = ImageTk.PhotoImage(img12)





    def bot():
        on_check()
        limit()

    # ENT
    C1 = Checkbutton(frame2, height=170, width=280, variable=CheckVar1, onvalue="sore throat", offvalue=0,
                     cursor="hand2", activebackground="#23527c", image=img9_re1, bg=off_color, command=bot)
    C1.place(x=0, y=28)
    C2 = Checkbutton(frame2, variable=CheckVar2, height=170, width=280, cursor="hand2", onvalue="dry cough", offvalue=0,
                     command=bot, image=img9_re2, bg=off_color, activebackground="#23527c")
    C2.place(x=0, y=220)
    C3 = Checkbutton(frame2, variable=CheckVar3, onvalue="runny nose", offvalue=0, height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re3, activebackground="#23527c")
    C3.place(x=0, y=410)
    # Orthopedic
    C4 = Checkbutton(frame2, variable=CheckVar4, onvalue="joint/muscle pain", offvalue=0, height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re4, activebackground="#23527c")
    C4.place(x=320, y=28)
    C5 = Checkbutton(frame2, variable=CheckVar5, onvalue="inflammed joints", offvalue=0, height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re5, activebackground="#23527c")
    C5.place(x=320, y=220)
    C6 = Checkbutton(frame2, variable=CheckVar6, onvalue="grating of joints", offvalue=0, height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re6, activebackground="#23527c")
    C6.place(x=320, y=410)
    #
    C7 = Checkbutton(frame2, variable=CheckVar7, onvalue="shoulder tension", offvalue="", height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re7, activebackground="#23527c")
    C7.place(x=640, y=28)
    C8 = Checkbutton(frame2, variable=CheckVar8, onvalue="loss of appetite", offvalue="", height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re8, activebackground="#23527c")
    C8.place(x=640, y=220)
    C9 = Checkbutton(frame2, variable=CheckVar9, onvalue="sensitive to light", offvalue="", height=170, width=280,
                     cursor="hand2", command=bot, bg=off_color, image=img9_re9, activebackground="#23527c")
    C9.place(x=640, y=410)
    # BDS(Bachlor of Dental Sergon)
    C10 = Checkbutton(frame2, variable=CheckVar10, onvalue="mouth swelling", offvalue=0, height=170, width=280,
                      cursor="hand2", command=bot, bg=off_color, image=img9_re10, activebackground="#23527c")
    C10.place(x=960, y=28)
    C11 = Checkbutton(frame2, variable=CheckVar11, onvalue="tooth bleeding", offvalue=0, height=170, width=280,
                      cursor="hand2", command=bot, bg=off_color, image=img9_re11, activebackground="#23527c")
    C11.place(x=960, y=220)
    C12 = Checkbutton(frame2, variable=CheckVar12, onvalue="tooth pain", offvalue=0, height=170, width=280,
                      cursor="hand2", command=bot, bg=off_color, image=img9_re12, activebackground="#23527c")
    C12.place(x=960, y=410)
    # deselect
    Deselect = Button(root, text="Deselect all", activebackground="red", font='Verdana', bg="#189AB4", fg="#141414",
                      command=des, cursor="hand2")
    Deselect.place(x=1240, y=650)

    sub2 = Button(frame2, text="SUBMIT", anchor='w', width=10, font='Verdana', activebackground="red",
                  cursor="hand2", bg="#189AB4", fg="#141414", command=submit1)
    sub2.place(x=1240, y=665)


    C1.deselect()
    C2.deselect()
    C3.deselect()
    C4.deselect()
    C5.deselect()
    C6.deselect()
    C7.deselect()
    C8.deselect()
    C9.deselect()
    C10.deselect()
    C11.deselect()
    C12.deselect()
    root.mainloop()




    #print(master_user)
    root.mainloop()



def d_advice():
    window = Toplevel()
    #ws.state("zoomed")
    window.title(string='Doctor advice')
    window.geometry('1000x700+200+100')

    frame3 = Frame(master=window,height=57,bg="#D4F1F4" )
    frame3.pack(fill=BOTH)

    frame2 = Frame(master=window,height=1000, bg="white")
    frame2.pack(fill=BOTH,side=LEFT,expand=True)

    image=Image.open('medical.jpg')
    pic1=ImageTk.PhotoImage(image)

    label1 = Label(frame2,height=630,width=1382,image=pic1)
    label1.place(x=0,y=0)

    lss = [doctor_ka_patient]

    conn1 = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    cursor = conn1.cursor()
    cursor.execute("SELECT p_comments FROM symptoms WHERE p_name=%s",lss)
    comments = cursor.fetchall()
    final_comments = organizer(comments)
    #print(final_comments)

    conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    crsr = conn.cursor()
    crsr.execute("SELECT age FROM p_register WHERE username='"+doctor_ka_patient+"'")
    uage = crsr.fetchall()
    crsr1 = conn.cursor()
    crsr1.execute("SELECT gender FROM p_register WHERE username='" + doctor_ka_patient + "'")
    ugender = crsr1.fetchall()
    crsr2 = conn.cursor()
    crsr2.execute("SELECT symp FROM symptoms WHERE p_name='" + doctor_ka_patient + "' and doctor_name='"+ master_doctor + "'")
    usympt = crsr.fetchall()
    final_age = organizer(uage)
    final_gender = organizer(ugender)

    try:
        crsr.fetchall()  # fetch (and discard) remaining rows
    except sq.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    crsr.execute("SELECT username FROM p_login")
    conn.close()

    try:
        cursor.fetchall()  # fetch (and discard) remaining rows
    except sq.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    cursor.execute("SELECT p_comments FROM symptoms WHERE p_name=%s",lss)
    conn1.close()

    def add():
        med = textbox3.get()
        conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO medicine VALUES('" + doctor_ka_patient + "','" + master_doctor + "','" + med + "')")
        cursor.execute("commit")
        MessageBox.showinfo("Insert Status", "Inserted successfully")
        textbox3.delete(0,END)


    def submit():
        desc = textbox2.get(1.0, "end-1c")
        #print(desc)
        #print(master_user)
        conn1 = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
        cursor = conn1.cursor()
        cursor.execute(
            "UPDATE symptoms set d_comments='" + desc + "' where p_name='" + doctor_ka_patient + "'AND doctor_name='" + master_doctor + "'")
        cursor.execute("commit")
        MessageBox.showinfo("Update Status", "Updated successfully")
        conn1.close()
        window.destroy()


    label2 = Label(frame3,fg='white',text='DOCTOR  PRESCRIPTION',font=("Arial",16),bg='blue')
    label2.place(x=350,y=10)

    label6 = Label(frame2,fg='black',text='Patient Details : ',font=("Arial",12),bg='#40c4c6')
    label6.place(x=582,y=36)

    label7 = Label(frame2,fg='black',text="Name : ",font=("Arial",12),bg='#40c4c6')
    label7.place(x=582,y=70)

    label8 = Label(frame2,fg='black',text='Age : ',font=("Arial",12),bg='#40c4c6')
    label8.place(x=582,y=106)

    label9 = Label(frame2,fg='black',text='Gender : ',font=("Arial",12),bg='#40c4c6')
    label9.place(x=730,y=106)

    label10 = Label(frame2,fg='black',text=doctor_ka_patient,font=("Arial",12),bg='#40c4c6')
    label10.place(x=640,y=70)

    label11 = Label(frame2,fg='black',text=final_age,font=("Arial",12),bg='#40c4c6')
    label11.place(x=628,y=106)

    label12 = Label(frame2,fg='black',text=final_gender,font=("Arial",12),bg='#40c4c6')
    label12.place(x=796,y=106)

    label13 = Label(frame2, fg='black', text="Symptoms : ", font=("Arial", 12), bg='#40c4c6')
    label13.place(x=582, y=144)

    label14 = Label(frame2, fg='black', text=usympt, font=("Arial", 12), bg='#40c4c6', width=34)
    label14.place(x=674, y=144)

    image=Image.open('patient_des.jpeg')
    pic3=ImageTk.PhotoImage(image)

    label3 = Label(frame2,height=261,width=476,image=pic3)
    label3.place(x=60,y=30)

    textbox1 = Label(frame2,width=41,font=("Arial",14),bg='white',border=0,text=final_comments)
    textbox1.place(x=79,y=74)

    image=Image.open('doc_comments.png')
    pic4=ImageTk.PhotoImage(image)

    label4 = Label(frame2,height=265,width=480,image=pic4)
    label4.place(x=60,y=330)

    textbox2 = Text(frame2,width=41,height=9,font=("Arial",14),bg='white',border=0)
    textbox2.place(x=79,y=374)

    image=Image.open('medicine.png')
    pic5=ImageTk.PhotoImage(image)

    label5 = Label(frame2, height=390, width=372, image=pic5)
    label5.place(x=580, y=200)

    textbox3 = Entry(frame2, width=31, font=("Arial", 14), bg='white', border=0)
    textbox3.place(x=597, y=240)

    '''l1 = ["Vrushal", "Joshua", "Shruti", "Yash THE Great"]
    ttk.Label(frame2, text="")
    vari = ttk.Combobox(frame2, height=30, width=52, values=l1)
    vari.place(x=600, y=400)'''

    myButton5=Button(frame3,text="Back",fg='black',bg='white',activebackground="#40c4c6",cursor="hand2",border=0)
    myButton5.place(x=40,y=14)

    Button3=Button(frame2,width=5,height=1,text="ADD",font=("Arial",10),bg='white',activebackground="#40c4c6",cursor="hand2",command=add)
    Button3.place(x=720,y=540)

    '''Button4 = Button(frame2, width=7, height=1, text="DELETE", font=("Arial", 10), bg='white',
                     activebackground="#40c4c6", cursor="hand2")
    Button4.place(x=770, y=540)'''

    button_submit=Button(frame2,width=10,height=1,text="submit",command=submit,font=("Arial", 10))
    button_submit.place(x=750,y=600)

    window.mainloop()

#----------------------------Patient Home---------------------------

def p_home():

    ws = Toplevel()
    #ws.state("zoomed")
    ws.title(string='Patient home')
    ws.geometry('1380x750+200+100')
    ws.resizable(False,False)

    frame3 = Frame(master=ws, height=57, bg="#D4F1F4")
    frame3.pack(fill=BOTH)

    frame2 = Frame(master=ws, height=1000, bg="white")
    frame2.pack(fill=BOTH, side=LEFT, expand=True)

    image = Image.open('medical.jpg')
    pic1 = ImageTk.PhotoImage(image)

    label1 = Label(frame2, height=380, width=1379, image=pic1)
    label1.place(x=0, y=0)

    image = Image.open('p3.png')
    pic2 = ImageTk.PhotoImage(image)

    label2 = Label(frame2, height=261, width=565, image=pic2)
    label2.place(x=730, y=60)

    image = Image.open('I2.png')
    pic3 = ImageTk.PhotoImage(image)

    MyButton1 = Button(frame2, height=245, width=316, image=pic3, border=0,command=prev_consult,cursor="hand2")
    MyButton1.place(x=130, y=360)

    image = Image.open('I1.png')
    pic4 = ImageTk.PhotoImage(image)

    MyButton2 = Button(frame2, height=245, width=316, image=pic4, border=0,command=p_sym,cursor="hand2")
    MyButton2.place(x=500, y=360)

    image = Image.open('I3.jpeg')
    pic5 = ImageTk.PhotoImage(image)

    MyButton3 = Button(frame2, height=245, width=316, image=pic5, border=0,command=lab_test,cursor="hand2")
    MyButton3.place(x=870, y=360)



    ws.mainloop()

def lab_test():
    ws = Toplevel()
    ws.geometry('1380x750+200+100')
    ws.resizable(False, False)

    frame3 = Frame(master=ws, height=38, bg="light blue")
    frame3.pack(fill=BOTH)

    frame1 = Frame(master=ws, width=1000, bg="white")
    frame1.pack(fill=BOTH, side=RIGHT, expand=True)

    def n_back():
        ws.destroy()

    myButton2 = Button(frame3, text="Back", fg='black', bg='white',command=n_back)
    myButton2.place(x=6, y=5)

    image = Image.open('1.png')
    pic1 = ImageTk.PhotoImage(image)

    label1 = Label(frame1, height=218, width=290, image=pic1)
    label1.place(x=40, y=9)

    image = Image.open('2.png')
    pic2 = ImageTk.PhotoImage(image)

    label2 = Label(frame1, height=215, width=290, image=pic2)
    label2.place(x=365, y=10)

    image = Image.open('3.png')
    pic3 = ImageTk.PhotoImage(image)

    label3 = Label(frame1, height=218, width=290, image=pic3)
    label3.place(x=700, y=10)

    image = Image.open('4.png')
    pic4 = ImageTk.PhotoImage(image)

    label4 = Label(frame1, height=218, width=290, image=pic4)
    label4.place(x=1035, y=10)

    image = Image.open('5.png')
    pic5 = ImageTk.PhotoImage(image)

    label5 = Label(frame1, height=218, width=290, image=pic5)
    label5.place(x=40, y=226)

    image = Image.open('6.png')
    pic6 = ImageTk.PhotoImage(image)

    label6 = Label(frame1, height=218, width=290, image=pic6)
    label6.place(x=365, y=228)

    image = Image.open('7.png')
    pic7 = ImageTk.PhotoImage(image)

    label7 = Label(frame1, height=218, width=290, image=pic7)
    label7.place(x=700, y=228)

    image = Image.open('8.png')
    pic8 = ImageTk.PhotoImage(image)

    label8 = Label(frame1, height=218, width=290, image=pic8)
    label8.place(x=1035, y=228)

    image = Image.open('9.png')
    pic9 = ImageTk.PhotoImage(image)

    label9 = Label(frame1, height=219, width=290, image=pic9)
    label9.place(x=40, y=446)

    image = Image.open('10.png')
    pic10 = ImageTk.PhotoImage(image)

    label10 = Label(frame1, height=219, width=290, image=pic10)
    label10.place(x=365, y=446)

    image = Image.open('11.png')
    pic11 = ImageTk.PhotoImage(image)

    label11 = Label(frame1, height=219, width=288, image=pic11)
    label11.place(x=700, y=446)

    image = Image.open('12.png')
    pic12 = ImageTk.PhotoImage(image)

    label12 = Label(frame1, height=219, width=288, image=pic12)
    label12.place(x=1035, y=446)

    ws.mainloop()

def d_home():
    window = Toplevel()

    # setting window size
    window.resizable(False,False)
    window.geometry("1380x700+200+100")

    #window.state("zoomed")

    frame3 = Frame(master=window, height=57, bg="#D4F1F4")
    frame3.pack(fill=BOTH)

    frame2 = Frame(master=window, height=1000, bg="white")
    frame2.pack(fill=BOTH, side=LEFT, expand=True)

    image = Image.open('medical.jpg')
    pic1 = ImageTk.PhotoImage(image)

    label1 = Label(frame2, height=410, width=1379, image=pic1)
    label1.place(x=0, y=0)

    image = Image.open('d2.png')
    pic2 = ImageTk.PhotoImage(image)

    label2 = Label(frame2, height=222, width=518, image=pic2)
    label2.place(x=130, y=300)

    image = Image.open('add.png')
    pic3 = ImageTk.PhotoImage(image)

    label3 = Label(frame2, height=453, width=419, image=pic3)
    label3.place(x=867, y=70)

    '''label4 = Label(frame3,text=master_doctor,height=1,width=20)
    label4.place(x=400, y=20)'''

    # label username to be fetched from database
    """Label1=Label(frame2, text="username", font="arial" )
    Label1.place(x=30,y=20)"""



    # logout
    """Button(window,width=10,height=2,text="Logout",command= some_cmd1).place(x=300,y=20)"""
    '''myButton4 = Button(frame3, text="Log Out", fg='black', bg='white', activebackground="#40c4c6", cursor="hand2",
                       border=0)
    myButton4.place(x=1260, y=14)'''

    '''myButton5 = Button(frame3, text="Back", fg='black', bg='white', activebackground="#40c4c6", cursor="hand2",
                       border=0)'''
    #myButton5.place(x=40, y=14)

    # list l1 to be featched from database

    '''conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")

    cursor = conn.cursor(buffered=True)
    cursor.execute(
        "SELECT p_name FROM symptoms where  doctor_name==%s",label4.cget)
    cursor.execute("commit");
    p_user = cursor.fetchall()
    print(p_user)
    MessageBox.showinfo("Insert Status", "Inserted successfully");
    conn.close()
    print(p_user)'''
    lst=[]

    lst.append(master_doctor)
    #print(lst)
    conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    cursor = conn.cursor()
    cursor.execute("SELECT p_name FROM symptoms WHERE doctor_name=%s",lst)
    p_name= cursor.fetchall()

    fin_lst=organizer(p_name)
    '''print(p_name)
    MessageBox.showinfo("Insert Status", "Inserted successfully");'''
    conn.close()








    ttk.Label(frame2, text="")
    vari = ttk.Combobox(frame2, height=30, width=40, values=fin_lst)
    vari.place(x=948, y=190)

    def next_page():
        global doctor_ka_patient
        doctor_ka_patient = vari.get()
        #print("*********")
        #print(doctor_ka_patient)
        window.destroy()






        d_advice()

    # proceed button
    Button3 = Button(frame2, width=10, height=2, text="Submit", bg='white', activebackground="#40c4c6",
                     cursor="hand2",command=next_page)
    Button3.place(x=1042, y=530)

    window.mainloop()
#def organize2(train):



def prev_consult():

    ws = Toplevel()
    # ws.state("zoomed")
    ws.title(string='abc')
    ws.geometry('960x750+200+100')

    frame3 = Frame(master=ws, height=57, bg="#D4F1F4" )
    frame3.pack(fill=BOTH)

    frame2 = Frame(master=ws, height=1000, bg="white")
    frame2.pack(fill=BOTH, side=LEFT, expand=True)

    image = Image.open('medical.jpg')
    pic1 = ImageTk.PhotoImage(image)

    label1 = Label(frame2, height=630, width=1382, image=pic1)
    label1.place(x=0, y=0)

    image = Image.open('my.png')
    pic2 = ImageTk.PhotoImage(image)

    label2 = Label(frame2, height=492, width=885, image=pic2, bg='white')
    label2.place(x=30, y=60)

    label3 = Label(frame3, fg='black', text='PREVIOUS  CONSULTATION', font=("Arial", 16), bg="#D4F1F4")
    label3.place(x=350, y=10)

    # scbar = Scrollbar(frame2,orient=VERTICAL)
    textbox = Text(frame2,width=50,height=10,font=("Arial",18),  )
    # scbar.config(command=textbox.yview)
    # scbar.pack(side=RIGHT,fill=Y)
    lss=[master_user]
    conn1 = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    cursor = conn1.cursor()
    cursor.execute("SELECT d_comments FROM symptoms WHERE p_name=%s", lss)
    comments = cursor.fetchall()
    final_comments = organizer(comments)
    #print(final_comments)
    conn2 = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    cursor = conn1.cursor()
    cursor.execute("SELECT medicine FROM medicine WHERE p_name=%s", lss)
    med = cursor.fetchall()
    final_med=organizer(med)
    strn=""
    for element in final_med:
        strn=strn + element +"\n"

    #print(strn)



    label4=Label(frame2,bg='white',text="Doctor comments:",font=("Arial", 15,'bold'))
    label4.place(x=83,y=220)

    label5 = Label(frame2, bg='white', text="Medicines:", font=("Arial", 15,'bold'))
    label5.place(x=500, y=220)


    textbox = Text(frame2, width=30 , height=9 ,font=("Arial", 18), bg='white', border=2)
    textbox.place(x=83, y=245)

    textbox.insert(INSERT,final_comments)

    textbox2  = Text(frame2, width=28, height=9, font=("Arial", 18), bg='white', border=2)
    textbox2.place(x=500, y=245)

    textbox2.insert(INSERT,strn)
    def nw_cmd():
        ws.destroy()
    myButton5 = Button(frame3, text="Back", fg='black', bg='white', activebackground="#40c4c6", cursor="hand2",
                       border=0,command=nw_cmd)
    myButton5.place(x=40, y=14)
    textbox2.config(state=DISABLED)
    textbox.config(state=DISABLED)



    ws.mainloop()













    ''' textbox = Text(frame2, font=("Arial", 18), bg='white', border=0)
    textbox.place(x=83, y=210, height=40,width=60)

    myButton5 = Button(frame3, text="Back", fg='black', bg='white', activebackground="#40c4c6", cursor="hand2",
                       border=0)
    myButton5.place(x=40, y=14)

    ws.mainloop()'''


def organizer(l):

    fresh = []
    final = []
    for element in l:
        var = element
        for alph in var:
            if alph == "(" or alph == "," or alph == "`" or alph == "[" or alph == "'" or alph == ")" or alph=="" or alph=="]":
                pass
            else:
                fresh.append(alph)
        string = ''.join(str(item) for item in fresh)
        final.append(string)
        fresh = []
    return final


def ad_home():

    conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    crsr = conn.cursor()
    crsr.execute("SELECT username FROM p_login")
    uname = crsr.fetchall()
    final_user_p=organizer(uname)
    #print(final_user_p)



    try:
            crsr.fetchall()  # fetch (and discard) remaining rows
    except sq.errors.InterfaceError as ie:
            if ie.msg == 'No result set to fetch from.':
                # no problem, we were just at the end of the result set
                pass
            else:
                raise
    crsr.execute("SELECT username FROM p_login")
    conn.close()

    conn1 = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    cursor = conn1.cursor()
    cursor.execute("SELECT username FROM d_login")
    uname1 = cursor.fetchall()
    final_user_d=organizer(uname1)
    #print(final_user_d)

    try:
        cursor.fetchall()  # fetch (and discard) remaining rows
    except sq.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    cursor.execute("SELECT username FROM d_login")
    conn1.close()



    root1 = Toplevel()
    root1.resizable(False, False)
    root1.geometry("400x450+200+100")
    root1.title("ADMIN HOME")

    img = Image.open('d_prec.jpg')
    test = ImageTk.PhotoImage(img)
    image_label = Label(root1, bg='#ab23ff')
    image_label.configure(image=test)
    image_label.image = test
    image_label.pack()

    # label for list of patients
    lb1 = Label(root1, text='Patients:', bg="#99E7D1")
    l = ('Consolas', 13)
    lb1.config(font=l)
    lb1.place(x=60, y=50)

    # list l1 of patients to be featched from p_register/login table
    ttk.Label(root1, text="")
    vari1 = ttk.Combobox(root1, height=30, width=40, values=final_user_p)
    vari1.place(x=60, y=70)




    # label for list of doctors
    lb2 = Label(root1, text='Doctors:', bg='#99E7D1')
    l = ('Consolas', 13)
    lb2.config(font=l)
    lb2.place(x=60, y=170)

    # list l2 of doctors to be fetched from d_login table
    ttk.Label(root1, text="")
    vari = ttk.Combobox(root1, height=30, width=40, values=final_user_d).place(x=60, y=200)

    # label for register button
    lb2 = Label(root1, text='Register a new Doctor ->', bg='#99E7D1')
    l = ('Consolas', 13)
    lb2.config(font=l)
    lb2.place(x=60, y=300)

    bttn(root1, 90, 350, 'R E G I S T E R', 'black', '#00ccff', d_reg)


    root1.mainloop()


def p_desc():
    root = Toplevel()
    root.geometry("650x750+200+100")
    root.title("PATIENT Symptom")

    #print(doctor_type)
    #submit button
    def submit2():

        history = []


        if CheckVarb4.get() == "blood pressure":
            #print(CheckVarb4.get())
            history.append(CheckVarb4.get())
        if CheckVarb3.get() == "vertigo":
            #print(CheckVarb3.get())
            history.append(CheckVarb3.get())
        if CheckVarb2.get() == "stroke":
            #print(CheckVarb2.get())
            history.append(CheckVarb2.get())
        if CheckVarb1.get() == "asthma":
            #print(CheckVarb1.get())
            history.append(CheckVarb1.get())



        desc = p_message.get(1.0,"end-1c")
        d = selected.get()






        conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
        my_hist = " ".join(history)

        cursor = conn.cursor()
        cursor.execute(
            "UPDATE symptoms set medical_history='"+ my_hist + "', doctor_name='"+ d +"' where p_name='" +master_user+ "'")
        cursor.execute("commit")
        cursor.execute(
            "UPDATE symptoms set p_comments='" + desc + "' where p_name='" + master_user + "'AND doctor_name='"+ d +"'")
        cursor.execute("commit")
        MessageBox.showinfo("Update Status", "Updated successfully")
        conn.close()
        root.destroy()


        #------------------------------inserting patient comments in database---------------------------










    #fetching doctor name from doctor type
    conn = sq.connect(host="localhost", user="root", password="SOMEPASSWORD", database="health")
    crsr = conn.cursor()
    list0 = [doctor_type]
    crsr.execute(
        "select username from d_register where degree=%s", list0)
    uname = crsr.fetchall()
    #print(uname)
    final_user_p = organizer(uname)
    #print(final_user_p)


    try:
        crsr.fetchall()  # fetch (and discard) remaining rows
    except sq.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    crsr.execute(
        "select name from d_register where degree=%s", list0)
    conn.close()


    def destroyer():
        root.destroy()
    # Frame1

    frame1 = Frame(root, width=650, height=30, bg="#D4F1F4")
    frame1.place(x=0, y=0)
    patient_label = Label(frame1, text=master_user, width=10, font='Verdana', bg="#D4F1F4")
    patient_label.place(x=0, y=2)
    patient_quit = Button(frame1, text="Back", anchor='w', width=10, font='Verdana', activebackground="red",
                          command=destroyer, cursor="hand2", bg="#75E6DA", bd=4)
    patient_quit.place(x=555, y=0)
    # Frame2
    frame2 = Frame(root, width=650, height=800, bg="#189AB4")
    frame2.place(x=0, y=30)
    patient_text = Label(frame2, text="Choose a Doctor:", activebackground="#d6b600", font='Verdana', bg="#23527c",
                         fg="black")
    patient_text.place(x=0, y=10)
    im = Image.open("d_prec1.jpg")
    pic1 = ImageTk.PhotoImage(im)
    l2 = Label(frame2, image=pic1)
    l2.place(x=-50, y=-20)
    # COMBOBOX
    selected = StringVar(frame2)
    selected.set(' SELECT Doctor ')

    option = OptionMenu(frame2, selected, *final_user_p)
    option.place(x=20, y=5)
    # text window for patient's message
    p_message = Text(frame2, height=7, width=45,font=("Arial", 18), bg='white', border=2)
    p_message.insert(END, "Describe your symptoms")
    p_message.place(x=20, y=45)


    CheckVarb1 = StringVar()
    CheckVarb2 = StringVar()
    CheckVarb3 = StringVar()
    CheckVarb4 = StringVar()

    # image
    img1 = Image.open("asthma.jpeg")
    img9_re1 = ImageTk.PhotoImage(img1)

    img2 = Image.open("stroke.jpeg")
    img9_re2 = ImageTk.PhotoImage(img2)

    img3 = Image.open("vert.jpeg")
    img9_re3 = ImageTk.PhotoImage(img3)

    img4 = Image.open("b_pre.jpeg")
    img9_re4 = ImageTk.PhotoImage(img4)

    # Button color change
    off_color = "#6AD5E7"
    on_color = "#4169E1"

    def on_check():
        if CheckVarb1.get() == "asthma":
            Cb1["bg"] = on_color
        else:
            Cb1["bg"] = off_color
        if CheckVarb2.get() == "stroke":
            Cb2["bg"] = on_color
        else:
            Cb2["bg"] = off_color
        if CheckVarb3.get() == "vertigo":
            Cb3["bg"] = on_color
        else:
            Cb3["bg"] = off_color
        if CheckVarb4.get() == "blood pressure":
            Cb4["bg"] = on_color
        else:
            Cb4["bg"] = off_color

    pre_med = Label(frame2, text="Choose A Pre-Medical Condition:-                ", width=70, font='Verdana',
                    bg="#D4F1F4")
    pre_med.place(x=0, y=250)
    # ENT
    Cb1 = Checkbutton(frame2, height=170, width=280, variable=CheckVarb1, onvalue="asthma", offvalue=0, cursor="hand2",
                      activebackground="#23527c", image=img9_re1, bg=off_color, command=on_check)
    Cb1.place(x=320, y=490)
    Cb2 = Checkbutton(frame2, variable=CheckVarb2, height=170, width=280, cursor="hand2", onvalue="stroke", offvalue=0,
                      command=on_check, image=img9_re2, bg=off_color, activebackground="#23527c")
    Cb2.place(x=320, y=290)
    Cb3 = Checkbutton(frame2, variable=CheckVarb3, onvalue="vertigo", offvalue=0, height=170, width=280, cursor="hand2",
                      command=on_check, bg=off_color, image=img9_re3, activebackground="#23527c")
    Cb3.place(x=0, y=490)
    # Osteoarthritis
    Cb4 = Checkbutton(frame2, variable=CheckVarb4, onvalue="blood pressure", offvalue=0, height=170, width=280,
                      cursor="hand2", command=on_check, bg=off_color, image=img9_re4, activebackground="#23527c")
    Cb4.place(x=0, y=290)

    submit_button=Button(frame2, text="S U B M I T",  command=submit2)
    submit_button.place(x=560,y=680)

    Cb1.deselect()
    Cb2.deselect()
    Cb3.deselect()
    Cb4.deselect()
    root.mainloop()









#p_desc()
home()
#new_frame()
#prev_consult()

#d_advice()

