import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import os
window = tk.Tk()
window.geometry()
geo = window.geometry
geo("400x400+400+400")
filelist = os.listdir("/home/jacob/Documents/Stardust")
listboxoffiles = tk.Listbox(window, selectmode="multiple")
listboxoffiles.pack()
for item in filelist:
    listboxoffiles.insert(tk.END, item)

def download():
    selecteditems = []
    for i in listboxoffiles.curselection():
        selecteditems.append(listboxoffiles.get(i))
    print(selecteditems)
    savepath = asksaveasfilename(initialfile=selecteditems[0])
    print(savepath)

buttondownload = tk.Button(window, text="Download",command=download)
buttondownload.pack()
#Create
window.mainloop()