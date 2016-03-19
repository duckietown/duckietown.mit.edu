#!/usr/bin/env python
from dateutil import parser
import logging
import os
import yaml
from contextlib import contextmanager
logging.basicConfig()
logger = logging.getLogger(__name__)

class MyExc(Exception):
    pass

def main():
    try:
        import sys
        args = sys.argv[1:]
        if len(args) != 2:
            msg = 'Expected two arguments, got %r.' % args
            
            raise MyExc(msg)

        people_filename = args[0]
        lectures_filename = args[1]
        
        res = go(people_filename, lectures_filename)
        print(res)

    except MyExc as e:
        logger.error(e)
        sys.exit(-2)
    except Exception as e:
        import traceback
        logger.error(traceback.format_exc(e))
        sys.exit(-1)


def go(people_filename, lectures_filename):
    
    context = Context()

    people_contents = read_people(people_filename, context)
    
    
    logger.info('people: %s' % people_contents)
    
    lectures_contents = read_lectures(lectures_filename, context)
    
    logger.info('lectures: %s' % lectures_contents)
    
    context.bail()
    
    res = generate(lectures_contents, people_contents, context)
    
    context.bail()
    
    if context.warnings:
        logger.warning(context.get_warnings())

    head = """---
layout: page
title: Lectures
---
   

*Lectures recorded by [Chris Welch](http://chriswelchphotography.com) and Sasha Galitsky.*
   
<style type='text/css'>
    .incomplete { color: red }
</style>
 
"""
    return head + res

class Context():

    def __init__(self):
        self.warnings = []
        self.errors = []
        self.stack = []

    def _convert(self, s):
        return ":".join(self.stack)+':'+ s
        
    def warn(self, s):
        self.warnings.append(self._convert(s))
    
    def error(self, s):
        self.errors.append(self._convert(s))
    
    @contextmanager 
    def sub(self, w):
        self.stack.append(w)
        yield
        self.stack.pop(-1)
        
    def get_warnings(self):
        s = "Please fix the following problems:"
        for w in self.warnings:
            s += "\n" + w
        return s

    def get_errors(self):
        s = "You need to fix the following problems:"
        for w in self.errors:
            s += "\n" + w
        return s
    
    def bail(self):
        if self.errors:
            logger.error(self.get_errors())
            msg = 'Errors in the input.'
            raise MyExc(msg)
        

    
def generate_vimeo(url, context):  # @UnusedVariable

    id_video = url.split('/')[-1]
    newurl = 'https://player.vimeo.com/video/%s' % id_video
    s = """\n
<iframe src="IFRAME" 
        width="400" height="281" frameborder="0" 
        webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
"""

    s = s.replace("IFRAME", newurl)

    return s

def generate_lecture(id_lecture, lecture, people, context):
    s = "\n\n"
    title = lecture['title']
    s += '<h2>%s: %s </h2>\n' % (id_lecture, title)

    vimeo = lecture['vimeo']

    if not vimeo:
        s += '<p class="incomplete">(Video not available yet.)</p>\n'

    s += '<table><tr>'
    for url in vimeo:
        s += '<td>'
        s += generate_vimeo(url, context)
        s += '</td>'
    s += '</tr></table>'

    if lecture['presenters']:
        s += '<p>Presenters: '
        def f(p):

            if p in people:
                person = people[p]
                url = person['url']
                name = person['name']
                if url:
                    return "<a href='%s'>%s</a>" % (url, name)
                else:
                    return name
                return p
            else:
                context.warn('No person %r.' % p)
                return p
        s += ', '.join(f(_) for _ in lecture['presenters'])
        s += '</p>'
    else:
        s += '<p class="incomplete">(No presenters specified.)</p>'
    return s



def generate(lectures, people, context):
    s = "\n\n"
    order = sorted(lectures)
    for l in order:
#         presenters = []
#         for p in presenters:
#             get_person(people, p)
#  
        lecture = lectures[l]
        with context.sub(l):
            s += generate_lecture(l, lecture, people, context)
    return s
 
 
def read_yaml_dict(filename):
    if not os.path.exists(filename):
        msg = 'Could not find file %r.' % filename
        raise Exception(msg)

    yaml_string = open(filename).read()
    try:
        values = yaml.load(yaml_string)
    except yaml.YAMLError as e:
        msg = 'Yaml file is invalid:\n---\n%s' % e
        raise MyExc(msg)

    if not isinstance(values, dict):
        msg = 'Invalid content: %s' % values
        raise MyExc(msg)

    return values

def read_people(people_filename, context):

    import glob

    values = {}
    listing = glob.glob(people_filename)
    for filename in listing:
        handle = os.path.splitext(os.path.basename(filename))[0]
        logger.info('%s - %s ' % (handle, filename))
        value = read_yaml_dict(filename)
#     values = read_yaml_dict(people_filename)
#     for k, value in list(values.items()):
        values[handle] = normalize_person(handle, value, context)
    return values

def read_lectures(lectures_filename, context):
    values = read_yaml_dict(lectures_filename)
    for k, value in list(values.items()):
        values[k] = normalize_lecture(k, value, context)
    return values

def normalize(id_struct, struct, key, function, context):
    with context.sub(id_struct):
        if not key in struct:
            msg = 'Could not find %r in %r' % (key, struct)
            raise MyExc(msg)
        if not key in struct:
            msg = 'No %r field in %r' % (key, struct)
            raise MyExc(msg)
        value = struct[key]
        try:
            with context.sub(key):
                struct[key] = function(value, context)
        except MyExc as e:
            logger.error('Problem with %r in %s: %s\n\n%s' % (key, id_struct, struct, e))
            raise

def normalize_vimeo(v, context):  # @UnusedVariable
    """ must be list of strings """
    if isinstance(v, str) and 'http' in v:
        return [v]
    if not isinstance(v, list):
        msg = 'Expect list of strings'
        raise MyExc(msg)
    return v


def normalize_title(v, context):
    if v is None:
        return '(untitled)'
    context.warn('untitled lecture')
    return v

def normalize_name(v, context):  # @UnusedVariable
    return v

def normalize_date(v, context):  # @UnusedVariable
    try:
        dt = parser.parse(v)
    except ValueError as e:
        msg = 'Cannot parse date %r:\n\n%s' % (v, e)
        raise MyExc(msg)
    return dt

def normalize_person(id_record, record, context):
    normalize(id_record, record, 'name', normalize_name, context)
    return record

def normalize_presenters(presenters, context):
    if presenters is None:
        presenters = []

    if len(presenters) == 0:
        context.warn('No presenters')

    return presenters

def normalize_lecture(id_record, record, context):
    normalize(id_record, record, 'date', normalize_date, context)
    normalize(id_record, record, 'title', normalize_title, context)
    normalize(id_record, record, 'vimeo', normalize_vimeo, context)
    normalize(id_record, record, 'presenters', normalize_presenters, context)

    return record

# ## colored loggin

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

import platform
if platform.system() != 'Windows':
    emit2 = add_coloring_to_emit_ansi(logging.StreamHandler.emit)
    logging.StreamHandler.emit = emit2


if __name__ == '__main__':
    main()
