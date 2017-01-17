import re
import urllib


def __get__html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def __get_images(html):
    __reg = r'src="(.*?\.jpg)" width'
    __img__re = re.compile(__reg)
    __img__src = re.findall(__img__re, html)
    x = 0
    for __img in __img__src:
        if x > 80:
            urllib.urlretrieve(__img, '%s.jpg' % x)
        x += 1
        print "%d.jpg" % x
    return __img__src


html = __get__html("http://feature.mtime.com/item/2016/RogueOne/")
print __get_images(html)
# print re.findall("^http*.jpg", __get_images(html))
