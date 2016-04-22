#!usr/bin/env python
import os, yaml, glob, sys
sys.path.append("../../")
from generate_lectures import read_yaml_dict
yaml_files = glob.glob( "images/*.yaml")

people = {
        'training' : {},
        'operations' : {},
        'sponsors' : {},
        'management': {},
        'special-ops':{},
        'advisory':{},
    }

for filename in yaml_files:
    
    person = read_yaml_dict(filename)
    name = filename.replace("images/","").replace(".yaml", "")
    person_jpg = name +".jpg"
    person_full_name = person["name"]
    tag = None
    for tag_type in people.keys():
        if tag_type in person["tags"]:
            tag = tag_type
    if tag == None: print name; continue

    people[tag][person_full_name] = person_jpg

sorted_people = {}
for tag in people:
    names = people[tag].keys()
    def ordering(name):
        """ Order by last name """
        last = name.split(' ')[-1]
        res = ord(last[0])
        return res

    names.sort(key=ordering)
    sorted_people[tag] = [(name, people[tag][name]) for name in names]

for tag in sorted_people:
    print "tag: %s length: %d " % (tag, len(sorted_people[tag]))

formatting = { # row by column
        'operations': (3,9,.65 ),
        "advisory": (3, 2, .85),
        "training":(4,6, 0.6),
        "management":(1,2, 1),
        "special-ops":(1,3, .8),
        "sponsors":(1,2, .8)
        }

def generate_middle_text():
    middle = ""
    for tag in order:
        text = headerbox[tag]+"\n"
        text += gen_table(tag, formatting[tag]) + "}\n"
        middle += text
    return middle


def gen_table(tag, (row,column,width)):
    start = r"""
            \begin{center}
            \begin{tabularx}{\linewidth}"""
    start += '{%s}\n'  % " ".join(["X"]*column)
    end = r""" 
            \end{tabularx}
            \end{center}
            
            """

    images = ""
    names = ""
    completed_rows = ""
    endline = r"\\"
    for r in range(row):
        images = ""
        names = ""
        for c in range(column): 
            index = r*column + c
            if index >= len(sorted_people[tag]):
                if c!= column-1:
                    images += "&"
                    names +="&"
                else:
                    names += endline + "\n"
                    images += endline + "\n"
            else:
                name, img = sorted_people[tag][index]
                path = "images/" + img
                if not os.path.exists(path):
                    print "img des not exist: ", path, name
                    img = "MISSING.jpg"

                if c != column-1:
                    images += "{\\centering \includegraphics[width=%s\linewidth]{%s}}&\n"% (width, img)
                    names += "{\\tiny \\centering %s }& "% name
                else:
                    images +="{\\centering \includegraphics[width=%s\linewidth]{%s}}%s \n"%(width,img, endline)
                    names += "{\\tiny \\centering %s }%s \n " %(name, endline)
        completed_rows += "%s\n%s" % (images, names)
    
    full_table = "\n".join([start, completed_rows, end])
    return full_table
    



headerbox={
        'management':"\headerbox{Management}{name=management,column=0,row=0, span=1}{",
        'training':"\headerbox{Engineers in Training}{name=training,column=1,span=2, above=bottom, below=staff}{",
        'advisory':"\headerbox{Advisors}{name=advisory,below=management, column=0, span=1, above=bottom}{",
        'operations':"\headerbox{Staff}{name=staff,column=1, span=3, row=0}{",
        'sponsors':"\headerbox{Sponsors}{name=sponsors,column=3,span=1, above=bottom}{",
        'special-ops':"\headerbox{Special Operations}{name=special-ops,column=3,span=1, below=staff, above=sponsors}{",
        }

order = ["management", "advisory", "operations", "sponsors", "special-ops", "training"]

stock_table =r"""
\begin{center}

\begin{tabularx}{\linewidth}{X X X X X X X X X}

\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}&
\includegraphics[width=\linewidth]{censi.jpg}\\

\tiny andrea censi long name & \tiny andrea censi & \tiny andrea censi & \tiny andrea censi & \tiny andrea censi &\tiny andrea censi & \tiny andrea censi & \tiny andrea censi & \tiny andrea censi \\
   \end{tabularx}
\end{center}

"""


begin_document=r"""
\documentclass[landscape,a0paper,fontscale=0.292]{baposter}

\usepackage[vlined]{algorithm2e}
\usepackage{times}
\usepackage{calc}
\usepackage{url}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{relsize}
\usepackage{multirow}
\usepackage{booktabs}

\usepackage{graphicx}
\usepackage{multicol}
\usepackage[T1]{fontenc}
\usepackage{ae}
\usepackage{array}
\usepackage{tabularx}

\graphicspath{{images/}}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Begin of Document
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\begin{document}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Here starts the poster
%%---------------------------------------------------------------------------
%% Format it to your taste with the options
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\definecolor{mycolor}{rgb}{1,0.2,0.3}

\begin{poster}{
 % Show grid to help with alignment
 grid=false,
 % Column spacing
 colspacing=0.7em,
 % Color style
 headerColorOne=mycolor,
 borderColor=mycolor,
 % Format of textbox
 textborder=rounded,
 % Format of text header
 headerborder=open,
 headershape=rounded,
 headershade=plain,
 background=none,
 bgColorOne=mycolor,
  bgColorTwo=white,
  borderColor=orange,
  headerColorOne=orange,
  headerColorTwo=orange,
  headerFontColor=white,
  boxColorOne=white,
  boxColorTwo=white,
 headerheight=0.1\textheight}
 % Eye Catcher
 {
      \includegraphics[width=0.05\linewidth]{logo.jpg}
 }
 % Title
 {\sc\Huge Duckietown Engineering}
 % Authors
 % {Spring 2016\\[1em]
 % {\texttt{Massachusetts Institute of Technology}}}
 % University logo
 {
  \begin{tabular}{r}
    \includegraphics[height=0.1\textheight]{logo}\\
    %\raisebox{0em}[0em][0em]{\includegraphics[height=0.03\textheight]{logo.jpg}}
  \end{tabular}
 }
  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""

end_document=r"""
\end{poster}%
%
\end{document}
"""


middle = generate_middle_text()
with open("auto_roster.tex", "wb") as f:
    f.write(begin_document)
    f.write(middle)
    f.write(end_document)


