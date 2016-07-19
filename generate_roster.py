#!/usr/bin/env python
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

from generate_lectures import *  # @UnusedWildImport

def main():
    try:
        import sys
        args = sys.argv[1:]
        if len(args) != 1:
            msg = 'Expected one arguments, got %r.' % args

            raise MyExc(msg)

        people_filename = args[0]
        res = go(people_filename)
        print(res)
        
    except MyExc as e:
        logger.error(e)
        sys.exit(-2)
    except Exception as e:
        import traceback
        logger.error(traceback.format_exc(e))
        sys.exit(-1)


def go(people_filename):
    
    context = Context()

    people_contents = read_people(people_filename, context)

    
    logger.info('people: %s' % people_contents)
    
    if context.warnings:
        logger.warning(context.get_warnings())

    res = generate_roster(people_contents)

    head = """  
    
<style type='text/css'>
    table#roster TD {  vertical-align: top;}
    table#roster  tr td:first-child { text-align: center;}
    table#roster  tr td { padding-left: 2em; }
    tr.roles td {padding-top: 2em; margin-right: -4em; font-size: 150%;
    color: #004; font-weight: bold; }
     
    table#roster  tr td {padding-top: 2em;}
    /*tr#first {display: none;}*/
    h1 {display: none;}
    
    .position {font-weight: bold; }
    td.photo {width: 10em; }
    .bio { font-size: 90%; line-height: 80%;}
</style>
"""

    foot = """  """
    
    return head + res + foot

def generate_roster(people):

    s = "\n\n"

    s += """
<table id='roster'>
"""

    s += """
<tr class='roles' id="first" > <td colspan="2">Duckietown Engineering Co. </td> </tr>
"""

    s += generate_roster_tag(people, 'management')

    s += """
<tr class='roles'   > <td colspan="2"> Advisory board </td> </tr>
"""

    s += generate_roster_tag(people, 'advisory')

    s += """
<tr class='roles'  > <td colspan="2"> Sponsors  </td> </tr>
"""

    s += generate_roster_tag(people, 'sponsors')


    s += """
<tr class='roles'   > <td colspan="2"> Operations </td> </tr>
"""

    s += generate_roster_tag(people, 'operations', expected=24)

    s += """
<tr class='roles'   > <td colspan="2"> Special Operations </td> </tr>
"""

    s += generate_roster_tag(people, 'special-ops')

    s += """
<tr class='roles' > <td colspan="2"> Duckietown Engineering Training Program </td> </tr>
"""

    s += generate_roster_tag(people, 'training', expected=26)

    s += """
</table>"""

    return s


def generate_roster_tag(people, tag, expected=None):
    people = select(people, tag)


    s = ""

    def get_order(k):
        score = people[k]['order'] * 1000

        name = people[k]['name']
        if name is None:
            score += 1000
        else:
            last = name.split(' ')[-1]
            score += ord(last[0])

        logger.debug('score %r -> %r' % (name, score))
        return score

    ordered = sorted(people, key=get_order)

    logger.info('tag %r: %s selected: %s' % (tag, len(people), ", ".join(ordered)))

    for id_person in ordered:
        p = people[id_person]
        s += "\n\n" + generate_person(id_person, p) + "\n\n"

    if expected is not None:
        n = len(ordered)
        missing = expected - n
        if missing > 0:
            url_DB = 'https://github.com/duckietown/website/tree/gh-pages/media/staff'
            s += '\n\n<tr class="missing"><td colspan="2">'
            s += '(Plus other %d people ' % missing
            s += ' who have not yet added their bio <a href="%s">in our DB</a>.)' % url_DB
            s += '</td></tr>'
            s += '\n\n'

    return s

def generate_person(id_person, p):
    s = "<tr><td class='photo'>"

    img_local_url = "media/staff/%s.jpg" % id_person

    img_missing_local_url = "media/staff/MISSING.jpg"
    if not os.path.exists(img_local_url):
        logger.warn('Image %r does not exist' % img_local_url)
        img_local_url = img_missing_local_url

    img_url = "http://duckietown.mit.edu/"+img_local_url
    name = p['name']
    if name is None:
        name = '("%s" should add information in DB)' % id_person
    position = p['position']
    url = p['url']
    
    s += '<img class="person" src="%s"/>' % img_url
    s += "</td><td>"

    if url is not None:
        s += '<span class="name"><a href="%s">%s</a></span>' % (url, name)
    else:
        s += '<span class="name"> %s</span>' % name
    s += '<br/><span class="position">%s</span>' % position

    if 'roster_note' in p:
        s += '<p>%s</p>' % p['roster_note']

    bio = p['bio'].strip()
    if bio:
        s += '<p><span class="bio">%s</span></p>' % bio
        
    s += "</td></tr>"
    return s


def select(people, tag):
    return dict([(k, p) for k, p in people.items() if tag in p['tags']])


if __name__ == '__main__':
    main()
