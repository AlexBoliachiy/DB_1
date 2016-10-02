import os
import re
import sys
import webbrowser
from lxml import etree
from lxml.html import parse
from lxml.html.clean import Cleaner
from urllib.request import urlopen


def third():
    dom = parse("http://hotline.ua/computer/noutbuki-netbuki/")
    name = dom.xpath("//b[@class='m_r-10']/a")
    pic = dom.xpath("//img[@class='max-120']")
    # description = dom.xpath("//div[@class='cell grey-6 p_b-10 gd-tech']")
    # for x in description:
    # print(x.text.replace('\n', '').encode().decode('utf-8', 'ignore')
    # pass
    root = etree.Element("Notebooks")
    for x in range(len(name)):
        element = etree.Element("Notebook")

        c = etree.Element("name")
        c.text = name[x].text.replace('\n', '')
        c2 = etree.Element("src")
        c2.text = 'http://hotline.ua' + pic[x].get("src").replace(" ", '')
        element.append(c)
        element.append(c2)
        root.append(element)
    xslt = etree.parse('xml.xsl')
    transform = etree.XSLT(xslt)
    newdom = transform(root)
    with open("temp.html","w") as file:
        file.write(etree.tounicode(newdom, pretty_print=True))
        path = os.path.abspath("temp.html")
        webbrowser.open("file://" + path)


