import pygame, sys
from button import Button as Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/ThaleahFat.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        CREDITS_TEXT = get_font(45).render("This game was made by Team Forest.", True, "White")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        CREDITS_TEXT1 = get_font(36).render("Lai Chun Hei 20221143.", True, "White")
        CREDITS_RECT1 = CREDITS_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(CREDITS_TEXT1, CREDITS_RECT1)

        CREDITS_TEXT2 = get_font(36).render("Tsang Hoi Fung 20179698​.", True, "White")
        CREDITS_RECT2 = CREDITS_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(CREDITS_TEXT2, CREDITS_RECT2)

        CREDITS_TEXT3 = get_font(36).render("Ng Pak Hei 20220768​", True, "White")
        CREDITS_RECT3 = CREDITS_TEXT.get_rect(center=(640, 450))
        SCREEN.blit(CREDITS_TEXT3, CREDITS_RECT3)

        CREDITS_TEXT4 = get_font(36).render("Chow Ching Nam Benny 20180876", True, "White")
        CREDITS_RECT4 = CREDITS_TEXT.get_rect(center=(640, 500))
        SCREEN.blit(CREDITS_TEXT4, CREDITS_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(CREDITS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(CREDITS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("The Legendary", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        MENU_TEXT2 = get_font(100).render("Mysterious Tree", True, "#b68f40")
        MENU_RECT2 = MENU_TEXT.get_rect(center=(600, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("assets/Credits Rect.png"), pos=(640, 450), 
                            text_input="CREDITS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()    
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()