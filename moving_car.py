import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
# from circle import draw_circle


# Initialize Pygame and OpenGL
# pygame.init()
# pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
# gluOrtho2D(0, 800, 0, 600)

def draw_circle(x, y, radius, color):
    num_segments = 30  # Number of segments to approximate the circle
    theta = 2 * math.pi / num_segments  # Angle between each segment
    c = math.cos(theta)  # Cosine of the angle
    s = math.sin(theta)  # Sine of the angle
    t = 1 - c  # Difference from 1 to cosine
    x0 = radius  # Initial x position
    y0 = 0  # Initial y position
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)  # Set the color for the circle
    glVertex2f(x, y)  # Center of the circle
    for i in range(num_segments + 1):
        x1 = x0  # x position of the vertex
        y1 = y0  # y position of the vertex
        x0 = x0 * c - y0 * s  # Rotate x position
        y0 = x1 * s + y0 * c  # Rotate y position
        glVertex2f(x + x0, y + y0)  # Vertex of the circle
    glEnd()


# Initialize Pygame and OpenGL
pygame.init()
pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
gluOrtho2D(0, 800, 0, 600)

# Car position and speed
car_x = 100
car_speed = 5

def draw_car(x, y):
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x - 20, y)
    glVertex2f(x + 70, y)
    glVertex2f(x + 70, y + 20)
    glVertex2f(x - 20, y + 20)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(.5, 1.0, 1.0)
    glVertex2f(x + 10, y + 20)
    glVertex2f(x + 50, y + 20)
    glVertex2f(x + 40, y + 40)
    glVertex2f(x + 10, y + 40)
    glEnd()
    draw_circle(x, y, 10, (1.0, 1.0, 0.0)) 
    draw_circle(x + 55, y, 10, (1.0, 1.0, 0.0)) 

    # circle.draw_circle(x + 30, y + 20, 10, (1, 0, 0))

def main():
    global car_x
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        
        # Update car position
        car_x += car_speed
        if car_x > 800:
            car_x = -60
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        draw_car(car_x, 250)
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
