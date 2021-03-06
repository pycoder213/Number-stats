import pygame, random, time # importing libraries
pygame.font.init() # initialising pygame font
pygame.init() # initialising pygame

# Creating color variables
RED = 255, 0, 0
GREEN  = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# Assigning screen size variables
SC_WIDTH, SC_LENGTH = 500, 350

# Creating Window
WIN = pygame.display.set_mode((SC_WIDTH, SC_LENGTH))
pygame.display.set_caption("Number Stats")

FONT = pygame.font.SysFont('comicsans', 40)

# BACK END DO FUNCTIONS BELOW






# function that will draw everything on the screen
def draw_window(user_input, retry=False, win=False):
    WIN.fill(WHITE)
    input_text = TEXT_FONT.render(str(user_input), 1, WHITE)
    print(int(user_input))

    box = pygame.Rect(SC_WIDTH//2-200, SC_LENGTH//2-30, 400, 60)

    pygame.draw.rect(WIN, BLACK, box)
    WIN.blit(input_text, (SC_WIDTH//2-200, SC_LENGTH//2-30))

    pygame.display.update()


# Main function
def main():
    user_input = ''
    
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # checking for quit
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    user_input+= '0'

        draw_window(user_input)
                
        



main()


"""

Back-End Task:

Is it Prime
Is it Even
Is it a square number
Is it a cube number
Number square root 2dp
Number cube root 2dp
Number squared
Number cubed

Create Functions/lambdas at dedicated area (line 22)

"""
