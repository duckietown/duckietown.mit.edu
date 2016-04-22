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
    name = filename.strip(".yaml").strip("images/")
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
    names.sort()
    sorted_people[tag] = [(name, people[tag][name]) for name in names]
print sorted_people['management']
print sorted_people['advisory']


for tag in sorted_people:
    print "tag: %s length: %d " % (tag, len(sorted_people[tag]))

formatting = { # row by column
        'operations': (3,9,1 ),
        "advisors": (3, 2, .85),
        "training":(4,6, 0.5),
        "management":(1,2, 1),
        "special-ops":(1,3, .5),
        "sponsors":(1,2, 1)
        }

def generate_middle_text():
    middle = ""
    for tag in headerbox:
        text = headerbox[tag]+"\n"
        text += gen_table(formatting[tag]) + "}\n"
        middle += text
    return middle


def gen_table((row,column,width)):
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
            if c != column-1:
                images += "\includegraphics[width=%s\linewidth]{censi.jpg}&\n"% width
                names += "\smaller andrea censi & "
            else:
                images +="\includegraphics[width=%s\linewidth]{censi.jpg}%s \n"%(width,endline)
                names += "\smaller andrea censi %s \n " %(endline)
        completed_rows += "%s\n%s" % (images, names)
    
    full_table = "\n".join([start, completed_rows, end])
    return full_table
    



headerbox={
        'management':"\headerbox{Management}{name=management,column=0,row=0, span=1}{",
        'training':"\headerbox{Engineers in Training}{name=training,column=1,span=2, above=bottom, below=staff}{",
        'advisors':"\headerbox{Advisors}{name=advisory,below=management, column=0, span=1, above=bottom}{",
        'operations':"\headerbox{Staff}{name=staff,column=1, span=3, row=0}{",
        'sponsors':"\headerbox{Sponsors}{name=sponsors,column=3,span=1, above=bottom}{",
        'special-ops':"\headerbox{Special Operations}{name=special-ops,column=3,span=1, below=staff, above=sponsors}{",
        }

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

\smaller andrea censi long name & \smaller andrea censi & \smaller andrea censi & \smaller andrea censi & \smaller andrea censi &\smaller andrea censi & \smaller andrea censi & \smaller andrea censi & \smaller andrea censi \\
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
 {\sc\Huge Duckietown Roster}
 % Authors
 {Ari is cool\\[1em]
 {\texttt{Something about MIT}}}
 % University logo
 {
  \begin{tabular}{r}
    \includegraphics[height=0.1\textheight]{logo}\\
    \raisebox{0em}[0em][0em]{\includegraphics[height=0.03\textheight]{logo.jpg}}
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


