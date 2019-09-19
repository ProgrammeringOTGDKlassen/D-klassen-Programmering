import sys, os


def nav_to_folder_w_file(folder_path: str):
    abs_file_path = os.path.abspath(__file__)                # Absolute Path of the module
    file_dir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
    parent_dir = os.path.dirname(file_dir)                   # Directory of the Module directory
    new_path = os.path.join(parent_dir, folder_path)   # Get the directory for StringFunctions
    sys.path.append(new_path)


# GUI--------------------------------------------------------
nav_to_folder_w_file('GUI')

# ------------------------------------------------------------


# DATA---------------------------------------------------------
nav_to_folder_w_file('DATA')
from damp_datalayer import DAMPData
# ------------------------------------------------------------


# LOCAL_FOLDER (this folder)----------------------------------
nav_to_folder_w_file('APP')


class eventhandler():
  
  def __init__(self, data):
    self.data = data
    self.db = data.db


  def check_correct_password(self, username: str, password: str):
    c = self.db.cursor()
    if not username or not password:
      return False
    c.execute('SELECT password, id FROM users WHERE username = ?', (username,))
    p = c.fetchone()
    data_password = self.data.decrypt_password(p[0])
    if data_password == password:
        return True, p[1]
    else:
        return False, None


  def check_paramators_add_user(self, user):
    if not user.name or not user.email or not user.country or not user.username or not user.password:
      return False
    else:
      return True


  def check_same_password(self, password, re_password):
    if password == re_password:
      return True
    else:
      return False