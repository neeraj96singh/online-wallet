import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
import signup_support
import sqlite3
conn = sqlite3.connect('online_wallet.db')
def vp_signup_start_gui():
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    signup_support.init(root, top)
    root.mainloop()
w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    signup_support.init(w, top, *args, **kwargs)
    return (w, top)
def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None
class New_Toplevel_1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        top.geometry("600x450+611+349")
        top.title("Sign Up")
        top.configure(background="#d9d9d9")
        def create():
            name = self.Entry1.get()
            name = name.strip()
            pwd = self.Entry2.get()
            pwd = pwd.strip()
            address = self.Entry3.get()
            address = address.strip()
            phone = self.Entry4.get()
            phone = phone.strip()
            cursor = conn.execute('''select * from users where user_name = '%s' '''%(name))
            if cursor.fetchone():
                prev_user = 1
            else:
                prev_user = 0
            if name == '' and pwd == '' and address == '' and phone == '':
                self.Message1.configure(text = '''Fields cannot be blanked''')
            elif prev_user != 0:
                self.Message1.configure(text='''User name already exists''')
            else:
                cursor = conn.execute('''insert into users(user_name, pwd, address, phone, wallet, ltd) values('%s', '%s', '%s', '%s', 'NULL', 'NULL') '''%(name, pwd, address, phone))
                conn.commit()
                self.Message1.configure(text='''Account created successfully. Login to continue''')
        self.Label1 = Label(top)
        self.Label1.place(relx=0.27, rely=0.09, height=46, width=262)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''New User''')
        self.Label1.configure(width=262)
        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.31, height=26, width=57)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Name :''')
        self.Label3 = Label(top)
        self.Label3.place(relx=0.08, rely=0.4, height=26, width=79)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Password :''')
        self.Label4 = Label(top)
        self.Label4.place(relx=0.08, rely=0.49, height=26, width=70)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Address :''')
        self.Label5 = Label(top)
        self.Label5.place(relx=0.08, rely=0.58, height=26, width=116)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Phone Number :''')
        self.Message1 = Message(top)
        self.Message1.place(relx=0.42, rely=0.8, relheight=0.18, relwidth=0.34)
        self.Message1.configure(background="#6a6a6a")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''''')
        self.Message1.configure(width=70)
        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.42, rely=0.31, relheight=0.05, relwidth=0.34)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.42, rely=0.4, relheight=0.05, relwidth=0.34)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.42, rely=0.49, relheight=0.05, relwidth=0.34)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.42, rely=0.58, relheight=0.07, relwidth=0.34)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Button1 = Button(top)
        self.Button1.place(relx=0.38, rely=0.71, height=33, width=96)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Sign Up''')
        self.Button1.configure(width=96)
        self.Button1.configure(command = create)
if __name__ == '__main__':
    vp_signup_start_gui()


