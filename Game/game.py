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