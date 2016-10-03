from first import first


def second():
    root = first()
    for x in root.xpath("//page"):
        for y in root.xpath("//page[@url='%s']" % x.get("url")):
            print(x.get("url"), '--', len(root.xpath("//page[@url='%s']/fragment[@type='text']" % x.get("url"))))

