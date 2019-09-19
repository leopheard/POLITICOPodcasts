from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/PPY1840735050" #GLOBALTRANSLATIONS
url2 = "https://feeds.megaphone.fm/serdcast" #NERDCAST
url3 = "https://feeds.megaphone.fm/POL9526976537" #OFFMESSAGE
url4 = "https://feeds.simplecast.com/0WAkD8tI" #PLAYBOOKAUDIOBRIEFING
url5 = "https://feeds.simplecast.com/bWkOmgFt" #PULSECHECKS
url6 = "https://feeds.simplecast.com/Q7fb3j2T" #POLITICOMONEY
url7 = "https://feeds.simplecast.com/y6yyKu_h" #WOMENRULE

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/b1e39e90-4a0d-11e7-b1aa-2f52b1d6bc60/image/uploads_2F1558381350768-bncx4pfk1vl-aaacec0ec7771275578a9d96df91cad3_2FGlobalTranslation_Final.jpg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/3203c268-81c7-11e6-a0e4-ffa09ce0cb1a/image/uploads_2F1490990042872-n5kc8litbw126jy0-bf2caed744896f1d73d613a670a22fc2_2FNerdcast-FinalTagline_REV6.jpg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/4a356fe0-81cb-11e6-a9c6-2faab6abb1d4/image/uploads_2F1539702660842-jfin9wve49-d4d2b9299e88f29b1f6efdb0ef3fdf82_2FALBERTA-noname-OffMessage_Logo_FINAL_Rev4.jpg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://cdn.simplecast.com/images/78b88d91-969b-4340-973b-cc81688b2d98/c374f0d5-9816-4837-87de-f2615cb2651a/1510597298artwork.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://cdn.simplecast.com/images/57e73d0a-dce0-413c-a342-50aa222ebb97/98586637-f494-4c41-9a23-18c7aab1671f/1510085764artwork.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://cdn.simplecast.com/images/57e73d0a-dce0-413c-a342-50aa222ebb97/98586637-f494-4c41-9a23-18c7aab1671f/1510085764artwork.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://cdn.simplecast.com/images/57e73d0a-dce0-413c-a342-50aa222ebb97/98586637-f494-4c41-9a23-18c7aab1671f/1510085764artwork.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

if __name__ == '__main__':
    plugin.run()
