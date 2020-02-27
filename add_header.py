#!/usr/bin/env python3

import os
import itertools
import sys
import re

from ipykernel import kernelspec as ks
import nbformat
from nbformat.v4.nbbase import new_markdown_cell

#from generate_contents import NOTEBOOK_DIR, REG, iter_notebooks, get_notebook_title

#NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')
NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__))

def prev_this_next(it):
    a, b, c = itertools.tee(it,3)
    next(c)
    return zip(itertools.chain([None], a), b, itertools.chain(c, [None]))


PREV_TEMPLATE = "< [{title}]({url}) "
CONTENTS = "| [Contents](Index.ipynb) |"
NEXT_TEMPLATE = " [{title}]({url}) >"
NAV_COMMENT = "<!--NAVIGATION-->\n"

COLAB_LINK = """

<a href="https://colab.research.google.com/github/csmastersUH/data_analysis_with_python_spring_2020/blob/master/{notebook_filename}"><img align="left" src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" title="Open and Execute in Google Colaboratory"></a>
"""

def iter_notebooks():
    return sys.argv[1:]

def iter_navbars():
    for prev_nb, nb, next_nb in prev_this_next(iter_notebooks()):
        navbar = NAV_COMMENT
        #if prev_nb:
        #    navbar += PREV_TEMPLATE.format(title=get_notebook_title(prev_nb),
        #                                   url=prev_nb)
        #navbar += CONTENTS
        #if next_nb:
        #    navbar += NEXT_TEMPLATE.format(title=get_notebook_title(next_nb),
        #                                   url=next_nb)

        navbar += COLAB_LINK.format(notebook_filename=os.path.basename(nb))
            
        yield os.path.join(NOTEBOOK_DIR, nb), navbar

def get_notebook_exercises(nb):
    result = []
    for cell in nb.cells:
#        if cell.source.startswith('<div class="alert alert-info">') and cell.cell_type != "code":
        if cell.source.startswith('#### <div class="alert alert-info">') and cell.cell_type != "code":
#            line = cell.source.splitlines()[0]
            line = cell.source
            exercise_name = re.search(r">(.*)<", line).group(1)
#            exercise_name = re.search(r"^#### (.*)$", line, re.MULTILINE).group(1)
            result.append(exercise_name)
    return result

def to_nbsphinx(s):
    """Use the sphinx naming style for anchors of headings"""
    s = s.replace(" ", "-").lower()
    return "".join(filter(lambda c : c not in "()", s))

def to_github(s):
    """Use the github naming style for anchors of headings"""
    s = s.replace(" ", "-")
    s = re.sub(r"\)$", "&#41;", s)   # In notebook the link cannot end in closing parenthesis
    return s

def write_navbars():
    for nb_name, navbar in iter_navbars():
        nb = nbformat.read(nb_name, as_version=4)
        nb_file = os.path.basename(nb_name)
        is_comment = lambda cell: cell.source.startswith(NAV_COMMENT)

        exercises = get_notebook_exercises(nb)
        n = len(exercises)
        if n > 0:
            exercise_links = [ "[%s](<#%s>)" % (e, to_github(e)) for e in exercises ]
            longest_field = max(len(e) for e in exercise_links)
            print(exercise_links)
            print("%i exercises" % n)
            columns = 3
            if n < columns:
                columns = n
            table = []
            empty=" " * (longest_field + 2)
            column_title = "-".center(longest_field + 2)
            dash="-" * (longest_field + 2)
            table.append("|%s\n" % (("%s|" % column_title)*columns))  # No column title
            table.append("|%s\n" % (("%s|" % dash)*columns))         # separator line
            for i, e in enumerate(exercise_links):
                if i % columns == 0:                                 # Start a new row
                    table.append("|")
                table.append(" %s |" % e.center(longest_field))
                if i % columns == (columns-1):                       # Row is full
                    table.append("\n")
            remainder = n % columns
            if remainder > 0:
                table.append("%s\n" % (("%s|" % empty)* (columns - remainder)))

            table = "".join(table)
            print(table)
            header = "%s\n%s\n" % (navbar, table)
        else:
            header = "%s\n" % (navbar)   # no exercises
        if is_comment(nb.cells[0]):
            print("- amending navbar for {0}".format(nb_file))
            nb.cells[0].source = header
        else:
            print("- inserting navbar for {0}".format(nb_file))
            nb.cells.insert(0, new_markdown_cell(source=header))

        if is_comment(nb.cells[-1]):
            nb.cells[-1].source = navbar
        else:
            nb.cells.append(new_markdown_cell(source=navbar))
        nbformat.write(nb, nb_name)


if __name__ == '__main__':
    write_navbars()
