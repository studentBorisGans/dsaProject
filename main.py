import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption("Mines")

# CONSTANTS
size = (750, 500)
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


clock = pygame.time.Clock()
run = True

while run:
    time = clock.tick(60) / 1000 #60 fps and time is the number of milliseconds spent per instance of while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nQuitting...")
            run = False
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

    pygame.display.update()
    




# def main():
#     run = True
#     while run:







    

