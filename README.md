# CIFI Hunter Simulation

A modular combat and progression simulator for an incremental-style RPG within CIFI.  
It models the hunter Borge — built to test balance, stat growth and performance without wasting manual hours in-game.

---

##  Features

- **Turn based combat system** — Hunter and enemies trade attacks and regen over time.  
- **Stat scaling** — levels, relics, and inscryptions affect damage, HP, and regen etc.  
- **Modular structure** — attributes, upgrades, monsters, and loot are all separate systems.  
- **Simulation based testing** — evaluate progression pacing or performance instantly.  
- **Optional performance profiling** — integrated [`pyheat`](https://pypi.org/project/py-heat/) visualization for slow loops.

---

##  Purpose

Instead of grinding in-game for multiple days to see how far a Hunter build can go and wasting resources , this tool runs the same fight loops in seconds.  
You can edit Hunter stats to match your real build and get accurate results for:

- Expected stage reach  
- Death frequency  
- Average run duration  

In the future, stat data (Hunter levels, relics, inscryptions) will be loaded from a **YAML file** for easier editing.

---

## Prerequisites

- **Python 3.9+**

---

### Installation

```
git clone https://github.com/YOUR_USERNAME/CIFI_Sim.git
cd CIFI_Sim
pip install -r requirements.txt
```

---

##  Future Plans

- Rewrite nested loops into a proper turn queue system for cleaner logic and faster simulation  
- Add a loot table with resource drops, rarity weights, etc.
- Implement YAML-based config files for Hunter stats, relics, and inscryptions  
- Introduce a graphical summary or CSV export for simulation results  
- Expand enemy scaling formulas to better reflect late-game stat growth  
