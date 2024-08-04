import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def GetForcast():
    # get near term forcast
    url = "https://weather.gc.ca/marine/marine_bulletins_e.html?Bulletin=fqcn13.cwto"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    pattern = 'Eastern Lake Superior[\\w\\W]*?(Whitefish)'

    split = re.search(pattern, text)
    start, end = split.span()

    returnInfo = []
    returnInfo.append("forcast")
    returnInfo.append(text[start:end-9])
     # get extended forcast
    url = "https://weather.gc.ca/marine/marine_bulletins_e.html?Bulletin=fqcn53.cwto"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    pattern = 'Lake Superior[\\w\\W]*?(Whitefish)'
    split = re.search(pattern, text)
    start, end = split.span()

    returnInfo.append("extended forcast")
    returnInfo.append(text[start:end-9])
    returnText="".join(returnInfo) 
    return returnText
    #print(text)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def main():
   print(GetForcast())

if __name__== "__main__" :
    main()
