import bisect
import itertools
import functools


NUMBER_OF_PLAYERS = int(input("Number of players? "))

possiblePoints = [2, 3, 4, 10, 11]
allPoints = ()

for point in possiblePoints:
    for _ in range(4):
        allPoints += (point,)



@functools.cache
def findAddendsRecurisive(numbers, path, total , runningTotal):
    if total == runningTotal:
        solutions.add(path)
        return 
    elif runningTotal > total:
        return 
    for input in numbers:
        mutableNumbers = list(numbers)
        mutableNumbers.remove(input)
        newNumbers = tuple(mutableNumbers)
        mutablePath = list(path)
        bisect.insort(mutablePath, input)
        newPath = tuple(mutablePath)
        findAddendsRecurisive(newNumbers, newPath, total, runningTotal + input)


def findAddends(numbers, total):
    global solutions
    solutions = set()
    path = ()
    runningTotal = 0
    findAddendsRecurisive(numbers, path, total, runningTotal)
    return solutions


allPaths = findAddends(allPoints, 120 / NUMBER_OF_PLAYERS)

print(len(allPaths))

print(allPaths)

solutions = set()


#Try all combinations of solutions to see if they work
for possibleSolution in itertools.combinations_with_replacement(allPaths, NUMBER_OF_PLAYERS):
    possibleSolutionCombined = tuple(sorted(functools.reduce(lambda x, y: x+y, possibleSolution)))
    if possibleSolutionCombined == allPoints:
        solutions.add(frozenset(possibleSolution))

for solution in solutions:
    print(solution)

print("Number of ways to draw", len(solutions))

