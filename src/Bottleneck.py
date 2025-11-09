from pyheat import PyHeat

if __name__ == "__main__":
    # Profile the sim
    ph = PyHeat('src/BorgeSimulation.py')
    ph.create_heatmap()
    ph.show_heatmap()
