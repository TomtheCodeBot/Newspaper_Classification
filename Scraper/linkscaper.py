import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

### Function to get links from baochinhphu
def getLinkBaochinhphu(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    for parent in soup.find_all(class_="story"):
        ### Find the element that contains the URL of the search results
        p_tag = parent.find("p", class_="title")
        a_tag = p_tag.find("a", class_=None)
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        urls.append(url_input)
    return urls

### Function to get links from vietnamnet
def getLinkVietnamnet(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    html_text = requests.get(url, headers=headers)
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    for parent in soup.find_all('div',class_="clearfix item"):
        ### Find the element that contains the URL of the search results
        a_tag = parent.find("a", class_="m-t-5 w-240 d-ib thumb left m-r-20")
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        urls.append(url_input)
    return urls

### Funtion to get links from thanhnien
def getLinkThanhnien(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    div = soup.find(class_="relative")
    for parent in div.find_all(class_="story"):
        ### Find the element that contains the URL of the search results
        a_tag = parent.find("a", class_="story__thumb")
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        urls.append(url_input)
    return urls

### Function to get links from VNExpress
def getLinkVNExpress(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    div = soup.select("div.width_common.list-news-subfolder")
    for parent in div[0].find_all(class_="title-news"):
        ### Find the element that contains the URL of the search results
        a_tag = parent.find("a", class_=None)
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        ### function to get links from webpages
        urls.append(url_input)
    return urls

### Function to get links from Phapluat
def getLinkPhapluat(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    div = soup.find(class_="col-list-content")
    for parent in div.find_all(class_="item-news item-news-common"):
        ### Find the element that contains the URL of the search results
        a_tag = parent.find("a", class_=None)
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        ### function to get links from webpages
        urls.append(url_input)
    return urls
### Function to get links from VOV
def getLinkVOV(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    div = soup.find(class_="views-element-container")
    for a_tag in div.find_all(class_="vovvn-title position-relative"):
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        ### function to get links from webpages
        urls.append(url_input)
    return urls
### Function to get links from dantri
def getLinkDantri(url):
    html_text = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'})
    ### Parse to BeautifulSoup
    soup = BeautifulSoup(html_text.text, "html.parser")
    urls = []
    div = soup.find(class_="dt-list dt-list--lg")
    for a_tag in div.find_all(class_="news-item__avatar"):
        ### Set the base link
        base = url
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url_input = urljoin(base, link)
        ### function to get links from webpages
        urls.append(url_input)
    return urls
### function to get links from webpages
def getLinks(url, website_name):
    if website_name == "baochinhphu":
        return getLinkBaochinhphu(url)
    if website_name == "vietnamnet":
        return getLinkVietnamnet(url)
    if website_name == "thanhnien":
        return getLinkThanhnien(url)
    if website_name == "vnexpress":
        return getLinkVNExpress(url)
    if website_name == "phapluat":
        return getLinkPhapluat(url)
    if website_name == "vov":
        return getLinkVOV(url)
    if website_name == "dantri":
        return getLinkDantri(url)
    return None

### Outputs links to a .txt file.
def textOuput(urllist,filename):
    ### Opening filename and append the content.
    with open(filename,'a') as f:
        for i in urllist:
            inputlink = i+'\n'
            f.writelines(inputlink)

if __name__=="__main__":

    """### Testing drivers.
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    ### Open it, go to a website, and get results
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.get("https://www.website.com")
    print(wd.page_source)  ### Results of the webpage

    ### Testing scraping certain tags of the webpage.

    ### Accessing reddit search querries
    wd.get("https://www.reddit.com/search/?q=covid19")
    urls = []
    ### Parsing to beautifulsoup as html
    soup = BeautifulSoup(wd.page_source, "html.parser")

    ### finding all tags that has this class ( this class ID is the ID of each search results )
    for parent in soup.find_all(class_="y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE"):
        ### Find the element that contains the URL of the search results
        a_tag = parent.find("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
        ### Set the base link
        base = "https://www.reddit.com/search/?q=covid19"
        ### taking the content of the href element ( usually it's a link to the website )
        link = a_tag.attrs['href']
        ### Genarate the link of the destination when you lick on that href element
        url = urljoin(base, link)
        urls.append(url)
    print(urls)"""

    ### TODO: Link scraper for vnexpress, vtv, bbc, ... (Done)
    """### Testing scraping news article of baochinhphu
    print(getLinks("https://baochinhphu.vn/Chinh-tri/442.vgp","baochinhphu"))

    ### Testing scraping news article of vietnamnet
    print(getLinks("https://vietnamnet.vn/vn/thoi-su/chinh-tri/", "vietnamnet"))

    ### Testing scraping news article of thanhnien
    print(getLinks("https://thanhnien.vn/thoi-su/chinh-tri/", "thanhnien"))

    ### Testing scraping news article of vnexpress
    print(getLinks("https://vnexpress.net/thoi-su/chinh-tri", "vnexpress"))"""

    """### Testing scarping and inputting links in the file.
    textOuput(getLinks("https://thanhnien.vn/thoi-su/chinh-tri/", "thanhnien"),"chinhtri-thanhnien.txt")"""

    """### Testing scarping and inputting links in the file.
    print(getLinks("https://plo.vn/thoi-su/chinh-tri/?trang=2", "phapluat"))"""
    """### Testing scarping and inputting links in the file.
    print(getLinks("https://dantri.com.vn/xa-hoi/chinh-tri/trang-1.htm", "dantri"))"""
    ### TODO: Actual gathering of data
    ### TODO: Data clean-ups