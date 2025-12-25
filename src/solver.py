import time
import numpy as np

# Import from your other files
from tsp_utils import load_cities, load_distance_matrix
from tsp_problem import TSPProblem, TSP_RandomKey
from algorithms import run_ga, run_brkga
from visualize import visualize_five_starts

def solver():
    # 1. Load Data
    print("Loading data...")
    city_file_path = r"./data/cityData.txt"
    dist_file_path = r"./data/intercityDistance.txt"
    
    try:
        cities = load_cities(city_file_path)
        dist_matrix = load_distance_matrix(dist_file_path)
    except FileNotFoundError:
        print("Error: cityData.txt or intercity Distance.txt not found.")
        return

    # 2. Setup Problems
    problem_discrete = TSPProblem(dist_matrix)
    problem_continuous = TSP_RandomKey(cities, dist_matrix)

    # 3. Run GA
    print("\nRunning Genetic Algorithm (GA)...")
    start_time = time.time()
    res_ga = run_ga(problem_discrete, population_size=100, generations=500)
    ga_time = time.time() - start_time
    print(f"GA Result: {res_ga.F[0]:.4f} (Time: {ga_time:.2f}s)")

    # 4. Run BRKGA
    print("\nRunning BRKGA...")
    start_time = time.time()
    res_brkga = run_brkga(problem_continuous, population_size=100, generations=500)
    brkga_time = time.time() - start_time
    print(f"BRKGA Result: {res_brkga.F[0]:.4f} (Time: {brkga_time:.2f}s)")

    # 5. Compare & Visualize
    if res_ga.F[0] < res_brkga.F[0]:
        print("\nBest Algorithm: GA")
        best_tour = res_ga.X
    else:
        print("\nBest Algorithm: BRKGA")
        best_tour = np.argsort(res_brkga.X)

    # Show results
    visualize_five_starts(cities, best_tour)

if __name__ == "__main__":
    main()