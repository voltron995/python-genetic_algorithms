from datetime import datetime
from collections import OrderedDict

from genetic_algorithms.cCrossover import run_test as cRun_test
from genetic_algorithms.crossover import run_test


deltas = OrderedDict()

start = datetime.now()
run_test()
end = datetime.now()
deltas['python'] = end - start

start = datetime.now()
cRun_test()
end = datetime.now()
deltas['cython'] = end - start

runtimes = OrderedDict([(k, v.total_seconds()) for k, v in deltas.items()])

format_str = '  %%%ds: %%s seconds' % max([len(k) for k in runtimes])

message = '\n'.join([format_str % item
                     for item in runtimes.iteritems()])
print 'Runtimes:'
print message
