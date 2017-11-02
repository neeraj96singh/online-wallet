import sqlite3
import Submit
import recharge_submit
import movie_submit
import unknown1_support
import signup
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
import unknown_support
conn = sqlite3.connect('online_wallet.db')
cursor = conn.execute('''create table if not exists users (id integer primary key AutoIncrement, user_name varchar(50), pwd varchar(50), address varchar(500), phone varchar(20), wallet varchar(10), ltd varchar(100))''')
def vp_start_gui():
    global val, w, root
    root = Tk()
    top = New_Toplevel_1(root)
    unknown_support.init(root, top)
    root.mainloop()
w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel_1(w)
    unknown_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {Courier New} -size 10 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 20 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 14 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        def check():
            chall_user = self.Entry1.get()
            chall_pwd = self.Entry2.get()
            if chall_user == "" and chall_pwd == "":
                self.Message1.configure(text='''User name or Password cannot be blank.''')
            else:
                cursor = conn.execute('''SELECT id  FROM users WHERE user_name = '%s' AND pwd = '%s' ''' % (chall_user, chall_pwd))
                result = cursor.fetchall()
                if len(result) != 0:
                    self.Message1.configure(text='''Successful''')
                    root.destroy()
                    def vp_loggedin_start_gui():
                        global val, w, root
                        root = Tk()
                        unknown1_support.set_Tk_var()
                        top = New_Toplevel_1(root)
                        unknown1_support.init(root, top)
                        root.mainloop()
                    w = None
                    def create_New_Toplevel_1(root, *args, **kwargs):
                        global w, w_win, rt
                        rt = root
                        w = Toplevel(root)
                        unknown1_support.set_Tk_var()
                        top = New_Toplevel_1(w)
                        unknown1_support.init(w, top, *args, **kwargs)
                        return (w, top)
                    def destroy_New_Toplevel_1():
                        global w
                        w.destroy()
                        w = None
                    class New_Toplevel_1():
                        def __init__(self, top=None):
                            _bgcolor = '#d9d9d9'
                            _fgcolor = '#000000'
                            _compcolor = '#d9d9d9'
                            _ana1color = '#d9d9d9'
                            _ana2color = '#d9d9d9'
                            font10 = "-family {Courier New} -size 10 -weight normal -slant" \
                                     " roman -underline 0 -overstrike 0"
                            font13 = "-family {Segoe UI} -size 14 -weight normal -slant " \
                                     "roman -underline 0 -overstrike 0"
                            font14 = "-family {Segoe UI} -size 20 -weight bold -slant " \
                                     "roman -underline 0 -overstrike 0"
                            font15 = "-family {Segoe UI} -size 12 -weight bold -slant " \
                                     "roman -underline 0 -overstrike 0"
                            font16 = "-family {Segoe UI} -size 9 -weight bold -slant roman" \
                                     " -underline 0 -overstrike 0"
                            self.style = ttk.Style()
                            if sys.platform == "win32":
                                self.style.theme_use('winnative')
                            self.style.configure('.', background=_bgcolor)
                            self.style.configure('.', foreground=_fgcolor)
                            self.style.configure('.', font="TkDefaultFont")
                            self.style.map('.', background=
                            [('selected', _compcolor), ('active', _ana2color)])
                            top.geometry("600x450+650+150")
                            top.title("Online Wallet")
                            top.configure(background="#d9d9d9")
                            top.configure(highlightbackground="#d9d9d9")
                            top.configure(highlightcolor="black")
                            def money_submit():
                                amount = self.Entry1.get()
                                amount = (int)(amount.strip())
                                trans = self.TCombobox1.current()
                                if amount != "" and trans != -1:
                                    cursor = conn.execute(
                                        '''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                    conn.commit()
                                    prev_bal = (cursor.fetchone()[0])
                                    if prev_bal == 'NULL':
                                        up_bal = amount
                                    else:
                                        up_bal = (int)(prev_bal) + amount
                                    cursor = conn.execute(
                                        '''update users set wallet = '%s' where user_name = '%s' and pwd = '%s' ''' % (up_bal, chall_user, chall_pwd))
                                    cursor = conn.execute(
                                        '''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                    conn.commit()
                                    bal_up = cursor.fetchone()[0]
                                    self.Label3.configure(text='''Your Balance : Rs. %s''' % (bal_up))
                                    cursor = conn.execute('''update users set ltd = 'Money Added Rs. %s' where user_name = '%s' and pwd = '%s' '''%(amount, chall_user, chall_pwd))
                                    cursor = conn.execute('''select ltd from users where user_name = '%s' and pwd = '%s' '''%(chall_user, chall_pwd))
                                    info = cursor.fetchone()[0]
                                    self.Label5.configure(text='''Last Transaction Details : %s'''%(info))
                                    Submit.vp_moneysubmit_start_gui()
                            def recharge_done():
                                phone = self.Entry2.get()
                                phone = phone.strip()
                                operator = self.TCombobox2.current()
                                if phone != "" and operator != -1:
                                    cursor = conn.execute('''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                    conn.commit()
                                    prev_bal = cursor.fetchone()[0]
                                    if int(prev_bal)>=200:
                                        up_bal = int(prev_bal) - 200
                                        cursor = conn.execute('''update users set wallet = '%s' where user_name = '%s' and pwd = '%s' ''' % (up_bal, chall_user, chall_pwd))
                                        cursor = conn.execute('''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                        conn.commit()
                                        bal_up = cursor.fetchone()[0]
                                        self.Label3.configure(text='''Your Balance : Rs. %s''' % (bal_up))
                                        self.Label5.configure(text='''Last Transaction Details : Recharge Done Rs. 200''')
                                        cursor = conn.execute('''update users set ltd = 'Recharge Done Rs. 200' where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                        cursor = conn.execute('''select ltd from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                        info = cursor.fetchone()[0]
                                        self.Label5.configure(text='''Last Transaction Details : %s''' % (info))
                                        recharge_submit.vp_rechargedone_start_gui()
                                    elif (prev_bal) != 'NULL':
                                        pass
                                    else:
                                        pass
                            def movie_done():
                                location = self.Entry3.get()
                                location = location.strip()
                                movie = self.TCombobox3.current()
                                if location != "" and movie != -1:
                                    cursor = conn.execute('''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                    conn.commit()
                                    prev_bal = cursor.fetchone()[0]
                                    if int(prev_bal) >= 200:
                                        up_bal = int(prev_bal) - 200
                                        cursor = conn.execute('''update users set wallet = '%s' where user_name = '%s' and pwd = '%s' ''' % (up_bal, chall_user, chall_pwd))
                                        cursor = conn.execute('''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                        conn.commit()
                                        bal_up = cursor.fetchone()[0]
                                        self.Label3.configure(text='''Your Balance : Rs. %s''' % (bal_up))
                                        self.Label5.configure(text='''Last Transaction Details : Movie Booked Rs. 200''')
                                        cursor = conn.execute('''update users set ltd = 'Movie Booked Rs. 200' where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                        cursor = conn.execute('''select ltd from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                                        info = cursor.fetchone()[0]
                                        self.Label5.configure(text='''Last Transaction Details : %s''' % (info))
                                        movie_submit.vp_moviedone_start_gui()
                                    if (prev_bal) != 'NULL':
                                        pass
                            def logout():
                                root.destroy()
                                vp_start_gui()
                            self.style.configure('TNotebook.Tab', background=_bgcolor)
                            self.style.configure('TNotebook.Tab', foreground=_fgcolor)
                            self.style.map('TNotebook.Tab',
                                           background=[('selected', _compcolor), ('active', _ana2color)])
                            self.tNo41 = ttk.Notebook(top)
                            self.tNo41.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.01)
                            self.tNo41.configure(width=604)
                            self.tNo41.configure(takefocus="")
                            self.tNo41_t0 = ttk.Frame(self.tNo41)
                            self.tNo41.add(self.tNo41_t0, padding=3)
                            self.tNo41.tab(0, text="Home", underline="-1", )
                            self.TNotebook1_t2 = ttk.Frame(self.tNo41)
                            self.tNo41.add(self.TNotebook1_t2, padding=3)
                            self.tNo41.tab(1, text="Add Money", underline="-1", )
                            self.tNo41_t2 = ttk.Frame(self.tNo41)
                            self.tNo41.add(self.tNo41_t2, padding=3)
                            self.tNo41.tab(2, text="Recharge", underline="-1", )
                            self.tNo41_t3 = ttk.Frame(self.tNo41)
                            self.tNo41.add(self.tNo41_t3, padding=3)
                            self.tNo41.tab(3, text="Movie Tickets", underline="-1", )
                            self.Label1 = Label(self.tNo41_t0)
                            self.Label1.place(relx=0.22, rely=0.05, height=36, width=342)
                            self.Label1.configure(activebackground="#f9f9f9")
                            self.Label1.configure(activeforeground="black")
                            self.Label1.configure(background="#d9d9d9")
                            self.Label1.configure(disabledforeground="#a3a3a3")
                            self.Label1.configure(font=font14)
                            self.Label1.configure(foreground="#000000")
                            self.Label1.configure(highlightbackground="#d9d9d9")
                            self.Label1.configure(highlightcolor="black")
                            self.Label1.configure(text='''Your Online Wallet''')
                            self.Label1.configure(width=342)
                            self.Label2 = Label(self.tNo41_t0)
                            self.Label2.place(relx=0.08, rely=0.19, height=46, width=242)
                            self.Label2.configure(activebackground="#f9f9f9")
                            self.Label2.configure(activeforeground="black")
                            self.Label2.configure(background="#d9d9d9")
                            self.Label2.configure(disabledforeground="#a3a3a3")
                            self.Label2.configure(font=font15)
                            self.Label2.configure(foreground="#000000")
                            self.Label2.configure(highlightbackground="#d9d9d9")
                            self.Label2.configure(highlightcolor="black")
                            self.Label2.configure(text='''Hello %s''' % (chall_user))
                            self.Label3 = Label(self.tNo41_t0)
                            self.Label3.place(relx=0.63, rely=0.21, height=26, width=182)
                            self.Label3.configure(activebackground="#f9f9f9")
                            self.Label3.configure(activeforeground="black")
                            self.Label3.configure(background="#d9d9d9")
                            self.Label3.configure(disabledforeground="#a3a3a3")
                            self.Label3.configure(font=font16)
                            self.Label3.configure(foreground="#000000")
                            self.Label3.configure(highlightbackground="#d9d9d9")
                            self.Label3.configure(highlightcolor="black")
                            cursor = conn.execute('''select wallet from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                            bal = cursor.fetchone()[0]
                            conn.commit()
                            self.Label3.configure(text='''Your Balance : Rs. %s''' % (bal))
                            self.Button1 = Button(self.tNo41_t0)
                            self.Button1.place(relx=0.83, rely=0.0, height=33, width=86)
                            self.Button1.configure(activebackground="#d9d9d9")
                            self.Button1.configure(activeforeground="#000000")
                            self.Button1.configure(background="#d9d9d9")
                            self.Button1.configure(disabledforeground="#a3a3a3")
                            self.Button1.configure(foreground="#000000")
                            self.Button1.configure(highlightbackground="#d9d9d9")
                            self.Button1.configure(highlightcolor="black")
                            self.Button1.configure(pady="0")
                            self.Button1.configure(text='''Logout''')
                            self.Button1.configure(command=logout)
                            self.Label5 = Label(self.tNo41_t0)
                            self.Label5.place(relx=0.07, rely=0.55, height=26, width=270)
                            self.Label5.configure(activebackground="#f9f9f9")
                            self.Label5.configure(activeforeground="black")
                            self.Label5.configure(background="#d9d9d9")
                            self.Label5.configure(disabledforeground="#a3a3a3")
                            self.Label5.configure(foreground="#000000")
                            self.Label5.configure(highlightbackground="#d9d9d9")
                            self.Label5.configure(highlightcolor="black")
                            cursor = conn.execute('''select ltd from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                            info = cursor.fetchone()[0]
                            self.Label5.configure(text='''Last Transaction Details : %s''' % (info))
                            self.Label6 = Label(self.tNo41_t0)
                            self.Label6.place(relx=0.07, rely=0.45, height=26, width=80)
                            self.Label6.configure(activebackground="#f9f9f9")
                            self.Label6.configure(activeforeground="black")
                            self.Label6.configure(background="#d9d9d9")
                            self.Label6.configure(disabledforeground="#a3a3a3")
                            self.Label6.configure(foreground="#000000")
                            self.Label6.configure(highlightbackground="#d9d9d9")
                            self.Label6.configure(highlightcolor="black")
                            cursor = conn.execute('''select id from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                            u_id = cursor.fetchone()[0]
                            self.Label6.configure(text='''User ID : 100%s''' % (u_id))
                            self.Label7 = Label(self.tNo41_t0)
                            self.Label7.place(relx=0.07, rely=0.64, height=26, width=400)
                            self.Label7.configure(activebackground="#f9f9f9")
                            self.Label7.configure(activeforeground="black")
                            self.Label7.configure(background="#d9d9d9")
                            self.Label7.configure(disabledforeground="#a3a3a3")
                            self.Label7.configure(foreground="#000000")
                            self.Label7.configure(highlightbackground="#d9d9d9")
                            self.Label7.configure(highlightcolor="black")
                            cursor = conn.execute('''select address from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                            u_address = cursor.fetchone()[0]
                            self.Label7.configure(text='''Address : %s''' % (u_address))
                            self.Label8 = Label(self.tNo41_t0)
                            self.Label8.place(relx=0.07, rely=0.74, height=26, width=130)
                            self.Label8.configure(activebackground="#f9f9f9")
                            self.Label8.configure(activeforeground="black")
                            self.Label8.configure(background="#d9d9d9")
                            self.Label8.configure(disabledforeground="#a3a3a3")
                            self.Label8.configure(foreground="#000000")
                            self.Label8.configure(highlightbackground="#d9d9d9")
                            self.Label8.configure(highlightcolor="black")
                            cursor = conn.execute('''select phone from users where user_name = '%s' and pwd = '%s' ''' % (chall_user, chall_pwd))
                            u_phone = cursor.fetchone()[0]
                            self.Label8.configure(text='''Phone No : %s''' % (u_phone))
                            self.Label4 = Label(self.TNotebook1_t2)
                            self.Label4.place(relx=0.32, rely=0.07, height=46, width=202)
                            self.Label4.configure(background="#d9d9d9")
                            self.Label4.configure(disabledforeground="#a3a3a3")
                            self.Label4.configure(font=font14)
                            self.Label4.configure(foreground="#000000")
                            self.Label4.configure(text='''Add Money''')
                            self.Label4.configure(width=202)
                            self.Label9 = Label(self.TNotebook1_t2)
                            self.Label9.place(relx=0.1, rely=0.36, height=26, width=192)
                            self.Label9.configure(background="#d9d9d9")
                            self.Label9.configure(disabledforeground="#a3a3a3")
                            self.Label9.configure(font=font13)
                            self.Label9.configure(foreground="#000000")
                            self.Label9.configure(text='''Enter the Amount :''')
                            self.Label9.configure(width=192)
                            self.Entry1 = Entry(self.TNotebook1_t2)
                            self.Entry1.place(relx=0.52, rely=0.36, relheight=0.06, relwidth=0.34)
                            self.Entry1.configure(background="white")
                            self.Entry1.configure(disabledforeground="#a3a3a3")
                            self.Entry1.configure(font=font10)
                            self.Entry1.configure(foreground="#000000")
                            self.Entry1.configure(insertbackground="black")
                            self.Label10 = Label(self.TNotebook1_t2)
                            self.Label10.place(relx=0.08, rely=0.5, height=36, width=262)
                            self.Label10.configure(background="#d9d9d9")
                            self.Label10.configure(disabledforeground="#a3a3a3")
                            self.Label10.configure(font=font13)
                            self.Label10.configure(foreground="#000000")
                            self.Label10.configure(text='''Choose Payment Option :''')
                            self.Label10.configure(width=262)
                            self.Button2 = Button(self.TNotebook1_t2)
                            self.Button2.place(relx=0.37, rely=0.86, height=33, width=136)
                            self.Button2.configure(activebackground="#d9d9d9")
                            self.Button2.configure(activeforeground="#000000")
                            self.Button2.configure(background="#d9d9d9")
                            self.Button2.configure(disabledforeground="#a3a3a3")
                            self.Button2.configure(foreground="#000000")
                            self.Button2.configure(highlightbackground="#d9d9d9")
                            self.Button2.configure(highlightcolor="black")
                            self.Button2.configure(pady="0")
                            self.Button2.configure(text='''Add Money''')
                            self.Button2.configure(width=136)
                            self.Button2.configure(command=money_submit)
                            self.TCombobox1 = ttk.Combobox(self.TNotebook1_t2)
                            self.TCombobox1.place(relx=0.55, rely=0.52, relheight=0.06, relwidth=0.31)
                            self.value_list = ['Credit Card', 'Debit Card', 'Net Banking', 'UPI/Wallet']
                            self.TCombobox1.configure(values=self.value_list)
                            self.TCombobox1.configure(textvariable=unknown1_support.combobox)
                            self.TCombobox1.configure(takefocus="")
                            self.TCombobox1.configure(text='''''')
                            self.Label11 = Label(self.tNo41_t2)
                            self.Label11.place(relx=0.32, rely=0.07, height=46, width=192)
                            self.Label11.configure(background="#d9d9d9")
                            self.Label11.configure(disabledforeground="#a3a3a3")
                            self.Label11.configure(font=font14)
                            self.Label11.configure(foreground="#000000")
                            self.Label11.configure(text='''Recharge''')
                            self.Label11.configure(width=192)
                            self.Label12 = Label(self.tNo41_t2)
                            self.Label12.place(relx=0.03, rely=0.33, height=26, width=292)
                            self.Label12.configure(background="#d9d9d9")
                            self.Label12.configure(disabledforeground="#a3a3a3")
                            self.Label12.configure(font=font13)
                            self.Label12.configure(foreground="#000000")
                            self.Label12.configure(text='''Enter your Mobile Number :''')
                            self.Label12.configure(width=292)
                            self.Entry2 = Entry(self.tNo41_t2)
                            self.Entry2.place(relx=0.58, rely=0.33, relheight=0.06, relwidth=0.34)
                            self.Entry2.configure(background="white")
                            self.Entry2.configure(disabledforeground="#a3a3a3")
                            self.Entry2.configure(font=font10)
                            self.Entry2.configure(foreground="#000000")
                            self.Entry2.configure(insertbackground="black")
                            self.Label13 = Label(self.tNo41_t2)
                            self.Label13.place(relx=0.0, rely=0.45, height=26, width=282)
                            self.Label13.configure(background="#d9d9d9")
                            self.Label13.configure(disabledforeground="#a3a3a3")
                            self.Label13.configure(font=font13)
                            self.Label13.configure(foreground="#000000")
                            self.Label13.configure(text='''Choose Your Operator :''')
                            self.Label13.configure(width=282)
                            self.Button3 = Button(self.tNo41_t2)
                            self.Button3.place(relx=0.35, rely=0.86, height=33, width=196)
                            self.Button3.configure(activebackground="#d9d9d9")
                            self.Button3.configure(activeforeground="#000000")
                            self.Button3.configure(background="#d9d9d9")
                            self.Button3.configure(disabledforeground="#a3a3a3")
                            self.Button3.configure(foreground="#000000")
                            self.Button3.configure(highlightbackground="#d9d9d9")
                            self.Button3.configure(highlightcolor="black")
                            self.Button3.configure(pady="0")
                            self.Button3.configure(text='''Recharge''')
                            self.Button3.configure(width=196)
                            self.Button3.configure(command=recharge_done)
                            self.TCombobox2 = ttk.Combobox(self.tNo41_t2)
                            self.TCombobox2.place(relx=0.6, rely=0.48, relheight=0.06, relwidth=0.31)
                            self.value_list = ['Airtel', 'Vodafone', 'Reliance Jio', 'IDEA', 'BSNL']
                            self.TCombobox2.configure(values=self.value_list)
                            self.TCombobox2.configure(textvariable=unknown1_support.combobox)
                            self.TCombobox2.configure(takefocus="")
                            self.Label14 = Label(self.tNo41_t3)
                            self.Label14.place(relx=0.32, rely=0.05, height=51, width=220)
                            self.Label14.configure(background="#d9d9d9")
                            self.Label14.configure(disabledforeground="#a3a3a3")
                            self.Label14.configure(font=font14)
                            self.Label14.configure(foreground="#000000")
                            self.Label14.configure(text='''Movie Tickets''')
                            self.Label15 = Label(self.tNo41_t3)
                            self.Label15.place(relx=0.05, rely=0.31, height=37, width=215)
                            self.Label15.configure(background="#d9d9d9")
                            self.Label15.configure(disabledforeground="#a3a3a3")
                            self.Label15.configure(font=font13)
                            self.Label15.configure(foreground="#000000")
                            self.Label15.configure(text='''Enter your location :''')
                            self.Entry3 = Entry(self.tNo41_t3)
                            self.Entry3.place(relx=0.53, rely=0.33, relheight=0.06, relwidth=0.34)
                            self.Entry3.configure(background="white")
                            self.Entry3.configure(disabledforeground="#a3a3a3")
                            self.Entry3.configure(font=font10)
                            self.Entry3.configure(foreground="#000000")
                            self.Entry3.configure(insertbackground="black")
                            self.Label16 = Label(self.tNo41_t3)
                            self.Label16.place(relx=0.05, rely=0.45, height=37, width=204)
                            self.Label16.configure(background="#d9d9d9")
                            self.Label16.configure(disabledforeground="#a3a3a3")
                            self.Label16.configure(font=font13)
                            self.Label16.configure(foreground="#000000")
                            self.Label16.configure(text='''Select your Movie :''')
                            self.Button4 = Button(self.tNo41_t3)
                            self.Button4.place(relx=0.32, rely=0.88, height=33, width=236)
                            self.Button4.configure(activebackground="#d9d9d9")
                            self.Button4.configure(activeforeground="#000000")
                            self.Button4.configure(background="#d9d9d9")
                            self.Button4.configure(disabledforeground="#a3a3a3")
                            self.Button4.configure(foreground="#000000")
                            self.Button4.configure(highlightbackground="#d9d9d9")
                            self.Button4.configure(highlightcolor="black")
                            self.Button4.configure(pady="0")
                            self.Button4.configure(text='''Book''')
                            self.Button4.configure(width=236)
                            self.Button4.configure(command=movie_done)
                            self.TCombobox3 = ttk.Combobox(self.tNo41_t3)
                            self.TCombobox3.place(relx=0.55, rely=0.5, relheight=0.06, relwidth=0.31)
                            self.value_list = ['Dabbang 2', 'Bahubali', 'Don 2', 'Rustam', 'PK']
                            self.TCombobox3.configure(values=self.value_list)
                            self.TCombobox3.configure(textvariable=unknown1_support.combobox)
                            self.TCombobox3.configure(takefocus="")
                            self.TCombobox3.configure(text='''''')
                    if __name__ == '__main__':
                        vp_loggedin_start_gui()
                else:
                    self.Message1.configure(text='''Invalid User name or Password.''')
        def signup_new():
            signup.vp_signup_start_gui()
        top.geometry("600x450+650+150")
        top.title("New Toplevel 1")
        top.configure(background="#d9d9d9")
        self.Label1 = Label(top)
        self.Label1.place(relx=0.27, rely=0.04, height=56, width=262)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Online Wallet''')
        self.Label1.configure(width=262)
        self.Label2 = Label(top)
        self.Label2.place(relx=0.12, rely=0.31, height=37, width=141)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''User Name :''')
        self.Label3 = Label(top)
        self.Label3.place(relx=0.12, rely=0.44, height=37, width=119)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Password :''')
        self.Button1 = Button(top)
        self.Button1.place(relx=0.33, rely=0.64, height=33, width=96)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Sign In''')
        self.Button1.configure(width=96)
        self.Button1.configure(command=check)
        self.Button2 = Button(top)
        self.Button2.place(relx=0.53, rely=0.64, height=33, width=86)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Sign Up''')
        self.Button2.configure(width=86)
        self.Button2.configure(command=signup_new)
        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.52, rely=0.33, relheight=0.05, relwidth=0.34)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.52, rely=0.47, relheight=0.05, relwidth=0.34)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Message1 = Message(top)
        self.Message1.place(relx=0.32, rely=0.8, relheight=0.07, relwidth=0.39)
        self.Message1.configure(background="#737373")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#89787a")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''''')
        self.Message1.configure(width=236)
if __name__ == '__main__':
    vp_start_gui()
