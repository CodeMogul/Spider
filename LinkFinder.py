from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
    
    # Method called when start of a tag is encountered
    # @param tag : tag encountered
    # @param attrs: attributes of that tag ex:class, href
    # attrs is a list of tupples [(attribute, value),..] 
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
    
    def page_links(self):
        return self.links

    # Kind of virtual method, requires to be inherite
    def error(self, message):
        print("Error: " + message)
