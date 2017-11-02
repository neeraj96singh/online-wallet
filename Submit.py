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
import Submit_support
def vp_moneysubmit_start_gui():
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    Submit_support.init(root, top)
    root.mainloop()
w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
    Submit_support.init(w, top, *args, **kwargs)
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
        top.geometry("400x100+650+189")
        top.title("Transaction Successful")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.lab37 = Label(top)
        self.lab37.place(relx=-0.02, rely=0.31, height=26, width=602)
        self.lab37.configure(background="#d9d9d9")
        self.lab37.configure(disabledforeground="#a3a3a3")
        self.lab37.configure(foreground="#000000")
        self.lab37.configure(text="Money Added Successfully")
        self.lab37.configure(width=602)
        self.lab37.place(relx=-0.25, rely=0.25)
if __name__ == '__main__':
    vp_moneysubmit_start_gui()