import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption("Mines")

# CONSTANTS
size = (750, 500)
numSquares = 25
squareSize = 100
borderSize = 2


# size is temp for now it should become dynamic; idea is that the control bar (left side) is half the width and height of the main box

# info = pygame.display.Info()
# width = info.current_w
# height = info.current_h #instead of doing pygame.FULLSCREEN
# print(f"Width: {width}, Height: {height}")

screen = pygame.display.set_mode(size)
# add pygame.FULLSCREEN ^                                 
background = pygame.Surface(size)
background.fill(pygame.Color('#FFFFFF'))
manager = pygame_gui.UIManager(size)


def drawBoard():
    # pygame.draw.rect(screen, )
    for i in range(numSquares):
        column = i % 5
        row = i // 5

        squareX = column*squareSize
        squareY = row * squareSize

        pygame.draw.rect(screen, "black", [250 +  squareX, squareY, squareSize, squareSize])
        pygame.draw.rect(screen, "gold", [250 + squareX + borderSize, squareY + borderSize, squareSize - 2 * borderSize, squareSize - 2 * borderSize])
        print(f"Row: {row}, Column: {column} I: {i}")






clock = pygame.time.Clock()
run = True

while run:
    time = clock.tick(60) / 1000 #60 fps and time is the number of milliseconds spent per instance of while loop


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nQuitting...")
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0] // 100
            y = event.pos[1] // 100
            click = (x, y)
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                print("Quitting...")
                run = False
            if event.key == pygame.K_SPACE:
                print("Space!!")
        manager.process_events(event)
    
    manager.update(time)

    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    drawBoard()
    pygame.display.flip()


    







    

