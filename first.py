from lxml import etree, cssselect
from lxml.html import parse, fromstring
from lxml.html.clean import Cleaner
from urllib.request import urlopen
import re


def GetSites(count):
    urls = []
    doc_html = parse("http://korrespondent.net/")
    href = doc_html.xpath("//a")
    for x in href:
        if 'http:' in x.get("href"):
            if x.get("href") not in urls:
                urls.append(x.get("href"))
        if len(urls) == count:
            break
    return urls


def first():
    sites = GetSites(20)
    root = etree.Element("data")
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True
    for cur_url in sites:
        element = etree.Element("page", url=cur_url)
        root.append(element)
        cur_tree = cleaner.clean_html(parse(cur_url)) # remove all scripts like: <script>...</script>
        fragments = cur_tree.xpath("//text() | //img[@src]")
        for x in fragments:
            if hasattr(x,'get') and x.get("src") is not None:
                new_img_fragment = etree.Element("fragment", type='image')
                new_img_fragment.text = x.get("src")
                element.append(new_img_fragment)
            else:
                x = x.replace('\r\n', '')
                if x.isspace() is False and x != '':
                    new_text_fragment = etree.Element("fragment", type='text')
                    new_text_fragment.text = x
                    element.append(new_text_fragment)
    # print(etree.tounicode(root, pretty_print=True))
    return root
