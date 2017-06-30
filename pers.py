from cub import *
from weapon import *
import random

class Characher:
    def __init__(self,name,race):
        self.name = name
        self.health = [0,0,0,0]
        self.enemy = 0
        self.atribut={'Physical':{'Strenght':1,'Dexterity':1,'Stamina':1},
                      'Social':{'Charisma':1,'Manipulation':1,'Appearance':1},
                      'Mental':{'Perception':1,'Intelligence':1,'Wits':1}}
        self.abilities={'Talents':{'Athletics':0,'Brawl':0,'Dodge':0,'Intimidation':0,'Cunning':0,'Leadership':0},
                        'Skills':{'Firearms':0,'Melee':0,'Securiti':0,'Stealth':0,'Acting':0,'Search':0},
                        'Knowledges':{'Computer':0,'Finance':0,'Investigation':0,'Medicine':0,'Politics':0,'Religion':0}}
        self.weapon_use=fist
        self.race=race#Пока только Демон и Человек. Можно подумать и над другими существами, а-ля Животные и Вампиры
        self.willpower = [5,5]#Сила воли. На данный момент и максимальная
        self.faith = [5,5]#Вера. На данный момент и максимальная
        self.throe = 4#Мука
        self.status = 1#1 - живой. 0 - мертв
###
###Прочие действия
###
        
#
#Функция отметки противника, занесение его в атрибут Enemy
#
    def start_fight(self,enemy):
        self.enemy = enemy
        self.enemy.enemy = self

#
#Функция определения инициативы в бою
#
    def initiative(self):
        initiative = random.randint(1,10) + self.atribut['Physical']['Dexterity'] + self.atribut['Mental']['Wits']
        return initiative

#
#Функция проникновения. Использовать при зломе замков, обходе всяких камер и лазерных защит
#
    def penetr(self,hard):# Надо придумать название получше
        return prov(self.atribut['Physical']['Dexterity']
                    + self.abilities['Skills']['Securiti'],hard,self.health[3])
    
#
#Функция прыжка. Будет определять высоту прыжка в боевке и возможность использовать это в диалоговом
#Каждый успех = 2 фута вверх
    def jump(self,hard):
        return prov(self.atribut['Physical']['Strenght'],hard,self.health[3])
#
#Функция выламывания двери силой
#
    def puch_door(self,hard,time,c_hard):
        return c_prov(self.atribut['Physical']['Strenght'],
                      hard,self.health[3],time,c_hard)
#
#Функция преследования
#
    def pursuit(self,hard,time,c_hard):
        return c_prov(self.atribut['Physical']['Dexterity']
                      +self.abilities['Talents']['Athletics'],hard,time,c_hard)
#
#Функция стелс
#
    def steals(self,hard):
        return prov(self.atribut['Physical']['Dexterity']
                    +self.abilities['Skills']['Stealth'],hard,self.health[3])
#
#Функция слежки
#
    def shadowing(self):
        return steals(self.enemy.atribut['Mental']['Wits']
                      +self.enemy.atribut['Mental']['Perception'])
###
###Ментальные действия. В диалоговом режиме
###

#
#Функция взлома компьютера
#
    def hack(self,hard):#hard - сложность действия
        return prov(self.atribut['Mental']['Wits']
             + self.abilities['Knowledges']['Computer'],hard,self.health[3])
#
#Функция расследования
#
    def investigation(self,hard):
        return prov(self.atribut['Mental']['Perception']
                    + self.abilities['Knoowledges']['Investigation'],hard,self.health[3])
#
#Функция исследования. Будет использоваться в случае необходимости развивать какую-нибудь из отреслей в режиме стратегии. В зависимсти от отрасли выбирается навык
#
    def recearch(self,hard,domain):
        return prov(self.atribut['Mental']['Intelligence']
                    + self.abilities['knowlendges'][domain],hard,self.health[3])
###
###Социальные действия. В диалоговом режиме
###

#
#Функция обмана\Притворства
#
    def fraud(self):
        return prov(self.atribut['Social']['Manipulation']
                    + self.abilities['Talents']['Cunning'],7,self.health[3])
#
#Функция запугивания
#
    def intimidation(self):
        return prov(self.atribut['Social']['Manipulation']
                    + self.abilities['Talents']['Intimidation'],6,self.health[3])
#
#Функция красноречия. Сюда же относятся и выступления.
#
    def speach(self,hard):
        return prov(self.atribut['Social']['Charisma']
                    + self.abilities['Skills']['Acting'],hard,self.health[3])

###
###Боевые действия. В платформере
###

#
#Функция атаки голыми руками\кастет
#
    def melee_attack(self):
        dmg=0
        if(self.enemy.health[3]=='!'):
            a='+'*(self.atribut[self.weapon_use.owner[0]][self.weapon_use.owner[1]] +
                   self.abilities[self.weapon_use.owner[2]][self.weapon_use.owner[3]])
        else:
            a=prov(self.atribut[self.weapon_use.owner[0]][self.weapon_use.owner[1]] +
                   self.abilities[self.weapon_use.owner[2]][self.weapon_use.owner[3]],6,self.health[3])
        #print (a)
        if (a!='-' and a!='0'):
            dmg=no_fail_prov(self.atribut['Physical']['Strenght']+(len(a)-1)+self.weapon_use.bonus,6,self.health[3])
            self.enemy.absorb_dmg(dmg,self.weapon_use.dmg_type)
        elif(a=='-'):
            print("!ПРОВАЛ!")
        else:
            print("Промах")
#
#Функция поглощения урона
#
    def absorb_dmg(self,dmg,dmg_type):
        if(self.race=='Demon' and dmg_type!='aggravating' or self.race=='Human' and dmg_type=='externally'):
            b=no_fail_prov(self.atribut['Physical']['Stamina'],6,0)
        else: b=0
        self.lost_hp(dmg-b,dmg_type)
        print(self.health,'Поглощено',b,'урона. Из',dmg)
        
#
#Функция здоровья
#
    def lost_hp(self,dmg,d_type):
        if(d_type=='externally'): a=0
        elif(d_type=='lethal'): a=1
        else: a=2
        for i in range(dmg):
            self.health[a]+=1
            print(self.health[a],'!')
            if(d_type=='externally' and self.health[0]+self.health[1]+self.health[2]>7):
                print(self.health[a],'!!')
                self.health[0]-=2
                self.health[1]+=1
                print(self.health[a],'!!!')
            if(self.health[1] + self.health[2] == 8):
                print('Персонаж умер',self.health)
                self.status = 0
                break
            elif(d_type=='lethal' and self.health[0]+self.health[1]+self.health[2]==8 or
                 d_type=='aggravating' and self.health[0]+self.health[1]+self.health[2]==8):
                print('Персонаж умер',self.health)
                self.status = 0
                break
        self.check_hp()
#
#Функция отвечающая за ранения
#
    def check_hp(self):
        if(0<=self.health[0]+self.health[1]+self.health[2]<=1): self.health[3]=0
        elif(1<self.health[0]+self.health[1]+self.health[2]<=3): self.health[3]=1
        elif(3<self.health[0]+self.health[1]+self.health[2]<=5): self.health[3]=2
        elif(5<self.health[0]+self.health[1]+self.health[2]<7): self.health[3]=5
        else: self.health[3]='!'


    
pl_ch = Characher('Torton','Demon')
test_en = Characher('Borbon','Human')
#Babbi_Bob = Characher('Barbon','Demon')
