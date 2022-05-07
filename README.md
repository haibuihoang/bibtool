# Usage

```
usage: bibtool [-h] [-o OUTPUT] [-a] [-u] [-d] inputfile

positional arguments:
  inputfile             The input bibtex file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output bibtex file
  -a, --abbrev          Abrevivate journal names
  -u, --url             Remove URL fields
  -d, --doi             Remove DOI fields
 ```
 
 
 # Note:
 
 The journal names abbreviation data base is included in `abbrev_journal.csv`, please add additional journals to your need. 
 
 The main script is a Python 3 script `bibtool.py`, which require `pandas`, `bibtexparser` packages.
 
 `bibtool` is a zsh script wrapper, but you can write anther shell wrapper as well
 
