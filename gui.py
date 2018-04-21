from Tkinter import *
import ttk
import tkFileDialog
import ntpath

def browsefile(): 
    file = tkFileDialog.askopenfilename(filetypes = (("Text files", "*.txt"),("All files", "*.*") ))
    if file: 
        try: 
            root_to_file = file
            # extract the filename 
            head, tail = ntpath.split(file)        
            #filename.set(file)
            filename.set(tail or ntpath.basename(head))
        except: 
            print("Failed to select file \n'%s'"% file)
            return
    
root = Tk()
root.title("Symmetric Graph Drawing Tool (SGDT)")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


feet = StringVar()
root_to_file = ""
filename = StringVar()

ttk.Label(mainframe, text="Please select a file containing a graph: ").grid(column=0, row=0, sticky=W)

browse = ttk.Button(mainframe, text = "Browse", command = browsefile, width = 10)
browse.grid(column=1, row=0, sticky=(E))

ttk.Label(mainframe, text="You have chosen: ").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, textvariable=filename).grid(column=1, row=1, sticky=(W))

    
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

browse.focus()
#root.bind('<Return>', calculate)

root.mainloop()
