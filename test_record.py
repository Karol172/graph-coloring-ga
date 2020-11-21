
class TestRecord:
    def __init__(self, population, crossover_type, crossover_probability, graph):
        self.population = population
        self.crossover_type = crossover_type
        self.crossover_probability = crossover_probability
        self.best_results = list()
        self.position_results = list()
        self.iter = list()
        self.graph = graph

    def append(self, result):
        self.best_results.append(result[0])
        self.position_results.append(result[1])
        self.iter.append(result[2].index(result[2][-1] + 1))
