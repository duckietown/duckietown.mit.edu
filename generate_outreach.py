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

###
# TODO:
# condition on existence of link urls in yaml so that links don't appear for "NONE"
# format text better
# addition of a picture for every entry?


def read_file(fn):
    with open(fn) as f:
        return f.read()



tail = """

"""

class MyExc(Exception):
    pass

def main():
    try:

        outreach_data = sys.stdin.read()
        outreach = yaml.load(outreach_data)

        generate_head(outreach)
        generate_html(outreach)
        print(tail)

    except MyExc as e:
        logger.error(e)
        sys.exit(-2)
    except Exception as e: 
        import traceback
        logger.error(traceback.format_exc(e))
        sys.exit(-1)

def generate_head(outreach):

    print("""---
layout: page
title: Outreach
permalink: outreach.html
---

<style type="text/css">
        #map {
        width: 100%;
        height: 400px;
        background-color: grey;
      }
</style>

""")

    outreach_no_media = [d for d in outreach if d.get('tags',[])[0] != 'media']
    logger.info('outreach_no_media: %r' % outreach_no_media)
    print(generate_map(outreach_no_media))
	
def generate_map(outreach):
    s=""
    s+="""
<div id="map"></div>
<script>
function initMap() {
"""
    s+="""var boston = {lat: 42.3601, lng: -71.0589};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 2,
          center: boston
        });"""
#    s+="var bounds = new google.maps.LatLngBounds();"
    s+="var infoWindow = new google.maps.InfoWindow(), marker, i;"
    s+="var service = new google.maps.places.PlacesService(map);"
    s+= generate_info_windows(outreach)
    s+= generate_markers(outreach)
#    s+= """var boundsListener = google.maps.event.addListener((map), 'bounds_changed', function(event) {
#        this.setZoom(14);
#        google.maps.event.removeListener(boundsListener);
#    });"""
    s+="""
      }

    </script>
<script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDCdYZ3gHK80cDg8NKT8g24JQJVLyUYqc8&callback=initMap&libraries=places">
    </script>
"""
    return s
    
def generate_markers(outreach):    
    s=""
    s+= """var image = { 
            url: 'media/duckie2.png', 
            scaledSize: new google.maps.Size(20,20), 
            origin: new google.maps.Point(0, 0), 
            anchor: new google.maps.Point(0, 20) 
  };"""
    i=0
    for d in outreach:
        institution = d.get('institution')
        s+= """ 
            var request = { 
               query: '%s' 
            }; """ % (institution)
        s+= """
         service.textSearch(request, callback%d); 
         function callback%d(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: '%s' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[%d][0]);
                infoWindow.open(map, marker);
            }
        })(marker, %d)); 
          };}; """ % (i,i,generate_hover(d),i,i)
        i+=1

    return s
        
def generate_hover(d):
    institution = d.get('institution')
    title = d.get('title')
    tags = d.get('tags')
    tag = tags[0]
    s=""
    s+="%s \\n" % institution
    s+="%s \\n" % title
    s+="(%s" % tag.title()
    if tag != 'research':
        s+=" Class"
    s+=")"
    logger.info("institution: %s" % institution)
    return s

def generate_info_windows(outreach):
    
    s=""
    s+="""
    // Info Window Content
    var infoWindowContent = []
"""
    for d in outreach:
        tag=d.get('tags')[0]
        s+="""infoWindowContent.push(['<div class="info_content">' +
        '<h3>%s' """ % tag.title()
        if tag != 'research':
            s+= "+ ' Class'"
        s+="""+ ': <a href="%s">%s</a> at <a href="%s">%s</a> </h3>' +
        '<p>%s</p>' + '</div>']);""" % (d.get('project_url'), d.get('title'), d.get('institution_url'), d.get('institution'), d.get('desc').strip() )
    return s

def generate_html(outreach):



    print("""

## Education
    
    """)

    print("""

### Graduate

""")

    print(generate_html_tag(outreach, ['graduate']))

    print("""

### Undergraduate

""")

    print(generate_html_tag(outreach, ['undergraduate']))

    print("""

### High School

""")

    print(generate_html_tag(outreach, ['high school']))

    print("""

### Elementary School

""")

    print(generate_html_tag(outreach, ['elementary school']))



    print("""

## Research
    
    """)

    print(generate_html_tag(outreach, ['research']))

    print("""

## Media Coverage
    
    """)

    print(generate_html_tag(outreach, ['media']))

    if False:
        print("""

    ## Untagged outreach 
        
        """)

        print(generate_html_tag(outreach, None))



def generate_html_tag(outreach, tags_to_include):
    
    def select(d):
        tags = d.get('tags', [])
        if tags is None:
            tags = []
        if tags_to_include is None:
            return len(tags) == 0
        return any([_ in tags for _ in tags_to_include])
    
    selected = [d for d in outreach if select(d)]
    
    logger.info('tags_to_include %r: selected %d' % (tags_to_include, len(selected)))
    s = ""
    for d in selected:
        id_outreach = d.get('id')
        title = d.get('title', '')
        institute = d.get('institution','')
        classes = []
        if not title:
            title = 'Missing title'
            classes.append('missing')

        s += '\n\n'
        desc = d.get('desc', '')
        if not desc:
            desc = ''
        if not desc:
            desc = '<span class="missing">Missing description</span>'
#             classes.append('missing')
        desc = desc.strip()
        desc = desc.replace('\n', ' ')
        institute_url = d.get('institute_url')
        s += """<p id="%s" class="%s"><a class="title" href="%s">%s</a> - """ % (id_outreach, " ".join(classes), institute_url, institute)
        project_url = d.get('project_url')
        s += ('<a class="title" href="%s">%s</a>: ' %  (project_url, title))

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
