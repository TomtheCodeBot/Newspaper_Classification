import time

from webdriver_manager.chrome import ChromeDriverManager


import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

### NOTE: These functions are still protypes. Eventhough its functionalities are 85-90% effective, there is still a 10% bug chance. Please check the output and fix them (Also please leave a log for me to read, in this folder.)

### Get content from baochinhphu
def getContentBaochinhphu(url):
    html_text = requests.get(url, headers={'User-Agent':'test'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find(class_="article-body cmscontents")
    whole_article = []
    for subdiv in div.find_all('div', style=re.compile(r'text-align: justify;')):
        whole_article.extend(subdiv.stripped_strings)
    for p in div.find_all('p', class_=None):
        whole_article.extend(p.stripped_strings)
    return " ".join(whole_article)

### Get content from vietnamnet
def getContentVietnamnet(url):
    ### Add header to by pass error 403.
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get(url,headers=headers)
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find(id="ArticleContent")
    whole_article = []
    for p in div.find_all('p', class_="t-j"):
        whole_article.extend(p.stripped_strings)

    for p in div.find_all('p', class_=None):
        whole_article.extend(p.stripped_strings)

    return " ".join(whole_article)

### Get content for thanhnien
def getContentThanhnien(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find(id='abody')

    whole_article = []
    for subdiv in div.find_all(lambda tag: tag.name == 'div' and not tag.attrs):
        whole_article.extend(subdiv.stripped_strings)
    for subdiv in div.find_all(lambda tag: tag.name == 'p' and not tag.attrs):
        whole_article.extend(subdiv.stripped_strings)
    return " ".join(whole_article)

### Get content from vnexpress
def getContentVNExpress(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find('article')
    whole_article = []
    for p in div.find_all('p'):
        whole_article.extend(p.stripped_strings)
    return " ".join(whole_article)

### Get content from phapluat
def getContentPhapLuat(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find(id="abody")
    whole_article = []
    for p in div.find_all('p', style="text-align: justify;"):
        whole_article.extend(p.stripped_strings)
    return " ".join(whole_article)

### Get content from vov
def getContentVOV(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find(class_="text-long")
    whole_article = []
    for p in div.find_all('p'):
        whole_article.extend(p.stripped_strings)
    if len(whole_article)<2:
        for subdiv in div.find_all("figcaption"):
            whole_article.extend(subdiv.stripped_strings)
    return " ".join(whole_article)

### Get content from dantri
def getContentDantri(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    ### Locate the main article.
    div = soup.find(class_="ta-justify")
    whole_article = []
    for p in div.find_all('p'):
        whole_article.extend(p.stripped_strings)
    return " ".join(whole_article)
### Getting content from website
def getContent(url, website_name):
    if website_name == "baochinhphu":
        return getContentBaochinhphu(url)
    if website_name == "vietnamnet":
        return getContentVietnamnet(url)
    if website_name == "thanhnien":
        return getContentThanhnien(url)
    if website_name == "vnexpress":
        return getContentVNExpress(url)
    if website_name == "phapluat":
        return getContentPhapLuat(url)
    if website_name == "vov":
        return getContentVOV(url)
    if website_name == "dantri":
        return getContentDantri(url)
    return None

### Adding data to csv file
def addDataCSV(filename, idlist, datalist, label):
    ### Creating empty dataframes
    data = pd.DataFrame(columns=['ID', 'data', 'label'])
    for i in range(0,len(idlist)):
        ### Adding data
        data = data.append({'ID':idlist[i],'data':datalist[i],'label':label[i]},ignore_index=True)
    ### Save to a csv file
    data.to_csv(filename,mode='a',index=False,header=False)

if __name__ == "__main__":

    ### TODO: Scraper for content (Done)

    """### Testing scraper on baochinhphu.
    print(textpreprocess.preprocessingText(getContent("https://baochinhphu.vn/Suc-khoe/Bac-Giang-da-qua-giai-doan-chong-dich-kho-khan-nhat/435113.vgp","baochinhphu"),True))

    ### Testing scraper on vietnamnet.
    print(getContent("https://vietnamnet.vn/vn/thoi-su/quoc-hoi/chu-tich-quoc-hoi-day-nhanh-chien-luoc-vac-xin-covid-19-de-mien-dich-cong-dong-745533.html","vietnamnet"))

    ### Testing scraper on thanhnien.
    print(getContent("https://thanhnien.vn/thoi-su/ong-phan-van-mai-lam-pho-bi-thu-thuong-truc-thanh-uy-tphcm-1391929.html","thanhnien"))

    ### Testing scraper on vnexpress.
    print(getContent("https://vnexpress.net/de-nghi-bo-chung-chi-ngoai-ngu-tin-hoc-khi-bo-nhiem-can-bo-4286936.html","vnexpress"))"""

    """### Testing scraper on phapluat
    print(getContent("https://plo.vn/thoi-su/chinh-tri/cu-tri-mong-som-hoan-thanh-cao-toc-tphcm-moc-bai-984029.html","phapluat"))"""

    """### Testing scraper on vov
    print(getContent("https://vov.vn/xa-hoi/giao-duc/giao-vien-du-doan-nhieu-thi-sinh-dat-diem-9-10-de-thi-tieng-anh-hon-nam-truoc-872361.vov","vov"))"""

    """### Testing scraper on dantri
    print(getContent("https://vtv.vn/chinh-tri/viet-nam-mong-muon-thuc-day-manh-me-hon-nua-quan-he-huu-nghi-va-hop-tac-nhieu-mat-voi-maroc-20210707193940965.htm","dantri"))"""