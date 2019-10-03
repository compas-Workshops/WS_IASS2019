from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import rhinoscriptsyntax as rs
import scriptcontext as sc

import compas_rhino
import compas_tna

from compas_tna.diagrams import FormDiagram


__commandname__ = "TNA_relax"


def RunCommand(is_interactive):
    if 'TNA' not in sc.sticky:
        raise Exception("Initialise the plugin first!")

    TNA = sc.sticky['TNA']

    form = TNA['form']
    proxy = TNA['proxy']

    proxy.package = 'compas_tna.utilities'

    fixed = list(form.vertices_where({'is_fixed': True}))

    form.data = proxy.relax_boundary_openings_proxy(form.to_data(), fixed)

    form.draw(layer=TNA['settings']['layer.form'], clear_layer=True, settings=TNA['settings'])


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)