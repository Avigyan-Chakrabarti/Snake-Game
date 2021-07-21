import pygame
import random
import os
pygame.init()

pygame.mixer.init()

#Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,200,0)
blue=(0,0,200)

#Creating Window
screen_width = 1000
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height))

#Background Image
bgimg = pygame.image.load("bgimage.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

#Game Title
pygame.display.set_caption("Avigyan's Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def welcome():
    gamewindow.fill((233,220,229))
    text_screen("Welcome to Snakes Game",blue,260,250)
    text_screen("Press Space bar to play",black,250,300)
        

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

#Game Loop
def gameloop():
    #Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20,screen_width-200)
    food_y = random.randint(20,screen_height-100)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps=60
    snk_list=[]
    snk_length = 1
    if(not os.path.exists("Highscore.txt")):
        with open("Highscore.txt","w") as f:
            f.write("0")
    with open("Highscore.txt","r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("Highscore.txt","w") as f:
                f.write(str(highscore))
            gamewindow.fill(white)
            text_screen("Game Over!",red,300,200)
            text_screen("Press Enter to continue",black,250,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gaming()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
                        if score>int(highscore):
                            highscore = score


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score += 10
                food_x = random.randint(20,screen_width-200)
                food_y = random.randint(20,screen_height-100)
                snk_length+=5
                if(score>int(highscore)):
                    highscore = score


            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score: "+str(score)+"  Highscore: "+str(highscore),black,5,5)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            pygame.draw.rect(gamewindow,green,[food_x,food_y,snake_size,snake_size])
            plot_snake(gamewindow,red,snk_list,snake_size)
            if not 0<snake_x<screen_width:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if not 0<snake_y<screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

def gaming():
    exit_game = False
    fps=60
    
    while not exit_game:
        welcome()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bgmusic.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(fps)

if(__name__=="__main__"):
    gaming()