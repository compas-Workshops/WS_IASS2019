"""Compute the equilibrium of a simple statically determined system and
visualise the result using a form and force diagram.

author: Tom Van Mele
email: vanmelet@ethz.ch

"""
import os

import compas
import compas_ags

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram
from compas_ags.viewers import Viewer
from compas_ags.ags import graphstatics


# 0. set directory to location of this py file, find obj file

HERE = os.path.abspath(os.path.dirname(__file__))
FILE = os.path.join(HERE, 'simple_truss.obj')


# 1. make form diagram from obj

form = FormDiagram.from_obj(FILE)


# 2. make force diagram from form diagram

force = ForceDiagram.from_formdiagram(form)


# 3. set the fixed points

left  = list(form.vertices_where({'x': 0.0, 'y': 0.0}))[0]
right = list(form.vertices_where({'x': 6.0, 'y': 0.0}))[0]


# 4. set the magnitude of the applied load

form.set_edge_force_by_index(1, 100.0)


# 5. update diagrams

graphstatics.form_update_q_from_qind(form)
graphstatics.force_update_from_form(force, form)


# 6. visualise

viewer = Viewer(form, force, delay_setup=False)

viewer.draw_form(
    vertexsize=0.15,
    vertexcolor={key: '#000000' for key in (left, right)},
    vertexlabel={key: key for key in form.vertices()},
    edgelabel={uv: index for index, uv in enumerate(form.edges())}
)

viewer.draw_force(
    vertexsize=0.15,
    vertexlabel={key: key for key in force.vertices()}
)

viewer.show()
