import lingpy
from lingpy import *

# load the hand manual alignment file as wordlist object
wl=Wordlist('hm-111-17_16feb.tsv')

# this will get the dictionary which cogid is key and the index of the row is value 
wl_paps=wl.get_paps(ref="COGID",entry='concept',,missing="?",modify_ref=False)

# create taxa, check the "get_entries" first 
wl_entres=wl.get_entries("DOCULECT") # this one has full taxa 
wl_taxa=wl_entries[2]# this one has full taxa 

# convert to nex
 lingpy.convert.strings.pap2nex(wl_taxa, wl_paps, missing='?', filename='wl_feb16_nex')
