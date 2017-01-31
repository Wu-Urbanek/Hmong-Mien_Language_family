#library
from lingpy import *
import pandas as pd

# inputing data, follow the Lingpy instructions 
wl=Wordlist('Hmo_wl.qlc')
wl.add_entries('tokens','ipa',lambda x:ipa2tokens(x))
wl.add_entries('classes','tokens',lambda x:''.join(tokens2class(x,model='sca')))
## temp output
wl.output('qlc',filename='Hmo_Jan23_2')

# LexStat, the default is SCA.  
lex=LexStat(wl)
lex.get_scorer(verbose=True,force=True)
lex.cluster(method='lexstat',threshold=0.5)
## temp output
lex.output('qlc',filename='Hmo_Jan23_lexstat',ignore=['scorer'])

# get etymdict create a etymdict dictionary, every key is a cognate word and the value is the tax has the cognate or not 
etd = lex.get_etymdict(ref='lexstatid',entry='ipa')

# etd to data frame, this is the main part of our nex file 

etd_df=pd.DataFrame.from_dict(etd)

taxa=lex.taxa

for i in range(17):
	etd_df.rename(index={i:taxa[i]},inplace=True)

# cognate change to 1, others remain 0
etd_df[etd_df !=0]=1

eted_df.to_csv('Hmo_cognates.csv') 


