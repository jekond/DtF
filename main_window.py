import pygame
import dialog
import new_game
import button_class
import pers

pygame.init()

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

size=[1300,680]

screen=pygame.display.set_mode(size)

main_done = False

clock=pygame.time.Clock()
# -------- Основной цикл программы -----------
while main_done==False:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            main_done=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print (pygame.mouse.get_pos())
            pos = pygame.mouse.get_pos()
            start = button_class.start_game_button.click_on_button(pos)
            dialog_ch = button_class.start_dialog_button.click_on_button(pos)
            if(start=='start'):
                new_game.show_time(white,screen)
            elif(dialog_ch!=0):
                dialog.show_time(black,white,screen)
                #new_game.show_time(white,screen)
    # Flag that we are done so we exit this loop

    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
        
     
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

        
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
     
     
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
    screen.fill(white)
    button_class.start_game_button.draw_rect(screen,black)
    button_class.start_dialog_button.draw_rect(screen,black)
    pygame.display.flip()
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # Ограничить до 20 кадров в секунду
    clock.tick(20)

pygame.quit ()
