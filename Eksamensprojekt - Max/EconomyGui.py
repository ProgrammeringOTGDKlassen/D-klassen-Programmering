from econodata import EconomyData, User
import econo_func as ef
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
            userID = self.data.get_userID(username)
            self.master.destroy()
            mainGui(userID)
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
    
    def sign_up(self):
        self.username = self.entry_username.get()
        self.first_name = self.entry_first_name.get()
        self.last_name = self.entry_last_name.get()
        self.email = self.entry_email.get()
        self.password = self.entry_password.get()
        if self.username == "" or self.first_name == "" or self.last_name == "" or self.email == "" or self.password == "":
            self.err_box()
        else:
            self.user = User(self.first_name, self.last_name, self.username, self.email, self.password)
            self.data.add_user(self.user)
            self.login()

    def err_box(self):
        self.label_error.config(text = "Please fill out all entries!", foreground = "red")
        self.label_password.config(foreground = "black")
        self.label_conf_password.config(foreground = "black")
        self.label_username.config(foreground = "black")

    def err_username(self, username):
        self.label_error.config(text = "Username already taken!", foreground = "red")
        self.label_username.config(foreground = "red")

    def err_password(self):
        self.label_error.config(text = "Passwords aren't the same!", foreground = "red")
        self.label_password.config(foreground = "red")
        self.label_conf_password.config(foreground = "red")
        self.label_username.config(foreground = "black")

    def check_sign_up(self):
        self.username = self.entry_username.get()
        if not self.data.check_username(self.username):
            self.err_username(self.username)
        else:
            self.password = self.entry_password.get()
            self.conf_password = self.entry_conf_password.get()
            if self.password == self.conf_password:
                self.sign_up()
            else:
                self.err_password()

    def build_GUI(self):
        self.label_username = ttk.Label(self, text = 'Username:')
        self.label_first_name = ttk.Label(self, text = 'Fist name:')
        self.label_last_name = ttk.Label(self, text = 'Last name:')
        self.label_email = ttk.Label(self, text = 'Email:')
        self.label_password = ttk.Label(self, text = 'Password:')
        self.label_conf_password = ttk.Label(self, text = 'Confirm Password:')
        self.label_error = ttk.Label(self, text = "")
        self.entry_username = ttk.Entry(self)
        self.entry_first_name = ttk.Entry(self)
        self.entry_last_name = ttk.Entry(self)
        self.entry_email = ttk.Entry(self)
        self.entry_password = ttk.Entry(self, show = "*")
        self.entry_conf_password = ttk.Entry(self, show = "*")
        self.button_create_acc = ttk.Button(self, text = 'Create account', command = self.check_sign_up)
        self.button_login = ttk.Button(self, text = 'Have an account?\nLogin', command = self.login)
        self.label_error.grid(row = 0, column = 0)
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
    def __init__(self, userID, master = None):
        ttk.Frame.__init__(self, master)
        self.data = EconomyData()
        self.userID = userID
        self.build_GUI()
    
    def build_GUI(self):
        self.data_panel = ttk.Frame(self)
        self.statistics_panel = ttk.Frame(self)
        self.button_panel = ttk.Frame(self)
        self.optained_v = self.data.get_optained(self.userID)
        self.optained = ttk.Label(self.data_panel, text = f'test {self.optained_v}')
        self.label_test = ttk.Label(self.statistics_panel, text = "æprt")
        self.optained.grid(row = 1, column = 0)
        self.label_test.grid(row = 1, column = 0)
        self.data_panel.pack(side = tk.LEFT)
        self.statistics_panel.pack(side = tk.LEFT)
        self.pack()


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
    height = int(screen_height/3)
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (width/2))
    root.geometry(f'{width}x{height}+{x}+{y}')

    app = EconomySignupGui(root)
    app.master.title('Economy Signup')
    app.mainloop()

def mainGui(userID: str):
    root = tk.Tk()
    root.geometry('1920x1080')
    root.state('zoomed')
    app = EconomyMainGUI(userID, root)
    app.master.title('Economy logged in')
    app.mainloop()


loginGui()
