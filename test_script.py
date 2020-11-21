from ga import GraphColoringProblem
from test_record import TestRecord
import threading

data = ['graphs/graph1.txt', 'graphs/graph2.txt', 'graphs/graph3.txt', 'graphs/graph4.txt', 'graphs/graph5.txt']
population_options = [x for x in range(5, 100, 5)]
crossover_type_options = ['one_point', 'two_point', 'uniform']
crossover_probability_options = [float(x/100) for x in range(0, 100, 5)]


results = list()
for graph in data:
    results.append(list())
    for pop in population_options:
        results[-1].append(list())
        for ct in crossover_type_options:
            results[-1][-1].append(list())
            for cp in crossover_probability_options:
                results[-1][-1][-1].append(TestRecord(pop, ct, cp, graph))

REPEAT_NO = 20
THREAD_NO = 64
MAX_ITER = 1000

sem = threading.Semaphore(THREAD_NO)


def thread_function(test_case):
    for i in range(REPEAT_NO):
        model = GraphColoringProblem(test_case.graph)
        print("[{}] Started case population: {} crossover type: {} crossover probability: {}".format(i+1,
                                 test_case.population, test_case.crossover_type, test_case.crossover_probability))
        test_case.append(model.solve(population=test_case.population, crossover_type=test_case.crossover_type,
                                     crossover_probability=test_case.crossover_probability, max_iteration=MAX_ITER))
    sem.release()


threads = []
for g_i in range(len(data)):
    for p_i in range(len(population_options)):
        for ct_i in range(len(crossover_type_options)):
            for cp_i in range(len(crossover_probability_options)):
                threads.append(threading.Thread(target=thread_function, args=(results[g_i][p_i][ct_i][cp_i],)))
                threads[-1].start()
                sem.acquire()

for i in range(len(threads)):
    threads[i].join()





