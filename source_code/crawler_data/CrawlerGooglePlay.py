from bs4 import BeautifulSoup
import json
import requests

soup = BeautifulSoup (open("phone.html", encoding = "utf8"), features = "lxml")
listA = soup.find_all('a', class_ = 'Si6A0c')
listLink = []
for i in range(len(listA)):
    listLink.append(listA[i].get('href'))

soup = BeautifulSoup (open("tablet.html", encoding = "utf8"), features = "lxml")
listA = soup.find_all('a', class_ = 'Si6A0c')
for i in range(len(listA)):
    listLink.append(listA[i].get('href'))

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

def crawlContents(fileName, i):
    setupFile(fileName, False)
    deli = ""

    for j in range(i, i + 10):
        link = requests.get(listLink[j])
        soup = BeautifulSoup(link.content, 'html.parser')
        name = soup.find_all('h1')
        company = soup.find_all(class_ = 'Vbfug')
        ratingAndDownloads = soup.find_all(class_ = 'ClM7O')
        reviewsAndAge = soup.find_all(class_ = 'g1rdde')
        descirbe = soup.find_all(class_ = 'Uc6QCc')
        
        data = {}

        data['name'] = name[0].text
        data['company'] = company[0].text
        data['rating'] = ratingAndDownloads[0].text
        data['downloads'] = ratingAndDownloads[1].text
        data['reviews'] = reviewsAndAge[0].text
        data['age'] = reviewsAndAge[2].text
        data['describe'] = descirbe[0].text

        writeFile(fileName, data, deli)
        deli = ",\n"

    setupFile(fileName, True)

if __name__ == "__main__":
    for i in range(93):
        fileName = "googleplay" + str(i * 10) + "_" + str(i * 10 + 9) + ".json"
        crawlContents(fileName, i)