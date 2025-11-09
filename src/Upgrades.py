class upgrades:
    """
    Do not touch unless in game CIFI values change
    """
    def __init__(self, hunter):
        self.hunter = hunter
        self.upgrades = {
            "Revives":      {"min_level": 0, "max_level": 2, "effects": [1]},
            "LifeSteal":    {"min_level": 0, "max_level": 5, "effects": [0.06]},
            "Potion":       {"min_level": 0, "max_level": 5, "effects": [0.02]},
            "Impact":       {"min_level": 0, "max_level": 10, "effects": {"stun_duration": 0.1, "additional_damage": 2}},
            "Omen":         {"min_level": 0, "max_level": 10, "effects": [0.08]},
            "LuckyLoot":    {"min_level": 0, "max_level": 10, "effects": [0.2]},
            "POG":          {"min_level": 0, "max_level": 15, "effects": [0.04]},
            "FOW":          {"min_level": 0, "max_level": 15, "effects": [0.1]},
        }


    def apply_upgrades(self, upgrade_name, effects, upgrade_level):
        upgrade_info = self.upgrades[upgrade_name]

        # check if the provided level is within the allowed range
        if upgrade_info["min_level"] <= upgrade_level <= upgrade_info["max_level"]:
            if isinstance(effects, list):
                # For lists with a single value (e.g., LifeSteal, Potion)
                scaled_effect = effects[0] * upgrade_level
                self.apply_single_effect(upgrade_name, scaled_effect)
            elif isinstance(effects, dict):
                # For dicts (e.g., Impact)
                self.apply_dict_effects(upgrade_name, effects, upgrade_level)
            else:
                print(f"Unsupported upgrade effects type for {upgrade_name}. Skipping upgrade.")

    def apply_single_effect(self, upgrade_name, effect):
        if upgrade_name in self.upgrades:
            name = upgrade_name.lower()
            method_name = f"apply_{name}"
            #print(name,method_name)
            upgrade_function = getattr(self.hunter, method_name)

            if callable(upgrade_function):
                upgrade_function(effect)
            else:
                print(f"Method {method_name} not found. Skipping upgrade.")
        else:
            raise ValueError(f"Invalid upgrade name: {upgrade_name}")

    def apply_dict_effects(self, upgrade_name, effects, upgrade_level):
        if upgrade_name == "Impact":
            stun_duration = effects["stun_duration"] * upgrade_level
            additional_damage = effects["additional_damage"] * upgrade_level
            self.hunter.apply_impact(stun_duration, additional_damage)

