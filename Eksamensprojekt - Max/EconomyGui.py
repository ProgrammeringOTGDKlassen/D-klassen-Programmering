from econodata import EconomyData, User
import tkinter as tk
import tkinter.ttk as ttk

class EconomyLoginGui(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = EconomyData()
        self.build_GUI()
    
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if self.data.user_login(username, password):
            self.master.destroy()
            mainGui()
        else:
            print("Du fik sgu corona")
        
    def sign_up(self):
        self.master.destroy()
        signUpGui()

    def build_GUI(self):
        self.label_username = ttk.Label(self, text = 'Username:')
        self.label_password = ttk.Label(self, text = 'Password:')
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show = "*")
        self.button_login = ttk.Button(self, text = 'Login', command = self.login)
        self.button_create = ttk.Button(self, text = '''Don't have an account?\nSign up here''', command = self.sign_up)

        self.label_username.grid(row = 1, column = 0)
        self.entry_username.grid(row = 2, column = 0)
        self.label_password.grid(row = 3, column = 0)
        self.entry_password.grid(row = 4, column = 0)
        self.button_login.grid(row = 6, column = 0, pady = 10)
        
        self.button_create.grid(row = 10, column = 0)

        self.pack()


class EconomySignupGui(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = EconomyData()
        self.build_GUI()

    def login(self):
        self.master.destroy()
        loginGui()

    def sign_up_func(self):
        pass

    def build_GUI(self):
        self.label_username = ttk.Label(self, text = 'Username:')
        self.label_first_name = ttk.Label(self, text = 'Fist name:')
        self.label_last_name = ttk.Label(self, text = 'Last name:')
        self.label_email = ttk.Label(self, text = 'Email:')
        self.label_password = ttk.Label(self, text = 'Password:')
        self.label_conf_password = ttk.Label(self, text = 'Confirm Password:')
        self.entry_username = ttk.Entry(self)
        self.entry_first_name = ttk.Entry(self)
        self.entry_last_name = ttk.Entry(self)
        self.entry_email = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show = "*")
        self.entry_conf_password = ttk.Entry(self, show = "*")
        self.button_create_acc = ttk.Button(self, text = 'Create account', command = self.sign_up_func)
        self.button_login = ttk.Button(self, text = 'Have an account?\nLogin', command = self.login)
        
        self.label_username.grid(row = 1, column = 0)
        self.entry_username.grid(row = 2, column = 0)
        self.label_first_name.grid(row = 3, column = 0)
        self.entry_first_name.grid(row = 4, column = 0)
        self.label_last_name.grid(row = 5, column = 0)
        self.entry_last_name.grid(row = 6, column = 0)
        self.label_email.grid(row = 7, column = 0)
        self.entry_email.grid(row = 8, column = 0)
        self.label_password.grid(row = 9, column = 0)
        self.entry_password.grid(row = 10, column = 0,)
        self.label_conf_password.grid(row = 11, column = 0)
        self.entry_conf_password.grid(row = 12, column = 0)

        self.button_create_acc.grid(row = 13, column = 0, pady = 10)
        self.button_login.grid(row = 14, column = 0)
        self.pack()

class EconomyMainGUI(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = EconomyData()
        self.build_GUI()
    
    def build_GUI(self):
        self.data_panel = ttk.Frame(self)
        self.statistics_panel = ttk.Frame(self)
        self.button_panel = ttk.Frame(self)

def loginGui():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width/6)
    height = int(screen_height/6)
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    root.geometry(f'{width}x{height}+{x}+{y}')

    app = EconomyLoginGui(root)
    app.master.title('Economy Login')
    app.mainloop()

def signUpGui():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width/8)
    height = int(screen_height/3.2)
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (width/2))
    root.geometry(f'{width}x{height}+{x}+{y}')

    app = EconomySignupGui(root)
    app.master.title('Economy Signup')
    app.mainloop()

def mainGui():
    EconomyLoginGui().master.destroy()
    root = tk.Tk()
    root.geometry('1920x1080')
    root.state('zoomed')
    app = EconomyMainGUI(root)
    app.master.title('Economy logged in')
    app.mainloop()


loginGui()
