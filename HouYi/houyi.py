"""
from Game.game import Game

class HouYi(Game):
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
        # super().__init__(1000,100)
        self.defence = 100
    def houyi_fight(self,enemy_hp,enemy_power):
        my_final_hp = self.hp + self.defence - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if my_final_hp>enemy_final_hp:
            print("我方赢了！")
        elif my_final_hp<enemy_final_hp:
            print("敌方赢了！")
        else:
            # print("平局！")
            raise Exception("他妈的没有平局！！！")

houyi=HouYi(1000,100)
houyi.houyi_fight(1000,200)
"""
class HouYi():
    def __init__(self,hp,power,defence):
        self.hp = hp
        self.power = power
        # super().__init__(1000,100)
        self.defence = defence
    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp + self.defence - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)
            if self.hp<=0 and enemy_hp>self.hp:
                print("敌方赢了！")
                break
            elif enemy_hp<=0 and self.hp>enemy_hp:
                print("我方赢了！")
                break
            elif enemy_hp<=0 and self.hp==enemy_hp:
                print("平局！")
                break
houyi=HouYi(1000,100,100)
houyi.houyi_fight(1000,200)