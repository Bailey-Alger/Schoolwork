import tkinter

class InfoGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.name_value = tkinter.StringVar()
        self.address1_value = tkinter.StringVar()
        self.address2_value = tkinter.StringVar()

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.name = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.address1 = tkinter.Label(self.info_frame, textvariable=self.address1_value)
        self.address2 = tkinter.Label(self.info_frame, textvariable=self.address2_value)

        self.name.pack()
        self.address1.pack()
        self.address2.pack()

        self.info_button = tkinter.Button(self.button_frame, text='Show Info', command=self.showinfo)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.info_button.pack(side='left')
        self.quit_button.pack(side='right')
        
        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def showinfo(self):
        self.name_value.set('Bailey Alger')
        self.address1_value.set('1000 Drive Street')
        self.address2_value.set('Sarsota, FL 34567')

info_GUI = InfoGUI()
