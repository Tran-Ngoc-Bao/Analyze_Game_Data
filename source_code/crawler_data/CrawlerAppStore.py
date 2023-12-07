import requests
from bs4 import BeautifulSoup
import json

linkRoot = requests.get("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi")
soup = BeautifulSoup(linkRoot.content, 'html.parser')
listA = soup.find_all('a')
listLink = []
for i in range(48, 246):
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

    for j in range(i, i + 5):
        link = requests.get(listLink[j])
        soup = BeautifulSoup(link.content, 'html.parser')
        nameAndAge = soup.find_all(class_ = 'app-header__title')
        describe = soup.find_all('a', class_ = 'inline-list__item')
        rating = soup.find_all(class_ = 'we-rating-count')
        information = soup.find_all('dd', class_ = 'information-list__item__definition')

        data = {}

        if len(nameAndAge) == 0:
            data['nameAndAge'] = ""
        else:
            data['nameAndAge'] = nameAndAge[0].text

        if len(describe) == 0:
            data['describe'] = ""
        else:
            data['describe'] = describe[0].text

        if len(rating) == 0:
            data['rating'] = ""
        else:
            data['rating'] = rating[0].text

        data['company'] = information[0].text
        data['size'] = information[1].text
        data['price'] = information[7].text

        writeFile(fileName, data, deli)
        deli = ",\n"

    setupFile(fileName, True)

def crawlContentsSpecial():
    setupFile("appstore_195_197.json", False)
    deli = ""

    for j in range(195, 198):
        link = requests.get(listLink[j])
        soup = BeautifulSoup(link.content, 'html.parser')
        nameAndAge = soup.find_all(class_ = 'app-header__title')
        describe = soup.find_all('a', class_ = 'inline-list__item')
        rating = soup.find_all(class_ = 'we-rating-count')
        information = soup.find_all('dd', class_ = 'information-list__item__definition')

        data = {}

        if len(nameAndAge) == 0:
            data['nameAndAge'] = ""
        else:
            data['nameAndAge'] = nameAndAge[0].text

        if len(describe) == 0:
            data['describe'] = ""
        else:
            data['describe'] = describe[0].text

        if len(rating) == 0:
            data['rating'] = ""
        else:
            data['rating'] = rating[0].text

        data['company'] = information[0].text
        data['size'] = information[1].text
        data['price'] = information[7].text

        writeFile("appstore_195_197.json", data, deli)
        deli = ",\n"

    setupFile("appstore_195_197.json", True)

if __name__ == "__main__":
    for i in range(36, 39):
        fileName = "appstore_" + str(i * 5) + "_" + str(i * 5 + 4) + ".json"
        crawlContents(fileName, i)
    crawlContentsSpecial()