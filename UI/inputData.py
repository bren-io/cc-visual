import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

lowerBound = 1;
upperBound = 1000;

class GetUserData(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Collatz Conjecture Visual")
        self.geometry("900x500")

        self.title = ctk.CTkLabel(self, text="Collatz Conjecture", font=ctk.CTkFont(size=100))
        self.title.place(x=50, y=20)

    #get entry data
    def submit_button():
        entry1data=self.entry1.get()
        entry2data=self.entry2.get()
        entry3data=self.entry3.get()

        dataList=[entry1data, entry2data, entry3data]
        print(dataList)

        return dataList

    def user_input():
        #first num
        self.entry1 = ctk.CTkEntry(self, width=400, height=30)
        self.startNum1 = ctk.CTkLabel(self, text="First starting number", font=ctk.CTkFont(size=20))
        self.startNum1.place(x=150, y=200)
        self.entry1.place(x=400, y=200)

        #second num
        self.entry2 = ctk.CTkEntry(self, width=400, height=30)
        self.startNum2 = ctk.CTkLabel(self, text="Second starting number", font=ctk.CTkFont(size=20))
        self.startNum2.place(x=150, y=250)
        self.entry2.place(x=400, y=250)

        #third num
        self.entry3 = ctk.CTkEntry(self, width=400, height=30)
        self.startNum3 = ctk.CTkLabel(self, text="Third starting number", font=ctk.CTkFont(size=20))
        self.startNum3.place(x=150, y=300)
        self.entry3.place(x=400, y=300)

        #create submit button
        self.submitButton = ctk.CTkButton(self, text="Submit", command = submit_button)
        self.submitButton.place(x=400, y=350)
         
#GetUserData().mainloop()