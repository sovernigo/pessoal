from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

window = 0  # glut window number
tam = 5


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black and opaque


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    pos = 0.15
    glColor3f(1.0, 0.8, 0.8)
    glBegin(GL_QUADS)

    for i in range(tam):
        theta = (2 * 3.1415 * i) / tam
        x = 0.4 * np.sin(theta)
        y = 0.4 * np.cos(theta)
        glVertex2f(0.0, 0.0)
        glVertex2f(pos * y, -pos * x)
        glVertex2f(x, y)
        glVertex2f(-pos * y, pos * x)

        pos = -pos

    glEnd()

    glFlush()


def keyboard(button, x, y):
    global tam
    if button == b'\x1b':
        glutDestroyWindow(window)
    if button == b'\r':
        tam = tam + 1


# initialization
glutInit()  # initialize glut

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(720, 720)  # set window size
glutInitWindowPosition(50, 50)  # set window position
window = glutCreateWindow(b'Hello')  # create window with title

glutDisplayFunc(display)  # set draw function callback
glutIdleFunc(display)  # draw all the time

glutKeyboardFunc(keyboard)

init()
glutMainLoop()
