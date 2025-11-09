class attributes:
    """
    Do not touch unless CIFI scalings change
    """
    def __init__(self, hunter):
        self.hunter = hunter
        self.attributes = {
            "Ares":         {"min_level": 1, "max_level": 999, "effects":  {"max_health": 0.01, "additional_damage": 0.002}, "cost": 1},
            "Ylith":        {"min_level": 0, "max_level": 999, "effects":  {"regen_increase": 0.009, "flat_regen": 0.04}, "cost": 1},
            "Baal":         {"min_level": 0, "max_level": 6, "effects": [1.11], "cost": 3},
            "Barrier":      {"min_level": 0, "max_level": 10, "effects": [0.08], "cost": 2},
            "Inhaler":      {"min_level": 0, "max_level": 10, "effects": [0.008]},
            "Punches":      {"min_level": 0, "max_level": 6, "effects": {"crit_chance": 4.4, "crit_power": 0.08}, "cost": 3},
            "Sensors":      {"min_level": 0, "max_level": 6, "effects": {"evade_chance": 1.6, "effect_chance": 1.2}, "cost": 3},
            "Spartan":      {"min_level": 0, "max_level": 6, "effects": [1.5]},
            "Timeless":     {"min_level": 0, "max_level": 5, "effects": [0.14],"cost": 3},
            "BFB":          {"min_level": 0, "max_level": 3, "effects": [0.001],"cost": 5},
            "Weakspot":     {"min_level": 0, "max_level": 6, "effects": [0.11],"cost": 2},
            "Atlas":        {"min_level": 0, "max_level": 6, "effects": {"damage_reduction": 0.007, "effect_chance": 0.014,"crit_chance": 0.025, "as_reduction": 0.04},"cost": 3},
        }


    def apply_attributes(self, attribute_name, effects, attribute_level):
        attribute_info = self.attributes[attribute_name]

        # check if the provided level is within the allowed range
        if attribute_info["min_level"] <= attribute_level <= attribute_info["max_level"]:
            if isinstance(effects, list):
                # for lists with a single value (e.g., Baal, Inhaler)
                scaled_effect = effects[0] * attribute_level
                self.apply_single_effect(attribute_name, scaled_effect)
            elif isinstance(effects, dict):
                # For dicts (e.g., Ares, Ylith)
                self.apply_dict_effects(attribute_name, effects, attribute_level)
            else:
                print(f"Unsupported attribute effects type for {attribute_name}. Skipping attribute.")

    def apply_single_effect(self, attribute_name, effect):
        if attribute_name in self.attributes:
            name = attribute_name.lower()
            method_name = f"apply_{name}"
            #print(name,method_name)
            attribute_function = getattr(self.hunter, method_name)

            if callable(attribute_function):
                attribute_function(effect)
            else:
                print(f"Method {method_name} not found. Skipping attribute.")
        else:
            raise ValueError(f"Invalid attribute name: {attribute_name}")



    def apply_dict_effects(self, attribute_name, effects, attribute_level):
        attribute_effects = {
            "Ares": self.apply_ares,
            "Ylith": self.apply_ylith,
            "Punches": self.apply_punches,
            "Sensors": self.apply_sensors,
            "Atlas": self.apply_atlas,
        }

        effect_method = attribute_effects.get(attribute_name, "")
        if effect_method:
            effect_method(effects, attribute_level)

    def apply_ares(self, effects, attribute_level):
        max_health = effects["max_health"] * attribute_level
        additional_damage = effects["additional_damage"] * attribute_level
        self.hunter.apply_ares(max_health, additional_damage)

    def apply_ylith(self, effects, attribute_level):
        regen_increase = effects["regen_increase"] * attribute_level
        flat_regen = effects["flat_regen"] * attribute_level
        self.hunter.apply_ylith(regen_increase, flat_regen)

    def apply_punches(self, effects, attribute_level):
        crit_chance = effects["crit_chance"] * attribute_level
        crit_power = effects["crit_power"] * attribute_level
        self.hunter.apply_punches(crit_chance, crit_power)

    def apply_sensors(self, effects, attribute_level):
        evade_chance = effects["evade_chance"] * attribute_level
        effect_chance = effects["effect_chance"] * attribute_level
        self.hunter.apply_sensors(evade_chance, effect_chance)

    def apply_atlas(self, effects, attribute_level):
        damage_reduction = effects["damage_reduction"] * attribute_level
        effect_chance = effects["effect_chance"] * attribute_level
        crit_chance = effects["crit_chance"] * attribute_level
        as_reduction = effects["as_reduction"] * attribute_level
        self.hunter.apply_atlas(damage_reduction, effect_chance, crit_chance, as_reduction)
