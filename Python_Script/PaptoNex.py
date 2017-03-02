import lingpy
from lingpy import *
import sys
#################################
# python3 PaptoNex.py input output 
#################################

# load the hand manual alignment file as wordlist object
wl=Wordlist(sys.argv[1])

# this will get the dictionary which cogid is key and the index of the row is value
wl_paps=wl.get_paps(ref="COGIDS",entry='CONCEPT',missing="?",modify_ref=False)

# create taxa
wl_taxa=wl.language

# convert to nex
lingpy.convert.strings.pap2nex(wl_taxa, wl_paps, missing='?', filename=sys.argv[2])
