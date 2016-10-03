import os
import re
import sys
import unicodedata
import webbrowser
from lxml import etree
from lxml.html import parse
from lxml.html.clean import Cleaner
from urllib.request import urlopen


def third():


    dom = parse("http://hotline.ua/computer/noutbuki-netbuki/")
    name = dom.xpath("//b[@class='m_r-10']/a")
    pic = dom.xpath("//img[@class='max-120']")
    worth = dom.xpath("//div[@class='text-14 text-12-640']/b")
    # description = dom.xpath("//div[@class='cell grey-6 p_b-10 gd-tech']/text()")
    # for x in description:
    # print(x.text.replace('\n', '').encode().decode('utf-8', 'ignore')
    # pass
    root = etree.Element("Notebooks")
    for x in range(len(name) - 1):
        element = etree.Element("Notebook")

        c = etree.Element("name")
        c.text = name[x].text.replace('\n', '')
        c2 = etree.Element("src")
        c2.text = 'http://hotline.ua' + pic[x].get("src").replace(" ", '')
        c3 = etree.Element("worth")
        c3.text = worth[x].text.encode().decode("ascii", errors='ignore')


        element.append(c)
        element.append(c2)
        element.append(c3)
        root.append(element)

    with open("file3.xml", "wb") as f:
        f.write(etree.tounicode(root, pretty_print=True).encode("utf-8"))
    xslt = etree.parse('xml.xsl')
    transform = etree.XSLT(xslt)
    newdom = transform(root)

    with open("temp.html", "w") as file:
        print(etree.tounicode(newdom, pretty_print=True))
        file.write(etree.tounicode(newdom, pretty_print=True))

        path = os.path.abspath("temp.html")
        webbrowser.open("file://" + path)
