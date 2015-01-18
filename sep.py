import requests
from lxml import etree

url = "http://plato.stanford.edu/contents.html"
res = requests.get(url)
parser = etree.HTMLParser()
root = etree.fromstring(res.content, parser)
import ipdb;ipdb.set_trace()
subject_elements = root.xpath('/html/body/div/div/ul/li')
topics = []
for el in subject_elements:
    title = el.xpath('a').text
    contrib = el.text
    topics.append({
        'title': title.text,
        'contrib': contrib
    })

print topics
