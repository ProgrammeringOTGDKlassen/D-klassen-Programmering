from econodata import EconomyData, User
import econo_func as ef
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import tkinter.ttk as ttk

class EconomyLoginGui(ttk.Frame):
    def __init__(self, master = None):
        ttk.Frame.__init__(self, master)
        self.data = EconomyData()
        # self.data.create_tables()
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
    
    def is_float(self, money):
        try:
            money = float(money)
            return money
        except ValueError:
            return False

    def is_int(self, money):
        try:
            money = int(money)
            return money
        except ValueError:
            return False

    def add_cat(self):
        category = self.entry_add_cat.get()
        self.data.add_cat(category)
    
    def add_job(self):
        if self.data.has_job(self.userID):
            self.label_error.config(text = 'You already have a job. Delete that first.')
            self.entry_job_name.delete(0, tk.END)
            self.entry_job_salary.delete(0, tk.END)
            self.entry_job_payday.delete(0, tk.END)
        else:
            job_name = self.entry_job_name.get()
            job_salary = self.entry_job_salary.get()
            job_payday = self.entry_job_payday.get()
            job_payday = self.is_int(job_payday)
            job_salary = self.is_float(job_salary)
            if job_salary == False:
                self.label_error.config(text = 'Please make sure you only used numbers!')
                self.label_job_salary.config(foreground = 'red')
            elif job_payday == False:
                self.label_error.config(text = 'Please make sure you only used numbers!')
                self.label_job_payday.config(foreground = 'red')
                self.label_job_salary.config(foreground = 'black')
            else:
                if self.data.add_job(self.userID, job_name, job_salary, job_payday):
                    self.entry_job_name.delete(0, tk.END)
                    self.entry_job_salary.delete(0, tk.END)
                    self.entry_job_payday.delete(0, tk.END)
                    self.label_job_salary.config(foreground = 'black')
                    self.update_job_labels1()

    def remove_job(self):
        self.data.remove_job(self.userID)
        self.update_job_labels2()

    def money_obtained(self):
        money_obtained = self.entry_money_obtained.get()
        money_obtained = self.is_float(money_obtained)
        if money_obtained == False:
            self.label_error.config(text = 'Please make sure you only used numbers!')
            self.label_money_obtained.config(foreground = 'red')
            self.label_sel_cat.config(foreground = 'black')
        else:
            category = self.combo_sel_cat.get()
            if category == "":
                self.label_error.config(text = 'Please select a category!')
                self.label_sel_cat.config(foreground = 'red')
                self.label_money_obtained.config(foreground = 'black')
            else:
                categoryID = self.data.get_cat_id(category)
                if self.data.add_money_obtained(self.userID, categoryID, money_obtained):
                    self.entry_money_obtained.delete(0, tk.END)
                    self.combo_sel_cat.set('')
                    self.label_money_obtained.config(foreground = 'black')
                    self.label_sel_cat.config(foreground = 'black')
                    self.update_money_labels()

    def money_used(self):
        money_used = self.entry_money_used.get()
        money_used = self.is_float(money_used)
        if money_used == False:
            self.label_error.config(text = 'Please make sure you only used numbers!')
            self.label_money_used.config(foreground = 'red')
            self.label_sel_cat.config(foreground = 'black')
        else:
            category = self.combo_sel_cat.get()
            if category == "":
                self.label_error.config(text = 'Please select a category!')
                self.label_sel_cat.config(foreground = 'red')
                self.label_money_used.config(foreground = 'black')
            else:
                categoryID = self.data.get_cat_id(category)
                if self.data.add_money_used(self.userID, categoryID, money_used):
                    self.entry_money_used.delete(0, tk.END)
                    self.combo_sel_cat.set('')
                    self.label_money_used.config(foreground = 'black')
                    self.label_sel_cat.config(foreground = 'black')
                    self.update_money_labels()

    def update_job_labels1(self):
        job = self.data.get_job(self.userID)
        self.data.calc_days_for_payday(self.userID)
        self.label_djob_name = ttk.Label(self.data_panel, text = 'Current job name:')
        self.label_djob_name_v = ttk.Label(self.data_panel, text = f'{job[0]}') 
        self.label_djob_salary = ttk.Label(self.data_panel, text = 'Current salary:')
        self.label_djob_salary_v = ttk.Label(self.data_panel, text = f'{job[1]}')
        self.label_djob_payday = ttk.Label(self.data_panel, text = 'Payment every :')
        self.label_djob_payday_v = ttk.Label(self.data_panel, text = f'{job[2]} days')
        self.label_djob_nextpayment = ttk.Label(self.data_panel, text = 'Next payment:')
        self.label_djob_nextpayment_v = ttk.Label(self.data_panel, text = f'{job[3]}')
        self.button_djob_remove = ttk.Button(self.data_panel, text = 'Remove job', command = self.remove_job, width = 35)
        self.label_djob_name.grid(row = 1, column = 0, padx = (0,0))
        self.label_djob_name_v.grid(row = 1, column = 1, padx = (0,100))
        self.label_djob_salary.grid(row = 2, column = 0, padx = (0,0))
        self.label_djob_salary_v.grid(row = 2, column = 1, padx = (0,100))
        self.label_djob_payday.grid(row = 3, column = 0, padx = (0,0))
        self.label_djob_payday_v.grid(row = 3, column = 1, padx = (0,100))
        self.label_djob_nextpayment.grid(row = 4, column = 0, padx = (0,0))
        self.label_djob_nextpayment_v.grid(row = 4, column = 1, padx = (0,100))
        self.button_djob_remove.grid(row = 5, column = 0, columnspan = 2, pady = (0,93), padx = (0,30))
    
    def update_job_labels2(self):
        self.label_djob_name_v.config(text = '') 
        self.label_djob_salary_v.config(text = '')
        self.label_djob_payday_v.config(text = '')
        self.label_djob_nextpayment_v.config(text = '')

    def update_money_labels(self):
        self.statistics_panel.destroy()
        self.button_panel.destroy()
        self.data_panel.destroy()
        self.build_GUI()

    def build_GUI(self):
        #Different variables etc
        self.button_panel = ttk.Frame(self)
        self.data_panel = ttk.Frame(self)
        self.statistics_panel = ttk.Frame(self)
        catagories = self.data.get_cat_list()
        self.button_panel.grid_columnconfigure(0, minsize = 200)
        self.button_panel.grid_columnconfigure(1, minsize = 200)

        #Button_panel
        self.label_add_cat = ttk.Label(self.button_panel, text = 'Add a new category')
        self.entry_add_cat = ttk.Entry(self.button_panel, width = 23)
        self.button_add_cat = ttk.Button(self.button_panel, text = 'Add category', command = self.add_cat, width = 23)
        self.label_sel_cat = ttk.Label(self.button_panel, text = 'Select category for obtained/used money')
        self.combo_sel_cat = ttk.Combobox(self.button_panel, values = catagories, state = 'readonly', width = 20)
        self.label_money_obtained = ttk.Label(self.button_panel, text = 'Money obtained')
        self.entry_money_obtained = ttk.Entry(self.button_panel, width = 23)
        self.button_money_obtained = ttk.Button(self.button_panel, text = 'Add money obtained', command = self.money_obtained, width = 23)
        self.label_money_used = ttk.Label(self.button_panel, text = 'Money used')
        self.entry_money_used = ttk.Entry(self.button_panel, width = 23)
        self.button_money_used = ttk.Button(self.button_panel, text = 'Add money used', command = self.money_used, width = 23)
        self.label_error = ttk.Label(self.button_panel, text = "", foreground = "red")
        self.label_job_name = ttk.Label(self.button_panel, text = "Add job name")
        self.entry_job_name = ttk.Entry(self.button_panel, width = 23)
        self.label_job_salary = ttk.Label(self.button_panel, text = "Add job salary")
        self.entry_job_salary = ttk.Entry(self.button_panel, width = 23)
        self.label_job_payday = ttk.Label(self.button_panel, text = "Days between payments")
        self.entry_job_payday = ttk.Entry(self.button_panel, width = 23)
        self.button_add_job = ttk.Button(self.button_panel, text = "Add job", command = self.add_job, width = 23)

        self.label_add_cat.grid(row = 1, column = 0, padx = (113,0), pady = 2)
        self.entry_add_cat.grid(row = 1, column = 1, pady = 2)
        self.button_add_cat.grid(row = 1, column = 2, pady = 2, padx = (0,10))
        self.label_sel_cat.grid(row = 2, column = 0, pady = 2)
        self.combo_sel_cat.grid(row = 2, column = 1, pady = 2)
        self.label_money_obtained.grid(row = 3, column = 0, padx = (132,0), pady = 2)
        self.entry_money_obtained.grid(row = 3, column = 1, pady = 2)
        self.button_money_obtained.grid(row = 3, column = 2, pady = 2, padx = (0,10))
        self.label_money_used.grid(row = 4, column = 0, padx = (154,0))
        self.entry_money_used.grid(row = 4, column = 1)
        self.button_money_used.grid(row = 4, column = 2, padx = (0,10))
        self.label_error.grid(row = 0, column = 1)
        self.label_job_name.grid(row = 5, column = 0, padx = (144,0), pady = (10,2))
        self.entry_job_name.grid(row = 5, column = 1, pady = (10,2))
        self.label_job_salary.grid(row = 6, column = 0, padx = (143,0), pady = 2)
        self.entry_job_salary.grid(row = 6, column = 1, pady = 2)
        self.label_job_payday.grid(row = 7, column = 0, padx = (91,0), pady = 2)
        self.entry_job_payday.grid(row = 7, column = 1, pady = 2)
        self.button_add_job.grid(row = 9, column = 1, pady = (2,10))
        
        #Data_panel
        if self.data.has_job(self.userID):
            job = self.data.get_job(self.userID)
            self.data.calc_days_for_payday(self.userID)
            self.label_djob_name = ttk.Label(self.data_panel, text = 'Current job name:')
            self.label_djob_name_v = ttk.Label(self.data_panel, text = f'{job[0]}') 
            self.label_djob_salary = ttk.Label(self.data_panel, text = 'Current salary:')
            self.label_djob_salary_v = ttk.Label(self.data_panel, text = f'{job[1]}')
            self.label_djob_payday = ttk.Label(self.data_panel, text = 'Payment every :')
            self.label_djob_payday_v = ttk.Label(self.data_panel, text = f'{job[2]} days')
            self.label_djob_nextpayment = ttk.Label(self.data_panel, text = 'Next payment:')
            self.label_djob_nextpayment_v = ttk.Label(self.data_panel, text = f'{job[3]}')
            self.button_djob_remove = ttk.Button(self.data_panel, text = 'Remove job', command = self.remove_job, width = 35)
            self.label_djob_name.grid(row = 1, column = 0, padx = (0,0))
            self.label_djob_name_v.grid(row = 1, column = 1, padx = (0,100))
            self.label_djob_salary.grid(row = 2, column = 0, padx = (0,0))
            self.label_djob_salary_v.grid(row = 2, column = 1, padx = (0,100))
            self.label_djob_payday.grid(row = 3, column = 0, padx = (0,0))
            self.label_djob_payday_v.grid(row = 3, column = 1, padx = (0,100))
            self.label_djob_nextpayment.grid(row = 4, column = 0, padx = (0,0))
            self.label_djob_nextpayment_v.grid(row = 4, column = 1, padx = (0,100))
            self.button_djob_remove.grid(row = 5, column = 0, columnspan = 2, pady = (0,93), padx = (0,30))

        balance_v = self.data.calc_current_balance(self.userID)
        self.label_dbalance = ttk.Label(self.data_panel, text = 'Account balance:')
        self.label_dbalance_v = ttk.Label(self.data_panel, text = f'{balance_v}')
        self.label_dbalance.grid(row = 6, column = 0, padx = (130,0))
        self.label_dbalance_v.grid(row = 6, column = 1, padx = (0,100))
        
        #Statisics_panel
        self.x, self.y = self.data.calc_date_balance(self.userID,0)
        self.f = Figure(figsize=(10,5), dpi=100)
        self.f.set_facecolor('#F0F0F0')
        self.a = self.f.add_subplot(111,)
        self.a.plot(self.x, self.y, marker = 'o')
        for i_x, i_y in zip(self.x, self.y):
            self.a.text(i_x, i_y, '   {}'.format(i_y))
        #self.a.set_facecolor('#F0F0F0')

        canvas = FigureCanvasTkAgg(self.f, self.statistics_panel)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, expand=True)
        #Packing
        self.statistics_panel.pack(side = tk.BOTTOM)
        self.data_panel.pack(side = tk.RIGHT)
        self.button_panel.pack(side = tk.TOP)
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
