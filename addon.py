from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
#URL1 = "https://podcasts.apple.com/us/podcast/the-official-project-censored-show/id1239961997?mt=2"
URL1 = "https://feed.podbean.com/projectcensored/feed.xml"
URL2 = "https://www.projectcensored.org/feed/podcast/along-the-line"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('latest_projectcensored'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/9c/0a/1e/9c0a1e34-7f7a-aecc-4b90-be410bf95bf5/mza_9015145626714141933.jpg/939x0w.jpg"},
   {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_projectcensored'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/9c/0a/1e/9c0a1e34-7f7a-aecc-4b90-be410bf95bf5/mza_9015145626714141933.jpg/939x0w.jpg"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('latest_ATL'),
            'thumbnail': "https://www.projectcensored.org/wp-content/uploads/2019/01/alongthelinelogo2-1.jpg"},
   {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_ATL'),
            'thumbnail': "https://www.projectcensored.org/wp-content/uploads/2019/01/alongthelinelogo2-1.jpg"},
   ]
    return items

@plugin.route('/all_projectcensored/')
def all_projectcensored():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_projectcensored/')
def latest_projectcensored():
    soup1 = mainaddon.get_soup1(URL1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/all_ATL/')
def all_ATL():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/latest_ATL/')
def latest_ATL():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup2)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
