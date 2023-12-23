import matplotlib.pyplot as plt
import numpy as np
from game_class import game

G = game(100, 100)

S = np.random.choice([0,1],(100, 100))

G.set_state(S)

G.display()
G.tick()

while True:
    if sum(sum(G.state)) == 0:
        break
    G.display()
    G.tick()

