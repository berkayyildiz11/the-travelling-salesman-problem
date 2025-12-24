import numpy as np
from src.tsp_utils import load_distance_matrix, load_cities
from src.tsp_problem import TSP_RandomKey, TSPProblem

cities_coordinates = load_cities("data/cityData.txt")
distance_matrix = load_distance_matrix("data/intercityDistance.txt")
problem1 = TSPProblem(distance_matrix)

x = np.arange(len(distance_matrix))  # [0,1,2,...]
out = {}
problem1._evaluate(x, out)
print("Total distance:", out["F"])

problem2 = TSP_RandomKey(cities_coordinates, distance_matrix)

x = np.arange(len(distance_matrix))  # [0,1,2,...]
out = {}
problem2._evaluate(x, out)
print("Total distance:", out["F"])
