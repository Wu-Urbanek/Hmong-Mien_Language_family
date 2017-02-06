# Hmong-Mien_Language_family
#### Purpose 1 : Automatically generate cognates
Two algorithms will be applied to geneate cognates automatically : Lexstat and Edited distance.<br />
The results will be compared with manually aligned cognates. <br />

#### Purpose 2 : Phylogenetic tree reconstruction
Phylogenetic tree will be reconstructed by using our own cogante data.

### Method 
#### Data download 
The Global Lexicostatistical Database <br />
http://starling.rinet.ru/cgi-bin/main.cgi?root=new100&encoding=utf-eng <br />

**Converting the xls file to word list format**

```
python3 convert_wordlist.py [input xls file] [output csv file]
```
** Example **

```
python3 convert_wordlist.py hmo.xls hmo_complate_wl.csv
```
** Converting phonetic symbols to IPA symbols


### Lingpy : detecting cognates automatically


