# Solution to Euler Problems 18 and 67 (since they are the same problem with different sizes)


def solution(triFile: str) -> (int):
    '''Creates a new triange where a value is the max of the two lower values
    summed with the corresponding value in the original triangle'''
    # Setup triangle from file
    original = list()
    with open(triFile) as f:
        for line in f:
            original.append(list(map(int, line.strip().split())))

    # Compute my answer
    triangle = list()
    triangle.append(original[-1])  # Hard code first values
    for i in range(len(original) - 2, -1, -1):
        triangle.append(list())
        for j, val in enumerate(original[i]):
            triangle[-1].append(val + max(triangle[-2][j], triangle[-2][j + 1]))
    return triangle[-1][0]

print("Solution to 18:", solution("p018_triangle.txt"))
print("Solution to 67:", solution("p067_triangle.txt"))
input("Press enter to continue...")  # Just so the screen doesn't close
