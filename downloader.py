from bs4 import BeautifulSoup
import requests
import os
import ssl
import shutil
import urllib.request as request
from contextlib import closing
from tqdm import tqdm

ssl._create_default_https_context = ssl._create_unverified_context

urls = {'abstract':'https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/','full_text':'https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_comm/txt/'}
base_path = "/home/AI_Pune_Team/000_data/pubmed_downloaded/"


for path,url in urls.items():
    print(f"downloading {path} !")
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    for i in tqdm(soup.find_all('a', href = True)):
        href = f"{url}{i['href']}"
        if href.endswith(".gz"):
            print(href)
            with closing(request.urlopen(href)) as r:
                with open(os.path.join(base_path,path,i['href']), 'wb') as f:
                    shutil.copyfileobj(r, f)
