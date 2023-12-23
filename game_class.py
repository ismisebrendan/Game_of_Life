import matplotlib.pyplot as plt
import numpy as np

class game():

    def __init__(self, L_x, L_y):
        self.size_x = L_x
        self.size_y = L_y
        self.state = np.zeros((L_x, L_y))
        self.state_temp = np.zeros((L_x, L_y))

    def set_state(self, arr):
        self.state = arr
    
    def display(self):
        plt.pcolormesh(np.arange(1,self.size_x+1, 1), np.arange(1,self.size_y+1, 1), self.state, cmap='plasma')
        plt.show()

    def check_neigbhours(self, site):
        x, y = site
        neighbours = np.zeros((3,3))

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                neighbours[i+1, j+1] = self.state[(x+i)%self.size_x, (y+j)%self.size_y]
        return neighbours

    def update_cell(self, site):
        x, y = site
        live = sum(sum(self.check_neigbhours(site))) - self.state[x,y]
        if self.state[x,y] == 0 and live == 3:
            self.state_temp[x,y] = 1
        elif self.state[x,y] == 1 and (live == 3 or live == 2):
            self.state_temp[x,y] = 1
        else:
            self.state_temp[x,y] = 0

    def tick(self):
        self.state_temp = np.zeros((self.size_x, self.size_y))
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.update_cell((x, y))
        
        self.state = self.state_temp