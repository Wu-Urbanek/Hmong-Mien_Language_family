# Hmong-Mien_Language_family

#### Purpose 1 : Automatically generate cognates
Two algorithms will be applied to geneate cognates automatically : Lexstat and Edited distance.
The results will be compared with manually aligned cognates. In contrast to most previous studies, partial cognates will be compared, as compounding is a very frequent process in the Hmong-Mien languages, and meaningful handling of cognates cannot be carried out when only considering cognacy as a binary relation.

#### Purpose 2 : Phylogenetic tree reconstruction
Phylogenetic tree will be reconstructed by using our own cogante data.

### Method 

#### 1. Data download 
The Global Lexicostatistical Database at 
http://starling.rinet.ru/cgi-bin/main.cgi?root=new100&encoding=utf-eng 

**Converting the xls file to word list format**

```shell
$ python3 convert_wordlist.py [input xls file] [output csv file]
```

Note that the [LexiBank](glottobank.org/) project of the Glottobank group has already written code that downloads the data directly from the website. This is more secure than using XLS files provided by the GLD team, since the data are fully provided in Unicode. We are working with a download from 08.02.2017 (which should not have significantly changed until now).

**Example**

```
python3 convert_wordlist.py hmo.xls hmo_complate_wl.csv
```

#### 2. Preprocessing data

**Generating the orthography data** 

```
lingpy ortho_profile -i output.csv --column=ipa
```
The purpose of having this process is to generate a orthography.tsv file for tokenization and convert phonetic symbol to IPA. 
**This command line does not work with latest version of lingpy properly. Further checking needed!** 


#### 3. Detecting cognates automatically ( Lingpy )
**Converting phonetic symbols to IPA symbols**

The script [helper-2017-02-10.py](https://github.com/MacyL/Hmong-Mien_Language_family/blob/master/helper/helper-2017-02-10.py) can be used to convert the GLD-specific orthographies to IPA-like sounds, it also corrects for certain GLD-specific idiosyncrasies of annotation which make it difficult to process the data with lingpy. The file will create a TSV-file [hm-111-17.sv](https://github.com/MacyL/Hmong-Mien_Language_family/blob/master/helper/hm-111-17.tsv) that can directly be used in lingpy for cognate detection analysis.

**Full pipeline to generate cognates:** 
```shell
python3	congnate_detect_pipeline.py [input wordlist] [orthography file] [output file name]
```
The input data is in word list format, the orthography provides a template for tokenizing the words. And the output is the name we wish have. This pipeline generated three files. cognates, scores, and partial cognates. 

**Example**

```shell
python3	congnate_detect_pipeline.py output.csv orthography.tsv hm
```

**Commandline executable script to generating NEX file** 

```shell
python3	PaptoNex.py input output
```
The input data is in word list format. Following the input file is the output file name. Please make sure that the input file has a column named "COGIDS", or change the script accordingly. 

#### 4. Phylogenetic tree ( MrBayes )
To generate the language tree, we applied MCMC method. <br />
Mrbayes can execute in batch mode. The script is located in Mrbayes_Script.
And the command is :
```shell
./mb < Use_default.txt >log.txt&
```

### Notes for the project ###

**Lingpy installation:**
To view the detail instruction, visit : https://github.com/lingpy/lingpy <br />

Lingpy required python-igraph. To install python-igraph for python 2.7, the commandline is . <br />
```shell
pip install python-igraph
```
However, Ubuntu 16.04 users who work with **python 3.5.2** might run into some installation problems. Mostly, the problems occur when there is no C compiler installed or missing igraph-dependent libraries.  <br />
Try the following methods. 
1. Download the package from their github repository
2. Execute the following commands. 

```shell
sudo apt-get install pkg-config 
sudo apt-get install -y libigraph0-dev
cd python-igraph-master
sudo python3 setup.py install
```
**NEX file**
The script above can generate the nex file. However, the dialect/language names should contains no white space. For example, we altered *Eastern Xiangxi* to *Eastern-Xiangxi*. 
