import tkinter as tk
from db_manager import db_manager as dbm
class GUI:
    def __init__(self):        
        self.window = tk.Tk()
        self.window.geometry("500x500")
        #self.frame = tk.Frame(self.window)

        self.frame = tk.Frame(self.window)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas,command=self.canvas.yview)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.window.title("DB manager")

        def button_click():
            print("Button clicked!")
            
        def load_data():
            data = dbm().fetchData()

            for entry in data:
                listbox = tk.Listbox(self.canvas,height=5,width=5)
                listbox.pack(fill=tk.X, expand=False)
                #scrollbar = tk.Scrollbar(listbox,command=self.canvas.yview)
                #scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

                for e in entry:
                    listbox.insert(tk.END,e)
                listbox.pack()

        def clear_data():
            for child in self.canvas.winfo_children():
                if isinstance(child, tk.Listbox):
                    child.destroy()
            #self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        menubar = tk.Menu(self.window)

        # Create a dropdown menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Option 1", command=button_click)
        file_menu.add_command(label="Option 2", command=button_click)
        menubar.add_cascade(label="File", menu=file_menu)

        load_button = tk.Menu(menubar, tearoff=0)
        load_button.add_command(label="Load Data", command=load_data)
        load_button.add_command(label="Clear Data",command=clear_data)
        menubar.add_cascade(label="Data", menu=load_button)

        # Configure the window to use the menubar
        self.window.config(menu=menubar)
        self.window.mainloop()

GUI()