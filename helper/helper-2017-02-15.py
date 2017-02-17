from lingpy import *
from lingpy.compare.partial import Partial

try:
    part = Partial('hm-111-17.bin.tsv', segments='segments')
except:
    part = Partial('hm-111-17.tsv', segments='segments')
    part.get_scorer(runs=10000)
    part.output('tsv', filename='hm-111-17.bin')

# manually correct error in data
part.partial_cluster(method='lexstat', cluster_method='infomap', threshold=0.6,
        ref='cogids')

part.add_entries('note', 'cogid', lambda x: '')
part.add_entries('morphemes', 'cogid', lambda x: '')
part.output('tsv', filename='hm-111-17-t06', ignore='all', prettify=False)

