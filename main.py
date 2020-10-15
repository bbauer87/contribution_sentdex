# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk


LARGE_FONT= ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        verif(globals())

        # New loop
        for F in CLASSES:
            frame = CLASSES[F](container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Old loop, just to reference:
##        for F in (PageStart, PageOne, PageTwo):
##            frame = F(container, self)
##            self.frames[F] = frame
##            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageStart")

    # Now everytime you use this method you need to pass
    # the class name in string format ("" or '').
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


# New name, instead of StartPage.
class PageStart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        # Change in show_frame parameter
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame("PageOne"))
        button.pack()
        
        # Change in show_frame parameter
        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        # Change in show_frame parameter
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame("PageStart"))
        button1.pack()
        
        # Change in show_frame parameter
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        # Change in show_frame parameter
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame("PageStart"))
        button1.pack()
        
        # Change in show_frame parameter
        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2.pack()


def verif(param):
    global CLASSES   

    # Empty dic of classes
    CLASSES = {}
    # We need to declarate aClass before iterating throught globals()
    aClass = ""
    for aClass in param:
        # You need to use a pattern in your classes names. In this
        # example, they start with "Page".

        if aClass.startswith("Page"):
            CLASSES[aClass] = param[aClass]



app = SeaofBTCapp()
app.mainloop()
