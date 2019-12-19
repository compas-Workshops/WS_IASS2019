import compas
import compas_rhino
import compas_tna

from compas.rpc import Proxy

from compas_tna.diagrams import FormDiagram
from compas_tna.diagrams import ForceDiagram
from compas_tna.rhino import DiagramHelper

import rhinoscriptsyntax as rs


tna = Proxy('compas_tna.equilibrium')


def horizontal(form, force, alpha=100, kmax=500):
    """Compute horizontal equilibrium by parallelising the form and force diagram.

    Parameters
    ----------
    form : compas_tna.diagrams.FormDiagram
        The form diagram.
    force : compas_tna.diagrams.ForceDiagram
        The force diagram.
    alpha : int (100)
        Weighting factor for the calculation of the target vectors.
        ``alpha = 100`` means target vectors parallel to the edges of the form diagram.
        ``alpha = 0`` means target vectors parallel to the edges of the force diagram.
    kmax : int (500)
        Maximum number of iterations.

    Notes
    -----
    This is a wrapper around the proxy for the function ``compas_tna.equilibrium.horizontal_nodal``.

    """
    formdata, forcedata = tna.horizontal_nodal_proxy(form.to_data(), force.to_data(), alpha=alpha, kmax=kmax)
    form.data = formdata
    force.data = forcedata


def vertical(form, zmax):
    """Compute the scale of the force diagram such that the maximum z-coordinate
    of all vertices corresponds to a chosen value.

    Parameters
    ----------
    form : compas_tna.diagrams.FormDiagram
        The form diagram.
    zmax : float
        The maximum z-coordinate of all vertices of the equilibrium network.

    """
    formdata, scale = tna.vertical_from_zmax_proxy(form.to_data(), zmax)
    form.data = formdata
    return scale


# 1. make the form diagram from selected line elements

guids = compas_rhino.select_lines()
rs.HideObjects(guids)

form = FormDiagram.from_rhinolines(guids)
form.draw(layer='TNA::FormDiagram', clear_layer=True)


# # 2. identify the supports

keys = form.vertices_on_boundary()
if keys:
    form.set_vertices_attributes(['is_anchor', 'is_fixed'], [True, True], keys=keys)
    form.draw(layer='TNA::FormDiagram', clear_layer=True)


# # 3. update the boundaries
 # Note: add only one foot per support to control the direction of the horizontal component
 #       of the reaction force

form.update_boundaries(feet=1)
form.draw(layer='TNA::FormDiagram', clear_layer=True)


# # 4. make the force diagram

force = ForceDiagram.from_formdiagram(form)
force.draw(layer='TNA::ForceDiagram', clear_layer=True)

DiagramHelper.move(force)
force.draw(layer='TNA::ForceDiagram', clear_layer=True)


# # 5. compute horizontal equilibrium

horizontal(form, force, alpha=100, kmax=500)
force.draw(layer='TNA::ForceDiagram', clear_layer=True)


# # 6. compute vertical equilibrium based on a chosen height of the highest point of the equilibrium network

while True:
    zmax = rs.GetReal('Z Max')
   
    if not zmax:
        break
   
    else:
        scale = vertical(form, zmax)
        force.attributes['scale'] = scale
       
       
        settings = {
            'show.forces'    : True,
            'show.reactions' : True,
            'scale.forces'   : 0.02,
            'scale.reactions': 1.0
        }
       
        form.draw(layer='TNA::FormDiagram', clear_layer=True, settings=settings)
