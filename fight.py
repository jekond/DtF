from pers import *


def fight():
    initiative_list = []
    pl_ch.start_fight(test_en)
    initiative_list += pl_ch.initiative(),pl_ch.enemy.initiative()
    while(pl_ch.status == 1 and pl_ch.enemy.status == 1):
        print(pl_ch.name,'наносит удар')
        pl_ch.melee_attack()
        print(pl_ch.enemy.name,'наносит удар')
        pl_ch.enemy.melee_attack()
        print(pl_ch.status,pl_ch.enemy.status)
    return 'ggwp'

    
    
