import tkinter as tk
import customtkinter as ctk
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#make_scene_flag = False
lowerBound = 1
upperBound = 1000

class GetUserData(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Collatz Conjecture Visual")
        self.geometry("900x500")

        self.title = ctk.CTkLabel(self, text="Collatz Conjecture", font=ctk.CTkFont(size=100))
        self.title.place(x=50, y=20)

       # def user_input():
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
        self.submitButton = ctk.CTkButton(self, text="Submit", command = self.submit_button)
        self.submitButton.place(x=400, y=350)

        #self.entry1_filled = ''
        #self.entry2_filled = ''
        #self.entry3_filled = ''

    def submit_button(self):
        print("submit button")
        make_scene_flag = False
        entry1data=int(self.entry1.get())
        entry2data=int(self.entry2.get())
        entry3data=int(self.entry3.get())

        dataList = [entry1data, entry2data, entry3data]
        #print(dataList)
        
        '''
        self.entry1_filled = dataList[0]
        self.entry2_filled = dataList[1]
        self.entry3_filled = dataList[2]
        '''

        # for entry in dataList:
        #     if not entry.isdigit():
        #         return
            
        #     entry = int(entry)
        #     if not (lowerBound <= entry <= upperBound):
        #         return
            
            # Function to generate Collatz sequence
        def collatz_sequence(n):
            sequence = [n]
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
                sequence.append(n)
            return sequence

        # Makes a list of collatz sequences
        def collatz_sequences_list(integers):
            sequences = []
            for n in integers:
                sequences.append(collatz_sequence(n))

            return sequences


        # Function to generate branches
        def generate_branches(sequences):
            branch_lst = []
            line_start = (0, 0, 0)  # Start point of branch
            for sequence in sequences:
                branches = []
                for i in range(len(sequence) - 1):
                    length = random.uniform(0.5, 0.8)  # Random length for branching
                    line_end = (sequence[i] / 10 + length, sequence[i + 1] / 10 + length, 0)  # End point of branch
                    branches.append((line_start, line_end))
                    line_start = line_end
                branch_lst.append(branches)
            return branch_lst

        # init scene
        def make_scene():
            # Start pygame
            pygame.init()

            # Set up display
            width, height = 800, 600
            pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

            # Set up OpenGL perspective
            gluPerspective(45, (width / height), 0.1, 25)
            glTranslatef(0.0, -1, -15)


        # Function to draw line
        def draw_line(start, end):
            angle = random.uniform(-0.3, 0.3)  # Random angle for branching
            # glRotatef(angle, 0.0, 1.0, 0.0)
            glBegin(GL_LINES)
            glVertex3fv(start)
            glVertex3fv(end)
            glEnd()
            glRotate(angle, end[0], end[1], end[2])


        def seq_render(usr_input):
            running = True
            vals = [10, 17, 6, 12, 40, 50, 10, 20, 30, 15]  # Initial value for Collatz sequence
            while running:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                # Generate Collatz sequence
                sequences = collatz_sequences_list(usr_input)

                # Generate branches
                branches_lst = generate_branches(sequences)

                # Clear screen
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                for branches in branches_lst:
                    for branch in branches:
                        draw_line(branch[0], branch[1])

                # Update display
                pygame.display.flip()
                pygame.time.wait(300)  # Adjust the delay for visualization

            pygame.quit()

        userInput = dataList
    
        print(dataList)
        if make_scene_flag is False:
            make_scene()
            make_scene_flag = True
        while True:
            seq_render(dataList)
        
        #return dataList


         
GetUserData().mainloop()