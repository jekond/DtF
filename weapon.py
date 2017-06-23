class Weapon:
    def __init__(self,name,bonus):
        self.name = name
        self.w_type = ''
        self.dmg_type = ''
        self.bonus = bonus
        self.owner = ['','','','']#Класс Персонаж, Тип атрибута, атрибут. Тип абилки, абилка

class Melee(Weapon):
    def __init__ (self,name,bonus):
        Weapon.__init__(self,name,bonus)
        self.w_type = 'Melee'
        self.owner = ['Physical','Dexterity','Skills','Melee']

class Externally_melee(Melee):
    def __init__(self,name,bonus):
        Melee.__init__(self,name,bonus)
        self.dmg_type = 'externally'

class Fists(Externally_melee):
    def __init__(self):
        Externally_melee.__init__(self,'Рукопашный бой',0)
        self.owner = ['Physical','Dexterity','Talents','Brawl']

fist = Fists()#Обект для рукопашной


class Lethal_melee(Melee):
    def __init__(self,name,bonus):
        Melee.__init__(self,name,bonus)
        self.dmg_type = 'lethal'

knife = Lethal_melee('Нож',1) 

class Range(Weapon):
    def __init__ (self,name,bonus):
        Weapon.__init__(self,name,bonus)
        self.w_type = 'Range'
        self.dmg_type = 'lethal'
        self.owner = ['Mental','Perception','Skills','Firearms']        
