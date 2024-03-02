import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def draw_collatz_tree(starting_points):
    for start in starting_points:
        sequence = collatz_sequence(start)
        x, y, z = 0, 0, 0
        for num in sequence:
            glColor3f(0, 0, 0)
            glBegin(GL_LINES)
            glVertex3f(x, y, z)
            glVertex3f(x, y+1, z)
            glEnd()
            glTranslatef(0, 1, 0)  # Move up for the next level
            if num % 2 == 0:
                x += 1
            else:
                x -= 1
                y += 1
            glTranslatef(x, y, z)  # Move to the next position

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -20.0, -30)

    starting_points = [27, 17, 31, 7, 15]  # Example starting points

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_collatz_tree(starting_points)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
