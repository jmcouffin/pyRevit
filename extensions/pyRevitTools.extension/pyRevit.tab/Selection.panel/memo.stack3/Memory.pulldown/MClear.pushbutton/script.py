import os
import os.path as op
import pickle as pl

from pyrevit import revit
from pyrevit import script


__doc__ = 'Clears selection from memory. Works like the MC button in a '\
          'calculator. This is a project-dependent (Revit *.rvt) memory. '\
          'Every project has its own memory saved in user temp folder '\
          'as *.pym files.'


datafile = script.get_document_data_file("SelList", "pym")

f = open(datafile, 'wb')
pl.dump([], f)
f.close()
