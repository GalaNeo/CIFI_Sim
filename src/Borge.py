import random
from Upgrades import upgrades
from Attributes import attributes
from BorgeMonsters import enemy

class Hunter:
    # base atr
    base_health = 43
    base_attack = 3
    base_regen = 0.025
    base_damage_reduction = 0
    base_evasion = 1.00
    base_effect_chance = 4
    base_crit_chance = 5
    base_crit_power = 1.30
    base_attack_speed = 5

    inscryption_03_bonus = 6
    inscryption_04_bonus = 0.65
    inscryption_11_bonus = 2
    inscryption_13_bonus = 1
    inscryption_14_bonus = 1.10
    inscryption_23_bonus = 0.04
    inscryption_24_bonus = 0.4
    inscryption_27_bonus = 24
    inscryption_44_bonus = 1.08

    relic_4_bonus = 0.02
    relic_9_bonus = 1.05

    """
    Edit attribute and upgrades according to your hunter's
    """
    upgrade_levels = {
        "Revives": 1,
        "LifeSteal": 2,
        "Potion": 0,
        "Impact": 1,
        "Omen": 0,
        "LuckyLoot": 10,
        "POG": 0,
        "FOW": 1,
    }

    attribute_levels = {
        "Ares": 1,
        "Ylith": 1,
        "Baal": 3,
        "Barrier": 1,
        "Inhaler": 1,
        "Punches": 1,
        "Sensors": 1,
        "Spartan": 1,
        "Timeless": 1,
        "BFB": 0,
        "Weakspot": 1,
        "Atlas": 0,
    }

    def __init__(self, health_lvl, attack_lvl, regen_lvl, damage_reduction_lvl, evasion_lvl, effect_chance_lvl, crit_chance_lvl, crit_power_lvl, attack_speed_lvl,
                 inscryption_03_lvl, inscryption_04_lvl, inscryption_11_lvl, inscryption_13_lvl, inscryption_14_lvl, inscryption_23_lvl, inscryption_24_lvl,
                 inscryption_27_lvl, inscryption_44_lvl, relic_4_levels, relic_9_levels):



        self.inscryption_03 = inscryption_03_lvl * self.inscryption_03_bonus
        self.inscryption_04 = inscryption_04_lvl * self.inscryption_04_bonus
        self.inscryption_11 = inscryption_11_lvl * self.inscryption_11_bonus
        self.inscryption_13 = inscryption_13_lvl * self.inscryption_13_bonus
        self.inscryption_14 = pow(self.inscryption_14_bonus, inscryption_14_lvl)
        self.inscryption_23 = inscryption_23_lvl * self.inscryption_23_bonus
        self.inscryption_24 = inscryption_24_lvl * self.inscryption_24_bonus
        self.inscryption_27 = inscryption_27_lvl * self.inscryption_27_bonus
        self.inscryption_44 = pow(self.inscryption_44_bonus, inscryption_44_lvl)

        self.relic_4 =  1 + (self.relic_4_bonus * relic_4_levels) #hp relic
        self.relic_9 = pow(self.relic_9_bonus, relic_9_levels) #loot relic

        '''
        print("\nInscryption 03", self.inscryption_03, "\nInscryption 04", self.inscryption_04, "\nInscryption 11", self.inscryption_11, "\nInscryption 13", self.inscryption_13,
              "\nInscryption 14", self.inscryption_14, "\nInscryption 23", self.inscryption_23, "\nInscryption 24", self.inscryption_24, "\nInscryption 27", self.inscryption_27,
              "\nInscryption 44", self.inscryption_44, "\nRelics 4 and 9", self.relic_4, self.relic_9)

        '''

        self.health_lvl = health_lvl
        self.attack_lvl = attack_lvl
        self.regen_lvl = regen_lvl
        self.damage_reduction_lvl = damage_reduction_lvl
        self.evasion_lvl = evasion_lvl
        self.effect_chance_lvl = effect_chance_lvl
        self.crit_chance_lvl = crit_chance_lvl
        self.crit_power_lvl = crit_power_lvl
        self.attack_speed_lvl = attack_speed_lvl



        ###
        self.revives = 0
        self.c_lifesteal = 0
        self.potion = 0
        self.omen = 0
        self.luckyloot = 0
        self.fow = 0
        self.pog = 0
        self.stun_duration = 0
        self.impact_damage = 0
        ###
        self.ares_max_health = 0
        self.ares_additional_damage = 0
        self.ylith_flat = 0
        self.ylith_increase = 0
        self.baal = 0
        self.barrier = 0
        self.inhaler = 0
        self.spartan = 0
        self.punches_chance = 0
        self.punches_power = 0
        self.sensors_evade = 0
        self.sensors_effect = 0
        self.timeless = 0
        self.bfb = 0
        self.weakspot = 0
        self.atlas = 0
        ###
        self.boss_dr = 0
        self.boss_effect_chance = 0
        self.boss_crit_chance = 0
        self.boss_attackspeed = 0
        ###

        self.upgrade_system = upgrades(self)
        self.attribute_system = attributes(self)

        ###
        self.max_health = (self.base_health + (self.health_lvl * (2.5 + 0.01 * int(self.health_lvl / 5))) + self.inscryption_03 + self.inscryption_27) * ( 1 + self.ares_max_health) * (self.relic_4)
        self.health = self.max_health
        self.attack = (self.base_attack + self.impact_damage + self.inscryption_13 + (self.attack_lvl * (0.5 + 0.01 * int(self.attack_lvl / 10)))) * (1 + self.ares_additional_damage)
        self.regen = (self.base_regen + self.ylith_flat + (self.regen_lvl * (0.03 + 0.01 * int(self.regen_lvl / 30)))) * (1 + self.ylith_increase)
        self.damage_reduction = self.base_damage_reduction + (self.damage_reduction_lvl * 1.44) + self.inscryption_24 + self.spartan
        self.evasion = self.base_evasion + (self.evasion_lvl * 0.34) + self.sensors_evade
        self.effect_chance = self.base_effect_chance + (self.effect_chance_lvl * 0.5) + self.inscryption_11 + self.sensors_effect
        self.crit_chance = self.base_crit_chance + (self.crit_chance_lvl * 0.18) + self.inscryption_04 + self.punches_chance
        self.crit_power = self.base_crit_power + (self.crit_power_lvl * 0.01) + self.punches_power
        self.unaffected_as = self.base_attack_speed - ((self.attack_speed_lvl * 0.03) + self.inscryption_23)
        self.attack_speed = self.unaffected_as
        self.attack_timer = 0

        self.apply_upgrades(self.upgrade_levels)
        self.apply_attributes(self.attribute_levels)
        self.apply_stats()

        #print(self.revives, self.max_health,self.health,self.attack,self.regen,self.damage_reduction,self.evasion,
             # self.effect_chance,self.crit_chance,self.crit_power,self.attack_speed,self.attack_timer,)


    def apply_upgrades(self, upgrade_levels):

        for upgrade_name, level in upgrade_levels.items():
            #print("test")
            # call the apply_upgrades method of the upgrades class with the specified upgrade level
            self.upgrade_system.apply_upgrades(upgrade_name, self.upgrade_system.upgrades[upgrade_name]["effects"], level)

    def apply_attributes(self, attribute_levels):

        for attribute_name, level in attribute_levels.items():
            # print("test")
            # call the apply_attributes method of the attributes class with the specified attribute level
            self.attribute_system.apply_attributes(attribute_name, self.attribute_system.attributes[attribute_name]["effects"],level)

    def apply_stats(self):
        self.max_health = (self.base_health + (self.health_lvl * (2.5 + 0.01 * int(self.health_lvl / 5))) + self.inscryption_03 + self.inscryption_27) * (1 + self.ares_max_health) * (self.relic_4)
        self.health = self.max_health
        self.attack = (self.base_attack + self.impact_damage + self.inscryption_13 + (self.attack_lvl * (0.5 + 0.01 * int(self.attack_lvl / 10)))) * (1 + self.ares_additional_damage)
        self.regen = (self.base_regen + self.ylith_flat + (self.regen_lvl * (0.03 + 0.01 * int(self.regen_lvl / 30)))) * (1 + self.ylith_increase)
        self.damage_reduction = self.base_damage_reduction + (self.damage_reduction_lvl * 1.44) + self.inscryption_24 + self.spartan
        self.evasion = self.base_evasion + (self.evasion_lvl * 0.34) + self.sensors_evade
        self.effect_chance = self.base_effect_chance + (self.effect_chance_lvl * 0.5) + self.inscryption_11 + self.sensors_effect
        self.crit_chance = self.base_crit_chance + (self.crit_chance_lvl * 0.18) + self.inscryption_04 + self.punches_chance
        self.crit_power = self.base_crit_power + (self.crit_power_lvl * 0.01) + self.punches_power
        self.unaffected_as = self.base_attack_speed - ((self.attack_speed_lvl * 0.03) + self.inscryption_23)
        self.attack_speed = self.unaffected_as
        self.attack_timer = 0

    # c_ = conditional cuz affected from effect chance , crit chance , etc.?


    def apply_revives(self, value):
        self.revives = value

    def apply_lifesteal(self, value):
        self.c_lifesteal = value

    def apply_potion(self, value):
        self.potion = value

    def apply_omen(self, value):
        self.omen = value

    def apply_luckyloot(self, value):
        self.luckyloot = value

    def apply_pog(self, value):
        self.pog = value

    def apply_fow(self, value):
        self.fow = value

    def apply_impact(self, stun_duration, impact_damage):
        self.stun_duration = stun_duration
        self.impact_damage = impact_damage


    ####################
    ##                ##
    ##   ATTRIBUTES   ##
    ##                ##
    ####################

    def apply_ares(self, max_health, additional_damage):
        self.ares_max_health = max_health
        self.ares_additional_damage = additional_damage

    def apply_ylith(self, regen_increase, flat_regen):
        self.ylith_flat = flat_regen
        self.ylith_increase = regen_increase

    def apply_baal(self, value):
        self.baal = value

    def apply_barrier(self, value):
        self.barrier = value

    def apply_inhaler(self, value):
        self.inhaler = value

    def apply_spartan(self, value):
        self.damage_reduction = value

    def apply_sensors(self, evade_chance, effect_chance):
        self.sensors_evade = evade_chance
        self.sensors_effect = effect_chance

    def apply_punches(self, crit_chance, crit_power):
        self.punches_chance = crit_chance
        self.punches_power = crit_power

    def apply_timeless(self, value):
        self.timeless = value

    def apply_bfb(self, value):
        self.bfb = value

    def apply_weakspot(self, value):
        self.weakspot = value


    def apply_atlas(self, damage_reduction, effect_chance, crit_chance,as_reduction):
        self.boss_dr = damage_reduction
        self.boss_effect_chance = effect_chance
        self.boss_crit_chance = crit_chance
        self.boss_attackspeed = as_reduction

    def use_potion(self):
        effect_chance = self.effect_chance
        effect_roll = random.uniform(0, 100)
        if effect_roll <= effect_chance:
            self.health = self.health + (self.max_health * self.potion)

    def attack_enemy(self, enemy):
        self.attack_speed = self.unaffected_as
        lifesteal = self.baal
        damage = self.calculate_damage()
        effect_chance = self.effect_chance

        if self.c_lifesteal > 0:
            lifesteal_roll = random.uniform(0, 100)
            if lifesteal_roll <= effect_chance:
                self.health = self.health + (damage * (lifesteal+self.c_lifesteal))
                #print("lifestealed pog!")
        else:
            self.health = self.health + (damage * lifesteal)
            #print("lifestealed meh")

        if self.fow > 0:
            fow_effect_roll = random.uniform(0, 100)
            if fow_effect_roll <= effect_chance:
                self.attack_speed = self.unaffected_as - self.fow

        if self.stun_duration > 0:
            stun_effect_roll = random.uniform(0, 100)
            if stun_effect_roll <= effect_chance:
                #print("before", enemy.unaffected_as)
                enemy.attack_speed = enemy.unaffected_as + self.stun_duration
                #print("after", enemy.attack_speed)

        enemy.receive_damage(damage)



    def calculate_damage(self):
        missing_health_pr = 1 - (self.health/self.max_health)
        bfb_damage = self.bfb * missing_health_pr * 100
        damage = self.attack * (1 + bfb_damage)
        crit_roll = random.uniform(0, 100)
        if crit_roll <= self.crit_chance:
            #print(" borge scored a critical hit!")
            return damage * self.crit_power   # More damage for a critical hit
        else:
            return damage

    def receive_damage(self, damage, enemy, is_critical):
        evade_chance = self.evasion
        evade_roll = random.uniform(0, 100)
        #print(self.health)
        if is_critical==True:
            weakspot_damage = damage * self.weakspot
            damage = damage - weakspot_damage

        if evade_roll > evade_chance:
            damage -= (self.damage_reduction / 100) * damage
            barrier_damage = damage * self.barrier
            #print(self.health)
            self.health -= damage
            enemy.receive_damage(barrier_damage)
            #print(barrier_damage)
            revives = self.revives
            #print(f" borge took {damage} damage. borge's health: {self.health}")
            if self.health <= 0 and revives > 0:
                #print('current revives', self.revives)
                self.respawn_hunter()
                self.revives -= 1
                #print('revives left', self.revives)

    def regeneration(self):

        regeneration_amount = 0
        missing_health = self.max_health - self.health
        regeneration_amount = self.regen
        inhaler_amount = (missing_health * self.inhaler)
        self.health += regeneration_amount + inhaler_amount
        if self.health > self.max_health:
            self.health = self.max_health

    def respawn_hunter(self):
        #print('\nHunter ', self.health)
        self.health = self.max_health * 0.8
        #print('\nHunter respawned', self.health)

    def print_stats(self):
        print(f"\nHunter Stats:")
        print(f"  Health: {self.health}/{self.max_health}")
        print(f"  Attack: {self.attack}")
        print(f"  Regen: {self.regen}")
        print(f"  Damage Reduction: {self.damage_reduction}")
        print(f"  Evasion: {self.evasion}")
        print(f"  Effect Chance: {self.effect_chance}")
        print(f"  Crit Chance: {self.crit_chance}")
        print(f"  Crit Power: {self.crit_power}")
        print(f"  Attack Speed: {self.attack_speed}")
        print(f"\nUpgrades and Effects")
        print(f"  Revives: {self.revives}")
        print(f"  Lifesteal: {self.c_lifesteal}")
        print(f"  AutoPotion: {self.potion}")
        print(f"  Omen: {self.omen}")
        print(f"  LuckyLoot : {self.luckyloot}")
        print(f"  FOW: {self.fow}")
        print(f"  POG: {self.pog}")
        print(f"  Impact: Stun Duration: {self.stun_duration} Additional Damage: {self.impact_damage}")
        print(f"\nAttributes and Effects")
        print(f"  Ares: Max Health {self.ares_max_health} Damage {self.ares_additional_damage}")
        print(f"  Ylith: Regen Increase {self.ylith_increase} Flat Regen {self.ylith_flat}")
        print(f"  Baal: {self.baal}")
        print(f"  Barrier: {self.barrier}")
        print(f"  Inhaler: {self.inhaler}")
        print(f"  Punches: Crit Chance {self.punches_chance} Crit Power {self.punches_power}")
        print(f"  Sensors: Effect Chance {self.sensors_effect} Evade Chance {self.sensors_evade}")
        print(f"  Spartan: {self.spartan}")
        print(f"  Timeless: {self.timeless}")
        print(f"  BFB: {self.bfb}")
        print(f"  Weakspot: {self.weakspot}")
        print(f"  Atlas: Add. DR: {self.boss_dr} Add. EffCh: {self.boss_effect_chance} Add. CritCh: {self.boss_crit_chance} Add. Reduced AS:{self.boss_attackspeed}")
