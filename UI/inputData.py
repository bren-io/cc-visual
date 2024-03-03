import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class GetUserData(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Collatz Conjecture Visual")
        self.geometry("900x500")

        #get entry data
        def submit_button():
            entry1data=self.entry1.get()
            entry2data=self.entry2.get()
            entry3data=self.entry3.get()

            dataList=[entry1data, entry2data, entry3data]

            return(dataList)
            #success test
            #successLabel = ctk.CTkLabel(self, text=entry1data)
            #successLabel.grid(row=4, column=0)


        #first num
        self.entry1 = ctk.CTkEntry(self, width=400, height=30)
        self.startNum1 = ctk.CTkLabel(self, text="First starting number", font=ctk.CTkFont(size=20))
        self.startNum1.grid(row=0, column=0, padx=80,)
        self.entry1.grid(row=0, column=1, sticky="nsew", pady=5, padx=5)


        #second num
        self.entry2 = ctk.CTkEntry(self, width=400, height=30)
        self.startNum2 = ctk.CTkLabel(self, text="Second starting number", font=ctk.CTkFont(size=20))
        self.startNum2.grid(row=1, column=0, padx=80,)
        self.entry2.grid(row=1, column=1, sticky="nsew", pady=5, padx=5)

        #third num
        self.entry3 = ctk.CTkEntry(self, width=400, height=30)
        self.startNum3 = ctk.CTkLabel(self, text="Third starting number", font=ctk.CTkFont(size=20))
        self.startNum3.grid(row=2, column=0, padx=80,)
        self.entry3.grid(row=2, column=1, sticky="nsew", pady=5, padx=5)

        #create submit button
        self.submitButton = ctk.CTkButton(self, text="Submit", command = submit_button)
        self.submitButton.grid(row=3)


app = GetUserData()
app.mainloop()