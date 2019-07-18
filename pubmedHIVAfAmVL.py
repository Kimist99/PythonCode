#Pubmed search for articles on HIV in African American women
import numpy as np
import pandas as pd
import pymed
from pymed import PubMed

pubmed = PubMed(tool="PubMedSearcher", email="myemail@xxx.com")

search_term = "HIV Viral Load African America" #place search terms in quotes
results = pubmed.query(search_term, max_results=500)
articleList = []
articleInfo = []

for article in results:
# Print the object type
# Convert to dictionary
    articleDict = article.toDict()
    articleList.append(articleDict)

# Create a dict list of articles from PUBMED API
for article in articleList:
    pubmedId = article['pubmed_id'].partition('\n')[0]
    # Append article info to dictionary with fields you wish to collect
    articleInfo.append({u'pubmed_id':pubmedId,
                       u'title':article['title'],
                       u'keywords':article['keywords'],
                       u'journal':article['journal'],
                       u'abstract':article['abstract'],
                      # u'conclusions':article['conclusions'],
                      # u'methods':article['methods'],
                      # u'results': article['results'],
                      # u'copyrights':article['copyrights'],
                      # u'doi':article['doi'],
                       u'publication_date':article['publication_date'], 
                       u'authors':article['authors']})

# Create pandas dataframe dict list
articlesPD = pd.DataFrame.from_dict(articleInfo)
df = articlesPD
PUBMEDcsv = df.to_csv (r'C:\Users\Desktop\export_dataframe.csv', index = None, header=True) 

