import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Initialize Pygame and OpenGL
pygame.init()
pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
gluOrtho2D(0, 800, 0, 600)

# Ball properties
ball_x = 100
ball_y = 600
ball_radius = 20
ball_color = (1.0, 0.0, 0.0)  # Red color
ball_velocity_x = 5
ball_velocity_y = 0
gravity = -1.9  # Gravitational acceleration (negative to pull down)
bounce_damping = 1.0  # Coefficient of restitution (bounce reduction factor)

def draw_circle(x, y, radius, color):
    num_segments = 30
    theta = 2 * math.pi / num_segments
    c = math.cos(theta)
    s = math.sin(theta)
    t = 1 - c
    x0 = radius
    y0 = 0
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y)
    for i in range(num_segments + 1):
        x1 = x0
        y1 = y0
        x0 = x0 * c - y0 * s
        y0 = x1 * s + y0 * c
        glVertex2f(x + x0, y + y0)
    glEnd()

def main():
    global ball_x, ball_y, ball_velocity_x, ball_velocity_y
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        
        # Apply gravity
        ball_velocity_y += gravity
        
        # Update ball position
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y
        
        # Check for collision with the window borders
        if ball_x + ball_radius > 800:
            ball_x = 800 - ball_radius
            ball_velocity_x = -ball_velocity_x
        elif ball_x - ball_radius < 0:
            ball_x = ball_radius
            ball_velocity_x = -ball_velocity_x
        
        if ball_y + ball_radius > 600:
            ball_y = 600 - ball_radius
            ball_velocity_y = -ball_velocity_y * bounce_damping
        elif ball_y - ball_radius < 0:
            ball_y = ball_radius
            ball_velocity_y = -ball_velocity_y * bounce_damping
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Draw the ball
        draw_circle(ball_x, ball_y, ball_radius, ball_color)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
