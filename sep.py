import requests
from lxml import etree

url = "FILL_ME_IN"
res = requests.get(url)
parser = etree.HTMLParser()
root = etree.fromstring(res.content, parser)
import ipdb;ipdb.set_trace()
