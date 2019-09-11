import tkinter as tk
import tkinter.ttk as ttk

import sys, os

def nav_to_folder_w_file(folder_path: str):
    abs_file_path = os.path.abspath(__file__)                # Absolute Path of the module
    file_dir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module
    parent_dir = os.path.dirname(file_dir)                   # Directory of the Module directory
    new_path = os.path.join(parent_dir, folder_path)   # Get the directory for StringFunctions
    sys.path.append(new_path)


# GUI--------------------------------------------------------
nav_to_folder_w_file('GUI')
from GUIs import *
# ------------------------------------------------------------


# DATA---------------------------------------------------------
nav_to_folder_w_file('DATA')

# ------------------------------------------------------------


# LOCAL_FOLDER (this folder)----------------------------------
nav_to_folder_w_file('APP')


def loading_screen():
    import cv2

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture('../Loading screen/Loading screen.mp4')

    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        success,frame = cap.read()

        if success == True:

            # Sets the videofile to fullscreen
            cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            # Display the resulting frame
            cv2.imshow("window", frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


def load_login_app():

    loading_screen()

    root = tk.Tk()
    # sets the icon top left to e predefined icon
    root.iconbitmap('../Icons/DAMP_ICON.ico')
    # defines the default windows size
    root.geometry("1280x720")
    # starts windows in maximized size
    root.state('zoomed')

    # defines the app inheriting root as base
    app = DampGui(root)
    # sets the title of the app
    app.master.title('DAMP')
    # starts the app
    app.mainloop()


def load_add_user_app():

    loading_screen()

    root = tk.Tk()
    # sets the icon top left to e predefined icon
    root.iconbitmap('../Icons/DAMP_ICON.ico')
    # defines the default windows size
    root.geometry("1280x720")
    # starts windows in maximized size
    root.state('zoomed')

    # defines the app inheriting root as base
    app = DampGui(root)
    # sets the title of the app
    app.master.title('DAMP')
    # starts the app
    app.mainloop()


def load_main_app():

    loading_screen()

    root = tk.Tk()
    # sets the icon top left to e predefined icon
    root.iconbitmap('../Icons/DAMP_ICON.ico')
    # defines the default windows size
    root.geometry("1280x720")
    # starts windows in maximized size
    root.state('zoomed')

    # defines the app inheriting root as base
    app = DampGui(root)
    # sets the title of the app
    app.master.title('DAMP')
    # starts the app
    app.mainloop()
