class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power
    def fight(self,enemy_hp,enemy_power):
        my_final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if my_final_hp>enemy_final_hp:
            print("我方赢了！")
        elif my_final_hp<enemy_final_hp:
            print("敌方赢了！")
        else:
            print("平局！")

# game=Game()
# game.fight(1000,120)

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
            print("平局！")

houyi=HouYi(1000,100)
houyi.houyi_fight(1000,200)