import numpy as np


# Exercise 1
def ways(n: int) -> int:
  
    if n < 0:
        return 0

    # Possible number of nickels we can use is from 0 to n // 5
    nickel_counts = np.arange(0, (n // 5) + 1)

    # Pennies required for each choice of nickels
    penny_counts = n - (5 * nickel_counts)

    # Only keep valid cases where pennies are non-negative
    valid_cases = penny_counts >= 0

    return np.count_nonzero(valid_cases)


if __name__ == "__main__":
    # Take input from the user
    n = int(input("Enter the amount in cents: "))
    result = ways(n)
    print(f"Number of ways to make {n} cents: {result}")
    

# Exercise 2
# Part 1
def lowest_score(names, scores) -> str:
    """
    Return the name of the student with the lowest score.
    """
    names = np.array(names)
    scores = np.array(scores)

    idx = np.argmin(scores)
    return names[idx]

# Part 2
def sort_names(names, scores) -> list:
    """
    Return a list of (name, score) pairs sorted by descending score.
    """   
    names = np.array(names)
    scores = np.array(scores)

    sorted_indices = np.argsort(scores)[::-1]
    sorted_names = names[sorted_indices]
    sorted_scores = scores[sorted_indices]
    return list(zip(sorted_names.tolist(), sorted_scores.tolist()))

if __name__ == "__main__":
    names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
    scores = np.array([99, 71, 85, 62, 91])

    print("")
    print(lowest_score(names, scores), "has lowest score")
    print("Students sorted by scores:", sort_names(names, scores))
