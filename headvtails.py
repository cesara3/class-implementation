
import random
import matplotlib.pyplot as plt
from collections import Counter

# --------------------------------------------
# Run one experiment of n coin flips
# Returns the number of heads
# --------------------------------------------
def flip_coins_once(n):
    heads = 0
    for _ in range(n):
        if random.choice(["H", "T"]) == "H":
            heads += 1
    return heads


# --------------------------------------------
# Run many experiments
# Returns a list of head counts
# --------------------------------------------
def run_coin_experiments(trials, n):
    results = []
    for i in range(trials):
        results.append(flip_coins_once(n))
    return results


# --------------------------------------------
# Print summary information
# --------------------------------------------
def print_summary(results):
    print("Average heads:", round(sum(results) / len(results), 4))
    print("Frequency count:", Counter(results))


# --------------------------------------------
# Plot histogram
# --------------------------------------------
def plot_histogram(results, n):
    plt.hist(results, bins=range(n + 2), align='left', edgecolor='black')
    plt.xlabel("Number of Heads")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of Heads in {n} Coin Flips")
    plt.xticks(range(n + 1))
    plt.show()


# --------------------------------------------
# Main program
# --------------------------------------------
trials = 100
n = 3

results = run_coin_experiments(trials, n)
print_summary(results)
plot_histogram(results, n)
