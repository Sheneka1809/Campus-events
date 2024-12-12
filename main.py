import os
import sys
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Base path where PyInstaller extracts files
    except AttributeError:
        base_path = os.path.abspath(".")  # Use current directory when running the script
    return os.path.join(base_path, relative_path)

def seminar(email_entered):
    seminar_page = Tk()
    seminar_page.title("CAMPUS EVENTS")
    seminar_page.geometry("300x500")
    seminar_page.resizable(False,False)
    seminar_page.iconbitmap(resource_path("logo.ico"))
    def redirect_to_main():
        seminar_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        seminar_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        seminar_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        seminar_page.destroy()
        organize(email_entered)
    menubar = Menu(seminar_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    seminar_page.config(menu=menubar)
    my_canvas = Canvas(seminar_page,bg="pink")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
    my_scrollbar = Scrollbar(seminar_page,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,80),window=second_frame,anchor="nw")
    my_canvas.create_text(140,40,text="SEMINARS...",font=("Calibri",25,"bold","italic"),fill="white")
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Seminar_events")
    seminar_data = c.fetchall()
    for data in seminar_data:
        s_r_email , s_r_event_name , s_r_event_date , s_r_event_time , s_r_event_place = data
        frame=LabelFrame(second_frame,bg="pink", borderwidth=30)
        frame.pack(expand=True, fill=BOTH)
        display1 = Label(frame,text=s_r_event_name,bg="pink")
        display2 = Label(frame,text=s_r_event_place,bg="pink")
        display3 = Label(frame,text=s_r_event_date,bg="pink")
        display4 = Label(frame,text=s_r_event_time,bg="pink")
        display5 = Label(frame,text="Published by "+s_r_email,bg="pink")
        display1.pack()
        display2.pack()
        display3.pack()
        display4.pack()
        display5.pack()
    second_frame.update_idletasks()
    my_canvas.config(scrollregion=my_canvas.bbox("all"))
    def _on_mousewheel(event):
        my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    my_canvas.bind_all("<MouseWheel>", _on_mousewheel)
    seminar_page.mainloop()

def workshop(email_entered):
    workshop_page = Tk()
    workshop_page.title("CAMPUS EVENTS")
    workshop_page.geometry("300x500")
    workshop_page.resizable(False,False)
    workshop_page.iconbitmap(resource_path("logo.ico"))
    def redirect_to_main():
        workshop_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        workshop_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        workshop_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        workshop_page.destroy()
        organize(email_entered)
    menubar = Menu(workshop_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    workshop_page.config(menu=menubar)
    my_canvas = Canvas(workshop_page,bg="pink")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
    my_scrollbar = Scrollbar(workshop_page,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,80),window=second_frame,anchor="nw")
    my_canvas.create_text(140,40,text="WORKSHOPS...",font=("Calibri",20,"bold","italic"),fill="white")
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Workshop_events")
    workshop_data = c.fetchall()
    for data in workshop_data:
        s_r_email , s_r_event_name , s_r_event_date , s_r_event_time , s_r_event_place = data
        frame=LabelFrame(second_frame,bg="pink", borderwidth=30)
        frame.pack(expand=True, fill=BOTH)
        display1 = Label(frame,text=s_r_event_name,bg="pink")
        display2 = Label(frame,text=s_r_event_place,bg="pink")
        display3 = Label(frame,text=s_r_event_date,bg="pink")
        display4 = Label(frame,text=s_r_event_time,bg="pink")
        display5 = Label(frame,text="Published by "+s_r_email,bg="pink")
        display1.pack()
        display2.pack()
        display3.pack()
        display4.pack()
        display5.pack()
    second_frame.update_idletasks()
    my_canvas.config(scrollregion=my_canvas.bbox("all"))
    def _on_mousewheel(event):
        my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    my_canvas.bind_all("<MouseWheel>", _on_mousewheel)
    workshop_page.mainloop() 

def symposium(email_entered):
    symposium_page = Tk()
    symposium_page.title("CAMPUS EVENTS")
    symposium_page.geometry("300x500")
    symposium_page.resizable(False,False)
    symposium_page.iconbitmap(resource_path("logo.ico"))
    def redirect_to_main():
        symposium_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        symposium_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        symposium_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        symposium_page.destroy()
        organize(email_entered)
    menubar = Menu(symposium_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    symposium_page.config(menu=menubar)
    my_canvas = Canvas(symposium_page,bg="pink")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
    my_scrollbar = Scrollbar(symposium_page,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,80),window=second_frame,anchor="nw")
    my_canvas.create_text(140,40,text="SYMPOSIUMS...",font=("Calibri",20,"bold","italic"),fill="white")
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Symposium_events")
    symposium_data = c.fetchall()
    for data in symposium_data:
        s_r_email , s_r_event_name , s_r_event_date , s_r_event_time , s_r_event_place = data
        frame=LabelFrame(second_frame,bg="pink", borderwidth=30)
        frame.pack(expand=True, fill=BOTH)
        display1 = Label(frame,text=s_r_event_name,bg="pink")
        display2 = Label(frame,text=s_r_event_place,bg="pink")
        display3 = Label(frame,text=s_r_event_date,bg="pink")
        display4 = Label(frame,text=s_r_event_time,bg="pink")
        display5 = Label(frame,text="Published by "+s_r_email,bg="pink")
        display1.pack()
        display2.pack()
        display3.pack()
        display4.pack()
        display5.pack()
    second_frame.update_idletasks()
    my_canvas.config(scrollregion=my_canvas.bbox("all"))
    def _on_mousewheel(event):
        my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    my_canvas.bind_all("<MouseWheel>", _on_mousewheel)
    symposium_page.mainloop()

def hackathon(email_entered):
    hackathon_page = Tk()
    hackathon_page.title("CAMPUS EVENTS")
    hackathon_page.geometry("300x500")
    hackathon_page.resizable(False,False)
    hackathon_page.iconbitmap(resource_path("logo.ico"))
    def redirect_to_main():
        hackathon_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        hackathon_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        hackathon_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        hackathon_page.destroy()
        organize(email_entered)
    menubar = Menu(hackathon_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    hackathon_page.config(menu=menubar)
    my_canvas = Canvas(hackathon_page,bg="pink")
    my_canvas.pack(side=LEFT,fill=BOTH,expand=True)
    my_scrollbar = Scrollbar(hackathon_page,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0,80),window=second_frame,anchor="nw")
    my_canvas.create_text(140,40,text="HACKATHONS...",font=("Calibri",20,"bold","italic"),fill="white")
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Hackathon_events")
    hackathon_data = c.fetchall()
    for data in hackathon_data:
        s_r_email , s_r_event_name , s_r_event_date , s_r_event_time , s_r_event_place = data
        frame=LabelFrame(second_frame,bg="pink", borderwidth=30)
        frame.pack(expand=True, fill=BOTH)
        display1 = Label(frame,text=s_r_event_name,bg="pink")
        display2 = Label(frame,text=s_r_event_place,bg="pink")
        display3 = Label(frame,text=s_r_event_date,bg="pink")
        display4 = Label(frame,text=s_r_event_time,bg="pink")
        display5 = Label(frame,text="Published by "+s_r_email,bg="pink")
        display1.pack()
        display2.pack()
        display3.pack()
        display4.pack()
        display5.pack()
    second_frame.update_idletasks()
    my_canvas.config(scrollregion=my_canvas.bbox("all"))
    def _on_mousewheel(event):
        my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    my_canvas.bind_all("<MouseWheel>", _on_mousewheel)
    hackathon_page.mainloop()

def organize(email_entered):
    organize_page = Tk()
    organize_page.title("CAMPUS EVENTS")
    organize_page.geometry("300x500")
    organize_page.resizable(False,False)
    organize_page.iconbitmap(resource_path("logo.ico"))
    image = Image.open("tk_bg.jpg")
    image = image.resize((300,500),Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(organize_page,image=bg_image)
    bg_label.place(x=0,y=0, relwidth=1,relheight=1)
    btn_image = Image.open("sea_bg.jpg")
    btn_image = btn_image.resize((80,40),Image.LANCZOS)
    btn_photo = ImageTk.PhotoImage(btn_image)
    canvas = Canvas(organize_page,width=300,height=500)
    canvas.pack(fill="both",expand=True)
    canvas.create_image(0,0,image=bg_image,anchor="nw")
    canvas.create_text(150,70,text="Organize Events...",font=("Calibri",25,"bold","italic"),fill="white")
    canvas.create_text(150,120,text="*Record view by "+email_entered,font=("Calibri",10,"italic"),fill="white")
    canvas.create_text(80,180,text="Event Type:",font=("Calibri",18,"bold"),fill="white")
    canvas.create_text(80,220,text="Event Name:",font=("Calibri",18,"bold"),fill="white")
    canvas.create_text(80,260,text="Date:",font=("Calibri",18,"bold"),fill="white")
    canvas.create_text(80,300,text="Time:",font=("Calibri",18,"bold"),fill="white")
    canvas.create_text(80,340,text="Campus Name:",font=("Calibri",18,"bold"),fill="white")
    def redirect_to_main():
        organize_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        organize_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        organize_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        organize_page.destroy()
        organize(email_entered)
    menubar = Menu(organize_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    organize_page.config(menu=menubar)
    n=StringVar()
    event_type_entry = ttk.Combobox(organize_page,width=10,values=['Seminar','Workshop','Symposium','Hackathon'],
                                  textvariable=n,state="readonly")
    canvas.create_window(230,180,window=event_type_entry)
    event_name_entry = Entry(organize_page)
    canvas.create_window(230,220,window=event_name_entry)
    def date_on_entry_click(event):
        if date_entry.get() == "dd-mm-yyyy":
            date_entry.delete(0, "end")  
    def date_on_focusout(event):
        if date_entry.get() == '':
            date_entry.insert(0, "dd-mm-yyyy")  
    date_entry = Entry(organize_page)
    date_entry.insert(0,"dd-mm-yyyy")
    date_entry.bind('<FocusIn>', date_on_entry_click) 
    date_entry.bind('<FocusOut>', date_on_focusout)
    canvas.create_window(230,260,window=date_entry)
    def time_on_entry_click(event):
        if time_entry.get() == "hh-mm-(am/pm)":
            time_entry.delete(0, "end")  
    def time_on_focusout(event):
        if time_entry.get() == '':
            time_entry.insert(0, "hh-mm-(am/pm)")  
    time_entry = Entry(organize_page)
    time_entry.insert(0,"hh-mm-(am/pm)")
    time_entry.bind('<FocusIn>', time_on_entry_click) 
    time_entry.bind('<FocusOut>', time_on_focusout)
    canvas.create_window(230,300,window=time_entry)
    place_entry = Entry(organize_page)
    canvas.create_window(230,340,window=place_entry)
    def store_event_details(email_entered):
        event_type_value = event_type_entry.get()
        event_name_value = event_name_entry.get()
        date_value = date_entry.get()
        time_value = time_entry.get()
        place_value = place_entry.get()
        if event_type_value=="" or event_name_value=="" or date_value=="" or date_value=="dd-mm-yyyy" or time_value=="" or time_value=="hh-mm-(am/pm)" or place_value=="":
            messagebox.showwarning("Warning","Fill all the details...")
        else:
            if event_type_value=='Seminar':
                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                c.execute("""CREATE TABLE IF NOT EXISTS Seminar_events 
                        (email TEXT ,event_name TEXT PRIMARY KEY,date TEXT,time TEXT,place TEXT)""")
                c.execute('SELECT event_name FROM Seminar_events')
                seminar_events = c.fetchall()
                def check_duplication():
                    for i in seminar_events:
                        if event_name_value in i:
                            return False 
                    return True 
                if check_duplication():
                    c.execute('INSERT INTO Seminar_events (email,event_name,date,time,place) VALUES (?,?,?,?,?)',
                            (email_entered,event_name_value,date_value,time_value,place_value))
                    conn.commit()
                    conn.close()
                    organize_page.destroy()
                    welcome(email_entered)
                else:
                    messagebox.showwarning("Error","This event name already exists. \n Give new event name...")
                
            elif event_type_value=='Workshop':
                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                c.execute("""CREATE TABLE IF NOT EXISTS Workshop_events 
                        (email TEXT ,event_name TEXT PRIMARY KEY,date TEXT,time TEXT,place TEXT)""")
                c.execute('SELECT event_name FROM Workshop_events')
                workshop_events = c.fetchall()
                def check_duplication():
                    for i in workshop_events:
                        if event_name_value in i:
                            return False 
                    return True 
                if check_duplication():
                    c.execute('INSERT INTO Workshop_events (email,event_name,date,time,place) VALUES (?,?,?,?,?)',
                            (email_entered,event_name_value,date_value,time_value,place_value))
                    conn.commit()
                    conn.close()
                    organize_page.destroy()
                    welcome(email_entered)
                else:
                    messagebox.showwarning("Error","This event name already exists. \n Give new event name...")
                
            elif event_type_value=='Symposium':
                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                c.execute("""CREATE TABLE IF NOT EXISTS Symposium_events 
                        (email TEXT ,event_name TEXT PRIMARY KEY,date TEXT,time TEXT,place TEXT)""")
                c.execute('SELECT event_name FROM Symposium_events')
                symposium_events = c.fetchall()
                def check_duplication():
                    for i in symposium_events:
                        if event_name_value in i:
                            return False 
                    return True 
                if check_duplication():
                    c.execute('INSERT INTO Symposium_events (email,event_name,date,time,place) VALUES (?,?,?,?,?)',
                            (email_entered,event_name_value,date_value,time_value,place_value))
                    conn.commit()
                    conn.close()
                    organize_page.destroy()
                    welcome(email_entered)
                else:
                    messagebox.showwarning("Error","This event name already exists. \n Give new event name...")
                
            elif event_type_value=='Hackathon':
                conn = sqlite3.connect('student.db')
                c = conn.cursor()
                c.execute("""CREATE TABLE IF NOT EXISTS Hackathon_events 
                        (email TEXT ,event_name TEXT PRIMARY KEY,date TEXT,time TEXT,place TEXT)""")
                c.execute('SELECT event_name FROM Hackathon_events')
                hackathon_events = c.fetchall()
                def check_duplication():
                    for i in hackathon_events:
                        if event_name_value in i:
                            return False 
                    return True 
                if check_duplication():
                    c.execute('INSERT INTO Hackathon_events (email,event_name,date,time,place) VALUES (?,?,?,?,?)',
                            (email_entered,event_name_value,date_value,time_value,place_value))
                    conn.commit()
                    conn.close()
                    organize_page.destroy()
                    welcome(email_entered)
                else:
                    messagebox.showwarning("Error","This event name already exists. \n Give new event name...")
                
    publish_btn = Button(organize_page,text="PUBLISH",command=lambda: store_event_details(email_entered),borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    canvas.create_window(150,420,window=publish_btn)
    organize_page.mainloop()

def view_mode(email_entered):
    view_mode_page = Tk()
    view_mode_page.title("CAMPUS EVENTS")
    view_mode_page.geometry("300x500")
    view_mode_page.resizable(False,False)
    view_mode_page.iconbitmap(resource_path("logo.ico"))
    image = Image.open("tk_bg.jpg")
    image = image.resize((300,500),Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(view_mode_page,image=bg_image)
    bg_label.place(x=0,y=0, relwidth=1,relheight=1)
    btn_image = Image.open("sea_bg.jpg")
    btn_image = btn_image.resize((100,100),Image.LANCZOS)
    btn_photo = ImageTk.PhotoImage(btn_image)
    canvas = Canvas(view_mode_page,width=300,height=500)
    canvas.pack(fill="both",expand=True)
    canvas.create_image(0,0,image=bg_image,anchor="nw")
    canvas.create_text(150,70,text="Event Types...",font=("Calibri",30,"bold","italic"),fill="white")
    canvas.create_text(150,120,text="*Record view by "+email_entered,font=("Calibri",10,"italic"),fill="white")
    def redirect_to_main():
        view_mode_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        view_mode_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        view_mode_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        view_mode_page.destroy()
        organize(email_entered)
    menubar = Menu(view_mode_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    view_mode_page.config(menu=menubar)
    def redirect_to_seminar():
        view_mode_page.destroy()
        seminar(email_entered)
    def redirect_to_workshop():
        view_mode_page.destroy()
        workshop(email_entered)
    def redirect_to_symposium():
        view_mode_page.destroy()
        symposium(email_entered)
    def redirect_to_hackathon():
        view_mode_page.destroy()
        hackathon(email_entered)
    event_type1 = Button(view_mode_page,text="Seminar",command=redirect_to_seminar,borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    event_type1.config(width=100,height=100)
    canvas.create_window(95,230,window=event_type1)
    event_type2 = Button(view_mode_page,text="Workshop",command=redirect_to_workshop,borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    event_type2.config(width=100,height=100)
    canvas.create_window(215,230,window=event_type2)
    event_type3 = Button(view_mode_page,text="Symposium",command=redirect_to_symposium,borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    event_type3.config(width=100,height=100)
    canvas.create_window(95,350,window=event_type3)
    event_type4 = Button(view_mode_page,text="Hackathon",command=redirect_to_hackathon,borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    event_type4.config(width=100,height=100)
    canvas.create_window(215,350,window=event_type4)
    view_mode_page.mainloop()

def welcome(email_entered):
    welcome_page = Tk()
    welcome_page.title("CAMPUS EVENTS")
    welcome_page.geometry("300x500")
    welcome_page.resizable(False,False)
    welcome_page.iconbitmap(resource_path("logo.ico"))
    image = Image.open("tk_bg.jpg")
    image = image.resize((300,500),Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(welcome_page,image=bg_image)
    bg_label.place(x=0,y=0, relwidth=1,relheight=1)
    btn_image = Image.open("sea_bg.jpg")
    btn_image = btn_image.resize((180,60),Image.LANCZOS)
    btn_photo = ImageTk.PhotoImage(btn_image)
    canvas = Canvas(welcome_page,width=300,height=500)
    canvas.pack(fill="both",expand=True)
    canvas.create_image(0,0,image=bg_image,anchor="nw")
    def redirect_to_main():
        welcome_page.destroy()
        main()
    def redirect_to_welcome(email_entered):
        welcome_page.destroy()
        welcome(email_entered)
    def redirect_to_view_mode(email_entered):
        welcome_page.destroy()
        view_mode(email_entered)
    def redirect_to_organize(email_entered):
        welcome_page.destroy()
        organize(email_entered)
    menubar = Menu(welcome_page)
    all_menu = Menu(menubar,tearoff=0,bg="pink")
    menubar.add_cascade(label='MENU',menu=all_menu)
    all_menu.add_command(label='Home',command=lambda: redirect_to_welcome(email_entered))
    all_menu.add_command(label='Organize',command=lambda: redirect_to_organize(email_entered))
    all_menu.add_command(label='Participate',command=lambda: redirect_to_view_mode(email_entered))
    all_menu.add_command(label='LogOut',command=redirect_to_main)
    welcome_page.config(menu=menubar)
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('SELECT usertype FROM app WHERE email=?',(email_entered,))
    usertype = c.fetchone()
    conn.close()
    canvas.create_text(150,70,text="Hello dear "+usertype[0]+"...",font=("Calibri",20,"bold","italic"),fill="white")
    participate_btn = Button(welcome_page,text="Event Participation",command=lambda: redirect_to_view_mode(email_entered),
                             borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    canvas.create_window(150,200,window=participate_btn)
    organize_btn = Button(welcome_page,text="Event Organization",command=lambda: redirect_to_organize(email_entered),
                          borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    canvas.create_window(150,300,window=organize_btn)
    participate_btn.config(width=180,height=60)
    organize_btn.config(width=180,height=60)
    welcome_page.mainloop()

def signup():
    signup_page  =Tk()
    signup_page.title("CAMPUS EVENTS")
    signup_page.geometry("300x500")
    signup_page.resizable(False,False)
    signup_page.iconbitmap(resource_path("logo.ico"))
    image = Image.open("tk_bg.jpg")
    image = image.resize((300,500),Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(signup_page,image=bg_image)
    bg_label.place(x=0,y=0, relwidth=1,relheight=1)
    btn_image = Image.open("sea_bg.jpg")
    btn_image = btn_image.resize((80,40),Image.LANCZOS)
    btn_photo = ImageTk.PhotoImage(btn_image)
    canvas = Canvas(signup_page,width=300,height=500)
    canvas.pack(fill="both",expand=True)
    canvas.create_image(0,0,image=bg_image,anchor="nw")
    canvas.create_text(150,70,text="Signup/Register...",font=("Calibri",20,"bold","italic"),fill="white")
    canvas.create_text(80,150,text="Username:",font=("Calibri",15,"bold"),fill="white")
    canvas.create_text(80,190,text="Email:",font=("Calibri",15,"bold"),fill="white")
    canvas.create_text(80,230,text="Password:",font=("Calibri",15,"bold"),fill="white")
    canvas.create_text(80,270,text="User Type:",font=("Calibri",15,"bold"),fill="white")
    def redirect_to_main():
        signup_page.destroy()
        main()
    back_btn = Button(signup_page,text="BACK",command=redirect_to_main,bg="pink")
    canvas.create_window(30,20,window=back_btn)
    username_entry = Entry(signup_page)
    canvas.create_window(210,150,window=username_entry)
    email_entry = Entry(signup_page)
    canvas.create_window(210,190,window=email_entry)
    password_entry = Entry(signup_page)
    canvas.create_window(210,230,window=password_entry)
    n=StringVar()
    usertype_entry = ttk.Combobox(signup_page,width=10,values=['Student','Staff','Administrator','Vendor'],textvariable=n,state="readonly")
    canvas.create_window(210,270,window=usertype_entry)
    def register_new():
        username_value = username_entry.get()
        email_value = email_entry.get()
        password_value = password_entry.get()
        usertype_value = usertype_entry.get()
        if username_value=="" or email_value=="" or password_value=="" or usertype_value=="":
            messagebox.showwarning("Warning","Fill all the details...")
        else:
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            c.execute("INSERT INTO app (username, email, password, usertype ) VALUES (?,?,?,?)", 
                (username_value,email_value,password_value,usertype_value))
            conn.commit()
            conn.close()
            redirect_to_main()
    register_btn = Button(signup_page,text="Register",command=register_new,borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    canvas.create_window(210,340,window=register_btn)
    signup_page.mainloop()

def login():
    login_page = Tk()
    login_page.title("CAMPUS EVENTS")
    login_page.geometry("300x500")
    login_page.resizable(False,False)
    login_page.iconbitmap(resource_path("logo.ico"))
    image = Image.open("tk_bg.jpg")
    image = image.resize((300,500),Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(login_page,image=bg_image)
    bg_label.place(x=0,y=0, relwidth=1,relheight=1)
    btn_image = Image.open("sea_bg.jpg")
    btn_image = btn_image.resize((80,40),Image.LANCZOS)
    btn_photo = ImageTk.PhotoImage(btn_image)
    canvas = Canvas(login_page,width=300,height=500)
    canvas.pack(fill="both",expand=True)
    canvas.create_image(0,0,image=bg_image,anchor="nw")
    canvas.create_text(150,100,text="Welcome...",font=("Calibri",30,"bold","italic"),fill="white")
    canvas.create_text(70,150,text="Email:",font=("Calibri",15,"bold","italic"),fill="white")
    canvas.create_text(70,200,text="Password:",font=("Calibri",15,"bold","italic"),fill="white")
    def redirect_to_main():
        login_page.destroy()
        main()
    back_btn = Button(login_page,text="BACK",command=redirect_to_main,bg="pink")
    canvas.create_window(30,20,window=back_btn)
    email_entry = Entry(login_page)
    canvas.create_window(200,150,window=email_entry)
    password_entry = Entry(login_page,show="*")
    canvas.create_window(200,200,window=password_entry)
    def redirect_to_welcome():
        email_entered = email_entry.get()
        password_entered = password_entry.get()
        if email_entered and password_entered:
            conn = sqlite3.connect('student.db')
            c = conn.cursor()
            c.execute("SELECT email FROM app")
            emails = c.fetchall()
            for i in emails:
                if email_entered in i:
                    c.execute("SELECT password,email FROM app WHERE email=?",(email_entered,))
                    crt_details = c.fetchall()
                    crt_password , crt_email = crt_details[0]
                    conn.close()
                    if password_entered==crt_password:
                        login_page.destroy()
                        welcome(email_entered)
                        return 
                    else:
                        messagebox.showerror("Error","Invalid Password")
                        return 
            messagebox.showwarning("Error","Please enter the registered mail id")
            return        
    login_btn = Button(login_page,text="LOGIN",command=redirect_to_welcome,borderwidth=5,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    canvas.create_window(210,280,window=login_btn)
    login_page.mainloop()

def main():
    root = Tk()
    root.title("CAMPUS EVENTS")
    root.geometry("300x500")
    root.resizable(False,False)
    root.iconbitmap(resource_path("logo.ico"))
    image = Image.open("tk_bg.jpg")
    image = image.resize((300,500),Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    bg_label = Label(root,image=bg_image)
    bg_label.place(x=0,y=0, relwidth=1,relheight=1)
    btn_image = Image.open("sea_bg.jpg")
    btn_image = btn_image.resize((80,40),Image.LANCZOS)
    btn_photo = ImageTk.PhotoImage(btn_image)
    canvas = Canvas(root,width=300,height=500)
    canvas.pack(fill="both",expand=True)
    canvas.create_image(0,0,image=bg_image,anchor="nw")
    canvas.create_text(150,120,text="CAMPUS EVENTS \n MANAGEMENT",font=("Algerian",20,"italic"),fill="white")
    def redirect_to_login():
        root.destroy()
        login()
    def redirect_to_signup():
        root.destroy()
        signup()
    login_btn = Button(root,text="LOGIN",borderwidth=5,command=redirect_to_login,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    login_btn.config(width=80,height=40)
    canvas.create_window(150,240,window=login_btn)
    signup_btn = Button(root,text="SIGN UP",borderwidth=5,command=redirect_to_signup,image=btn_photo,compound="center",font=("Calibri",15,"bold"))
    signup_btn.config(width=80,height=40)
    canvas.create_window(150,360,window=signup_btn)
    root.mainloop()

conn = sqlite3.connect('student.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS app (username TEXT, email TEXT PRIMARY KEY, password TEXT,usertype TEXT)")
conn.commit()
conn.close()

main() 
