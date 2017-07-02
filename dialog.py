import pygame

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
    start_slice = 0

    for i in range(len(text_list)):
        if(now_range + len(text_list[i]) > line_range+1):
            start_slice += 1
            form_text += ['']
            now_range = 0
        form_text[start_slice] += text_list[i]
        now_range += len(text_list[i])

    return form_text

def transform(text,black):
    first_word_text = text#Весь текст будет храниться в отдельных файлах. Новый уровень - новый файл. Либо стоит держать все в одном - еще не решил
    first_word = format_text(first_word_text)
    font = pygame.font.SysFont('Times New Roman',25)
    for i in range(len(first_word)):
        first_word[i] = font.render(first_word[i],True,black)
    return first_word


def show_text(text,screen):
    for i in range(len(text)):
        screen.blit(text[i], [200,200 + 20*i])

def show_time(black,white,screen):
    text = ['Первая проверка. Хз как пройдет - но вроде как схема правильная, так что заценим.','А вот и второе подъехало. Тоже должно работать по схеме и быть ахуенным. А если нет - пойду ногти стричь.']
    pos = (0,0,)
            
    done=False
    j = 0
    clock=pygame.time.Clock()
    first_word = transform(text[j],black)
    while done==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (pygame.mouse.get_pos())
                pos = pygame.mouse.get_pos()
                if(pos[0]<100 and j-1>=0):
                    j-=1
                    first_word = transform(text[j],black)
                elif(pos[0]>1000 and j+1<=(len(text)-1)):
                    j+=1
                    first_word = transform(text[j],black)
     
        # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

        
        # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
     
     
        # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
        screen.fill(white)
        show_text(first_word,screen)
            
        pygame.display.flip()
        # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

        # Ограничить до 20 кадров в секунду
        clock.tick(20)
#    pygame.quit ()
