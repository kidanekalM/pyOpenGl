import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
def square(size):
    glBegin(GL_POLYGON)
    glVertex(0.0, 1.0, 0.0)
    glVertex(1.0, 1, 0.0)
    glVertex(1/2, 0.0, 0.0)
    glColor(1,0.3,0.1)
    glEnd()   
   


def car():
    glBegin(GL_POLYGON)
    glVertex(0.0, 1.0, 0.0)
    glVertex(1, 1, 0.0)
    glVertex(1.5, 0.0, 0.0)
    glVertex(-0.5, 0.0, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex(1, 1, 0.0)  
    glVertex(0, 1.2, 0.0)
    glEnd()
def house():
    glBegin(GL_TRIANGLES)
    glColor3f(.1, 1, 1)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(0.0, -1.0,0.0)
    glColor(1,0.3,0.1)
    glEnd() 
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    glVertex3f(1,-1,0)
    glVertex3f(0,-1,0)
    glVertex3f(1,-2,0)
    glVertex3f(0,-2,0)
    glVertex3f(0,-1,0)
    glVertex3f(0,-2,0)
    glVertex3f(1,-1,0)
    glVertex3f(1,-2,0)

    glVertex3f(0.4,-2,0)
    glVertex3f(0.4,-1.6,0)

    glVertex3f(0.4,-1.6,0)
    glVertex3f(0.6,-1.6,0)

    glVertex3f(0.6,-1.6,0)
    glVertex3f(0.6,-2,0)

    glVertex3f(0.7,-1,0)
    glVertex3f(0.7,-1.2,0)

    glVertex3f(0.7,-1.2,0)
    glVertex3f(1,-1.2,0)

    glEnd()
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
       # house()
        car()

        pygame.display.flip()
        pygame.time.wait(10)


main()