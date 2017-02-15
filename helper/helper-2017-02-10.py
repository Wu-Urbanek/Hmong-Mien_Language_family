from lingpy import *
from segments.tokenizer import Tokenizer # https://github.com/bambooforest/segments

# create a tokenizer object
t = Tokenizer('orthography.tsv')

# make a dictionary to be passed to lingpy afterwards
D = {0: ['doculect', 'concept', 'concept_id', 'glottolog', 'word_is',
    'segments_is', 'segments', 'cog']}

correct = {
        'pa31 #': "pa31",
        "ɲɕʰɔ4 #": "ɲɕʰɔ4",
        }

# load csv file with help of the csv2list function in lingpy
csv = csv2list('output.csv', sep=',')
for i, (concept_id, concept, language, glottolog, words, cogid) in enumerate(csv):

    # only take the second element if there are more words
    ipa = words.split(' ~ ')[-1]
    ipa = correct.get(ipa, ipa)
    cognacy = '{0}-{1}'.format(concept_id, cogid)
    D[i+1] = [language, concept, concept_id, glottolog, words, t(ipa), t(ipa, 'IPA'), cognacy]
wl = Wordlist(D)
wl.renumber('cog') # adds column with name "cogid"
wl.output('tsv', filename='hm-{0}-{1}'.format(wl.height, wl.width),
        prettify=False, ignore='all')

with open('languages.tsv', 'w') as f:

    visited = []
    f.write('LANGUAGE\tGLOTTOLOG\n')
    for k, l, g in iter_rows(wl, 'doculect', 'glottolog'):
        if l not in visited:
            f.write(l+'\t'+g+'\n')
            visited += [l]
