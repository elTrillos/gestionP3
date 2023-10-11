import math
import pygame
import random
from obstacle import Obstacle
from proyectile import Proyectile
from screen import WIDTH, HEIGHT, FLOOR_HEIGHT, FLOOR_START

pygame.init()

SCREEN_SIZE = (WIDTH, HEIGHT)
BACKGROUND_COLOR = (255, 255, 255)
PROJECTILE_COLOR = (0, 0, 255)

def render_launch(proyectile_path, obstacle,player1,player2):
    for coords in proyectile_path:
        win.fill((0, 0, 0))
        pygame.display.update()
        pygame.draw.rect(win, (0, 255, 0), (FLOOR_START, HEIGHT-FLOOR_HEIGHT, WIDTH-FLOOR_START*2, FLOOR_HEIGHT))
        pygame.draw.rect(win, (255, 255, 0), (player1.x+FLOOR_START, HEIGHT-FLOOR_HEIGHT-player1.y-player1.height, player1.width, player1.height))
        pygame.draw.rect(win, (255, 255, 0), (player2.x+FLOOR_START, HEIGHT-FLOOR_HEIGHT-player2.y-player2.height, player2.width, player2.height))
        pygame.draw.circle(win, PROJECTILE_COLOR, (int(coords[0]+FLOOR_START), int(HEIGHT-FLOOR_HEIGHT - coords[1])), 5)
        pygame.display.flip()
        obstacle.draw(win)
        pygame.display.flip()
        clock.tick(60)



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
p1=Obstacle(50,0,50,50)
p2=Obstacle(500,0,50,50)
# Calculate the trajectory and print positions
#projectile_path=proyectile.calculate_trajectory(angle_deg, initial_velocity, initial_x, 0.01, time_step, gravity, wind_acceleration, obstacle)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    obs=Obstacle(random.randint(100,500),random.randint(0,50),random.randint(25,100),random.randint(25,100))
    state=0
    [projectile_path,state]=Proyectile.calculate_trajectory(angle_deg, initial_velocity, initial_x, 0.01, time_step, gravity, wind_acceleration, obs,p2)              
    render_launch(projectile_path, obs,p1,p2)
    if state==0:
        print("Projectile has reached the ground.")
    elif state==1:
        print("Projectile has reached the obstacle.")
    elif state==2:
        print("Projectile has reached the oponent.")
    
    

pygame.quit()