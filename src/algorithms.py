import numpy as np

from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.brkga import BRKGA
from pymoo.algorithms.soo.nonconvex.es import ES
from pymoo.optimize import minimize

from pymoo.operators.crossover.ox import OrderCrossover
from pymoo.operators.mutation.inversion import InversionMutation
from pymoo.operators.sampling.rnd import PermutationRandomSampling
from pymoo.termination import get_termination

def run_ga(problem, population_size=128, generations=200):
    algorithm = GA(
        pop_size=population_size,
        sampling=PermutationRandomSampling(),
        crossover=OrderCrossover(),
        mutation=InversionMutation(),
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", generations)

    result = minimize(
        problem,
        algorithm,
        termination,
        seed=1,
        verbose=True
    )

    return result

def run_brkga(problem, population_size=128, generations=200, elite_proportion=0.2, mutant_proportion=0.1):

    n_elites = int(population_size * elite_proportion)
    n_mutants = int(population_size * mutant_proportion)
    
    # The rest of the population is filled by offspring
    n_offsprings = population_size - n_elites - n_mutants

    algorithm = BRKGA(
        n_elites=n_elites,
        n_offsprings=n_offsprings,
        n_mutants=n_mutants,
        bias=0.7,
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", generations)

    result = minimize(
        problem,
        algorithm,
        termination,
        seed=1,
        verbose=True
    )

    return result

def run_es(problem, population_size=128, generations=200, sigma=0.1):
    algorithm = ES(
        n_offsprings=(4 * population_size),
        pop_size=population_size,
        rule=1.0 / 7.0,
        eliminate_duplicates=True
    )

    termination = get_termination("n_gen", generations)

    result = minimize(
        problem,
        algorithm,
        termination,
        seed=1,
        verbose=True
    )

    return result
