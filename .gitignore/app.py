import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk() #root holds the body of the whole app, all things get attached to the root
apps = []
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)
canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42") #makes a green canvas
canvas.pack() #attaches canvas to root

frame = tk.Frame(root, bg = "white")#places a white frame on top of the canvas
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1) #width/height dictate size of frame, relx/rely determine placement

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg = "#263D42", command=addApp) #creates a button labeled Open File, with size made and color
openFile.pack() #attaches openFile to root

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg = "#263D42", command=runApps) #creates a button labeled Open File, with size made and color
runApps.pack()

root.mainloop()