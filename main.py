import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
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

    if sequence[-1] != 1:
        sequence.append(1)

    return sequence

# Makes a list of collatz sequences
def collatz_sequences_list(start_points):
    sequences = [start_points]

    for n in start_points:
        sequences.append(collatz_sequence(n))

    return sequences

# Function to generate branches recursively
def recursive_branching(start_point, angle, length, depth, delta_angle, scale_factor):
    z_scale = 0.7

    if depth == 0:
        return []

    end_point = (
        start_point[0] + length * math.cos(angle),
        start_point[1] + length * math.sin(angle),
        0
    )

    branches = [(start_point, end_point)]

    # Generate branches recursively
    branches.extend(recursive_branching(end_point, angle - delta_angle, length * scale_factor, depth - 1, delta_angle, scale_factor))
    branches.extend(recursive_branching(end_point, angle + delta_angle, length * scale_factor, depth - 1, delta_angle, scale_factor))

    return branches

# Function to draw line
def draw_line(start, end):
    glBegin(GL_LINES)
    glVertex3fv(start)
    glVertex3fv(end)
    glEnd()

def main():
    # Initialize parameters
    width, height = 800, 600 # Setup display window
    start_point = (0, -1, 0)  # Start point of the tree
    angle = math.pi / 2  # Initial angle (pointing upwards)
    length = 0.7 # Initial branch length
    depth = 10  # Recursion depth
    delta_angle = math.pi / 17  # Angle between branches
    scale_factor = 0.7  # Scaling factor for branch length
    rotation_angle = 0 # Scene rotation

    # Start window
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    
    # Set up OpenGL perspective
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

    # Initalize tree
    vals = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]  # Initial value for Collatz sequence
    # Generate Collatz sequence
    sequences = collatz_sequences_list(vals)
    # Generate branches
    branches_lst = []
    for sequence in sequences:
        for start_value in sequence:
            branches_lst.extend(recursive_branching(start_point, angle, length, depth, delta_angle, scale_factor))

    # Controller
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -2)
        glRotatef(rotation_angle, 0, 1, 0)

        # Draw branches
        for branch in branches_lst:
            draw_line(branch[0], branch[1])

        # Update display
        pygame.display.flip()
        pygame.time.wait(10)  # Adjust the delay for visualization

        rotation_angle += 7

    pygame.quit()

if __name__ == "__main__":
    main()