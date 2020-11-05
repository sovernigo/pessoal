from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0  # glut window number


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black and opaque


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 1.0)

    glutWireTeapot(0.4)

    glFlush()


# initialization
glutInit()  # initialize glut

glutInitDisplayMode(GLUT_RGBA)

glutInitWindowSize(720, 720)  # set window size
glutInitWindowPosition(50, 50)  # set window position
glutCreateWindow(b'ex9')  # create window with title

glutDisplayFunc(display)  # set draw function callback
glutIdleFunc(display)  # draw all the time

gluLookAt(0,0,1, -0.5,0.2,0, 0,1,0)

init()
glutMainLoop()
