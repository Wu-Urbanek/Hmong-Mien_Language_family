import lingpy 
from lingpy import *
import numpy as np
from lingpy.evaluate.acd import bcubes, diff

###########
# Data input 
############

# manually annotate the partial cognates
WLmp=Wordlist('hm-111-17_16feb.tsv')

# auto detect the partial cognates
WLap=Wordlist('HM-March4-partial-final.tsv')

##############
# Compare the cognates : bcubes
##############

WLmp_bcube=bcubes(WLmp, 'cogid','cogids')
WLap_bcube=bcubes(WLap,'cogid','cogids')

###################
# Not sure if this make sence, but just trying out at this moment 
# get edit distance for every concept
###################
Lan=WLmp.language

lanD=dict()
for i in Lan:
	temp=WLmp.get_list(language=i, entry='SEGMENTS_IS')
	lanD[i]=temp

lanpair=list(permutations(Lan,2))

lanD_editD=dict()

for k,v in lanpair:
	seqA=['-' if x==0 else x for x in lanD[k]]
	seqB=['-' if x==0 else x for x in lanD[v]]
	temp=[edit_dist(seqA[i],seqB[i]) for i in range(0,len(seqA))]
	lanD_editD[(k,v)]=temp
