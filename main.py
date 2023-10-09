import math
import pygame
from obstacle import obstacle
from proyectile import proyectile

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN_SIZE = (WIDTH, HEIGHT)
BACKGROUND_COLOR = (255, 255, 255)
PROJECTILE_COLOR = (0, 0, 255)


win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Proyectile Motion")
running=True


# Input values
angle_deg = float(input("Enter the launch angle (degrees): "))
initial_velocity = float(input("Enter the initial velocity (m/s): "))
initial_x = float(input("Enter the initial x-position (m): "))
initial_y = float(input("Enter the initial y-position (m): "))
time_step = 0.01  # Time step for simulation
gravity = 9.81  # Acceleration due to gravity (m/s^2)
wind_acceleration = float(input("Enter the horizontal wind acceleration (m/s^2): "))
obstacle=obstacle(100,100,100,100)
# Calculate the trajectory and print positions
projectile_path=proyectile.calculate_trajectory(angle_deg, initial_velocity, initial_x, 0.01, time_step, gravity, wind_acceleration)
running=True
fraction=0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    win.fill((0, 0, 0))
    pygame.display.update()
    [x,y]=projectile_path[fraction]
    pygame.draw.circle(win, PROJECTILE_COLOR, (int(x), int(HEIGHT - y)), 5)
    obstacle.draw(win)
    pygame.display.flip()
    clock.tick(60)
    fraction+=1
pygame.quit()