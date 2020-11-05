from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

window = 0  # glut window number


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black and opaque


def display():
    x, y = 50, 50
    glClear(GL_COLOR_BUFFER_BIT)  # clear the screen

    # Draw a Red 1x1 Square centered at origin
    glClear(GL_COLOR_BUFFER_BIT)  # clear the screen

    glColor3f(1.0, 0.8, 0.8)

    glBegin(GL_POLYGON)

    for i in range(1000):
        # area = (3.14 * (i * i))
        theta = (2 * 3.1415 * i)/1000

        x = 0.3 * np.cos(theta)
        y = 0.3 * np.sin(theta)

        glVertex2f(-0.2 + x, 0.2 + y)

    glEnd()

    glColor3f(0.75, 0.54, 0.33)

    glBegin(GL_POLYGON)

    for i in range(1000):
        # area = (3.14 * (i * i))
        theta = (2 * 3.1415 * i)/1000

        x = 0.3 * np.cos(theta)
        y = 0.3 * np.sin(theta)

        glVertex2f(x, 0.5 + y)

    glEnd()

    glColor3f(1.0, 1.0, 0.6)

    glBegin(GL_POLYGON)

    for i in range(1000):
        theta = (2 * 3.1415 * i)/1000

        x = 0.3 * np.cos(theta)
        y = 0.3 * np.sin(theta)

        glVertex2f(0.2 + x, 0.2 + y)

    glEnd()

    glColor3f(0.75, 0.7, 0.6)  # Red

    glBegin(GL_TRIANGLES)  # Each set of 4 vertices form a quad
    glVertex2f(-0.3, -0.03)  # x, y
    glVertex2f(0.0, -1.0)
    glVertex2f(0.3, -0.03)

    glEnd()

    glFlush()


# initialization
glutInit()  # initialize glut

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(480, 480)  # set window size
glutInitWindowPosition(50, 50)  # set window position
window = glutCreateWindow(b'Hello')  # create window with title

glutDisplayFunc(display)  # set draw function callback
glutIdleFunc(display)  # draw all the time

init()
glutMainLoop()