import pygame
bob = 'Hel'
def format_text(non_form_text):#Преобразования текста под реалии PyGame
    text_list = []
    form_text = ['']
    start_slice = 0
    stop_slice = '.,!?:- '
    line_range = 30
    now_range = 0
    for i in range(len(non_form_text)):
        if(non_form_text[i] in stop_slice):
            text_list+=[non_form_text[start_slice:i+1]]
            start_slice = i+1
    print(text_list)
    start_slice = 0

    for i in range(len(text_list)):
        if(now_range + len(text_list[i]) > line_range+1):
            start_slice += 1
            form_text += ['']
            now_range = 0
        form_text[start_slice] += text_list[i]
        now_range += len(text_list[i])

    return form_text

def show_text(text):
    for i in range(len(text)):
        screen.blit(text[i], [200,200 + 20*i])

pygame.init()

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

#Определение шрифта
first_word_text = ''#Весь текст будет храниться в отдельных файлах. Новый уровень - новый файл. Либо стоит держать все в одном - еще не решил
first_word = format_text(first_word_text)
font = pygame.font.SysFont('Times New Roman',25)
for i in range(len(first_word)):
    first_word[i] = font.render(first_word[i],True,black)

#Разерность игрового окна
size=[633,470]
screen=pygame.display.set_mode(size)

pos = (0,0,)#координаты клика

check=0#Для проверки кликов, не проеби
        
done=False
 
# Используется для контроля частоты обновления экрана
clock=pygame.time.Clock()

 
# -------- Основной цикл программы -----------
while done==False:
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА БЫТЬ ПОД ЭТИМ КОММЕНТАРИЕМ
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print event.button
            print (pygame.mouse.get_pos())
            pos = pygame.mouse.get_pos()

    # Flag that we are done so we exit this loop
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    
 
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

    
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
 
 
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
    screen.fill(white)
    show_text(first_word)
        
    pygame.display.flip()
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # Ограничить до 20 кадров в секунду
    clock.tick(20)
pygame.quit ()
