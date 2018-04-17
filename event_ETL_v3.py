
# coding: utf-8

# # Web Scrapping

# ### Parsing a webpage with beautiful soup

# In[11]:


import requests
import urllib
from bs4 import BeautifulSoup


# In[6]:


page = requests.get('Descargar fichero
CSV, 38014 de')


# In[7]:


soup = BeautifulSoup(page.content,'html.parser')


# In[8]:


soup


# In[9]:


soup.prettify


# In[27]:


def process_results(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('li',class_='noimg')
    for result in results:
        #print(result.find('p').contents)
        print(result.find('p').text)
    return soup.find('li',class_='n').find('a')['href'] if soup.find('li',class_='n') is not None else ''


# In[28]:


if __name__ == '__main__':
    drug = 'fluoro'
    url = 'https://www.mayoclinic.org/drugs-supplements/search-results?keyword=' + drug
    next_url = process_results(url)
    while next_url != '':
        next_url = process_results(next_url)


# In[29]:


next_url


# In[12]:


import pandas as pd


# In[17]:


pd.read_csv('https://datos.madrid.es/egob/catalogo/206974-0-agenda-eventos-culturales-100.csv',sep=';', error_bad_lines=False,encoding='latin-1')

