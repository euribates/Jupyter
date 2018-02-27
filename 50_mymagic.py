#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IPython.core.magic import (
    register_line_magic,
    register_cell_magic,
    register_line_cell_magic,
    )

from IPython.display import HTML, Image

from pygments import highlight
from pygments.lexers import PythonLexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter, ImageFormatter


@register_line_magic
def lmagic(line):
    "my line magic"
    return HTML('<b>{}</b>'.format(line))


@register_cell_magic
def cmagic(line, cell):
    "my cell magic"
    return line, cell


@register_cell_magic
def showcode(line, cell):
    "pygments magic cell for Jupyter noebook"
    if not line:
        lexer = PythonLexer()
    else:
        lexer = get_lexer_by_name(line)
    return HTML(
        highlight(
            cell, 
            lexer,
            HtmlFormatter(hl_lines="1", noclasses=True),
            )
        )
del showcode

@register_cell_magic
def imagecode(line, cell):
    "pygments magic cell for Jupyter noebook"
    lexer = PythonLexer()
    return Image(
        highlight(
            cell, 
            lexer,
            ImageFormatter(image_format='PNG'),
            )
        )
del imagecode

@register_line_cell_magic
def lcmagic(line, cell=None):
    "Magic that works both as %lcmagic and as %%lcmagic"
    if cell is None:
        print("Called as line magic")
        return line
    else:
        print("Called as cell magic")
        return line, cell

# We delete these to avoid name conflicts for automagic to work
del lmagic, cmagic, lcmagic


