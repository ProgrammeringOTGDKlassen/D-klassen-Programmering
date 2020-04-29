import datetime
import math



def get_date():
    d = datetime.datetime.now()
    date = d.strftime("%Y %B %d")
    return date