import random
"""
Not used in current version
"""
class LootTable:

    def __init__(self):
        self.resources = [
            {"name": "Resource1", "value_per_amount": 3},
            {"name": "Resource2", "value_per_amount": 2},
            {"name": "Resource3", "value_per_amount": 1}
        ]

    def roll_loot(self):
        loot = []

        for resource in self.resources:
            amount = random.randint(1, 5)
            total_value = amount * resource["value_per_amount"]
            loot.append({"name": resource["name"], "amount": amount, "total_value": total_value})

        return loot


loot_table = LootTable()
result = loot_table.roll_loot()

