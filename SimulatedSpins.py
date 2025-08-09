import numpy as np
import random
from collections import Counter

# Define possible symbols (A, B, C, D) for each group
symbols = ['A', 'B', 'C', 'D']

# Function to generate a valid 3x4 slot machine layout
def generate_valid_matrix():
    grid = np.full((3, 4), '.', dtype=str)  # Fill grid with placeholders
    positions = list(range(12))  # Positions in the 3x4 grid
    random.shuffle(positions)  # Shuffle positions

    for symbol in symbols:
        group_positions = positions[:3]  # Pick 3 positions for this symbol
        positions = positions[3:]  # Remove used positions
        for pos in group_positions:
            row, col = divmod(pos, 4)
            grid[row, col] = symbol  # Place the symbol in the grid

    return tuple(grid.flatten())  # Return as a tuple for easy counting

# Simulate 50,000 spins
simulation_results = [generate_valid_matrix() for _ in range(50000)]

# Count occurrences of each unique outcome
outcome_counts = Counter(simulation_results)

# Get the 20 most frequent outcomes
most_common_outcomes = outcome_counts.most_common(20)

# Print the results as readable matrices
for rank, (outcome, count) in enumerate(most_common_outcomes, 1):
    print(f"#{rank} (Appeared {count} times):")
    matrix = np.array(outcome).reshape(3, 4)
    print(matrix, "\n")
