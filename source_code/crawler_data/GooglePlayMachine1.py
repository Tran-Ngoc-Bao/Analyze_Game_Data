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
            link = requests.get(listLink[i], timeout = 5)
        except requests.exceptions.Timeout:        
            continue

        soup = BeautifulSoup(link.content, 'html.parser')
        name = soup.find_all('h1')
        company = soup.find_all(class_ = 'Vbfug')
        ratingAndDownloads = soup.find_all(class_ = 'ClM7O')
        reviewsAndAge = soup.find_all(class_ = 'g1rdde')
        descirbe = soup.find_all(class_ = 'bARER')
        lastVersion = soup.find_all(class_ = 'xg1aie')
        classify = soup.find_all(class_ = 'Uc6QCc')
        privacy = soup.find_all(class_ = 'WpHeLc')
        
        data = {}

        data['link'] = listLink[i]

        if len(name) == 0:
            continue
        data['name'] = name[0].text

        data['company'] = company[0].text

        if len(ratingAndDownloads) == 1:
            data['rating'] = ""
            data['downloads'] = ""
        elif len(ratingAndDownloads) == 2:
            data['rating'] = ""
            data['downloads'] = ratingAndDownloads[0].text
        else:
            data['rating'] = ratingAndDownloads[0].text
            data['downloads'] = ratingAndDownloads[1].text

        if len(reviewsAndAge) == 1:
            data['reviews'] = ""
            data['age'] = reviewsAndAge[0].text
        elif len(reviewsAndAge) == 2:
            data['reviews'] = ""
            data['age'] = reviewsAndAge[1].text
        else:
            data['reviews'] = reviewsAndAge[0].text
            data['age'] = reviewsAndAge[2].text

        data['describe'] = descirbe[0].text
        data['lastVersion'] = lastVersion[0].text
        data['classify'] = classify[0].text
        data['privacy'] = "https://play.google.com" + privacy[1].get('href')

        writeFile(fileName, data, deli)
        deli = ",\n"

    setupFile(fileName, True)

if __name__ == "__main__":
    soup = BeautifulSoup (open("games.html", encoding = "utf8"), features = "lxml")
    listA = soup.find_all('a', class_ = 'Si6A0c')
    listLink = []
    for i in range(len(listA)):
        listLink.append(listA[i].get('href'))   
    length = len(listLink)
    l16 = int(length / 16)

    thread1 = threading.Thread(target = crawlContents, args = ("Part1.json", 0, l16, ))
    thread2 = threading.Thread(target = crawlContents, args = ("Part2.json", l16, l16 * 2, ))
    thread3 = threading.Thread(target = crawlContents, args = ("Part3.json", l16 * 2, l16 * 3, ))
    thread4 = threading.Thread(target = crawlContents, args = ("Part4.json", l16 * 3, l16 * 4, ))
    thread5 = threading.Thread(target = crawlContents, args = ("Part5.json", l16 * 4, l16 * 5, ))
    thread6 = threading.Thread(target = crawlContents, args = ("Part6.json", l16 * 5, l16 * 6, ))
    thread7 = threading.Thread(target = crawlContents, args = ("Part7.json", l16 * 6, l16 * 7, ))
    thread8 = threading.Thread(target = crawlContents, args = ("Part8.json", l16 * 7, l16 * 8, ))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()