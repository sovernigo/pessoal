from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0  # glut window number


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black and opaque


def draw():

    glBegin(GL_QUADS)
    glVertex2f(0.0, 0.0)  # x, y
    glVertex2f(0.0, 0.1)
    glVertex2f(0.2, 0.1)
    glVertex2f(0.2, 0.0)

    glEnd()


def drawCoord():

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINE_STRIP)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)

    glEnd()

    glColor3f(0.0, 1.0, 0.0)

    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)

    glEnd()


def display():

    #  Draw a Red 1x1 Square centered at origin

    glClear(GL_COLOR_BUFFER_BIT)  # clear the screen
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    drawCoord()
    glColor3f(0.5, 0.0, 1.0)
    draw()

    glColor3f(0.5, 0.3, 1.0)
    glTranslatef(0.1, 0.1, 0.0)
    draw()

    glColor3f(0.0, 0.5, 1.0)
    glRotatef(90, 0.0, 0.0, 1.0)
    draw()

    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(-0.1, -0.1, 0.0)
    draw()

    glFlush()

# initialization
glutInit()  # initialize glut

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(720, 720)  # set window size
glutInitWindowPosition(50, 50)  # set window position
window = glutCreateWindow(b'Rotation')  # create window with title

glutDisplayFunc(display)  # set draw function callback
#glutIdleFunc(display)  # draw all the time

init()
glutMainLoop()