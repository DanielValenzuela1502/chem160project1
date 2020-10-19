import random
from random import choice
npart=500
side=31  #Should be an odd number
maxsteps = 10000
time = 0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
density = 0.5
perc = 0
for ipart in range(npart):
    # Start particle at center
    x,y = side//2,side//2
    counter=0
    for x in range(side):
        for y in range(side):
            grid[x][y]=random.random()
            if  grid[x][y] < density:
                grid[x][y] = 1
            else:
                grid[x][y] = 0
    # perform the random walk until particle departs
    x,y = side//2,side//2
    for step in range(maxsteps):
        counter+=1
        grid[x][y]=0   #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
            time+= counter
            perc+=1
            break
        if grid[x][y] == 1:
            x -= sx
            y -= sy
        continue
        grid[x][y]=1   #Put particle in new location
avetime=time/npart
print(perc/npart)