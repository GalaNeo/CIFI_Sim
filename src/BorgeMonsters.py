import random

class enemy:

    base_health = 9
    base_attack = 2.5
    base_regen = -0.16
    base_crit_chance = 0.0322
    base_crit_power = 1.21
    base_attack_speed = 4.53

    def __init__(self, stage):




        self.stage = stage
        self.health, self.attack, self.regen, self.crit_chance, self.crit_power, self.unaffected_as = self.stat_scaling(stage)
        self.max_health = self.health
        self.attack_speed = self.unaffected_as
        self.attack_timer = 0



    def stat_scaling(self,stage):
        self.stage = stage
        health = enemy.base_health + (4 * self.stage)
        attack = enemy.base_attack + (0.7 * self.stage)
        regen = enemy.base_regen + (0.08 * self.stage)
        crit_chance = enemy.base_crit_chance + (0.04 * self.stage)
        crit_power = enemy.base_crit_power + (0.008 * self.stage)
        attack_speed = enemy.base_attack_speed - (0.006 * self.stage)
        #print(attack_speed, stage)

        return health, attack, regen, crit_chance, crit_power, attack_speed

    def attack_hunter(self, hunter):
        self.attack_speed = self.unaffected_as
        damage, is_critical = self.calculate_damage()
        hunter.receive_damage(damage, self, is_critical)



    def calculate_damage(self):
        crit = False
        base_damage = self.attack
        crit_roll = random.uniform(0, 1)
        if crit_roll <= self.crit_chance:
            crit = True
            #print(" monster scored a critical hit!")
            crit_damage = (base_damage * self.crit_power)
            return crit_damage, crit # More damage for a critical hit
        else:
            crit = False
            return base_damage, crit

    def get_enemy_health(self):
        return self.health

    def receive_damage(self, damage):
        self.health -= damage
        #print(damage)
        #print(f" monster took {damage} damage. monster's health: {self.health}")

    def regeneration(self,hunter):
        regeneration_amount = self.regen - (hunter.omen * self.regen)
        self.health += regeneration_amount
        if self.health > self.max_health:
            self.health = self.max_health

    def respawn_enemy(self, stage, hunter):
        #print('\nMonster respawned\n')
        self.health, self.attack, self.regen, self.crit_chance, self.crit_power, self.unaffected_as = self.stat_scaling(stage)
        self.max_health = self.health - (self.health * hunter.pog)
        #print(stage, self.health, self.attack, self.regen, self.crit_chance, self.crit_power, self.unaffected_as)
