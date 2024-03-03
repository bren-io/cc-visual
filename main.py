import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame import surface
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


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
    for val in starting_points:
        sequence = collatz_sequence(val)
        x, y, z = 1, 1, 0


        # each starting point will have a line
        # point on x, y, z coordinates
        seq_lines = []
        seq_vertices = []
        for idx, num in enumerate(sequence):
            glBegin(GL_LINES)
            if idx < len(sequence) - 1:
                seq_lines.append((num, sequence[idx + 1]))

            if sequence[idx] % 2 == 0:
                # rotation
                x += 1
            else:
                # rotation
                x -= 1
                y += 1

            vertex = (x, y, z)
            seq_vertices.append(vertex)
            print(vertex)
            glVertex3f(*vertex)
            glEnd()
            glTranslatef(x, y, z)  # Move to the next position

        # create vertex for each node/point from the sequence values



            # # Ensure points stay within the display frame
            # if abs(x) > 25:  # Adjust this value based on your requirement
            #     x *= -1
            # if abs(y) > 20:  # Adjust this value based on your requirement
            #     y *= -1  # Move points back within frame
        print(seq_lines)



def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)

    glTranslate(0, -60, -5)
    glRotatef(20, 0, 0, 0)

    start_vals = [6, 14, 17]

    draw_collatz_tree(start_vals)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # call collatz function
        pygame.display.flip()
        pygame.time.wait(10)




if __name__ == "__main__":
    main()
