import os

import random

import compas
import compas_ags

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from compas_ags.viewers import Viewer

from compas_ags.ags import graphstatics


# 1. make diagrams from obj

HERE = os.path.abspath(os.path.dirname(__file__))
FILE = os.path.join(HERE, 'grid.obj')

form = FormDiagram.from_obj(FILE)
force = ForceDiagram.from_formdiagram(form)


# 2. set the fixed points

for key, attr in form.vertices_where({'vertex_degree': 1}, True):
    attr['is_fixed'] = True


# 3. identify independent edges and assign random values

k, m, ind = graphstatics.form_identify_dof(form)

for u, v in ind:
    form.set_edge_attributes((u, v), ('is_ind', 'q'), (True, random.choice(range(2, 20))))


# 4. update diagrams

graphstatics.form_update_q_from_qind(form)
graphstatics.force_update_from_form(force, form)


# 5. visualise

viewer = Viewer(form, force, delay_setup=False)

viewer.draw_form(
    vertexsize=0.15,
    external_on=False
)

viewer.draw_force(
    vertexsize=0.15,
)

viewer.show()
