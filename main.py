import math
import pygame
import random
from time import sleep
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
        player1.draw(win)
        player2.draw(win)
        pygame.draw.circle(win, PROJECTILE_COLOR, (int(coords[0]+FLOOR_START), int(HEIGHT-FLOOR_HEIGHT - coords[1])), 5)
        obstacle.draw(win)
        pygame.display.flip()
        clock.tick(60)

def render_all(obstacle,player1,player2):
    win.fill((0, 0, 0))
    pygame.display.update()
    pygame.draw.rect(win, (0, 255, 0), (FLOOR_START, HEIGHT-FLOOR_HEIGHT, WIDTH-FLOOR_START*2, FLOOR_HEIGHT))
    player1.draw(win)
    player2.draw(win)
    obstacle.draw(win)
    pygame.display.flip()

def render_victory(player):
    win.fill((0, 0, 0))
    pygame.display.update()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"Player {player} wins!", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    win.blit(text, textRect)
    pygame.display.flip()
    sleep(5)


def inputHandler():
    angle_deg = float(input("Enter the launch angle (degrees): "))
    initial_velocity = float(input("Enter the initial velocity (m/s): "))
    return [angle_deg,initial_velocity]

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Proyectile Motion")
running=True


# Input values

time_step = 0.0166  # Time step for simulation
gravity = 9.81  # Acceleration due to gravity (m/s^2)
wind_acceleration = float(input("Enter the horizontal wind acceleration (m/s^2): "))
p1=Obstacle(50,0,50,50,(255, 255, 0))
p2=Obstacle(500,0,50,50,(255, 0, 255))
turn=0
currentPlayer=1
# Calculate the trajectory and print positions
#projectile_path=proyectile.calculate_trajectory(angle_deg, initial_velocity, initial_x, 0.01, time_step, gravity, wind_acceleration, obstacle)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    obs=Obstacle(random.randint(100,500),random.randint(0,50),random.randint(25,100),random.randint(25,100),(255, 0, 0))
    if currentPlayer==1:
        state=0
        render_all(obs,p1,p2)
        angle_deg,initial_velocity=inputHandler()
        [projectile_path,state]=Proyectile.calculate_trajectory(angle_deg, initial_velocity, p1.x, 0.01, time_step, gravity, wind_acceleration, obs,p2)              
        render_launch(projectile_path, obs,p1,p2)
        if state==0:
            print("Projectile has reached the ground.")
        elif state==1:
            print("Projectile has reached the obstacle.")
        elif state==2:
            print("Projectile has reached the oponent.")
            render_victory(1)
            break
        currentPlayer=2
    elif currentPlayer==2:
        state=0
        render_all(obs,p1,p2)
        angle_deg,initial_velocity=inputHandler()
        [projectile_path,state]=Proyectile.calculate_trajectory(angle_deg+90, initial_velocity, p2.x, 0.01, time_step, gravity, wind_acceleration, obs,p1)              
        render_launch(projectile_path, obs,p1,p2)
        if state==0:
            print("Projectile has reached the ground.")
        elif state==1:
            print("Projectile has reached the obstacle.")
        elif state==2:
            print("Projectile has reached the oponent.")
            render_victory(2)
            break
        currentPlayer=1
    
    

pygame.quit()