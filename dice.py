import random
import matplotlib.pyplot as plt


print("\n--- ONE DIE EVENT: Rolling ≥ 5 ---")

def simulate_one_die(trials):
    count = 0

    for i in range(trials):
        roll = random.randint(1, 6)
        if roll >= 5:
            count += 1

    estimated = count / trials
    exact = 2 / 6

    print("Estimated P(roll ≥ 5):", round(estimated, 4))
    print("Exact P(roll ≥ 5):", round(exact, 4))


print("\n--- TWO DICE EVENT: At Least One 6 ---")

def simulate_two_dice(trials):
    count = 0

    for i in range(trials):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        if (d1 == 6) or (d2 == 6):
            count += 1

    estimated = count / trials
    exact = 11 / 36

    print("Estimated P(at least one 6):", round(estimated, 4))
    print("Exact P(at least one 6):", round(exact, 4))


print("\n--- HISTOGRAM: Sum of Two Dice ---")

def simulate_dice_sums(trials):

    sums = []

    for i in range(trials):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        sums.append(d1 + d2)

    plt.hist(sums, bins=range(2, 14), align='left', edgecolor='black')
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Frequency")
    plt.title("Histogram of Two-Dice Sums")
    plt.xticks(range(2, 13))
    plt.show()

    print("Estimated average sum:", round(sum(sums) / trials, 4))


print("\n--- RUNNING THE SIMULATIONS ---")

trials_one_die = 10000
trials_two_dice = 20000
trials_histogram = 20000

simulate_one_die(trials_one_die)
print()

simulate_two_dice(trials_two_dice)
print()

simulate_dice_sums(trials_histogram)