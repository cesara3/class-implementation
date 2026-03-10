import random
import matplotlib.pyplot as plt
from collections import Counter

trials = 100  # number of experiments
n = 3           # number of coin flips per experiment

results = []    # store number of heads from each experiment

for trial in range(trials):
    heads = 0
    for flip in range(n):
        if random.choice(["H", "T"]) == "H":
            heads += 1
    results.append(heads)

# Print average number of heads
print("Average heads:", sum(results) / trials)

# Print how many times each outcome occurred
"""
The computer flipped 3 coins 1000 different times.
The number before the colon is how many heads happened.
The number after the colon is how many times that happened.
"""
print("Frequency count:", Counter(results))

# Histogram
plt.hist(results, bins=range(n+2), align='left')
plt.xlabel("Number of Heads")
plt.ylabel("Frequency")
plt.title(f"Histogram of Heads in {n} Coin Flips")
plt.show()



