# Hmong-Mien_Language_family
#### Purpose 1 : Automatically generate cognates
Two algorithms will be applied to geneate cognates automatically : Lexstat and Edited distance.
The results will be compared with manually aligned cognates. In contrast to most previous studies, partial cognates will be compared, as compounding is a very frequent process in the Hmong-Mien languages, and meaningful handling of cognates cannot be carried out when only considering cognacy as a binary relation.

#### Purpose 2 : Phylogenetic tree reconstruction
Phylogenetic tree will be reconstructed by using our own cogante data.

### Method 
#### Data download 
The Global Lexicostatistical Database at 
http://starling.rinet.ru/cgi-bin/main.cgi?root=new100&encoding=utf-eng 

**Converting the xls file to word list format**

```shell
$ python3 convert_wordlist.py [input xls file] [output csv file]
```

Note that the [LexiBank](glottobank.org/) project of the Glottobank group has already written code that downloads the data directly from the website. This is more secure than using XLS files provided by the GLD team, since the data are fully provided in Unicode. We are working with a download from 08.02.2017 (which should not have significantly changed until now).

** Example **

```
python3 convert_wordlist.py hmo.xls hmo_complate_wl.csv
```
** Converting phonetic symbols to IPA symbols

The script [helper-2017-02-10.py](https://github.com/MacyL/Hmong-Mien_Language_family/blob/master/helper/helper-2017-02-10.py) can be used to convert the GLD-specific orthographies to IPA-like sounds, it also corrects for certain GLD-specific idiosyncrasies of annotation which make it difficult to process the data with lingpy. The file will create a TSV-file [hm-111-17.sv](https://github.com/MacyL/Hmong-Mien_Language_family/blob/master/helper/hm-111-17.tsv) that can directly be used in lingpy for cognate detection analysis.

### Lingpy : detecting cognates automatically



