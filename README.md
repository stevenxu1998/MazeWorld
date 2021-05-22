# MazeWorld
**Description:**

- Developed a program in python that teaches itself to maximize the expected reward of a user traveling through a maze and minimize the number of steps to reach the final goal/destination
- Implemented four machine learning algorithms (i.e., value iteration, policy iteration, SARSA, and QLearning) that would attempt to accomplish the program’s objective 
- Analyzed and compared the performance of each machine learning algorithm 


The program will simulate the 3 Levels of the Maze which are shown below (level 1-left image, level 2-middle image, level 3-right image):

![task1](https://user-images.githubusercontent.com/35521547/119211671-90ee0e80-ba81-11eb-8522-a5caacbf1aad.png)
![task2](https://user-images.githubusercontent.com/35521547/119211674-93e8ff00-ba81-11eb-965f-c3737abad32d.png)
![task3](https://user-images.githubusercontent.com/35521547/119211677-96e3ef80-ba81-11eb-88a9-a01d7de9aeaa.png)

**Maze Game Legend:**

**Red Square** - User block (which always starts at the top left corner of the grid)

**Yellow Circle** - Final destination/goal

**Black Square** - Wall block of the Maze that the user cannot land on

**Blue Square** - Pit blocks that the user cannot land on during the simulation

**Rules of the Game:**

There will be 2000 simulations conducted per run
If the user lands on the yellow circle, then they will get a point added to their score and complete the level
If the user lands on a Wall block, then they will lose 0.3 points and automatically get moved back to their previous position
If the user lands on a Pit block, then they will lose 10 points 
If the user lands on anything else(i.e. a white square), then they will only lose 0.1 points
If the user tries to the move to a block that doesn't exist (ex: they try going up when they are already on a top most block), then they will lose 0.1 points and remain at their current position

At the end the program will plot all 2000 simulations and output a plot looking similar to the image shown below:
![plot](https://user-images.githubusercontent.com/35521547/119214208-08786980-ba93-11eb-8a6c-6efe09e8f31b.png)














