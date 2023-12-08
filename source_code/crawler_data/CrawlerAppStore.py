import requests
from bs4 import BeautifulSoup
import json

def setupFile(fileName, isAppend):
    if isAppend:
        mod = "a+"
        bra = ']'
    else:
        mod = "w"
        bra = '['
    with open(fileName, mod) as f:
        f.writelines(bra)

def writeFile(fileName, data, deli):
    with open(fileName, "a+") as f:
        f.writelines(deli)
        json.dump(data, f, indent = 2, ensure_ascii = False)

def crawlContents(fileName, start, end):
    setupFile(fileName, False)
    deli = ""

    for i in range(start, end):
        link = requests.get(listLink[i])
        while link.status_code != 200:
            link = requests.get(listLink[i])
        
        soup = BeautifulSoup(link.content, 'html.parser')
        nameAndAge = soup.find_all('h1')
        company = soup.find_all(class_ = 'product-header__identity')
        raking = soup.find_all(class_ = 'product-header__list__item')
        ratingAndReviews = soup.find_all(class_ = 'we-rating-count')
        price = soup.find_all(class_ = 'app-header__list__item--price')
        availablity = soup.find_all(class_ = 'gallery-nav__items')
        describe = soup.find_all(class_ = 'we-truncate')
        new = soup.find_all(class_ = 'whats-new__content')
        configurationAndSize = soup.find_all(class_ = 'information-list__item__definition')
        language = soup.find_all(class_ = 'information-list__item')

        data = {}
        data['link'] = listLink[i]
        data['nameAndAge'] = nameAndAge[0].text
        data['company'] = company[0].text
        data['ranking'] = raking[0].text

        if len(ratingAndReviews) == 0:
            data['ratingAndReviews'] = ""
        else:
            data['ratingAndReviews'] = ratingAndReviews[0].text

        data['price'] = price[0].text

        if len(availablity) == 0:
            data['availablity'] = ""
        else:
            data['availablity'] = availablity[0].text

        data['describe'] = describe[0].text

        if len(new) == 0:
            data['new'] = ""
        else:
            data['new'] = new[0].text
            
        data['configuration'] = configurationAndSize[3].text
        data['size'] = configurationAndSize[1].text
        data['language'] = language[4].text

        writeFile(fileName, data, deli)
        deli = ",\n"

    setupFile(fileName, True)

if __name__ == "__main__":
    linkRoot = requests.get("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi")
    soup = BeautifulSoup(linkRoot.content, 'html.parser')
    listA = soup.find_all('a')
    listLink = []
    for i in range(48, 246):
        listLink.append(listA[i].get('href'))
    length = len(listLink)
    l4 = int(length / 4)


    fileName = "part1.json"
    crawlContents(fileName, 0, l4)
    fileName = "part2.json"
    crawlContents(fileName, l4, l4 *2)
    fileName = "part3.json"
    crawlContents(fileName, l4 * 2, l4 * 3)
    fileName = "part4.json"
    crawlContents(fileName, l4 * 3, length)
