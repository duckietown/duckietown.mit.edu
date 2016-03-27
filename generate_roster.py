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
    img.person { height: 8em;}
    img.robot { height: 8em;}
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

    s += generate_roster_tag(people, 'operations')

    s += """
<tr class='roles' > <td colspan="2"> Duckietown Engineering Training Program </td> </tr>
"""

    s += generate_roster_tag(people, 'training')

    s += """
</table>"""

    return s


def generate_roster_tag(people, tag):
    people = select(people, tag)


    s = ""

    def get_order(k):
        score = people[k]['order'] * 1000
        return score

    ordered = sorted(people, key=get_order)

    logger.info('tag %r: %s selected: %s' % (tag, len(people), ", ".join(ordered)))

    for id_person in ordered:
        p = people[id_person]
        s += "\n\n" + generate_person(id_person, p) + "\n\n"

    return s

def generate_person(id_person, p):
    s = "<tr><td class='photo'>"
    img_url = "http://duckietown.mit.edu/media/staff/%s.jpg" % id_person
    name = p['name']
    position = p['position']
    url = p['url']
    
    s += '<img class="person" src="%s"/></td>' % img_url
    s += "</td><td>"

    if url is not None:
        s += '<span class="name"><a href="%s">%s</a></span>' % (url, name)
    else:
        s += '<span class="name"> %s</span>' % name
    s += '<br/><span class="position">%s</span>' % position

    if 'roster_note' in p:
        s += '<p>%s</p>' % p['roster_note']
    s += "</td></tr>"
    return s


def select(people, tag):
    return dict([(k, p) for k, p in people.items() if tag in p['tags']])


if __name__ == '__main__':
    main()
