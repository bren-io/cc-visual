import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Set up OpenGL perspective
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Function to draw line
def draw_line(start, end):
    glBegin(GL_LINES)
    glVertex3fv(start)
    glVertex3fv(end)
    glEnd()

# Main loop
running = True
line_start = (0, 0, 0)
line_end = (1, 1, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update line end point
    line_end = (line_end[0] + 0.1, line_end[1] + 0.1, line_end[2])

    # Clear screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw line
    draw_line(line_start, line_end)

    # Update display
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
