# librarzy 
import pandas as pd 
import lingpy as lp
from lingpy import *


# read in files 
x=pd.ExcelFile('hmo_filtered.xls', encoding='ud', index_col=0)
x.sheet_names
df=x.parse('Sheet1')

# select columns 
df_select=df[['Word','Western Xiangxi', 'Eastern Xiangxi', 'Qiandong', 'Chuanqiandian', 'Diandongbei', 'Hmong Daw', 'Hmong Njua', 'Bunu', 'Baonao', 'Numao', 'Longhua Jiongnai', 'Liuxiang Jiongnai', 'Xiaozhai Younuo', 'Huangluo Younuo', 'Northern Pa-Hng', 'Southern Pa-Hng', 'Hm-Nai']]

df_select_transpose=df_select.transpose()

word_list=[]
# create word list document
for i in df_select_transpose:
	temp=df_select_transpose[i].tolist()
	location=list(df_select_transpose.index)[1:]
	meaning=temp[0]	
	ipa_list=temp[1:]
	for j, val in enumerate(ipa_list):
		word_list.append({'CONCEPT':meaning,'LANGUAGE':location[j], 'IPA':ipa_list[j]})

word_list_dataframe=pd.DataFrame(word_list)
word_list_dataframe.index=word_list_dataframe.index+1
word_list_dataframe=word_list_dataframe[['CONCEPT','LANGUAGE','IPA']]
word_list_dataframe.to_csv('Hmo_wl.csv',encoding='utf-8',sep='\t')


	

