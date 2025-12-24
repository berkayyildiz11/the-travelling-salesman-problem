import numpy as np
from pymoo.core.problem import ElementwiseProblem

class TSPProblem(ElementwiseProblem):
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.n_cities = len(distance_matrix)

        super().__init__(
            n_var=self.n_cities,     # number of decision variables
            n_obj=1,                 # single objective
            n_constr=0,              # no constraints
            xl=0,                    # lower bound (city index)
            xu=self.n_cities - 1,    # upper bound (city index)
            type_var=int             # integer variables
        )

    def _evaluate(self, x, out, *args, **kwargs):
        # Calculate the total distance of the tour represented by x
        total_distance = 0.0

        for i in range(len(x)):
            from_city = x[i]
            to_city = x[(i + 1) % len(x)]  # wrap around to the start
            total_distance += self.distance_matrix[from_city][to_city]

        out["F"] = total_distance

class TSP_RandomKey(ElementwiseProblem):
    def __init__(self, cities_coordinates, distance_matrix, **kwargs):
        self.cities = cities_coordinates
        self.dist_matrix = distance_matrix
        n_cities = len(cities_coordinates)

        super().__init__(
            n_var=n_cities,
            n_obj=1,
            xl=0.0,
            xu=1.0,
            type_var=float,
            **kwargs
        )
    def _evaluate(self, x, out, *args, **kwargs):
        permutation = np.argsort(x)
        
        distance = 0.0
        for i in range(len(permutation) - 1):
            from_city = permutation[i]
            to_city = permutation[i + 1]
            distance += self.dist_matrix[from_city][to_city]
        # Return to start at the end
        distance += self.dist_matrix[permutation[-1]][permutation[0]]

        out["F"] = distance