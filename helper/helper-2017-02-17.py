from lingpy import *
from lingpy.compare.partial import Partial
from lingpy.evaluate.acd import partial_bcubes

try:
    lexx = LexStat('hm-jerry-scored.bin.tsv', segments='segments')
    lex = Partial('../hm-111-17_16feb.tsv', segments='segments')
    lex.cscorer = lexx.cscorer
except:
    lex = Partial('../hm-111-17_16feb.tsv', segments='segments')
    lex.get_scorer(runs=10000)
    lex.output('tsv', filename='hm-jerry-scored.bin')

# we test several thresholds
for i in range(2,8):
    lex.partial_cluster(method='lexstat', cluster_method='infomap',
            threshold=i*0.1, ref='t'+str(i))

    a, b, c = partial_bcubes(lex, 'cogids', 't'+str(i), pprint=False)
    print('{0:2} {1:.2f} {2:.2f} {3:.2f}'.format(i, a, b, c))
