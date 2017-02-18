######################
#library 
######################
import sys
from lingpy import *
from segments.tokenizer import Tokenizer
from lingpy.compare.partial import Partial

######################
# Task : load in word list, segment, detect cognate, output cognate 
# usage : python3 congate_detect_pipline.py wordlist token_template output
######################

# Preprocess
## load in required data: word list csv and phonetic data as segmentation template 
csv= csv2list(sys.argv[1], sep=',')
t=Tokenizer(sys.argv[2])

## set the template for lingpy  
D = {0: ['doculect', 'concept', 'concept_id', 'glottolog', 'word_is',
    'segments_is', 'segments', 'cog']} 

correct = {
        'pa31 #': "pa31",
        "ɲɕʰɔ4 #": "ɲɕʰɔ4"
        }

## tokenize, full cognate
for i, (concept_id, concept, language, glottolog, words, cogid) in enumerate(csv):
    # only take the second element if there are more words
    ipa = words.split(' ~ ')[-1]
    ipa = correct.get(ipa, ipa)
    cognacy = '{0}-{1}'.format(concept_id, cogid)
    D[i+1] = [language, concept, concept_id, glottolog, words, t(ipa), t(ipa, 'IPA'), cognacy]
wl = Wordlist(D)
# create a new column by cog column. The new column assign 
wl.renumber('cog')
print('Saving full cognate file...')
wl.output('tsv', filename='{0}-{1}'.format(sys.argv[3],'cognate'),prettify=False, ignore='all')


## get partical cognate
try:
	part=Partial('{0}-{1}-{2}.tsv'.format(sys.argv[3],'partial','temp'),segments='segments')
except:
	part=Partial(wl,segments='segments')
	part.get_scorer(runs=10000)
	part.output('tsv', filename='{0}-{1}-{2}'.format(sys.argv[3],'partial','temp'))

# manually correct error in data
part.partial_cluster(method='lexstat', cluster_method='infomap', threshold=0.6,
        ref='cogids')

part.add_entries('note', 'cogid', lambda x: '')
part.add_entries('morphemes', 'cogid', lambda x: '')
print('Saving partial cognate file')
part.output('tsv', filename='{0}-{1}-{2}'.format(sys.argv[3],'partial','final'), ignore='all', prettify=False)

 
