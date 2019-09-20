import tkinter as tk
import tkinter.ttk as ttk

import sys, os


def nav_to_folder_w_file(folder_path: str):
    abs_file_path = os.path.abspath(__file__)                # Absolute Path of the module
    file_dir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
    parent_dir = os.path.dirname(file_dir)                   # Directory of the Module directory
    new_path = os.path.join(parent_dir, folder_path)   # Get the directory for StringFunctions
    sys.path.append(new_path)


# DATA--------------------------------------------------------
nav_to_folder_w_file('DATA')
from damp_datalayer import DAMPData, User, Game
# ------------------------------------------------------------


# APP---------------------------------------------------------
nav_to_folder_w_file('APP')
import loading
from events import eventhandler
# ------------------------------------------------------------


# separate GUI as the login-screen
class DampLoginGui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()
        self.app_evnethandler = eventhandler(self.data)

        self.build_GUI()


    def launch_DAMP(self, userID):
        self.master.destroy()
        loading.load_main_app(userID)


    def returning(self, event):
        self.sign_in()


    def sign_in(self):
        username = self.name_entry.get()
        password = self.pass_entry.get()
        valid, userID = self.app_evnethandler.check_correct_password(username = username, password = password)
        if valid and userID != None:
            self.launch_DAMP(userID)
        else:
            print('Forkert!')


    def launch_add_user(self):
        self.master.destroy()
        loading.load_add_user_app()


    def build_GUI(self):
        # defining elements of GUI
        self.username_label = tk.Label(self, text = 'Username')
        self.password_label = tk.Label(self, text = 'Password')
        self.name_entry = tk.Entry(self)
        self.pass_entry = tk.Entry(self)
        self.but_sign_in = ttk.Button(self, text = 'Sign In', command = self.sign_in)
        self.create_user_label = tk.Label(self, text = "Don't have an account?")
        self.but_create_user = ttk.Button(self, text = 'Create User', command = self.launch_add_user)

        # placing elements of GUI
        self.username_label.grid(row = 0, sticky = tk.E)
        self.password_label.grid(row = 1, sticky = tk.E)
        self.name_entry.grid(row = 0, column = 1)
        self.pass_entry.grid(row = 1, column = 1)

        self.but_sign_in.grid(row = 3, column = 1)

        self.create_user_label.grid(row = 4, sticky = tk.E, pady=(20, 10))
        self.but_create_user.grid(row = 4, column = 1, pady=(20, 10))

        self.master.bind('<Return>', self.returning)

        self.pack()


# separate GUI as the "add-user"-screen
class DampAddUserGui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()
        self.app_evnethandler = eventhandler(self.data)

        self.build_GUI()


    def returning(self, event):
        self.add_user()


    def add_user(self):
        same_password = self.app_evnethandler.check_same_password(self.password_entry.get(), self.re_password_entry.get())
        if same_password:
            encrypt_password = self.data.encrypt_password(self.password_entry.get())
            u = User(self.name_entry.get(), self.mail_entry.get(), self.country_entry.get(), self.username_entry.get(), encrypt_password, 0)
            correct_parameters = self.app_evnethandler.check_paramators_add_user(u)
            if correct_parameters:
                userID = self.data.add_user(u)
                self.launch_DAMP(userID)
            else:
                print('Not all paramaters has been met')
        else:
            print('Not the same password')


    def launch_DAMP(self, userID):
        self.master.destroy()
        loading.load_main_app(userID)


    def launch_signin(self):
        self.destroy()
        self.master.destroy()
        loading.load_login_app()


    def build_GUI(self):
        # defining elements of GUI
        self.name_label = tk.Label(self, text = 'Name')
        self.mail_label = tk.Label(self, text = 'E-mail')
        self.country_label = tk.Label(self, text = 'Country')
        self.username_label = tk.Label(self, text = 'Username')
        self.password_label = tk.Label(self, text = 'Password')
        self.re_password_label = tk.Label(self, text = 'Re-enter Password')
        
        self.name_entry = tk.Entry(self)
        self.mail_entry = tk.Entry(self)
        self.country_entry = tk.Entry(self)
        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self)
        self.re_password_entry = tk.Entry(self)

        self.but_sign_in = ttk.Button(self, text = 'Sign Up', command = self.add_user)
        self.create_user_label = tk.Label(self, text = "Already have an account?")
        self.but_create_user = ttk.Button(self, text = 'Sign In', command = self.launch_signin)

        # placing elements of GUI
        self.name_label.grid(row = 0, sticky = tk.E)
        self.mail_label.grid(row = 1, sticky = tk.E)
        self.country_label.grid(row = 2, sticky = tk.E)
        self.username_label.grid(row = 3, sticky = tk.E)
        self.password_label.grid(row = 4, sticky = tk.E)
        self.re_password_label.grid(row = 5, sticky = tk.E)

        self.name_entry.grid(row = 0, column = 1)
        self.mail_entry.grid(row = 1, column = 1)
        self.country_entry.grid(row = 2, column = 1)
        self.username_entry.grid(row = 3, column = 1)
        self.password_entry.grid(row = 4, column = 1)
        self.re_password_entry.grid(row = 5, column = 1)

        self.but_sign_in.grid(row = 6, column = 1)

        self.create_user_label.grid(row = 7, sticky = tk.E, pady=(20, 10))
        self.but_create_user.grid(row = 7, column = 1, pady=(20, 10))

        self.master.bind('<Return>', self.returning)

        self.pack()


# main GUI
class DampGui(ttk.Frame):

    def __init__(self, master=None, userID=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()
        self.userID = userID

        self.get_user()
        self.build_GUI()
        self.update()


    def get_user(self):
        # defining the active user
        self.a_user = self.data.get_user_from_id(self.userID)


    def update(self):
        l = self.data.get_games_list(self.userID)
        self.games_view.delete(*self.games_view.get_children())
        for g in l:
            self.games_view.insert("", tk.END, values=(g.name, g.id))


    def build_GUI(self):
        self.window_height = self.master.winfo_height()
        self.window_width = self.master.winfo_width()
        
        self.navbar_height = (self.window_height * 0.10)
        self.navbar_width = self.window_width
        self.navbar = tk.Frame(self, width = self.navbar_width, height = self.navbar_height)

        self.sidebar_height = self.window_height - self.navbar_height
        self.sidebar_width = (self.window_width * 0.20)
        self.sidebar = tk.Frame(self, width = self.sidebar_width, height = self.sidebar_height)
        
        self.main_window_height = self.window_height - self.navbar_height
        self.main_window_width = self.window_width - self.sidebar_width
        self.main_window = tk.Frame(self, width = self.main_window_width, height = self.main_window_height)

        self.name_label = tk.Label(self.navbar, text = f'{self.a_user.name}')
        self.active_years = tk.Label(self.navbar, text = f'{self.a_user.active_years} years of service')
        self.name_label.grid(row = 0, column = 0)
        self.active_years.grid(row = 1, column = 0)

        self.games_view = ttk.Treeview(self.sidebar, column = ("column1", "column2"), show = 'headings')
        self.games_view.heading("#1", text="Games")
        self.games_view.heading("#2", text="id")
        self.games_view["displaycolumns"] = ("column1",)
        self.games_view.pack(side = tk.TOP)

        self.navbar.pack(side = tk.TOP)
        self.sidebar.pack(side = tk.LEFT)
        self.main_window.pack(side = tk.LEFT)
        self.pack()