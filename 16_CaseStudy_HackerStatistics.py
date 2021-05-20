# Hacker Statistics - Empire State Building Simulation
"""
Concepts:
-----------

Hacker Statistics:
    - Use simulated repeated measurements to gather more info about data.
    - The basic idea is that instead of literally repeating the data acquisition over and over again,
        we can simulate those repeated measurements using Python.

Random Walk:
    - Random Step: Any instance of an event, In this case, throwing a dice once.
    - A series of Random steps is known as RANDOM WALK.
    -

Distribution of Random Walk:
    - Running random walk multiple times, and noting down the eventual value of each walk.
    - Then these final value distribution is almost NORMAL DISTRIBUTION.
"""

"""
Problem: 
- You have to go to the Empire State Building from Step 50(assumption).
    In the Empire State Building bet, your next move depends on the number of eyes you throw with the dice.

- If the dice value is 1 or 2, then u go -1 step, else you go +1 step.
- If the value is 6, u will throw the dice again, and go the number of steps as the value of the thrown dice.
- Obviously, you cannot go lower than 0 step,  and u also have 0.1% chance of falling down to stair 0.
- Keeping all this in mind, you bet with a friend that you will reach 60 steps higher high within 100 attempts of throwing a dice.


Solution/Approach:

1. Simulate the entire process 1000's of times
    - where each event is 100 times a dice is thrown
    - and see the chances of reaching 60 steps

Tools needed:
    1. Random generators to simulate the dice - using seed to ensure reproducibility
"""
# --------------------------------------------------------------------------------------------------------------------------------------------

# import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def roll_dice():
    return np.random.randint(1, 7)


def random_step(random_walk):
    step = random_walk[-1]
    dice = roll_dice()

    if dice <= 2:
        step = max(0, step - 1)  # used MAX to avoid negative value, as we cannot go further down than 0th stair
    elif dice > 2 and dice < 6:  # OR 2 < dice < 6
        step += 1
    else:
        step += roll_dice()

    # Implement clumsiness: you have a 0.1% chance of falling down to the bottom
    if np.random.rand() <= 0.001:
        step = 0

    return step


def random_walk():
    random_walk = [0]

    # A random walk consist of many random steps , in this case its 100
    for i in range(100):
        step = random_step(random_walk)
        random_walk.append(step)
        # plt.plot(random_walk)
        # plt.show()

    return random_walk


def all_walks():
    all_walks = []

    # 500 Random Walks
    for j in range(500):
        r_walk = random_walk()
        all_walks.append(r_walk)

    return all_walks


def calc_chance(ends):
    end_gt_60 = len(ends[ends > 60])
    print(f"Chance of getting 60 steps high after 100 dice throws: {(end_gt_60 / 500) * 100}%")


def visualize_all_walks(all_walks):
    # plt.hist(all_walks, bins=10)
    np_all_walks = np.array(all_walks)
    # plt.plot(np_all_walks)

    # Now every row in np_all_walks represents the position after 1 throw for the 10 random walks.
    np_aw_t = np.transpose(np_all_walks)
    plt.plot(np_aw_t)  # This shows a progression of each RANDOM walk.
    # plt.show()

    # Final values of all the walks
    ends = np_aw_t[-1]
    plt.hist(ends)

    # plt.show()

    print(np_all_walks.shape)
    print(np_aw_t.shape)

    # To calculate the chance that this end point is greater than or equal to 60,
    # you can count the number of integers in ends that are greater than or equal to 60
    #   and divide that number by 500, the total number of simulations.
    calc_chance(ends)


def run():
    np.random.seed(123)

    all_walk_values = all_walks()
    visualize_all_walks(all_walk_values)


run()
