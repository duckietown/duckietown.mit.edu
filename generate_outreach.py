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
    #logger.info('outreach_no_media: %r' % outreach_no_media)
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
        lat = d.get('lat')
        lon = d.get('lon')
        s+= """
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(%.9f,%.9f),
         map: map,
         icon: image,
         title: '%s'
        }); """ % (lat,lon,generate_hover(d))
        if (d.get('active')):
            s+="""
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[%d][0]);
                infoWindow.open(map, marker);
            }
        })(marker, %d));""" % (i,i)
        i+=1
        

    return s
        
def generate_hover(d):
    institution = d.get('institution')
    title = d.get('title')
    if not title:
        title= "Under Development"
    tags = d.get('tags')
    tag = tags[0]
    s=""
    s+="%s \\n" % institution
    s+="%s \\n" % title
    s+="(%s" % tag.title()
    if tag != 'research' and tag!= 'independent' :
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
        title = d.get('title')
        if not title:
            title = "Under Development"
        info = """'<div class="info_content">'"""
        info += """+'<h3>%s' """ % tag.title()
        if tag != 'research' and tag!= 'independent':
            info+= "+ ' Class'"
        institute_url = d.get('institution_url')
        project_url = d.get('project_url')
        if project_url:
            info+="""+ ': <a href="%s">'""" % project_url  
        info+="+ ' %s'" % title
        if project_url:
            info+="+'</a>'"
        info+= "+' at '"
        if institute_url:
            info+="""+'<a href="%s">'""" % institute_url
        info+="+'%s'" % d.get('institution')
        if institute_url:
            info+="+'</a>'" 
        info+="+'</h3>'"
        desc = d.get('desc')
        if desc:
            info+="""+'<p>%s</p>'""" % desc.strip()
        info+="+'</div>'""" 
        s+="""infoWindowContent.push([%s]);\n""" % info
    return s

def generate_html(outreach):



    print("""

## Education
    
    """)

    selected = select_from_tags(outreach,['graduate'])
    if len(selected) != 0:
                                
        print("""

### Graduate

""")
        print(generate_html_tag(selected, ['graduate']))

    selected = select_from_tags(outreach,['undergraduate'])
    if len(selected) != 0:
        print("""

### Undergraduate

""")

        print(generate_html_tag(selected, ['undergraduate']))

    selected = select_from_tags(outreach,['high school'])
    if len(selected) != 0:
        print("""

### High School

""")

        print(generate_html_tag(selected, ['high school']))

    selected = select_from_tags(outreach,['elementary school'])
    if len(selected) != 0:
        print("""

### Elementary School

""")

        print(generate_html_tag(selected, ['elementary school']))

    selected = select_from_tags(outreach,['independent'])
    if len(selected) != 0:
        print("""

### Independent Study

""")
        print(generate_html_tag(selected, ['independent']))


    selected = select_from_tags(outreach,['research'])
    if len(selected) !=0:
        print("""

## Research
    
    """)

        print(generate_html_tag(selected, ['research']))

    selected = select_from_tags(outreach,['media'])
    if len(selected) !=0:
        print("""

## Media Coverage
    
    """)

        print(generate_html_tag(selected, ['media']))

    if False:
        print("""

    ## Untagged outreach 
        
        """)

        print(generate_html_tag(outreach, None))



def select_from_tags(outreach, tags_to_include, require_active=True):
    def select_elements(d):
        tags = d.get('tags', [])
        if tags is None:
            tags = []
        sel = False
        if tags_to_include is None:
            if (len(tags) == 0):
                sel = True
        else:
            sel = any([_ in tags for _ in tags_to_include])
        if require_active and not d.get('active'):
            sel = False
        return sel
    return [d for d in outreach if select_elements(d)]
                    

def generate_html_tag(selected, tags_to_include):
    

    logger.info('tags_to_include %r: selected %d' % (tags_to_include, len(selected)))
    s = ""
    for d in selected:
        id_outreach = d.get('id')
        title = d.get('title', '')
        if not title:
            title = "Under development"
        institute = d.get('institution','')
        classes = []
        if not title:
            title = ''
        s += '\n\n'
        desc = d.get('desc', '')
        if not desc:
            desc = ''
        desc = desc.strip()
        desc = desc.replace('\n', ' ')
        institute_url = d.get('institution_url')
        s += """<p id="%s" class="%s"> """ % (id_outreach, " ".join(classes)) 
        if institute_url:
            s+= """<a class="title" href="%s">""" % institute_url
        s+="%s" % institute
        if institute_url:
            s+="</a>"
        s+=" - "
        project_url = d.get('project_url')
        if project_url:
            s+="""<a class="title" href="%s"> """ % project_url
        s+= "%s" % title
        if project_url:
            s+="</a>"
        if desc:
            s += ": %s" % desc
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
