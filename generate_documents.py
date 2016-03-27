#!/usr/bin/env python
from contextlib import contextmanager
from dateutil import parser
import logging
import os
import platform
import sys
import yaml
logging.basicConfig()
logger = logging.getLogger(__name__)


head = """---
layout: default
title: Materials
permalink: materials.html
---

**Note: This is an open-source class. All materials should be available to everybody. If you get
a permission error somewhere, please notify us, at <a href="mailto:hr@duckietown.com">hr@duckietown.com</a>.**

<style type='text/css'>
.missing { color: red; }
.title {font-weight: bold; }
img.icon { border: 0;  width: 1em; }
</style>


<p style='color: darkred'>Note: at this point, the list of documents and the documents themselves
are drafts.</p>

<p><a style='font-weight: bold' href='media/collected.pdf'> All documents collated in one big PDF</a>. </p>

"""

tail = """

"""

class MyExc(Exception):
    pass

def main():
    try:

        documents_data = sys.stdin.read()
        documents = yaml.load(documents_data)

        print(head)
        print(generate_html(documents))
        print(tail)

    except MyExc as e:
        logger.error(e)
        sys.exit(-2)
    except Exception as e:
        import traceback
        logger.error(traceback.format_exc(e))
        sys.exit(-1)

def generate_html(documents):
    print("""

## Important documents for MIT students 
    
    """)

    print(generate_html_tag(documents, 'spring2016'))

    print("""

## Setup documents 
    
    """)

    print(generate_html_tag(documents, 'setup'))

    print("""

## Untagged documents 
    
    """)

    print(generate_html_tag(documents, None))

def icon_pdf():
    return "<img class='icon' src='media/pdf.gif'/>"

def icon_gdoc():
    return "<img class='icon' src='media/gdoc.png'/>"

def url_pdf(d):
    id_document = get_id(d)
    pdf_url = make_pdf_url(id_document)
    return pdf_url

def url_gdoc(d):
    return d['google_docs_share_link']

def make_pdf_url(id_document):
    return 'https://docs.google.com/document/d/%s/export?format=pdf' % id_document

def get_id(d):
    s = d['google_docs_share_link']

    # "https://docs.google.com/document/d/1hIZftFCZEpcvL-yp8kkYMjWzGBiNcwajdn2_ZxeirIM/edit?usp=sharing"

    s = s.replace('https://docs.google.com/document/d/', '')

    s = s.replace('/edit?usp=sharing', '')
    s = s.replace('https://drive.google.com/open?id=', '')

    return s

def generate_html_tag(documents, tag):
    
    def select(d):
        tags = d.get('tags', [])
        if tags is None:
            tags = []
        if tag is None:
            return len(tags) == 0
        return tag in tags
    
    selected = [d for d in documents if select(d)]
    
    logger.info('tag %r: selected %d' % (tag, len(selected)))
    s = ""
    for d in selected:
        id_document = d.get('id')
        title = d.get('title', '')
        classes = []
        if not title:
            title = 'Missing title'
            classes.append('missing')

        google_docs_share_link = d['google_docs_share_link']

        s += '\n\n'
        desc = d.get('desc', '')
        if not desc:
            desc = ''
        if not desc:
            desc = '<span class="missing">Missing description</span>'
#             classes.append('missing')
        desc = desc.strip()
        desc = desc.replace('\n', ' ')

        pdf_link = '<a href="%s">%s static pdf</a>' % (url_pdf(d), icon_pdf())

        s += ('<p id="%s" class="%s"><a class="title" href="%s">%s%s</a> (%s): ' %
        (id_document, " ".join(classes), google_docs_share_link, icon_gdoc(), title, pdf_link))

        s += desc


        s += '</p>'


        s += '\n\n'
    return s
    

logger.setLevel(logging.DEBUG)
def add_coloring_to_emit_ansi(fn):
    # add methods we need to the class
    def new(*args):
        levelno = args[1].levelno
        if(levelno >= 50):
            color = '\x1b[31m'  # red
        elif(levelno >= 40):
            color = '\x1b[31m'  # red
        elif(levelno >= 30):
            color = '\x1b[33m'  # yellow
        elif(levelno >= 20):
            color = '\x1b[32m'  # green
        elif(levelno >= 10):
            color = '\x1b[35m'  # pink
        else:
            color = '\x1b[0m'  # normal

        args[1].msg = color + str(args[1].msg) + '\x1b[0m'  # normal
        return fn(*args)
    return new

if platform.system() != 'Windows':
    emit2 = add_coloring_to_emit_ansi(logging.StreamHandler.emit)
    logging.StreamHandler.emit = emit2



def indent(s, prefix, first=None):
    s = str(s)
    assert isinstance(prefix, str)
    lines = s.split('\n')
    if not lines: return ''

    if first is None:
        first = prefix

    m = max(len(prefix), len(first))

    prefix = ' ' * (m - len(prefix)) + prefix
    first = ' ' * (m - len(first)) + first

    # differnet first prefix
    res = ['%s%s' % (prefix, line.rstrip()) for line in lines]
    res[0] = '%s%s' % (first, lines[0].rstrip())
    return '\n'.join(res)


if __name__ == '__main__':
    main()
