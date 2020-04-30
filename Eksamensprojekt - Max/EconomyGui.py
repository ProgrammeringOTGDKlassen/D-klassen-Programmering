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
        pass

    def build_GUI(self):
        self.label_username = ttk.Label(self, text = 'Username')
        self.label_password = ttk.Label(self, text = 'Password')
        self.entry_username = ttk.Entry(self)
        self.entry_password = ttk.Entry(self)
        self.button_login = ttk.Button(self, text = 'Login', command = self.login)
        self.button_create = ttk.Button(self, text = '''Don't have an account?\nSign up here''', command = self.sign_up)

        self.label_username.grid(row = 1, column = 0)
        self.entry_username.grid(row = 2, column = 0)
        self.label_password.grid(row = 3, column = 0)
        self.entry_password.grid(row = 4, column = 0,)
        self.button_login.grid(row = 6, column = 0, pady = 5)
        
        self.button_create.grid(row = 10, column = 0, pady = 10)

        self.pack()


class EconomySignupGui(ttk.Frame):
    pass


class EconomyMainGUI(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = EconomyData()
        self.build_GUI()
    
    def build_GUI(self):
        self.data_panel = ttk.Frame(self)
        self.statistics_panel = ttk.Frame(self)
        self.button_panel = ttk.Frame(self)

        self.button_panel.grid_columnconfigure()


def loginGui():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width/6)
    height = int(screen_height/6)
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (width/2))
    root.geometry(f'{width}x{height}+{x}+{y}')

    app = EconomyLoginGui(root)
    app.master.title('Economy Login')
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
# root = tk.Tk()
# root.geometry('1280x720')
# root.state('zoomed')

# app = Economy_GUI(root)
# app.master.title('Economy')
# app.mainloop()
