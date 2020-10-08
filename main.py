from math import ceil

from pygame import init, QUIT, quit, image, display, event, transform, MOUSEBUTTONDOWN, mouse, font, MOUSEMOTION

from classes.game import Game

init()

# Définition de la fenêtre
display.set_caption("Ludo", "assets/cheval.png")

# On initialise le jeu
game = Game()

# Importation de l'image d'arrière-plan
background = image.load("assets/plateau.png")
background = transform.scale(
    background, (game.screen_height, game.screen_width))
play_button = image.load("assets/play_button.png")
play_button = transform.scale(play_button, (200, 200))
play_button_rect = play_button.get_rect()
play_button_rect.x = ceil((game.screen.get_height() / 2) - 100)
play_button_rect.y = ceil((game.screen.get_width() / 2) - 100)

running = True

mouse_pos = font.Font(None, 24).render(
    str(mouse.get_pos()), 1, (0, 0, 0))

while running:
    game.screen.blit(background, (0, 0))

    if game.is_playing:
        game.screen.blit(mouse_pos, (0, 0))
        game.update()
    else:
        game.screen.blit(background, (0, 0))
        game.screen.blit(
            play_button, play_button_rect)
    if game.dice.image:
        game.screen.blit(game.dice.image, game.dice.rect)
    display.flip()

    for evt in event.get():

        if evt.type == QUIT:
            running = False
            quit()
        elif evt.type == MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(evt.pos):
                game.is_playing = True
                game.start()
            elif game.dice.rect.collidepoint(evt.pos):
                game.is_dice_pressed = True

        elif evt.type == MOUSEMOTION:
            mouse_pos = font.Font(None, 24).render(
                str(mouse.get_pos()), 1, (0, 0, 0))
            game.screen.blit(mouse_pos, (0, 0))
            display.flip()
