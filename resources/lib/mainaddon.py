import requests
import re
from bs4 import BeautifulSoup

url1 = "https://feeds.megaphone.fm/PPY1840735050" #GLOBALTRANSLATIONS
url2 = "https://feeds.megaphone.fm/serdcast" #NERDCAST
url3 = "https://feeds.megaphone.fm/POL9526976537" #OFFMESSAGE
url4 = "https://feeds.simplecast.com/0WAkD8tI" #PLAYBOOKAUDIOBRIEFING
url5 = "https://feeds.simplecast.com/bWkOmgFt" #PULSECHECKS
url6 = "https://feeds.simplecast.com/Q7fb3j2T" #POLITICOMONEY
url7 = "https://feeds.simplecast.com/y6yyKu_h" #WOMENRULE

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("https://feeds.megaphone.fm/PPY1840735050")
def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("https://feeds.megaphone.fm/serdcast")
def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
get_soup3("https://feeds.megaphone.fm/POL9526976537")
def get_soup4(url4):
    page = requests.get(url4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4
get_soup4("https://feeds.simplecast.com/0WAkD8tI")
def get_soup5(url5):
    page = requests.get(url5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup5))
    return soup5
get_soup5("https://feeds.simplecast.com/bWkOmgFt")
def get_soup6(url6):
    page = requests.get(url6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup6))
    return soup6
get_soup6("https://feeds.simplecast.com/Q7fb3j2T")
def get_soup7(url7):
    page = requests.get(url7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup7))
    return soup7
get_soup7("https://feeds.simplecast.com/y6yyKu_h")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/b1e39e90-4a0d-11e7-b1aa-2f52b1d6bc60/image/uploads_2F1558381350768-bncx4pfk1vl-aaacec0ec7771275578a9d96df91cad3_2FGlobalTranslation_Final.jpg?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/3203c268-81c7-11e6-a0e4-ffa09ce0cb1a/image/uploads_2F1490990042872-n5kc8litbw126jy0-bf2caed744896f1d73d613a670a22fc2_2FNerdcast-FinalTagline_REV6.jpg?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/4a356fe0-81cb-11e6-a9c6-2faab6abb1d4/image/uploads_2F1539702660842-jfin9wve49-d4d2b9299e88f29b1f6efdb0ef3fdf82_2FALBERTA-noname-OffMessage_Logo_FINAL_Rev4.jpg?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://cdn.simplecast.com/images/78b88d91-969b-4340-973b-cc81688b2d98/c374f0d5-9816-4837-87de-f2615cb2651a/1510597298artwork.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/7a/c4/c7/7ac4c7e6-975b-86ef-b899-bf3f3a678ea5/mza_119992604573376929.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/b1/0a/97/b10a97dd-887d-7194-2540-ca762ef9fefd/mza_6322448531695263244.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://is4-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ea/a2/eb/eaa2eb6e-3557-f9bf-c236-f0c79d188c0c/mza_5850662405940263070.jpg/600x600bb.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
