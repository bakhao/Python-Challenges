
def flatlandSpaceStations(n, c):
    # Sort the list of space stations to calculate distances correctly.
    spaceStations = sorted(c)
    firstDistance = spaceStations[0]
    lastDistance = n - 1 - spaceStations[-1]
    maxDistanceStation = max(firstDistance, lastDistance)
    for i in range(len(spaceStations) - 1):
        distanceBetweenStations = spaceStations[i + 1] - spaceStations[i]
        maxDistanceForCities = distanceBetweenStations // 2
        if maxDistanceForCities > maxDistanceStation:
            maxDistanceStation = maxDistanceForCities
    return maxDistanceStation
