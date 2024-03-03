import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Collatz Conjecture Visual")
        self.geometry("900x500")

        #create label
        self.title = ctk.CTkLabel(self, text="Collatz Conjecture", fg_color="transparent", font=ctk.CTkFont(size=50, weight="bold"))
        self.title.grid(row=0, column=0, pady=50, padx=10)

        

        self.mainloop()

App()

'''
class frick(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.entry = ctk.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
'''

