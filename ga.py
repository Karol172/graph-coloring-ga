import numpy as np
from geneticalgorithm import geneticalgorithm as ga


class GraphColoringProblem:
    def __init__(self, filepath):
        f = open(filepath, "r")
        self.no_edges = int(f.readline())
        self.edges = list(map(lambda x: (int(x[1]), int(x[2])), [line.strip().split() for line in f]))
        self.no_vertex = np.max(np.array(self.edges))

    def solve(self, population=100, mutation_probability=0.1, crossover_probability=0.5, crossover_type='uniform',
              parents_portion=0.3, max_iteration=None):
        params = {'max_num_iteration': max_iteration,
                  'population_size': population,
                  'mutation_probability': mutation_probability,
                  'elit_ratio': (1/population),
                  'crossover_probability': crossover_probability,
                  'parents_portion': parents_portion,
                  'crossover_type': crossover_type,
                  'max_iteration_without_improv': None}

        def target(x):
            penalty = 0
            for edge in self.edges:
                if x[edge[0]-1] == x[edge[1]-1]:
                    penalty += self.no_vertex
            return np.unique(x).size + penalty

        var_bounds = np.array([[1, self.no_vertex]]*self.no_vertex)
        model = ga(function=target, dimension=self.no_vertex, variable_type='int', variable_boundaries=var_bounds,
                   algorithm_parameters=params)
        model.run()
        return model.best_function, model.best_variable, model.report
