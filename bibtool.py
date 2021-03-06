import pandas as pd
import bibtexparser as bp
import argparse
import sys


def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("inputfile", help="The input bibtex file")
   parser.add_argument("-o", "--output", help="Output bibtex file")
   parser.add_argument("-a", "--abbrev", action="store_true",help="Abrevivate journal names")
   parser.add_argument("-u", "--url", action="store_true",help="Remove URL fields")
   parser.add_argument("-d", "--doi", action="store_true",help="Remove DOI fields")
   parser.add_argument("-t", "--type", action="store_true",help="Remove type fields")
   args=parser.parse_args()

       
   #abbrev=abbreviate('Journal of the American statistical association')

   try:
       with open(args.inputfile) as bibtex_file:
           bib_database = bp.load(bibtex_file)
   except:
       print(f"Cannot open {args.inputfile}")
       sys.exit(2)
       
   for i,e in enumerate(bib_database.entries):
      if (args.abbrev):
         if 'journal' in e:
            e['journal'] = abbreviate(e['journal'])
      if (args.url):
         e.pop('url', None)
      if (args.doi):
         e.pop('doi', None)
      if (args.type):
         e.pop('type', None)

      bib_database.entries[i] = e
     

   bibtex_str = bp.dumps(bib_database)
   if args.output:
       with open(args.output, "w") as o:
           o.write(bibtex_str)
   else:
       print(bibtex_str)
       
   return 0


def abbreviate(name):
   import os 
   scpdir=os.path.dirname(os.path.realpath(__file__))
   df=pd.read_csv(f"{scpdir}/abbrev_journal.csv",sep=';')
   subdf = df.loc[df['Journal'].str.lower() == name.lower()]
   if (len(subdf)>0): 
       return subdf['Abbreviation'].iloc[0]
   else: 
       print(f"{name} not found in database!")
       return name

main()
