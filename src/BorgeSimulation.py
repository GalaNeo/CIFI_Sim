from Borge          import Hunter
from BorgeMonsters  import enemy
from LootTable import LootTable
import time

# Main simulation script for testing the Hunter ("Borge")
# against progressively scaling enemies. Used to evaluate
# stat builds, scaling formulas, and general progression balance.

def create_hunter():
    """
    Edit stats according to the hunter's performance you want to simulate
    Also edit your Inscryption levels and relics
    """
    health_lvl = 1
    attack_lvl = 1
    regen_lvl = 1
    damage_reduction_lvl = 1
    evasion_lvl = 1
    effect_chance_lvl = 1
    crit_chance_lvl = 1
    crit_power_lvl = 1
    attack_speed_lvl = 1

    '''    
    Inscryption  # 44 x1.08 loot per lvl 10 levels
    Inscryption  # 27 +24 hp per lvl 10 levels
    Inscryption  # 24 +0.4 dr per lvl 8 lvls
    Inscryption  # 23 -0.04 as per lvl 5 lvls
    Inscryption  # 14 x1.10 loot per lvl 5 lvls
    Inscryption  # 13 +1 dmg per lvl 9 lvls
    Inscryption  # 11 +2 effect chance per lvl 3lvls
    Inscryption  # 4 +0.65 crit chance per lvl 6 lvls
    Inscryption  # 3 +6hp oer lvl 8 lvls
    '''
    inscryption_03_lvl = 8
    inscryption_04_lvl = 6
    inscryption_11_lvl = 3
    inscryption_13_lvl = 8
    inscryption_14_lvl = 5
    inscryption_23_lvl = 5
    inscryption_24_lvl = 8
    inscryption_27_lvl = 10
    inscryption_44_lvl = 10

    relic_4_lvl = 3 #hp relic
    relic_9_lvl = 3 #loot relic



    # create a new instance of the hunter with the initial stats
    Borge = Hunter(health_lvl, attack_lvl, regen_lvl, damage_reduction_lvl, evasion_lvl, effect_chance_lvl,crit_chance_lvl, crit_power_lvl, attack_speed_lvl,
                  inscryption_03_lvl, inscryption_04_lvl, inscryption_11_lvl, inscryption_13_lvl, inscryption_14_lvl, inscryption_23_lvl, inscryption_24_lvl,
                  inscryption_27_lvl, inscryption_44_lvl, relic_4_lvl, relic_9_lvl)

    #Borge.apply_upgrades(upgrade_levels)
    #Borge.apply_attributes(attribute_levels)


    return Borge

# --- Main loop ---
def Simulate(hunter, enemy, runs):
    """
    Run multiple simulations to estimate average performance.
    Each run continues until the Hunter dies, tracking stages cleared.
    """

    stage = enemy.stage
    total_run_time = 0
    current_run = 0
    combat_turn = 1
    regen_turn = 0
    highest_stage_reached = 0
    lowest_stage_died = float('inf')
    stage_count = {}

    print("Simulation Started")
    for _ in range(runs):

        starting_stage = stage
        current_stage = starting_stage
        starting_stage_kills = 0
        current_stage_kills = starting_stage_kills
        current_run += 1
        total_attack_time = 0
        regen_timer = 0

        if current_run % 20 == 0:
            completion = int(current_run / 20)
            print(completion,"/",int(runs/20)," Completed")

        while True :

            print("\nRun start", current_run)
            print("New run - starting stage:", current_stage)

            while hunter.health > 0:

                

                if regen_turn == 1:
                    combat_turn = 1
                    regen_turn = 0
                    regen_timer += 1
                    #print(hunter.health)
                    if (regen_timer % 1000 == 0):
                        #print(regen_timer/60000)
                        #print("Regenerating Hunter(Current hp+regen)" ,hunter.health,"+", hunter.regen,"")
                        hunter.regeneration()
                        #print("Regenerated (Current hp+regen)", hunter.health,"+", hunter.regen,"")
                        enemy.regeneration(hunter)
                elif combat_turn == 1:
                    regen_turn = 1
                    combat_turn = 0
                    hunter.attack_timer += 0.001
                    enemy.attack_timer += 0.001
                    if hunter.attack_timer >= (hunter.attack_speed):
                        #print("Hunter attacks", turns_per_run, "Attackspeed", hunter.attack_speed)
                        total_attack_time += hunter.attack_timer
                        hunter.attack_enemy(enemy)
                        #print(total_attack_time)
                        hunter.attack_timer = 0  # reset the attack timer

                    if enemy.attack_timer >= (enemy.attack_speed):
                        #print("Enemy attacks", turns_per_run, "Attackspeed", enemy.attack_speed, "health", enemy.health, enemy.max_health)
                        enemy.attack_hunter(hunter)
                        enemy.attack_timer = 0  # reset the attack timer

                    if enemy.health <= 0:
                        hunter.use_potion()
                        current_stage_kills += 1
                        if current_stage_kills >= 10:
                            #print(current_stage,'   ', hunter.health,'    ---hp-atk---    ', enemy.attack)
                            current_stage += 1
                            current_stage_kills = 0
                        #print("\n Borge Stage ", current_stage, 'Stage kills', current_stage_kills,'hp',hunter.health,"\n")
                        enemy.respawn_enemy(current_stage, hunter)
                        enemy.attack_timer = 0

                        if current_stage > 99:
                            break

            if hunter.health <= 0 or current_stage > 99:
                #print("test")
                total_run_time += total_attack_time
                #print("Current stage before revival", current_stage)
                hunter = create_hunter()
                #print("Current stage after revival", current_stage)
                #hunter.print_stats()
                hunter.attack_timer = 0

                if current_stage > highest_stage_reached:
                    highest_stage_reached = current_stage
                if current_stage < lowest_stage_died:
                    lowest_stage_died = current_stage

                break


        stage_count[current_stage] = stage_count.get(current_stage, 0) + 1
        #print('RESTART RUN', 'Died at Stage', current_stage)
    #print(total_run_time)
    print("\nHighest Stage Reached:", highest_stage_reached)
    print("Lowest Stage Died:", lowest_stage_died)

    print("Stage Occurrence Percentages:")
    total_runs = sum(stage_count.values())
    sorted_stage_count = dict(sorted(stage_count.items(), key=lambda x: x[0], reverse=False))
    for stage, count in sorted_stage_count.items():
        percentage = (count / total_runs) * 100
        print(f"Stage {stage}: {percentage:.2f}%")

    estimated_avg_time = (total_run_time / runs)/60
    print("\nAverage minutes taken", estimated_avg_time)
    print("\nSimulation Ended")






if __name__ == "__main__":
    # create a hunter

    t = time.localtime()
    current_time = time.strftime("\n%H:%M:%S", t)

    Borge = create_hunter()
    Borge.print_stats()
    Stage = 1
    Enemy = enemy(Stage)
    Runs = 1 # Number of times you want to run the simulation


    # Simulate the battle, Hunter, Starting Stage

    print(current_time)

    Simulate(Borge,Enemy,Runs)



    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)




