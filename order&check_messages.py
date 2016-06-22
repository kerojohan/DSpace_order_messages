# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys, getopt
import os
import re
import argparse
from xml.dom.minidom import Node
from xml.dom import minidom
from xml.etree import ElementTree as ET2
from html5lib.sanitizer import HTMLSanitizerMixin
from HTMLParser import HTMLParser
try:
    from html import escape  # python 3.x
except ImportError:
    from cgi import escape  # python 2.x

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('utf-8')
html = HTMLParser()
# Store input and output file names
ifile=''
ofile=''

class TestHTMLParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.elements = set()

    def handle_starttag(self, tag, attrs):
        self.elements.add(tag)

    def handle_endtag(self, tag):
        self.elements.add(tag)

def element_to_string(element):
    s = element.text or ""
    for sub_element in element:
        s += ET.tostring(sub_element)
    s += element.tail
    return s

def is_html(text):
    elements = set(HTMLSanitizerMixin.acceptable_elements)
    parser = TestHTMLParser()
    parser.feed(text)
    return True if parser.elements.intersection(elements) else False

 

def ordenar_messages(ifile,ofile,language):
    tree = ET.parse(ifile)
    data=[]
    root = tree.getroot()
    for country in root.findall('message'):
        rank=element_to_string(country).strip('\t\n\r').replace('\n', '').replace('\r', '').replace('  ','').replace('\t','')
        if (is_html(rank)):
            rank=html.unescape(rank)
        else:
            rank=escape(rank);    
        rank=re.sub(r'(&((?!amp;)(?!..;)))','&amp;', rank)
        name = country.get('key').strip()
        data.append((name, rank))
    orted_by_second = sorted(data, key=lambda tup: tup[0])
    a = ET.Element('catalogue')
    a.set('xmlns:i18n','http://apache.org/cocoon/i18n/2.1')
    a.set('xml:lang',language)
    for i in orted_by_second:
        b = ET.SubElement(a, 'message')
        b.set('key',i[0])
        b.text=i[1]
    xmlstr = minidom.parseString(ET.tostring(a)).toprettyxml(indent="   ")
    xmlstr2=re.sub(r'/>\n','></message>\n',xmlstr )
    with open(ofile, "w") as f:
        f.write(html.unescape(xmlstr2.encode('utf-8')))
    f.close()



parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
parser.add_argument('-l','--language',help='code of language. Ex: ca for catalan', required=True)
args = parser.parse_args()

try:
    ET2.parse(args.input)
except ET.ParseError:
    print('INPUT {} is corrupt'.format(args.input))

ordenar_messages(args.input,args.output, args.language)

try:
    ET2.parse(args.output)
except ET.ParseError as error:
    print('OUTPUT {} is corrupt'.format(args.output))
    print(error)
