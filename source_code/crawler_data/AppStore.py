from bs4 import BeautifulSoup
import json
import requests
import threading

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
        try:
            link = requests.get(listLink[i], timeout = 3)
        except requests.exceptions.Timeout:
            try:
                link = requests.get(listLink[i] , timeout = 3)
            except requests.exceptions.Timeout:
                try:
                    link = requests.get(listLink[i] , timeout = 3)
                except requests.exceptions.Timeout:
                    continue
        
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
    linkRoot = requests.get("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i-ph%E1%BB%95-th%C3%B4ng/id7003?l=vi")
    soup = BeautifulSoup(linkRoot.content, 'html.parser')
    listA = soup.find_all('a')
    for i in range(49, 246):
        listLink.append(listA[i].get('href'))
    length = len(listLink)
    l8 = int(length / 8)

    thread1 = threading.Thread(target = crawlContents, args = ("part1.json", 0, l8, ))
    thread2 = threading.Thread(target = crawlContents, args = ("part2.json", l8, l8 * 2, ))
    thread3 = threading.Thread(target = crawlContents, args = ("part3.json", l8 * 2, l8 * 3, ))
    thread4 = threading.Thread(target = crawlContents, args = ("part4.json", l8 * 3, l8 * 4, ))
    thread5 = threading.Thread(target = crawlContents, args = ("part5.json", l8 * 4, l8 * 5, ))
    thread6 = threading.Thread(target = crawlContents, args = ("part6.json", l8 * 5, l8 * 6, ))
    thread7 = threading.Thread(target = crawlContents, args = ("part7.json", l8 * 6, l8 * 7, ))
    thread8 = threading.Thread(target = crawlContents, args = ("part8.json", l8 * 7, length, ))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()