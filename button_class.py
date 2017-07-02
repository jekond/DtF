from pers import *
import pygame
class Button:
    def __init__(self,x,y,w,h,b_id):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.b_id = b_id

    def draw_rect(self,screen,black):
        pygame.draw.rect(screen,black,[self.x,self.y,self.w,self.h],0)

    def click_on_button(self,pos):
        if(pos[0]>self.x and pos[0]<self.x+self.w and pos[1]>self.y and pos[1]<self.y+self.h):
            return self.b_id
        else:
            return 0

start_game_button = Button(250,250,50,250,'start')
start_dialog_button = Button(800,250,50,250,'dialog')

class Charsheet_button(Button):
    def __init__(self):
        self.x_tp = [75]
        self.y_tp = [40,150]
        self.tp_w = 75
        self.x = [5]# проще всего просто указывать первое положение, после чего отступать на длину + 10 пикселей
        self.y_at = [60]# аналогично
        self.y_ab = [170]
        self.w = 200#Длина 200 пикселей
        self.h = 15#высотаа 10 пикселей
        self.b_at_type = ['Physical','Social','Mental']
        self.b_ab_type = ['Talents','Skills','Knowledges']
        self.b_at_id = ['Strenght','Dexterity','Stamina',
                        'Charisma','Manipulation','Appearance',
                        'Perception','Intelligence','Wits']
        self.b_ab_id = ['Athletics','Brawl','Dodge','Intimidation','Cunning','Leadership',
                        'Firearms','Melee','Securiti','Stealth','Acting','Search',
                        'Computer','Finance','Investigation','Medicine','Politics','Religion']
        self.exp = 30
    def add_point(self,abil_or_atrib,tp,ab_or_at,i):#pl_ch.abilities\atribut,b_at_type\b_ab_type,b_ab_id\b_at_id,номер в списке айдишников
        if(abil_or_atrib[tp][ab_or_at[i]]<5):
            if(abil_or_atrib == pl_ch.atribut and (self.exp - abil_or_atrib[tp][ab_or_at[i]] * 4)>=0):
                self.exp -= abil_or_atrib[tp][ab_or_at[i]] * 4
                abil_or_atrib[tp][ab_or_at[i]]+=1
            elif(abil_or_atrib[tp][ab_or_at[i]] == 0 and self.exp-3 >=0):
                self.exp -= 3
                abil_or_atrib[tp][ab_or_at[i]]+=1
            elif(abil_or_atrib == pl_ch.abilities and (self.exp - abil_or_atrib[tp][ab_or_at[i]] * 3)>=0 and abil_or_atrib[tp][ab_or_at[i]] != 0):
                self.exp -= abil_or_atrib[tp][ab_or_at[i]] * 3
                abil_or_atrib[tp][ab_or_at[i]]+=1
            else:
                print('Недостаточно очков опыта')
            print(self.exp)
        else:
            print(ab_or_at[i],"максимален")
            

    def make_table(self):
        for j in range(2):
            self.x+=[self.x[-1]+self.w+5]
            self.y_at+=[self.y_at[-1]+self.h]
            self.x_tp+= [self.x_tp[-1]+self.w+5]
        for ij in range(5):
            self.y_ab+=[self.y_ab[-1]+self.h]
        
test = Charsheet_button()
test.make_table()

'''
class Main_window_button(Button):
    def __init__(self,x,y,w,h,b_id):
        Button.__init__(x,y,w,h,b_id)
'''
    
