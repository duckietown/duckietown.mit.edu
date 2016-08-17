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
permalink: lectures.html
---
   

*Lectures recorded by [Chris Welch](http://chriswelchphotography.com) and Sasha Galitsky.*
   
<style type='text/css'>
    .notready, .incomplete { color: red }
    div.lecture {margin: 1em }
    span.lecture_id { color: gray; font-size: smaller }
    div.lecture h2 { margin-left: -1em} 
    
</style>
 
"""
    foot = """
    
   *Lectures recorded by [Chris Welch](http://chriswelchphotography.com) and Sasha Galitsky.* 
"""
    return head + res + foot

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


    #s += '<h2><span class="lecture_id">%s:</span> %s </h2>\n\n' % (id_lecture, title)
    s += '<h2> %s </h2>\n\n' % ( title)

    if not lecture['ready']:
        s += '<p class="notready">This lecture is not ready for publishing yet; files are missing,'
        s += ' or the videos are not edited.</p>'


    if lecture['presenters']:
        s += '<p>Presenters: '
        def f(p):

            if p in people:
                person = people[p]
                url = person['url']
                name = person['name']
                if name is None:
                    return p
                if url:
                    return "<a href='%s'>%s</a>" % (url, name)
                else:
                    return name
                return p
            else:
                context.warn('No person %r.' % p)
                return p
        s += ', '.join(f(_) for _ in lecture['presenters'])
        s += '</p>\n\n'
    else:
        s += '<p class="incomplete">(No presenters specified.)</p>\n\n'

    vimeo = lecture['vimeo']

    if not vimeo:
        s += '<p class="incomplete">(Video not available yet.)</p>\n\n'

    s += '<table><tr>\n'
    for url in vimeo:
        s += '   <td>'
        s += generate_vimeo(url, context)
        s += '</td>'
    s += '</tr></table>\n\n'


    if lecture['files']:
        s += '<ul class="materials">\n'
        for f in lecture['files']:
            s += ' <li><a href="%s">%s</a></li>\n' % (f['url'], f['desc'])
        s += '</ul>\n\n'


    s = "<div class='lecture'>\n\n" + indent(s, "    ") + '\n</div>\n\n'
    return s



def generate(lectures, people, context):
    s = "\n\n"
    order = sorted(lectures)
    for l in order:
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


def normalize_url(v, context):  # @UnusedVariable
    if v is None:
        context.warn('Empty URL')
    # TODO: not existing
    return v


def normalize_string(v, context):  # @UnusedVariable
    if v is None:
        context.warn('empty string')
    return v

def normalize_date(v, context):  # @UnusedVariable
    try:
        dt = parser.parse(v)
    except ValueError as e:
        msg = 'Cannot parse date %r:\n\n%s' % (v, e)
        raise MyExc(msg)
    return dt

def normalize_tags(v, context):
    if v is None:
        context.warn('No tags specified')
        return []
    return v

def normalize_position(v, context):
    if v is None:
        context.warn('No position specified')
        return ''
    return v

def normalize_bio(v, context):
    if v is None:
        context.warn('No bio.')
        return ''
    return v

def normalize_person(id_record, record, context):
    record['order'] = record.get('order', 100)
    normalize(id_record, record, 'name', normalize_name, context)
    normalize(id_record, record, 'position', normalize_position, context)
    normalize(id_record, record, 'url', normalize_url, context)
    normalize(id_record, record, 'bio', normalize_bio, context)
    normalize(id_record, record, 'tags', normalize_tags, context)
    return record

def normalize_presenters(presenters, context):
    if presenters is None:
        presenters = []

    if len(presenters) == 0:
        context.warn('No presenters')

    return presenters

def normalize_files(files, context):
    if files is None:
        files = []

    if len(files) == 0:
        context.warn('No files')

    for i, f in enumerate(files):
        normalize(str(i), f, 'desc', normalize_string, context)
        normalize(str(i), f, 'url', normalize_url, context)

    return files

# C01_intro:
#   title: "Welcome to Duckietown"
#   date: "Feb 3, 2016"
#   vimeo:
#   - https://vimeo.com/154523464
#   - https://vimeo.com/154547370
#
#   files:
#     - desc: Part 1 Keynote
#       url: https://www.dropbox.com/s/ybny46gfyr65wod/01-C01_intro-part1-AC.key?dl=1
#     - desc: Part 1 PDF
#       url: https://www.dropbox.com/s/p707ab16llzb3zw/01-C01-intro-part1-AC-steps.pdf?dl=1
#
#
#   presenters:
#   - censi
#   - paull

def normalize_bool(x, context):
    return x

def normalize_lecture(id_record, record, context):
    normalize(id_record, record, 'date', normalize_date, context)
    normalize(id_record, record, 'title', normalize_title, context)
    normalize(id_record, record, 'vimeo', normalize_vimeo, context)
    normalize(id_record, record, 'ready', normalize_bool, context)
    normalize(id_record, record, 'files', normalize_files, context)
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
