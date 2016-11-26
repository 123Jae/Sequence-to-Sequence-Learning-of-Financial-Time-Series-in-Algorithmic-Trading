import os, sys
sys.path.insert(0, os.path.join('build', 'pymake2'))

from pymake2 import *

from pymake2.template.latex import pdflatex
from pymake2.template.util  import fswatcher

pymake2({
    'name'    : 'thesis',
    'srcfile' : 'main.tex'
})
