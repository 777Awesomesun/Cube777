import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective

vertices_cube = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (1, 1, -1),
    (1, 1, 1),
    (-1, 1, -1),
    (-1, 1, 1)
)

edges_cube = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, g7)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(vertices_cube[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glutInit()  # Initialize GLUT
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    cube_rotation_angle = 0
    pyramid_rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  # Push the current matrix (for cube)
        glRotatef(cube_rotation_angle, 1, 1, 0)  # Rotate the cube
        draw_cube()
        glPopMatrix()  # Pop the matrix (cube's transformation)

        cube_rotation_angle += 1  # Increment rotation angle for cube
        pyramid_rotation_angle += 1  # Increment rotation angle for pyramid

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
