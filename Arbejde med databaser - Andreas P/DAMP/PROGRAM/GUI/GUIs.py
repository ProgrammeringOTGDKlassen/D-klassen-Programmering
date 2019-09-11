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
from damp_datalayer import DAMPData
# ------------------------------------------------------------


# APP---------------------------------------------------------
nav_to_folder_w_file('APP')
from loading import *
# ------------------------------------------------------------


# LOCAL_FOLDER (this folder)----------------------------------
nav_to_folder_w_file('GUI')



# classes
# ----------------------------------------------------------------------

# separate GUI as the login-screen
class DampLoginGui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass


# separate GUI as the "add-user"-screen
class DampAddUserGui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass


# main GUI
class DampGui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass

