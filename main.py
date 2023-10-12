import sys
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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)

def render_launch(proyectile_path, obstacle,player1,player2):
    for coords in proyectile_path:
        win.fill((0, 0, 0))

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
    text = font.render(f"Player {player} wins!", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    win.blit(text, textRect)

    pygame.display.flip()
    sleep(5)

# Initial values of a and b
a_difficulty = "None"
b_difficulty = "None"

difficulties = ["None", "Easy", "Medium", "Hard"]
a_difficulty_idx = 0
b_difficulty_idx = 0

def draw_buttons():
    # Clear the screen
    win.fill(WHITE)

    # Draw buttons for selecting difficulty for parameter A
    a_text = font.render(f"Wind Difficulty:", True, BLACK)
    win.blit(a_text, (50, 50))
    pygame.draw.rect(win, BLACK, (400, 45, 150, 40), 2)
    difficulty_text_a = font.render(difficulties[a_difficulty_idx], True, BLACK)
    win.blit(difficulty_text_a, (410, 50))

    # Draw buttons for selecting difficulty for parameter B
    b_text = font.render(f"Obstacle Difficulty:", True, BLACK)
    win.blit(b_text, (50, 100))
    pygame.draw.rect(win, BLACK, (400, 95, 150, 40), 2)
    difficulty_text_b = font.render(difficulties[b_difficulty_idx], True, BLACK)
    win.blit(difficulty_text_b, (410, 100))


    pygame.draw.rect(win, BLACK, (150, 200, 100, 40), 2)
    start_text = font.render("Start", True, BLACK)
    win.blit(start_text, (170, 205))

    # Update the display
    pygame.display.flip()



def input_text(input_count, input_text):
    render_all(obs,p1,p2)
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(50, 150, 140, 32) 

    color = pygame.Color('lightskyblue3') 
    active = False
    text = font.render(input_text, True, WHITE)
    win.blit(text, (50, 50))

    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running=False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False
    
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_BACKSPACE: 
                    user_text = user_text[:-1] 

                elif event.key == 13: 
                    if user_text.isnumeric():
                        if float(user_text) < 0:
                            text = font.render(f"Enter a positive value", True, (255,0,0))
                            win.blit(text, (50, 100))
                        else:
                            input_count += 1
                            return input_count, float(user_text)
                    else:
                        text = font.render(f"Enter a numeric value", True, (255,0,0))
                        win.blit(text, (50, 100))
                else: 
                    user_text += event.unicode

        pygame.draw.rect(win, color, input_rect) 
  
        text_surface = base_font.render(user_text, True, (255, 255, 255)) 
        win.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
        # set width of textfield so that text cannot get 
        # outside of user's text input 
        input_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Proyectile Motion")
selecting_difficulties = True

while selecting_difficulties:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 400 <= x <= 550 and 45 <= y <= 85:
                # Cycle through the difficulty levels for parameter A
                a_difficulty_idx = (a_difficulty_idx + 1) % len(difficulties)
            elif 400 <= x <= 550 and 95 <= y <= 135:
                # Cycle through the difficulty levels for parameter B
                b_difficulty_idx = (b_difficulty_idx + 1) % len(difficulties)
            elif 150 <= x <= 250 and 200 <= y <= 240:
                # Clicked the "Start" button, exit the loop
                selecting_difficulties = False
            a_difficulty = difficulties[a_difficulty_idx]
            b_difficulty = difficulties[b_difficulty_idx]
            

    draw_buttons()

# Input values
wind_params = {'None':[0,0], 'Easy':[0.25, 2.5], 'Medium':[2.5, 7.5], 'Hard':[7.5, 12.5]}
obstacle_params = {'None':[0,0], 'Easy':[50, 100], 'Medium':[100, 150], 'Hard':[150, 200]}

time_step = 0.0166  # Time step for simulation
gravity = 9.81  # Acceleration due to gravity (m/s^2)
wind_acceleration = random.uniform(wind_params[a_difficulty][0], wind_params[a_difficulty][1])*random.choice([-1, 1])

p1=Obstacle(50,0,50,50,(255, 255, 0))
p2=Obstacle(500,0,50,50,(255, 0, 255))
obs=Obstacle(random.randint(250,350),random.randint(0,50),
                 random.randint(obstacle_params[b_difficulty][0],obstacle_params[b_difficulty][1]),
                 random.randint(obstacle_params[b_difficulty][0],obstacle_params[b_difficulty][1]),(255, 0, 0))
turn=0
currentPlayer=1
running = True

# Calculate the trajectory and print positions
#projectile_path=proyectile.calculate_trajectory(angle_deg, initial_velocity, initial_x, 0.01, time_step, gravity, wind_acceleration, obstacle)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()

    if currentPlayer==1:
        state=0
        get_inputs = True
        input_count = 0

        while get_inputs:
            input_count, angle_deg = input_text(input_count, "P1 -> Enter the launch angle (degrees): ")
            input_count, initial_velocity = input_text(input_count, "P1 -> Enter the initial velocity (m/s):")
            if input_count == 2:
                get_inputs = False

        render_all(obs,p1,p2)

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
        get_inputs = True
        input_count = 0
        while get_inputs:
            input_count, angle_deg = input_text(input_count, "P2 -> Enter the launch angle (degrees): ")
            input_count, initial_velocity = input_text(input_count, "P2 -> Enter the initial velocity (m/s):")
            if input_count == 2:
                get_inputs = False

        render_all(obs,p1,p2)

        [projectile_path,state]=Proyectile.calculate_trajectory(-angle_deg+180, initial_velocity, p2.x, 0.01, time_step, gravity, wind_acceleration, obs,p1)              
        
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
