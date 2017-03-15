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

