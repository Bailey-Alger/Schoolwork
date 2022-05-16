import tkinter

class CtoFconverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.c_frame = tkinter.Frame(self.main_window)
        self.f_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.f_value = tkinter.StringVar()

        self.c_text = tkinter.Label(self.c_frame, text='Enter the Celsius temperature: ')
        self.c_entry = tkinter.Entry(self.c_frame)
        self.f_text = tkinter.Label(self.f_frame, text='Fahrenheit temperature: ')
        self.f_answer = tkinter.Label(self.f_frame, textvariable=self.f_value)

        self.c_text.pack(side='left')
        self.c_entry.pack(side='right')
        self.f_text.pack(side='left')
        self.f_answer.pack(side='right')

        self.convert_button = tkinter.Button(self.button_frame, text='Convert to Fahrenheit', command=self.convert)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.convert_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.c_frame.pack()
        self.f_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def convert(self):
        self.f_value.set(float(self.c_entry.get())*9/5+32)
        
temp_Converter = CtoFconverter()
