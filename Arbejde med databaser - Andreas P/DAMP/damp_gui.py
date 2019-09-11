from damp_datalayer import DAMPData
import tkinter as tk
import tkinter.ttk as ttk
import cv2

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('./Loading screen/Loading screen.mp4')

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



class Damp_Gui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.data = DAMPData()

        self.build_GUI()


    def build_GUI(self):
        pass

root = tk.Tk()
# sets the icon top left to e predefined icon
root.iconbitmap(r'C:\Users\andre\OneDrive - Syddansk Erhvervsskole\GitHub\D-klassen-Programmering\Arbejde med databaser - Andreas P\DAMP\Icons\DAMP_ICON.ico')
# defines the default windows size
root.geometry("1280x720")
# starts windows in maximized size
root.state('zoomed')

app = Damp_Gui(root)
app.master.title('DAMP')

app.mainloop()
