

from .bl import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# region Home Form
def home_form():

    # region Func Login Btn
    def login_btn_onclick():

        form.destroy()
        login_form()
    # endregion Func Login Btn

    # region Func Sign Btn
    def sign_btn_onclick():

        form.destroy()
        register_form()
    # endregion Sign Btn

    form = Tk()

    # region Form Info
    form.title(" Welcome")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images\home.ico")

    window_height = 400
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#FFF8DC",
    )
    body.pack(fill=BOTH, expand=True, padx=30, pady=80)
    body.propagate(False)
    # endregion Frame

    # region Label
    Label(
        master=body,
        text="----- Sign Up or Login -----",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 11, "normal")
    ).pack(side=TOP, padx=10, pady=(30, 0))
    # endregion Label

    # region Login Btn
    Button(
        master=body,
        text="Login",
        bg="#00008b",
        fg="#FFF8DC",
        activebackground="#036bcf",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        padx=5,
        pady=5,
        command=lambda: login_btn_onclick()
    ).pack(side=TOP, fill=X, pady=(30, 20), padx=30)
    # endregion Login Btn

    # region Sign UP Btn
    Button(
        master=body,
        text="Sign UP",
        bg="#00008b",
        fg="#FFF8DC",
        activebackground="#036bcf",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        padx=5,
        pady=5,
        command=lambda: sign_btn_onclick()
    ).pack(side=TOP, fill=X, pady=0, padx=30)
    # endregion Sign UP Btn

    form.mainloop()
# endregion Home Form


# region Login Form
def login_form():

    # region Func Login Btn
    def login_btn_onclick():
        username_str = username.get()
        password_str = password.get()

        status, output = login_user_bl(
            username=username_str,
            password=password_str
        )

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":
            messagebox.showinfo("SUCCESS", output)
            form.destroy()
            mainform(username_str)
    # endregion Func Login Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        home_form()
    # endregion Func Back Btn

    form = Tk()

    # region Form Info
    form.title(" Login User")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images\user.ico")

    window_height = 450
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#FFF8DC"
    )
    body.pack(fill=BOTH, expand=True, padx=30, pady=70)
    body.propagate(False)
    # endregion Frame

    # region Variable
    username = StringVar()
    password = StringVar()
    # endregion Variable

    # region Label
    Label(
        master=body,
        text="Login",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 11, "bold")
    ).pack(side=TOP, padx=10, pady=10)
    # endregion Label

    # region User Name
    Label(
        master=body,
        text="Username : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=(0, 10))

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=username,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion User Name

    # region Password
    Label(
        master=body,
        text="Password : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=(15, 10))

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=password,
        bd=1,
        show="*"
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Password

    # region Login Btn
    Button(
        master=body,
        text=" Login",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        pady=5,
        compound=LEFT,
        command=lambda: login_btn_onclick()
    ).pack(side=TOP, fill=X, pady=(30, 10), padx=30)
    # endregion Login Btn

    # region Back Btn
    Button(
        master=body,
        text="Back",
        bg="#c0c0c0",
        fg="#0d0d0d",
        activebackground="#c0c0c0",
        activeforeground="#0d0d0d",
        font=("tahoma", 10, "bold"),
        pady=5,
        compound=LEFT,
        command=lambda: back_btn_onclick()
    ).pack(side=TOP, fill=X, padx=30)
    # endregion Back Btn

    form.mainloop()
# endregion Login Form


# region Sign Up Form
def register_form():

    # region Func Sign Up Btn
    def register_btn_onclick():

        fullname_str = fullname.get()
        email_str = email.get()
        username_str = username.get()
        password_str = password.get()


        status, output = register_user_bl(
            fullname=fullname_str,
            email=email_str,
            username=username_str,
            password=password_str
        )


        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":
            messagebox.showinfo("SUCCESS", output)
            form.destroy()
            login_form()
    # endregion Func Sign Up Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        home_form()
    # endregion Func Back Btn

    form = Tk()

    # region Form Info
    form.title("Sign Up User")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images/user.ico")

    window_height = 500
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#FFF8DC"
    )
    body.pack(fill=BOTH, expand=True, padx=30, pady=30)
    body.propagate(False)
    # endregion Frame

    # region variable
    fullname = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()
    # endregion

    # region Label
    Label(
        master=body,
        text="Sign Up",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 11, "bold")
    ).pack(side=TOP, padx=10, pady=10)
    # endregion Label

    # region Full Name
    Label(
        master=body,
        text="Fullname : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=fullname,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Full Name

    # region email
    Label(
        master=body,
        text="Email : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=10, padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=email,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Email

    # region User Name
    Label(
        master=body,
        text="Username : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=username,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion User Name

    # region Password
    Label(
        master=body,
        text="Password : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=(15, 0), padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=password,
        bd=1,
        show="*"
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Password

    # region Sign Up Btn
    Button(
        master=body,
        text="Sign Up",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        pady=5,
        compound=LEFT,
        command=lambda: register_btn_onclick()
    ).pack(side=TOP, fill=X, pady=(30, 10), padx=30)
    # endregion Sign Up Btn

    # region Back Btn
    Button(
        master=body,
        text="Back",
        bg="#c0c0c0",
        fg="#0d0d0d",
        activebackground="#c0c0c0",
        activeforeground="#0d0d0d",
        font=("tahoma", 10, "bold"),
        pady=5,
        compound=LEFT,
        command=lambda: back_btn_onclick()
    ).pack(side=TOP, fill=X, padx=30)
    # endregion Back Btn

    form.mainloop()
# endregion Sign Up Form


# region Main Form
def mainform(username):

    # region Load Student Cours
    def load_student_course():

        status, output = get_assign_course_bl(username)

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":

            for item in output:
                assign_course_grid.insert('', 'end', values=tuple(item.values()))
    # endregion Load Student Cours

    # region Func Add Student Btn
    def add_student_btn_onclick():

        form.withdraw()
        student_menu_form(
            username=username,
            mainform=form
        )
    # endregion Func Add Student Btn

    # region Func Add Course Btn
    def add_course_btn_onclick():

        form.withdraw()
        course_menu_form(
            username=username,
            mainform=form
        )
    # endregion Func Add Course Btn

    # region Func Assign Course Btn
    def assign_course_btn_onclick():

        form.withdraw()
        assign_course_form(
            username=username, 
            assign_course_grid=assign_course_grid, 
            mainform=form
        )  
    # endregion Func Assign Course Btn
    
    # region Func Exit Btn
    def exit_btn_onclick():
        form.destroy()
    # endregion Func Exit Btn

    form = Tk()

    # region Form Info
    form.title(f" Hi {username}")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images\user.ico")

    window_width = 1300
    window_height = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#808080"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Add Student Btn
    add_std_img = PhotoImage(file=r'images/add_std.png')

    Button(
        master=footer,
        text="Add Student",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=add_std_img,
        compound=LEFT,
        pady=3,
        padx=7,
        command=lambda: add_student_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Add Student Btn

    # region Add Course Btn
    add_curs_img = PhotoImage(file=r'images/add_curs.png')

    Button(
        master=footer,
        text="Add Course",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=add_curs_img,
        compound=LEFT,
        pady=3,
        padx=7,
        command=lambda: add_course_btn_onclick()
    ).pack(side=LEFT, padx=(0, 10))
    # endregion Add Course Btn

    # region Assign Course Btn
    assign_curs_img = PhotoImage(file=r'images/assign_curs.png')

    Button(
        master=footer,
        text="Assign Course",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=assign_curs_img,
        compound=LEFT,
        pady=3,
        padx=7,
        command=lambda: assign_course_btn_onclick()
    ).pack(side=LEFT, padx=(0, 10))
    # endregion Assign Course Btn

    # region Exit Btn
    exit_img = PhotoImage(file=r'images/exit.png')

    Button(
        master=footer,
        text="Exit",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=exit_img,
        compound=LEFT,
        pady=3,
        padx=7,
        command=lambda: exit_btn_onclick()
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion Exit Btn

    # region Assign Course Grid  
    style = ttk.Style()
    style.theme_use('clam')
    
    scrollbar = ttk.Scrollbar(body, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)
    
    assign_course_grid = ttk.Treeview(
        master=body, 
        column=("Name","Family","National Code","Student ID","Course","Course Code", "owner"), 
        show='headings', 
        selectmode="extended",
        displaycolumns=("Name","Family","National Code","Student ID","Course","Course Code")
    )
    assign_course_grid.column("# 1", anchor=CENTER)
    assign_course_grid.heading("# 1", text="Name")
    assign_course_grid.column("# 2", anchor=CENTER)
    assign_course_grid.heading("# 2", text="Family")
    assign_course_grid.column("# 3", anchor=CENTER)
    assign_course_grid.heading("# 3", text="National Code")
    assign_course_grid.column("# 4", anchor=CENTER)
    assign_course_grid.heading("# 4", text="Student Code")
    assign_course_grid.column("# 5", anchor=CENTER)
    assign_course_grid.heading("# 5", text="Course")
    assign_course_grid.column("# 6", anchor=CENTER)
    assign_course_grid.heading("# 6", text="Course code")        
    assign_course_grid.pack(fill=BOTH, expand=True)
    
    
    assign_course_grid.configure(yscrollcommand=scrollbar.set)
    scrollbar['command'] = assign_course_grid.yview
    # endregion Assign Course Grid

    load_student_course()
    form.mainloop()
# endregion Main Form


# region Student Menu Form
def student_menu_form(username, mainform):

    # region Load Student Content
    def load_student():

        status, output = get_student_bl(username)

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":

            for student in output:
                student_grid.insert('', 'end', values=tuple(student.values()))
    # endregion Load Student Content

    # region Func Add Student Btn
    def add_student_btn_onclick():

        form.withdraw()
        add_student_form(
            username=username,
            student_grid=student_grid,
            mainform=form
        )
    # endregion Func Add Student Btn

    # region Func Edit Student Btn
    def edit_student_btn_onclick():

        select_item = student_grid.selection()

        if not select_item:
            messagebox.showerror("ERROR", "Error Select!")

        elif len(select_item) > 1:
            messagebox.showerror("ERROR", "Error Select!")

        else:
            select_id = select_item[0]
            name, family, gender, birthDay, nationalCode, studentId, username = student_grid.item(select_id, "values")

            answer = messagebox.askyesno(title='Confirmation',message=f'Edit student ?\n {f"Fullname : {name} {family} - Student ID : {studentId}"}')

            if answer:

                form.withdraw()
                edit_student_form(
                    old_name=name,
                    old_family=family,
                    old_gender=gender,
                    old_birthDay=birthDay,
                    old_nationalCode=nationalCode,
                    old_studentId=studentId,
                    username=username,
                    student_grid=student_grid,
                    mainform=form
                )
    # endregion Func Edit Student Btn

    # region Func Remove Student Btn
    def remove_student_btn_onclick():

        select_item = student_grid.selection()

        if not select_item:
            messagebox.showerror("ERROR", "Error Select!")

        else:
            remove_list = []
            message_list = []

            for item in select_item:
                student = student_grid.item(item, "values")
                remove_list.append(student)
                message_list.append(f"Fullname : {student[0]} {student[1]} - Student ID : {student[5]}")


            answer = messagebox.askyesno(title='Confirmation',message=f'Remove student ? \n {"n".join(message_list)}')


            if answer:
                status, output = remove_student_bl(remove_list=remove_list)

                if status == "ERROR":
                    messagebox.showerror("ERROR", output)

                elif status == "SUCCESS":

                    for item in select_item:
                        student_grid.delete(item)
    # endregion Func Remove Student Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn

    form = Toplevel()

    # region Form Info
    form.title("Student Menu")
    form.resizable(width=True, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images\list.ico")

    window_width = 1200
    window_height = 500
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#808080"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Add Student Btn
    add_img = PhotoImage(file=r'images/add_std.png')

    Button(
        master=footer,
        text="Add",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=add_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: add_student_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Add Student Btn

    # region Edit Student Btn
    edit_img = PhotoImage(file=r'images/edit_std.png')

    Button(
        master=footer,
        text="Edit",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=edit_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: edit_student_btn_onclick()
    ).pack(side=LEFT, padx=(0, 10))
    # endregion Edit Student Btn

    # region Remove Btn
    remove_img = PhotoImage(file=r'images/remove_std.png')

    Button(
        master=footer,
        text="Remove",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=remove_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: remove_student_btn_onclick()
    ).pack(side=LEFT, padx=(0, 10))
    # endregion Remove Course Btn

    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=back_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion Back Btn

    # region Student Grid
    style = ttk.Style()
    style.theme_use('clam')

    scrollbar = ttk.Scrollbar(body, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)

    student_grid = ttk.Treeview(
        master=body,
        column=("Name", "Family", "Gender", "Birth Day","National Code", "Student ID"),
        show='headings',
        selectmode="extended",
        displaycolumns=("Name", "Family", "Gender", "Birth Day","National Code", "Student ID")
    )
    student_grid.column("# 1", anchor=CENTER)
    student_grid.heading("# 1", text="Name")
    student_grid.column("# 2", anchor=CENTER)
    student_grid.heading("# 2", text="Family")
    student_grid.column("# 3", anchor=CENTER)
    student_grid.heading("# 3", text="Gender")
    student_grid.column("# 4", anchor=CENTER)
    student_grid.heading("# 4", text="Birth Day")
    student_grid.column("# 5", anchor=CENTER)
    student_grid.heading("# 5", text="National Code")
    student_grid.column("# 6", anchor=CENTER)
    student_grid.heading("# 6", text="Student ID")
    student_grid.pack(fill=BOTH, expand=True)

    student_grid.configure(yscrollcommand=scrollbar.set)
    scrollbar['command'] = student_grid.yview
    # endregion Student Grid

    load_student()
    form.mainloop()
# endregion Student Menu Form


# region Add Student Form
def add_student_form(username, student_grid, mainform):

    # region Func Add Btn
    def add_btn_onclick():

        name_str = name.get()
        family_str = family.get()
        gender_str = gender.get()
        birthDay_str = birthDay.get()
        nationalCode_str = nationalCode.get()
        studentId_str = studentId.get()

        status, output = add_student_bl(
            name=name_str,
            family=family_str,
            gender=gender_str,
            birthDay=birthDay_str,
            nationalCode=nationalCode_str,
            studentId=studentId_str,
            username=username
        )

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":

            messagebox.showinfo("SUCCESS", output)
            student_grid.insert('', 'end',  values=(name_str, family_str, gender_str, birthDay_str, nationalCode_str, studentId_str, username))
            back_btn_onclick()
    # endregion Func Add Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn

    form = Toplevel()

    # region Form Info
    form.title("Add Student")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images\add_std.ico")

    window_height = 500
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#FFF8DC"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region variable
    name = StringVar()
    family = StringVar()
    gender = StringVar()
    birthDay = StringVar()
    nationalCode = StringVar()
    studentId = StringVar()
    # endregion Variable

    # region Name
    Label(
        master=body,
        text="Name : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=name,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Name

    # region Family
    Label(
        master=body,
        text="Family : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=10, padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=family,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Family

    # region Birth Day
    Label(
        master=body,
        text="Birth Day : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=(15, 0), padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=birthDay,
        bd=1,
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Birth Day

    # region Gender
    Label(
        master=body,
        text="Gender : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=gender,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Gender

    # region National Cdoe
    Label(
        master=body,
        text="National Cdoe : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=nationalCode,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion National Cdoe

    # region Student ID
    Label(
        master=body,
        text="Student ID : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=(15, 0), padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=studentId,
        bd=1,
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Student ID

    # region Add Student Btn
    add_img = PhotoImage(file=r'images/add_std.png')

    Button(
        master=footer,
        text="Add",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=add_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: add_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Edit Student Btn

    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=back_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion Back Btn

    form.mainloop()
# endregion Add Student Form


# region Edit Student Form
def edit_student_form(old_name, old_family, old_gender, old_birthDay, old_nationalCode, old_studentId, student_grid, username, mainform):

    # region Func Edit Btn
    def edit_btn_onclick():

        name_str = name.get()
        family_str = family.get()
        gender_str = gender.get()
        birthDay_str = birthDay.get()
        nationalCode_str = nationalCode.get()
        studentId_str = studentId.get()

        status, output = edit_student_bl(
            old_name=old_name,
            old_family=old_family,
            old_gender=old_gender,
            old_birthDay=old_birthDay,
            old_nationalCode=old_nationalCode,
            old_studentId=old_studentId,
            name=name_str,
            family=family_str,
            gender=gender_str,
            birthDay=birthDay_str,
            nationalCode=nationalCode_str,
            studentId=studentId_str,
            username=username,
        )

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":

            messagebox.showinfo("SUCCESS", output)
            select_id = student_grid.selection()[0]
            student_grid.item(select_id,  values=(name_str, family_str, gender_str, birthDay_str, nationalCode_str, studentId_str, username))
            back_btn_onclick()
    # endregion Func Edit Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn

    form = Toplevel()

    # region Form Info
    form.title("Edit Student")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images/edit_std.ico")

    window_height = 500
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#FFF8DC"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Variable
    name = StringVar(value=old_name)
    family = StringVar(value=old_family)
    gender = StringVar(value=old_gender)
    birthDay = StringVar(value=old_birthDay)
    nationalCode = StringVar(value=old_nationalCode)
    studentId = StringVar(value=old_studentId)
    # endregion  Variable

    # region Name
    Label(
        master=body,
        text="Name : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=name,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Name

    # region Family
    Label(
        master=body,
        text="Family : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=10, padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=family,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Family

    # region Birth Day
    Label(
        master=body,
        text="Birth Day : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=(15, 0), padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=birthDay,
        bd=1,
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Birth Day

    # region Gender
    Label(
        master=body,
        text="Gender : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=gender,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Gender

    # region National Code
    Label(
        master=body,
        text="National Cdoe : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=nationalCode,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion National Code

    # region Student ID
    Label(
        master=body,
        text="Student ID : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, pady=(15, 0), padx=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=studentId,
        bd=1,
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Student ID

    # region Edit Student Btn
    edit_img = PhotoImage(file=r'images/edit_std.png')

    Button(
        master=footer,
        text="Edit",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=edit_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: edit_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Edit Student Btn

    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=back_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion Back Btn

    form.mainloop()
# endregion Edit Student Form


# region Course Menu Form
def course_menu_form(username, mainform):

    # region Load Course
    def load_course():

        status, output = get_course_bl(username)
        
        if status == "ERROR":
            messagebox.showerror("ERROR", output)
            
        elif status == "SUCCESS":

            for course in output:
                course_grid.insert('', 'end', values=tuple(course.values()))
    # endregion Load Course        

    # region Func Add course Btn
    def add_course_btn_onclick():

        form.withdraw()
        add_course_form(
            username=username, 
            course_grid=course_grid,
            mainform=form
        )    
    # endregion Func Add course Btn

    # region Func Edit Course Btn
    def edit_course_btn_onclick():

        select_item = course_grid.selection()

        if not select_item :
            messagebox.showerror("ERROR", "Error Select!")

        elif len(select_item)>1:
            messagebox.showerror("ERROR", "Error Select!")

        else:
            select_id = select_item[0]
            title, courseCode, price, username = course_grid.item(select_id, "values")

            answer = messagebox.askyesno(title='Confirmation',
                message=f'Edit course ?\n {f"Course Name : {title} - Course Code : {courseCode}"}')

            if answer:

                form.withdraw()
                edit_course_form(
                    old_title=title,
                    old_courseCode=courseCode,
                    old_price=price,
                    username=username, 
                    course_grid=course_grid,
                    mainform=form
                )
    # endregion Func Edit Course Btn
    
    # region Func Remove Course Btn
    def remove_course_btn_onclick():
        select_item = course_grid.selection()

        if not select_item:
            messagebox.showerror("ERROR", "Error Select!")

        else:
            remove_list = []
            message_list = []


            for item in select_item:
                course = course_grid.item(item, "values")
                remove_list.append(course)
                message_list.append(f"Fullname : {course[0]}  - Course Code : {course[1]}") 


            answer = messagebox.askyesno(title='Confirmation',
                message=f'Remove course ?\n {"n".join(message_list)}')

            if answer:
                status, output = remove_course_bl(remove_list=remove_list)
            
                if status == "ERROR":
                    messagebox.showerror("ERROR", output)
                    
                elif status == "SUCCESS":
                    
                    for item in select_item:
                        course_grid.delete(item)
    # endregion Func Remove Course Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn

    form = Toplevel()
    
    # region Form Info
    form.title("Course Menu")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images/list.ico")

    window_width = 700
    window_height = 500
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#808080"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Add Course Btn
    add_curs_img = PhotoImage(file=r'images\add_curs.png')

    Button(
        master=footer,
        text="Add",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=add_curs_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: add_course_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Add Course Btn

    # region Edit Course Btn
    edit_curs_img = PhotoImage(file=r'images/edit_curs.png')

    Button(
        master=footer,
        text="Edit",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=edit_curs_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: edit_course_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Edit Course Btn

    # region Remove Curse Btn
    remove_curs_img = PhotoImage(file=r'images/remove_curs.png')
    Button(
        master=footer,
        text="Remove",
        bg="#003fcd",
        fg="#FFF8DC",
        activebackground="#264b69",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=remove_curs_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda:remove_course_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Remove Curse Btn

    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=back_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=10)
    # endregion Back Btn
  
    # region Course Grid
    style = ttk.Style()
    style.theme_use('clam')
    
    scrollbar = ttk.Scrollbar(body, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)
    
    course_grid = ttk.Treeview(
        master=body, 
        column=("Title", "Course Code", "Price"), 
        show='headings', 
        selectmode="extended",
        displaycolumns=("Title", "Course Code", "Price")
    )
    course_grid.column("# 1", anchor=CENTER)
    course_grid.heading("# 1", text="Title")
    course_grid.column("# 2", anchor=CENTER)
    course_grid.heading("# 2", text="Course Code")
    course_grid.column("# 3", anchor=CENTER)
    course_grid.heading("# 3", text="Price")
    course_grid.pack(fill=BOTH, expand=True)
    
    
    course_grid.configure(yscrollcommand=scrollbar.set)
    scrollbar['command'] = course_grid.yview
    # endregion Course Grid
    
    load_course()
    form.mainloop()
# endregion Course Menu Form 


# region Add Course From
def add_course_form(username, course_grid, mainform):
    
    # region Func Add Course Btn
    def add_course_btn_onclick():

        title_str = title.get()
        courseCode_str = courseCode.get()
        price_str = price.get() 
        
        status, output = add_course_bl(
            title=title_str,
            courseCode=courseCode_str,
            price=price_str,
            username=username
        )
        
        if status == "ERROR":
            messagebox.showerror("ERROR", output)
            
        elif status == "SUCCESS":
            messagebox.showinfo("SUCCESS", output)
            course_grid.insert('', 'end',  values=(title_str, courseCode_str, price_str,username))
            back_btn_onclick()
    # endregion Func Add Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn
    
    form = Toplevel()

    # region Form Info
    form.title("Add Course")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images/add_curs.ico")

    window_height = 400
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#FFF8DC"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Variable
    title = StringVar()
    courseCode = StringVar()
    price = StringVar()
    # endregion Variable
    
    # region Title
    Label(
        master=body,
        text="Title : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=title,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Title
    
    # region Course Code
    Label(
        master=body,
        text="Course Code : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=courseCode,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Course Code

    # region Price
    Label(
        master=body,
        text="Price : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=price,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Price

    # region Add Course Btn
    add_curs_img = PhotoImage(file=r'images/add_curs.png')

    Button(
        master= footer,
        text="Add",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        image=add_curs_img,
        pady=3,
        padx=15,
        command=lambda: add_course_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Add Course Btn

    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        image=back_img,
        pady=7,
        padx=15,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion Back Btn

    form.mainloop()
# endregion Add Course From


# region Edit Course Form
def edit_course_form(old_title, old_courseCode, old_price, course_grid, username, mainform):
    
    # region Func Edit Btn
    def edit_course_btn_onclick():

        title_str = title.get()
        courseCode_str = courseCode.get()
        price_str = price.get()
        
        status, output = edit_course_bl(
            old_title=old_title,
            old_courseCode=old_courseCode,
            old_price=old_price,
            title=title_str,
            courseCode=courseCode_str,
            price=price_str,
            username=username,
        )
        
        if status == "ERROR":
            messagebox.showerror("ERROR", output)
            
        elif status == "SUCCESS":

            messagebox.showinfo("SUCCESS", output)
            select_id = course_grid.selection()[0]
            course_grid.item(select_id,  values=(title_str, courseCode_str, price_str, username))
            back_btn_onclick()
    # endregion Func Edit Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn
    
    form = Toplevel()

    # region Form Info
    form.title("Edit Course")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images/edit_curs.ico")

    window_height = 500
    window_width = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#808080"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Variable
    title = StringVar(value=old_title)
    courseCode = StringVar(value=old_courseCode)
    price = StringVar(value=old_price)
    # endregion Variable
    
    # region Title
    Label(
        master=body,
        text="Title : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=title,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Title
    
    # region Course Code
    Label(
        master=body,
        text="Course Code : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=courseCode,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Course Code

    # region Price
    Label(
        master=body,
        text="Price : ",
        fg="#0d0d0d",
        bg="#FFF8DC",
        font=("tahoma", 10, "bold"),
        anchor=W
    ).pack(side=TOP, fill=X, padx=10, pady=10)

    Entry(
        master=body,
        bg="#4d4d4d",
        fg="#FFF8DC",
        font=("tahoma", 11, "normal"),
        textvariable=price,
        bd=1
    ).pack(side=TOP, fill=X, padx=10)
    # endregion Price
 
    # region Edit Course Btn
    edit_curs_img = PhotoImage(file=r'images/edit_curs.png')

    Button(
        master=footer,
        text="Edit",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=edit_curs_img,
        compound=LEFT,
        pady=3,
        padx=7,
        command=lambda: edit_course_btn_onclick()
    ).pack(side=LEFT, padx=(0, 10))
    # endregion Edit Course Btn
    
    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=back_img,
        compound=LEFT,
        pady=3,
        padx=7,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion Back Btn
 
    form.mainloop()
# endregion Edit Course Form


# region Assign Course Form
def assign_course_form(username, assign_course_grid, mainform):
    
    # region Load Course
    def load_course():

        status, output = get_course_bl(username)

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":
            for course in output:
                course_grid.insert('', 'end', values=tuple(course.values()))
    # endregion Load Course

    # region Load Student
    def load_student():

        status, output = get_student_bl(username)

        if status == "ERROR":
            messagebox.showerror("ERROR", output)

        elif status == "SUCCESS":

            for student in output:
                select_keys = ['name', 'family', 'nationalCode', 'studentId']
                student={key: student[key] for key in select_keys}
                student_grid.insert('', 'end', values=tuple(student.values()))
    # endregion Load Student

    # region Func Assign Btn
    def assign_btn_onclick():
        
        select_student = student_grid.item(student_grid.focus())['values']
        select_course = course_grid.selection()

        if not select_student:
            messagebox.showerror("ERROR", "Error Select!")

        elif not select_course:
            messagebox.showerror("ERROR", "Error Select!")

        else:

            message_list = []

            for item in select_course:

                course = course_grid.item(item, "values")
                message_list.append(f"Full Name : {select_student[0]} {select_student[1]} - National Code : {select_student[2]} - Course : {course[0]}") 

            answer = messagebox.askyesno(title='Confirmation',
                message=f'Assign Course ?\n {"n".join(message_list)}')

            if answer:
                
                status, output = add_student_course_bl(select_student,course, username)
            
                if status == "ERROR":
                    messagebox.showerror("ERROR", output)
                    
                elif status == "SUCCESS":

                    messagebox.showinfo("SUCCESS", output)

                    for item in select_course:

                        course = course_grid.item(item, "values")

                        assign_course = {
                        "name":select_student[0],
                        "family":select_student[1],
                        "nationalCode":select_student[2],
                        "studentId":select_student[3],
                        "course_title":course[0],
                        "courseCode":course[1],
                        "owner":username,
                        }

                        assign_course_grid.insert('', 'end',values=tuple(assign_course.values()))
    # endregion Func Assign Btn

    # region Func Back Btn
    def back_btn_onclick():

        form.destroy()
        mainform.deiconify()
    # endregion Func Back Btn

    form = Toplevel()

    # region Form Info
    form.title("Assign Course")
    form.resizable(width=False, height=False)
    form.configure(bg="#808080")
    form.iconbitmap(r"images/assign_curs.ico")

    window_width = 1000
    window_height = 400
    screen_width = form.winfo_screenwidth()
    screen_height = form.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    form.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    # endregion Form Info

    # region Frame
    body = Frame(
        master=form,
        bg="#808080"
    )
    body.pack(fill=BOTH, expand=True)

    footer = Frame(
        master=form,
        bg="#9d9d9d",
        height=80
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    # endregion Frame

    # region Coures Grid
    style = ttk.Style()
    style.theme_use('clam')

    course_grid = ttk.Treeview(
        master=body,
        column=("Title", "Course Code"),
        show='headings',
        selectmode="extended",
        displaycolumns=("Title", "Course Code")
    )

    course_grid.column("# 1", anchor=CENTER)
    course_grid.heading("# 1", text="Title")
    course_grid.column("# 2", anchor=CENTER)
    course_grid.heading("# 2", text="Course Code")
    course_grid.pack(side=RIGHT, fill=BOTH, expand=True)
    # endregion Course Grid

    # region Student Grid
    student_grid = ttk.Treeview(
        master=body,
        column=("Name", "Family", "National Code", "Student ID"),
        show='headings',
        selectmode="browse",
        displaycolumns=("Name", "Family","National Code", "Student ID"),
    )
    
    student_grid.column("# 1", anchor=CENTER)
    student_grid.heading("# 1", text="Name")
    student_grid.column("# 2", anchor=CENTER)
    student_grid.heading("# 2", text="Family")
    student_grid.column("# 3", anchor=CENTER)
    student_grid.heading("# 3", text="National Code")
    student_grid.column("# 4", anchor=CENTER)
    student_grid.heading("# 4", text="Student ID")
    student_grid.pack(side=LEFT, fill=BOTH, expand=True)
    # endregion Student Grid

    # region Assign Btn
    assign_curs_img = PhotoImage(file=r'images/assign_curs.png')

    Button(
        master=footer,
        text=" Assign",
        bg="#117521",
        fg="#FFF8DC",
        activebackground="#17ab33",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        image=assign_curs_img,
        compound=LEFT,
        pady=3,
        padx=15,
        command=lambda: assign_btn_onclick()
    ).pack(side=LEFT, padx=10)
    # endregion Assign Btn

    # region Back Btn
    back_img = PhotoImage(file=r'images/back.png')

    Button(
        master=footer,
        text="Back",
        bg="#e81414",
        fg="#FFF8DC",
        activebackground="#ff3c03",
        activeforeground="#FFF8DC",
        font=("tahoma", 10, "bold"),
        compound=LEFT,
        image=back_img,
        pady=3,
        padx=15,
        command=lambda: back_btn_onclick()
    ).pack(side=RIGHT, padx=10)
    # endregion Back Btn

    load_student()
    load_course()
    form.mainloop()
# endregion Assign Course Form


