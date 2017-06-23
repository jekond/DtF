import pygame
from pers import *
from button_class import *
pygame.init()


# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

#Разерность игрового окна
size=[633,470]
screen=pygame.display.set_mode(size)

charcheet_img = pygame.image.load("Img/charcheet.png").convert()
point_img = pygame.image.load("Img/point.png").convert()
pygame.display.set_caption("New characher")

pos = (0,0,)#координаты клика

check=0#Для проверки кликов, не проеби
def click_on_tp(abil_or_atrib):
        for j in range(3):
            if(pos[0]>=test.x_tp[j] and pos[0]<=test.x_tp[j]+test.tp_w):
                test.choise_tp(abil_or_atrib,j)
        
def click_on_tbl(strok,Y,abil_or_atrib,tp,ab_or_at,check):#Для распределения поинтов атрибутов и абилити
    for i in range(3):
        for j in range(strok):
            if(pos[0]>=test.x[i] and pos[0]<=test.x[i]+test.w and pos[1]>=Y[j] and pos[1]<=Y[j]+test.h):
                test.add_point(abil_or_atrib,tp[i],ab_or_at,check)#Возможно стоит сделать b_type общую и для абилити, и для атрибутов
                check=0#. Тогда эту же функцию можно бует использовать для обоих поисков
                return 0
            check+=1
'''
1. Кол-во строк в баблице. Столбцов априори 3
2. Указываешь откуда брать значения ячеек по y
3. Указываешь словарь атрибутов или словать умений брать из класса персонажа
4. Указываешь тип атрибута или умения (Физический, ментальный, таланты, познания)
5. Указываешь список наименований атрибута или умения, из класса Кнопка
6. check - это переменная для счетчика, так и записывать ее
'''    
        
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
            if(pos[1]<test.y_at[-1]+15 and pos[1]>test.y_at[0]):#Обрабатывает клики распределения атрибутов
                click_on_tbl(3,test.y_at,pl_ch.atribut,test.b_at_type,test.b_at_id,check)
            elif(pos[1]<test.y_ab[-1]+15 and pos[1]>test.y_ab[0]):#брабатывает клики распределения способностей
                click_on_tbl(6,test.y_ab,pl_ch.abilities,test.b_ab_type,test.b_ab_id,check)

            elif(test.y_tp[0]<=pos[1]<=test.y_tp[0]+test.h):
                click_on_tp(test.b_at_type)
            elif(test.y_tp[1]<=pos[1]<=test.y_tp[1]+test.h):
                click_on_tp(test.b_ab_type)

    # Flag that we are done so we exit this loop
    # ОБРАБОТКА ВСЕХ СОБЫТИЙ ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
    
 
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ

    
    # ВСЯ ИГРОВАЯ ЛОГИКА ДОЛЖНА НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ
 
 
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ ПОД ЭТИМ КОММЕНТАРИЕМ
    screen.fill(white)
    screen.blit(charcheet_img,[0,0])
    
    pygame.display.flip()
    # ВЕСЬ КОД ДЛЯ РИСОВАНИЯ ДОЛЖЕН НАХОДИТЬСЯ НАД ЭТИМ КОММЕНТАРИЕМ

    # Ограничить до 20 кадров в секунду
    clock.tick(20)
pygame.quit ()
