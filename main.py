import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from UI.inputData import *
import random


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
            line_end = (sequence[i] / 100 + length, sequence[i + 1] / 100 + length, 0)  # End point of branch
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
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)


# Function to draw line
def draw_line(start, end):
    angle = random.uniform(-0.3, 0.3)  # Random angle for branching
    glRotatef(angle, 0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3fv(start)
    glVertex3fv(end)
    glEnd()


def seq_render(usr_input):
    running = True
    vals = [10, 17, 6, 12, 40, 50, 10, 20, 30, 15]  # Initial value for Collatz sequence
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Generate Collatz sequence
        sequences = collatz_sequences_list(vals)

        # Generate branches
        branches_lst = generate_branches(sequences)

        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for branches in branches_lst:
            for branch in branches:
                draw_line(branch[0], branch[1])

        # Update display
        pygame.display.flip()
        pygame.time.wait(1000)  # Adjust the delay for visualization

    pygame.quit()

def main():
    # Start GUI (tip look at tkinter app loop)
    while GetUserData().mainloop():
    # Get user input (from the gui usually, should be cached)
        userInput = GetUserData()
        print(userInput)
    # Generate the collatz sequence from the input (look at seq_render())
       # seq_render(userInput)
    # Save ??? (ideally store all data generated from user input to json, maybe later)
    # Else just reset and prompt user for more inputs (would save time instead of rebooting the program)
    # return 0

if __name__ == "__main__":
    main()